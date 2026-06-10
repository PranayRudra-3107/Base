import json
import re
from dataclasses import dataclass
from typing import Callable, Dict, List, Optional

from openai import OpenAI

from app.core.config import get_settings
from app.services.rag import LANGUAGE_NAMES, build_context, normalize_language
from app.services.vector_store import search_chunks

settings = get_settings()
client = OpenAI(api_key=settings.openai_api_key, timeout=60)


@dataclass(frozen=True)
class AgentSpec:
    id: str
    name: str
    role: str
    query: str
    focus: str


AGENT_SPECS = [
    AgentSpec(
        id="risk_analyst",
        name="Risk Analyst Agent",
        role="Find blockers, delivery risks, unresolved ownership, stale work, and escalation points.",
        query=(
            "risks blockers severity owners stale tickets delayed reopened dependencies unresolved "
            "questions action items decisions jira sprint"
        ),
        focus="risk register, blocker patterns, severity, owner hints, and next actions",
    ),
    AgentSpec(
        id="incident_analyst",
        name="Incident Analyst Agent",
        role="Review incidents, PagerDuty notes, operations chats, probable causes, impact, and prevention work.",
        query=(
            "pagerduty incident outage sev root cause customer impact timeline mitigation follow-up "
            "oncall runbook teams error latency"
        ),
        focus="incident history, root causes, impact, repeated patterns, and follow-up actions",
    ),
    AgentSpec(
        id="release_analyst",
        name="Release and Code Agent",
        role="Connect GitHub PRs, commits, branches, releases, tickets, and architecture changes.",
        query=(
            "github pull request pr commit branch release deploy feature flag migration code changes "
            "architecture ticket rollout"
        ),
        focus="recent changes, release readiness, PR or commit evidence, rollout risks, and source-code signals",
    ),
    AgentSpec(
        id="metrics_analyst",
        name="Metrics and Reliability Agent",
        role="Analyze traffic, latency, error rate, uptime, database health, and observability signals.",
        query=(
            "grafana metrics traffic p95 p99 latency error rate uptime database health slow queries "
            "replication storage connections cpu memory conversion"
        ),
        focus="operational health, metric anomalies, database signals, and what to verify next",
    ),
    AgentSpec(
        id="kt_agent",
        name="KT and Onboarding Agent",
        role="Turn project evidence into a practical first-week learning path and handoff checklist.",
        query=(
            "onboarding kt handoff architecture confluence runbook owners decisions first week checklist "
            "project overview services components priorities"
        ),
        focus="new-joiner KT, important systems, owners, first-week checklist, and source reading order",
    ),
]


MULTI_AGENT_SYSTEM_PROMPT = """You are {agent_name}.
Role: {agent_role}

Use only the provided project source context.
Do not invent facts, IDs, names, dates, metrics, or source filenames.
If evidence is missing, say what is missing.
Write all user-facing prose in {response_language}.
Keep ticket IDs, PR IDs, incident IDs, service names, metric names, URLs, and filenames unchanged.

Return only valid JSON with this exact shape:
{{
  "summary": "one concise paragraph",
  "findings": ["3 to 5 source-backed findings"],
  "risks": ["0 to 4 risks or gaps"],
  "actions": ["2 to 4 practical next actions"],
  "confidence": "high|medium|low",
  "missing_evidence": ["0 to 4 missing source types or gaps"]
}}"""


SYNTHESIS_SYSTEM_PROMPT = """You are the Synthesizer Agent for a project review board.
Combine specialist agent outputs into one concise, source-grounded review.
Do not invent new facts. Use only the specialist outputs and source list.
Write all user-facing prose in {response_language}.
Keep filenames, ticket IDs, PR IDs, incident IDs, service names, metrics, and URLs unchanged."""


