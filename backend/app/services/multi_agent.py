import json
import operator
from dataclasses import dataclass
from functools import lru_cache
from typing import Annotated, Callable, Dict, List, Literal, Optional

from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.runnables import RunnableConfig
from langchain_openai import ChatOpenAI
from langfuse import Langfuse
from langfuse.langchain import CallbackHandler
from langgraph.graph import END, START, StateGraph
from langgraph.runtime import Runtime
from pydantic import BaseModel
from typing_extensions import TypedDict

from app.core.config import get_settings
from app.services.rag import LANGUAGE_NAMES, build_context, normalize_language
from app.services.vector_store import search_chunks

settings = get_settings()


@dataclass(frozen=True)
class AgentSpec:
    id: str
    name: str
    role: str
    query: str
    focus: str


@dataclass
class ReviewContext:
    progress_callback: Optional[Callable[[Dict], None]] = None


class SpecialistPayload(BaseModel):
    summary: str
    findings: List[str]
    risks: List[str]
    actions: List[str]
    confidence: Literal["high", "medium", "low"]
    missing_evidence: List[str]


class VerifierPayload(BaseModel):
    summary: str
    unsupported_claims: List[str]
    evidence_gaps: List[str]
    confidence: Literal["high", "medium", "low"]


class ReviewState(TypedDict, total=False):
    tenant_id: str
    focus: str
    response_language: str
    agent_results: Annotated[List[Dict], operator.add]
    ordered_agent_results: List[Dict]
    chunks_used: int
    verifier: Dict
    sources: List[Dict]
    final_result: Dict


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


@lru_cache(maxsize=4)
def get_chat_model(temperature: float, max_completion_tokens: int) -> ChatOpenAI:
    return ChatOpenAI(
        api_key=settings.openai_api_key,
        model=settings.llm_model,
        temperature=temperature,
        max_completion_tokens=max_completion_tokens,
        timeout=60,
        max_retries=2,
    )


@lru_cache(maxsize=1)
def get_langfuse_client() -> Optional[Langfuse]:
    if not settings.langfuse_public_key or not settings.langfuse_secret_key:
        return None
    return Langfuse(
        public_key=settings.langfuse_public_key,
        secret_key=settings.langfuse_secret_key,
        base_url=settings.langfuse_base_url,
        environment=settings.langfuse_tracing_environment,
    )


def get_langfuse_handler() -> Optional[CallbackHandler]:
    if not get_langfuse_client():
        return None
    return CallbackHandler(public_key=settings.langfuse_public_key)


def message_text(message) -> str:
    content = getattr(message, "content", "")
    if isinstance(content, str):
        return content
    return str(content or "")


def message_tokens(message) -> Optional[int]:
    usage = getattr(message, "usage_metadata", None) or {}
    total = usage.get("total_tokens") if isinstance(usage, dict) else getattr(usage, "total_tokens", None)
    return int(total) if total is not None else None


def invoke_structured_model(
    schema,
    messages: List,
    temperature: float,
    max_completion_tokens: int,
    run_config: Optional[RunnableConfig] = None,
) -> tuple[Dict, Optional[int], str]:
    model = get_chat_model(temperature, max_completion_tokens).with_structured_output(
        schema,
        method="json_schema",
        include_raw=True,
    )
    result = model.invoke(messages, config=run_config)
    parsed = result.get("parsed")
    raw = result.get("raw")
    if isinstance(parsed, BaseModel):
        payload = parsed.model_dump()
    elif isinstance(parsed, dict):
        payload = parsed
    else:
        payload = {}
    return payload, message_tokens(raw), message_text(raw)


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