VERIFIER_SYSTEM_PROMPT = """You are the Verifier Agent for a project review board.
Check whether the specialist findings are supported by their cited source snippets.
Do not add new project facts.
Write all user-facing prose in {response_language}.

Return only valid JSON with this exact shape:
{{
  "summary": "short verification summary",
  "unsupported_claims": ["claims that need better evidence"],
  "evidence_gaps": ["missing source categories or weak evidence areas"],
  "confidence": "high|medium|low"
}}"""


def emit_progress(progress_callback: Optional[Callable[[Dict], None]], stage: str, message: str, detail: str = "") -> None:
    if progress_callback:
        progress_callback({"stage": stage, "message": message, "detail": detail})


def parse_json_object(raw: str) -> Dict:
    text = (raw or "").strip()
    if text.startswith("```"):
        text = re.sub(r"^```(?:json)?", "", text).strip()
        text = re.sub(r"```$", "", text).strip()
    return json.loads(text)


def source_citations(chunks: List[Dict]) -> List[Dict]:
    sources = []
    seen_docs = set()
    for chunk in chunks:
        metadata = chunk.get("metadata", {}) or {}
        doc_id = metadata.get("document_id") or "unknown"
        if doc_id in seen_docs:
            continue
        seen_docs.add(doc_id)
        sources.append({
            "filename": metadata.get("filename", "Unknown"),
            "document_id": doc_id,
            "relevance_score": chunk.get("score", 0),
            "source_type": "project",
            "url": None,
            "retrieval_mode": chunk.get("retrieval_mode", "semantic"),
            "semantic_score": chunk.get("semantic_score", 0),
            "keyword_score": chunk.get("keyword_score", 0),
            "matched_terms": chunk.get("matched_terms", []),
        })
    return sources


def merge_sources(agent_results: List[Dict]) -> List[Dict]:
    merged = {}
    for result in agent_results:
        for source in result.get("sources", []):
            key = source.get("document_id") or source.get("filename")
            if not key:
                continue
            existing = merged.get(key)
            if not existing or source.get("relevance_score", 0) > existing.get("relevance_score", 0):
                merged[key] = source
    return sorted(merged.values(), key=lambda item: item.get("relevance_score", 0), reverse=True)[:12]


def normalize_agent_payload(payload: Dict) -> Dict:
    def clean_list(value, limit):
        if not isinstance(value, list):
            return []
        return [str(item).strip() for item in value if str(item).strip()][:limit]

    confidence = str(payload.get("confidence") or "medium").lower()
    if confidence not in {"high", "medium", "low"}:
        confidence = "medium"
    return {
        "summary": str(payload.get("summary") or "").strip(),
        "findings": clean_list(payload.get("findings"), 5),
        "risks": clean_list(payload.get("risks"), 4),
        "actions": clean_list(payload.get("actions"), 4),
        "confidence": confidence,
        "missing_evidence": clean_list(payload.get("missing_evidence"), 4),
    }


def agent_query(spec: AgentSpec, focus: str) -> str:
    clean_focus = focus.strip()
    if clean_focus:
        return f"{clean_focus} {spec.query}"
    return spec.query