def run_specialist_agent(
    spec: AgentSpec,
    tenant_id: str,
    focus: str,
    response_language: str,
    run_config: Optional[RunnableConfig] = None,
) -> Dict:
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

    payload, tokens_used, raw_text = invoke_structured_model(
        SpecialistPayload,
        [
            SystemMessage(content=MULTI_AGENT_SYSTEM_PROMPT.format(
                agent_name=spec.name,
                agent_role=spec.role,
                response_language=response_language,
            )),
            HumanMessage(content=prompt),
        ],
        temperature=0.15,
        max_completion_tokens=1100,
        run_config=run_config,
    )
    if not payload:
        payload = {"summary": raw_text, "confidence": "medium"}
    payload = normalize_agent_payload(payload)

    return {
        "id": spec.id,
        "name": spec.name,
        "role": spec.role,
        "status": "completed",
        **payload,
        "sources": sources,
        "chunks_used": len(chunks),
        "tokens_used": tokens_used,
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


def run_verifier_agent(
    agent_results: List[Dict],
    response_language: str,
    run_config: Optional[RunnableConfig] = None,
) -> Dict:
    payload, tokens_used, raw_text = invoke_structured_model(
        VerifierPayload,
        [
            SystemMessage(content=VERIFIER_SYSTEM_PROMPT.format(response_language=response_language)),
            HumanMessage(content=verifier_input(agent_results)),
        ],
        temperature=0,
        max_completion_tokens=900,
        run_config=run_config,
    )
    if not payload:
        payload = {
            "summary": raw_text,
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
        "tokens_used": tokens_used,
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


def synthesize_review(
    focus: str,
    agent_results: List[Dict],
    verifier_result: Dict,
    sources: List[Dict],
    response_language: str,
    run_config: Optional[RunnableConfig] = None,
) -> tuple[str, Optional[int]]:
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

    response = get_chat_model(0.15, 1400).invoke(
        [
            SystemMessage(content=SYNTHESIS_SYSTEM_PROMPT.format(response_language=response_language)),
            HumanMessage(content=prompt),
        ],
        config=run_config,
    )
    return message_text(response), message_tokens(response)


def planner_node(state: ReviewState, runtime: Runtime[ReviewContext]) -> Dict:
    emit_progress(
        runtime.context.progress_callback,
        "planner",
        "Planner Agent is decomposing the review.",
        "Selecting risk, incident, release, metrics, and KT specialists.",
    )
    emit_progress(
        runtime.context.progress_callback,
        "retriever",
        "Source Retriever Agent is preparing specialist evidence searches.",
        "Each specialist will retrieve its own source-grounded context.",
    )
    return {}


def make_specialist_node(spec: AgentSpec):
    def specialist_node(
        state: ReviewState,
        config: RunnableConfig,
        runtime: Runtime[ReviewContext],
    ) -> Dict:
        emit_progress(
            runtime.context.progress_callback,
            spec.id,
            f"{spec.name} is reviewing project evidence.",
            spec.role,
        )
        result = run_specialist_agent(
            spec,
            state["tenant_id"],
            state["focus"],
            state["response_language"],
            run_config=config,
        )
        emit_progress(
            runtime.context.progress_callback,
            f"{spec.id}_done",
            f"{spec.name} finished with {result.get('confidence', 'medium')} confidence.",
            f"{result.get('chunks_used', 0)} chunk(s) reviewed.",
        )
        return {"agent_results": [result]}

    specialist_node.__name__ = spec.id
    return specialist_node


def collect_specialists_node(state: ReviewState) -> Dict:
    results_by_id = {
        result.get("id"): result
        for result in state.get("agent_results", [])
        if result.get("id")
    }
    ordered_results = [
        results_by_id[spec.id]
        for spec in AGENT_SPECS
        if spec.id in results_by_id
    ]
    total_chunks = sum(result.get("chunks_used", 0) or 0 for result in ordered_results)
    return {
        "ordered_agent_results": ordered_results,
        "chunks_used": total_chunks,
    }


def route_after_collection(state: ReviewState) -> Literal["no_evidence", "verifier"]:
    return "verifier" if state.get("chunks_used", 0) > 0 else "no_evidence"


def no_evidence_node(state: ReviewState, runtime: Runtime[ReviewContext]) -> Dict:
    emit_progress(
        runtime.context.progress_callback,
        "complete",
        "Project Review Board could not find source evidence.",
        "Upload or sync project sources before running the multi-agent review.",
    )
    return {
        "final_result": {
            "answer": "No relevant project sources were found for the multi-agent review. Upload Jira, GitHub, Teams, metrics, incidents, docs, or database health sources first.",
            "sources": [],
            "chunks_used": 0,
            "tokens_used": None,
            "answer_mode": "multi_agent",
            "agents": state.get("ordered_agent_results", []),
            "verifier": None,
        }
    }


def verifier_node(
    state: ReviewState,
    config: RunnableConfig,
    runtime: Runtime[ReviewContext],
) -> Dict:
    emit_progress(
        runtime.context.progress_callback,
        "verifier",
        "Verifier Agent is checking evidence support.",
        "Looking for unsupported claims and missing source categories.",
    )
    agent_results = state["ordered_agent_results"]
    return {
        "verifier": run_verifier_agent(
            agent_results,
            state["response_language"],
            run_config=config,
        ),
        "sources": merge_sources(agent_results),
    }


def synthesizer_node(
    state: ReviewState,
    config: RunnableConfig,
    runtime: Runtime[ReviewContext],
) -> Dict:
    emit_progress(
        runtime.context.progress_callback,
        "synthesizer",
        "Synthesizer Agent is preparing the final board review.",
        "Combining specialist findings into one source-grounded answer.",
    )
    agent_results = state["ordered_agent_results"]
    verifier_result = state["verifier"]
    sources = state["sources"]
    answer, synthesis_tokens = synthesize_review(
        state["focus"],
        agent_results,
        verifier_result,
        sources,
        state["response_language"],
        run_config=config,
    )
    specialist_tokens = sum(result.get("tokens_used") or 0 for result in agent_results)
    verifier_tokens = verifier_result.get("tokens_used") or 0
    tokens_used = specialist_tokens + verifier_tokens + (synthesis_tokens or 0)
    return {
        "final_result": {
            "answer": answer,
            "sources": sources,
            "chunks_used": state["chunks_used"],
            "tokens_used": tokens_used or None,
            "answer_mode": "multi_agent",
            "agents": agent_results,
            "verifier": verifier_result,
        }
    }


def build_review_graph():
    graph = StateGraph(ReviewState, context_schema=ReviewContext)
    graph.add_node("planner", planner_node)
    for spec in AGENT_SPECS:
        graph.add_node(spec.id, make_specialist_node(spec))
    graph.add_node("collect_specialists", collect_specialists_node)
    graph.add_node("no_evidence", no_evidence_node)
    graph.add_node("verifier", verifier_node)
    graph.add_node("synthesizer", synthesizer_node)

    graph.add_edge(START, "planner")
    for spec in AGENT_SPECS:
        graph.add_edge("planner", spec.id)
    graph.add_edge([spec.id for spec in AGENT_SPECS], "collect_specialists")
    graph.add_conditional_edges(
        "collect_specialists",
        route_after_collection,
        {"no_evidence": "no_evidence", "verifier": "verifier"},
    )
    graph.add_edge("no_evidence", END)
    graph.add_edge("verifier", "synthesizer")
    graph.add_edge("synthesizer", END)
    return graph.compile(name="base-project-review-board")


REVIEW_GRAPH = build_review_graph()


def run_project_review_board(
    tenant_id: str,
    focus: str = "",
    language: str = "en",
    progress_callback: Optional[Callable[[Dict], None]] = None,
) -> Dict:
    language_code = normalize_language(language)
    clean_focus = focus.strip() or "overall project health, risk, release readiness, incidents, metrics, and KT"
    run_config: RunnableConfig = {
        "run_name": "base-project-review-board",
        "tags": ["base", "multi-agent", "project-review"],
        "metadata": {
            "tenant_id": tenant_id,
            "framework": "langgraph",
            "langfuse_session_id": tenant_id,
            "langfuse_tags": ["base", "multi-agent", "project-review"],
        },
        "max_concurrency": len(AGENT_SPECS),
    }
    langfuse_handler = get_langfuse_handler()
    if langfuse_handler:
        run_config["callbacks"] = [langfuse_handler]

    final_state = REVIEW_GRAPH.invoke(
        {
            "tenant_id": tenant_id,
            "focus": clean_focus,
            "response_language": LANGUAGE_NAMES[language_code],
            "agent_results": [],
        },
        config=run_config,
        context=ReviewContext(progress_callback=progress_callback),
    )
    return final_state["final_result"]