def run_specialist_agent(spec: AgentSpec, tenant_id: str, focus: str, response_language: str) -> Dict:
    chunks = search_chunks(tenant_id, agent_query(spec, focus), k=6)
    sources = source_citations(chunks)
    if not chunks:
        return {
            "id": spec.id,
            "name": spec.name,
            "role": spec.role,
            "status": "skipped",
            "summary": "No matching project sources were found for this specialist.",
            "findings": [],
            "risks": ["Upload or sync more relevant project sources for this review area."],
            "actions": ["Add source exports or connector data that match this specialist's scope."],
            "confidence": "low",
            "missing_evidence": [spec.focus],
            "sources": [],
            "chunks_used": 0,
            "tokens_used": None,
        }

    prompt = f"""Review focus: {focus or "overall project review"}
Specialist focus: {spec.focus}

Project source context:
{build_context(chunks)}"""

    response = client.chat.completions.create(
        model=settings.llm_model,
        messages=[
            {
                "role": "system",
                "content": MULTI_AGENT_SYSTEM_PROMPT.format(
                    agent_name=spec.name,
                    agent_role=spec.role,
                    response_language=response_language,
                ),
            },
            {"role": "user", "content": prompt},
        ],
        temperature=0.15,
        response_format={"type": "json_object"},
        max_tokens=1100,
    )
    usage = getattr(response, "usage", None)
    try:
        payload = normalize_agent_payload(parse_json_object(response.choices[0].message.content))
    except Exception:
        payload = normalize_agent_payload({
            "summary": response.choices[0].message.content,
            "confidence": "medium",
        })

    return {
        "id": spec.id,
        "name": spec.name,
        "role": spec.role,
        "status": "completed",
        **payload,
        "sources": sources,
        "chunks_used": len(chunks),
        "tokens_used": usage.total_tokens if usage else None,
    }


def verifier_input(agent_results: List[Dict]) -> str:
    compact = []
    for result in agent_results:
        compact.append({
            "agent": result.get("name"),
            "summary": result.get("summary"),
            "findings": result.get("findings", []),
            "risks": result.get("risks", []),
            "actions": result.get("actions", []),
            "sources": [
                {
                    "filename": source.get("filename"),
                    "relevance_score": source.get("relevance_score"),
                    "matched_terms": source.get("matched_terms", []),
                }
                for source in result.get("sources", [])[:4]
            ],
        })
    return json.dumps(compact, indent=2)


def run_verifier_agent(agent_results: List[Dict], response_language: str) -> Dict:
    response = client.chat.completions.create(
        model=settings.llm_model,
        messages=[
            {"role": "system", "content": VERIFIER_SYSTEM_PROMPT.format(response_language=response_language)},
            {"role": "user", "content": verifier_input(agent_results)},
        ],
        temperature=0,
        response_format={"type": "json_object"},
        max_tokens=900,
    )
    usage = getattr(response, "usage", None)
    try:
        payload = parse_json_object(response.choices[0].message.content)
    except Exception:
        payload = {
            "summary": response.choices[0].message.content,
            "unsupported_claims": [],
            "evidence_gaps": [],
            "confidence": "medium",
        }
    confidence = str(payload.get("confidence") or "medium").lower()
    if confidence not in {"high", "medium", "low"}:
        confidence = "medium"
    return {
        "id": "verifier",
        "name": "Verifier Agent",
        "role": "Check source support and evidence gaps before synthesis.",
        "status": "completed",
        "summary": str(payload.get("summary") or "").strip(),
        "unsupported_claims": [
            str(item).strip()
            for item in payload.get("unsupported_claims", [])
            if str(item).strip()
        ][:5],
        "evidence_gaps": [
            str(item).strip()
            for item in payload.get("evidence_gaps", [])
            if str(item).strip()
        ][:5],
        "confidence": confidence,
        "tokens_used": usage.total_tokens if usage else None,
    }


def synthesis_input(focus: str, agent_results: List[Dict], verifier_result: Dict, sources: List[Dict]) -> str:
    payload = {
        "review_focus": focus or "overall project review",
        "specialist_agents": [
            {
                "name": result.get("name"),
                "summary": result.get("summary"),
                "findings": result.get("findings", []),
                "risks": result.get("risks", []),
                "actions": result.get("actions", []),
                "confidence": result.get("confidence"),
                "missing_evidence": result.get("missing_evidence", []),
            }
            for result in agent_results
        ],
        "verifier": verifier_result,
        "sources": [
            {
                "filename": source.get("filename"),
                "document_id": source.get("document_id"),
                "relevance_score": source.get("relevance_score"),
                "retrieval_mode": source.get("retrieval_mode"),
            }
            for source in sources
        ],
    }
    return json.dumps(payload, indent=2)


def synthesize_review(focus: str, agent_results: List[Dict], verifier_result: Dict, sources: List[Dict], response_language: str) -> tuple[str, Optional[int]]:
    prompt = f"""Create the final multi-agent project review.

Use this structure:
1. Executive readout
2. What each specialist found
3. Top risks or gaps
4. Recommended next actions
5. KT / onboarding focus
6. Evidence confidence

Input:
{synthesis_input(focus, agent_results, verifier_result, sources)}"""

    response = client.chat.completions.create(
        model=settings.llm_model,
        messages=[
            {"role": "system", "content": SYNTHESIS_SYSTEM_PROMPT.format(response_language=response_language)},
            {"role": "user", "content": prompt},
        ],
        temperature=0.15,
        max_tokens=1400,
    )
    usage = getattr(response, "usage", None)
    return response.choices[0].message.content or "", usage.total_tokens if usage else None


def run_project_review_board(
    tenant_id: str,
    focus: str = "",
    language: str = "en",
    progress_callback: Optional[Callable[[Dict], None]] = None,
) -> Dict:
    language_code = normalize_language(language)
    response_language = LANGUAGE_NAMES[language_code]
    clean_focus = focus.strip() or "overall project health, risk, release readiness, incidents, metrics, and KT"

    emit_progress(
        progress_callback,
        "planner",
        "Planner Agent is decomposing the review.",
        "Selecting risk, incident, release, metrics, and KT specialists.",
    )
    emit_progress(
        progress_callback,
        "retriever",
        "Source Retriever Agent is preparing specialist evidence searches.",
        "Each specialist will retrieve its own source-grounded context.",
    )

    agent_results = []
    for spec in AGENT_SPECS:
        emit_progress(
            progress_callback,
            spec.id,
            f"{spec.name} is reviewing project evidence.",
            spec.role,
        )
        result = run_specialist_agent(spec, tenant_id, clean_focus, response_language)
        agent_results.append(result)
        emit_progress(
            progress_callback,
            f"{spec.id}_done",
            f"{spec.name} finished with {result.get('confidence', 'medium')} confidence.",
            f"{result.get('chunks_used', 0)} chunk(s) reviewed.",
        )

    total_chunks = sum(result.get("chunks_used", 0) or 0 for result in agent_results)
    if total_chunks <= 0:
        emit_progress(
            progress_callback,
            "complete",
            "Project Review Board could not find source evidence.",
            "Upload or sync project sources before running the multi-agent review.",
        )
        return {
            "answer": "No relevant project sources were found for the multi-agent review. Upload Jira, GitHub, Teams, metrics, incidents, docs, or database health sources first.",
            "sources": [],
            "chunks_used": 0,
            "tokens_used": None,
            "answer_mode": "multi_agent",
            "agents": agent_results,
            "verifier": None,
        }

    emit_progress(
        progress_callback,
        "verifier",
        "Verifier Agent is checking evidence support.",
        "Looking for unsupported claims and missing source categories.",
    )
    verifier_result = run_verifier_agent(agent_results, response_language)

    sources = merge_sources(agent_results)
    emit_progress(
        progress_callback,
        "synthesizer",
        "Synthesizer Agent is preparing the final board review.",
        "Combining specialist findings into one source-grounded answer.",
    )
    answer, synthesis_tokens = synthesize_review(clean_focus, agent_results, verifier_result, sources, response_language)

    specialist_tokens = sum(result.get("tokens_used") or 0 for result in agent_results)
    verifier_tokens = verifier_result.get("tokens_used") or 0
    tokens_used = specialist_tokens + verifier_tokens + (synthesis_tokens or 0)

    return {
        "answer": answer,
        "sources": sources,
        "chunks_used": total_chunks,
        "tokens_used": tokens_used or None,
        "answer_mode": "multi_agent",
        "agents": agent_results,
        "verifier": verifier_result,
    }
