import json
import re
from typing import Dict, List

from openai import OpenAI

from app.core.config import get_settings
from app.services.rag import LANGUAGE_NAMES, build_context, normalize_language
from app.services.vector_store import keyword_search_chunks

settings = get_settings()
client = OpenAI(api_key=settings.openai_api_key, timeout=45)

STUDIO_SYSTEM_PROMPT = """You are a source-grounded project study assistant.
Use only the provided project source context.
Do not invent facts, IDs, names, dates, or metrics.
Write all user-facing prose in {response_language}.
Keep source filenames, ticket IDs, PR IDs, release IDs, service names, metrics, URLs, and code terms unchanged."""

DEFAULT_STUDIO_QUERY = (
    "project overview architecture risks blockers decisions incidents metrics tickets owners releases "
    "onboarding handoff priorities database github jira teams pagerduty confluence"
)


def source_citations(chunks: List[Dict]) -> List[Dict]:
    sources = []
    seen_docs = set()
    for chunk in chunks:
        metadata = chunk.get("metadata", {})
        doc_id = metadata.get("document_id")
        if doc_id in seen_docs:
            continue
        seen_docs.add(doc_id)
        sources.append({
            "filename": metadata.get("filename", "Unknown"),
            "document_id": doc_id or "unknown",
            "relevance_score": chunk.get("score", 0),
            "source_type": "project",
            "url": None,
            "retrieval_mode": chunk.get("retrieval_mode", "semantic"),
            "semantic_score": chunk.get("semantic_score", 0),
            "keyword_score": chunk.get("keyword_score", 0),
            "matched_terms": chunk.get("matched_terms", []),
        })
    return sources


def retrieve_studio_chunks(tenant_id: str, focus: str, k: int = 12) -> List[Dict]:
    query = focus.strip() if focus and focus.strip() else DEFAULT_STUDIO_QUERY
    return keyword_search_chunks(tenant_id, query, k=k)


def parse_json_object(raw: str) -> Dict:
    text = (raw or "").strip()
    if text.startswith("```"):
        text = re.sub(r"^```(?:json)?", "", text).strip()
        text = re.sub(r"```$", "", text).strip()
    return json.loads(text)


def normalize_quiz(payload: Dict, difficulty: str, count: int) -> Dict:
    questions = []
    for index, item in enumerate(payload.get("questions", [])[:count], start=1):
        options = [str(option).strip() for option in item.get("options", []) if str(option).strip()]
        if len(options) < 2:
            continue
        try:
            answer_index = int(item.get("answer_index", 0))
        except (TypeError, ValueError):
            answer_index = 0
        answer_index = max(0, min(answer_index, len(options) - 1))
        questions.append({
            "id": str(item.get("id") or f"q{index}"),
            "question": str(item.get("question", "")).strip(),
            "options": options[:5],
            "answer_index": answer_index,
            "hint": str(item.get("hint", "")).strip(),
            "explanation": str(item.get("explanation", "")).strip(),
            "source_hint": str(item.get("source_hint", "")).strip(),
        })
    return {
        "title": str(payload.get("title") or "Project source quiz").strip(),
        "difficulty": difficulty,
        "questions": questions,
    }


def generate_quiz(
    tenant_id: str,
    focus: str = "",
    difficulty: str = "medium",
    count: int = 6,
    language: str = "en",
) -> Dict:
    language_code = normalize_language(language)
    response_language = LANGUAGE_NAMES[language_code]
    chunks = retrieve_studio_chunks(tenant_id, focus, k=max(12, count * 2))
    if not chunks:
        return {
            "title": "Project source quiz",
            "difficulty": difficulty,
            "questions": [],
            "sources": [],
            "chunks_used": 0,
            "tokens_used": None,
        }

    prompt = f"""Create an interactive quiz from these project sources.

Focus: {focus or "overall project knowledge"}
Difficulty: {difficulty}
Number of questions: {count}

Return only valid JSON with this shape:
{{
  "title": "short quiz title",
  "questions": [
    {{
      "id": "q1",
      "question": "question text",
      "options": ["A", "B", "C", "D"],
      "answer_index": 0,
      "hint": "one helpful hint",
      "explanation": "why the answer is correct, citing the source filename or ID",
      "source_hint": "filename, ticket ID, PR ID, incident ID, or metric that supports this"
    }}
  ]
}}

Rules:
- Every answer must be supported by the source context.
- Prefer practical project questions about tickets, risks, incidents, PRs, metrics, owners, decisions, and architecture.
- Avoid trivia that cannot be answered from the context.
- Write in {response_language}.

Context:
{build_context(chunks)}"""

    response = client.chat.completions.create(
        model=settings.llm_model,
        messages=[
            {"role": "system", "content": STUDIO_SYSTEM_PROMPT.format(response_language=response_language)},
            {"role": "user", "content": prompt},
        ],
        temperature=0.2,
        response_format={"type": "json_object"},
        max_tokens=1800,
    )
    content = response.choices[0].message.content
    quiz = normalize_quiz(parse_json_object(content), difficulty, count)
    usage = getattr(response, "usage", None)
    return {
        **quiz,
        "sources": source_citations(chunks),
        "chunks_used": len(chunks),
        "tokens_used": usage.total_tokens if usage else None,
    }


def normalize_conversation(payload: Dict) -> Dict:
    turns = []
    for index, item in enumerate(payload.get("turns", [])[:18], start=1):
        speaker = str(item.get("speaker") or ("Host A" if index % 2 else "Host B")).strip()
        text = str(item.get("text", "")).strip()
        if text:
            turns.append({"speaker": speaker, "text": text})
    takeaways = [str(item).strip() for item in payload.get("takeaways", []) if str(item).strip()]
    return {
        "title": str(payload.get("title") or "Project conversation").strip(),
        "format": str(payload.get("format") or "deep_dive").strip(),
        "turns": turns,
        "takeaways": takeaways[:6],
    }


def excerpt(text: str, limit: int = 320) -> str:
    clean = re.sub(r"\s+", " ", text or "").strip()
    if len(clean) <= limit:
        return clean
    return clean[:limit].rsplit(" ", 1)[0] + "..."


def conversation_angle(format_name: str, index: int) -> str:
    if format_name == "critique":
        return "The review angle here is what this evidence says about risk, ownership, and missing follow-up."
    if format_name == "debate":
        return "One side reads this as readiness evidence, while the other side would ask what remains unresolved."
    if format_name == "brief":
        return "For a brief, this is one of the facts the listener should retain."
    return "This connects back to the project story because it gives concrete evidence instead of a generic summary."


def build_source_conversation(chunks: List[Dict], focus: str, format_name: str, length: str) -> Dict:
    max_evidence_turns = {"short": 4, "default": 6, "long": 8}.get(length, 6)
    selected = chunks[:max_evidence_turns]
    title_focus = focus or "project overview"
    turns = [
        {
            "speaker": "Host A",
            "text": f"Let's ground this discussion in the uploaded sources. The focus is {title_focus}, so I am going to pull out the strongest evidence and connect it to handoff decisions.",
        },
        {
            "speaker": "Host B",
            "text": f"I found {len(chunks)} relevant chunks across {len(source_citations(chunks))} source file(s). The useful part is that the conversation can stay anchored to exact files, tickets, metrics, and incidents.",
        },
    ]

    for index, chunk in enumerate(selected):
        metadata = chunk.get("metadata", {})
        filename = metadata.get("filename", "Unknown source")
        speaker = "Host A" if index % 2 == 0 else "Host B"
        turns.append({
            "speaker": speaker,
            "text": f"In {filename}, the supporting evidence says: \"{excerpt(chunk.get('text', ''))}\" {conversation_angle(format_name, index)}",
        })

    turns.append({
        "speaker": "Host B" if len(turns) % 2 else "Host A",
        "text": "So the practical takeaway is to treat this as a source-backed study conversation: verify the cited files, inspect the related tickets or incidents, and use the gaps as follow-up questions.",
    })

    filenames = []
    for chunk in chunks:
        filename = chunk.get("metadata", {}).get("filename", "Unknown")
        if filename not in filenames:
            filenames.append(filename)

    return {
        "title": "Source conversation: " + title_focus[:72],
        "format": format_name,
        "turns": turns,
        "takeaways": [
            f"Grounded in {len(chunks)} retrieved chunks.",
            f"Primary sources: {', '.join(filenames[:4])}.",
            "Use the cited files as the next inspection path.",
        ],
    }


def generate_conversation(
    tenant_id: str,
    focus: str = "",
    format_name: str = "deep_dive",
    length: str = "default",
    language: str = "en",
) -> Dict:
    chunks = retrieve_studio_chunks(tenant_id, focus, k=10)
    if not chunks:
        return {
            "title": "Project conversation",
            "format": format_name,
            "turns": [],
            "takeaways": [],
            "sources": [],
            "chunks_used": 0,
            "tokens_used": None,
        }

    conversation = build_source_conversation(chunks, focus, format_name, length)
    return {
        **conversation,
        "sources": source_citations(chunks),
        "chunks_used": len(chunks),
        "tokens_used": None,
    }


def artifact_base(chunks: List[Dict], artifact_type: str, title: str, summary: str = "") -> Dict:
    return {
        "artifact_type": artifact_type,
        "title": title,
        "summary": summary,
        "cards": [],
        "turns": [],
        "scenes": [],
        "slides": [],
        "panels": [],
        "sources": source_citations(chunks),
        "chunks_used": len(chunks),
        "tokens_used": None,
    }


def chunk_filename(chunk: Dict) -> str:
    return chunk.get("metadata", {}).get("filename", "Unknown source")


def chunk_label(chunk: Dict, index: int) -> str:
    metadata = chunk.get("metadata", {})
    filename = metadata.get("filename", "Unknown source")
    chunk_index = metadata.get("chunk_index")
    if chunk_index is None:
        return filename
    return f"{filename} chunk {chunk_index}"


def unique_filenames(chunks: List[Dict]) -> List[str]:
    names = []
    for chunk in chunks:
        filename = chunk_filename(chunk)
        if filename not in names:
            names.append(filename)
    return names


def generate_flashcards(tenant_id: str, focus: str = "", count: int = 6, language: str = "en") -> Dict:
    chunks = retrieve_studio_chunks(tenant_id, focus, k=max(6, count))
    result = artifact_base(
        chunks,
        "flashcards",
        f"Flashcards: {(focus or 'project study')[:72]}",
        "Source-grounded cards for quick review and recall.",
    )
    result["cards"] = [
        {
            "front": f"What should you remember from {chunk_filename(chunk)}?",
            "back": excerpt(chunk.get("text", ""), 360),
            "source_hint": chunk_label(chunk, index),
        }
        for index, chunk in enumerate(chunks[:count])
    ]
    return result


def generate_audio_overview(tenant_id: str, focus: str = "", style: str = "deep_dive", count: int = 6, language: str = "en") -> Dict:
    length = "short" if count <= 4 else "default"
    conversation = generate_conversation(tenant_id, focus, style if style in {"deep_dive", "brief", "critique", "debate"} else "deep_dive", length, language)
    return {
        **artifact_base(
            retrieve_studio_chunks(tenant_id, focus, k=10),
            "audio_overview",
            conversation["title"].replace("Source conversation", "Audio overview"),
            "A playable browser speech overview based on uploaded project sources.",
        ),
        "turns": conversation.get("turns", []),
        "sources": conversation.get("sources", []),
        "chunks_used": conversation.get("chunks_used", 0),
    }


def generate_video_overview(tenant_id: str, focus: str = "", count: int = 6, language: str = "en") -> Dict:
    chunks = retrieve_studio_chunks(tenant_id, focus, k=max(5, count))
    result = artifact_base(
        chunks,
        "video_overview",
        f"Video overview storyboard: {(focus or 'project overview')[:64]}",
        "Storyboard scenes that can become a narrated project explainer video.",
    )
    scenes = []
    for index, chunk in enumerate(chunks[:count], start=1):
        filename = chunk_filename(chunk)
        scenes.append({
            "scene": str(index),
            "title": f"Scene {index}: {filename}",
            "visual": f"Show a clean project card for {filename} with related tickets, metrics, or incidents highlighted.",
            "narration": excerpt(chunk.get("text", ""), 280),
            "source_hint": chunk_label(chunk, index),
        })
    result["scenes"] = scenes
    return result


def generate_slide_deck(tenant_id: str, focus: str = "", count: int = 6, language: str = "en") -> Dict:
    chunks = retrieve_studio_chunks(tenant_id, focus, k=max(5, count))
    filenames = unique_filenames(chunks)
    result = artifact_base(
        chunks,
        "slide_deck",
        f"Slide deck: {(focus or 'project briefing')[:72]}",
        "A source-grounded slide outline for presenting the project story.",
    )
    slides = [
        {
            "title": "Project Briefing",
            "bullets": [
                f"Focus: {focus or 'overall project context'}",
                f"Sources reviewed: {len(filenames)}",
                "Use this deck as a starting point for an interview demo or handoff.",
            ],
            "speaker_notes": "Open by explaining that every slide is grounded in uploaded project sources.",
        }
    ]
    for index, chunk in enumerate(chunks[: max(1, count - 2)], start=2):
        slides.append({
            "title": f"Evidence From {chunk_filename(chunk)}",
            "bullets": [
                excerpt(chunk.get("text", ""), 150),
                f"Source: {chunk_label(chunk, index)}",
            ],
            "speaker_notes": conversation_angle("brief", index),
        })
    slides.append({
        "title": "Next Actions",
        "bullets": [
            "Review cited files and open related tickets or incidents.",
            "Turn unresolved risks into owners and due dates.",
            "Refresh the deck after new project sources are uploaded.",
        ],
        "speaker_notes": "Close with the workflow: upload sources, generate artifacts, validate citations, then act.",
    })
    result["slides"] = slides[:count]
    return result


def generate_infographic(tenant_id: str, focus: str = "", count: int = 6, language: str = "en") -> Dict:
    chunks = retrieve_studio_chunks(tenant_id, focus, k=max(6, count))
    filenames = unique_filenames(chunks)
    result = artifact_base(
        chunks,
        "infographic",
        f"Infographic brief: {(focus or 'project intelligence')[:72]}",
        "A compact visual brief with source-backed panels.",
    )
    panels = [
        {"label": "Sources", "value": str(len(filenames)), "body": ", ".join(filenames[:4]) or "No source files found"},
        {"label": "Evidence Chunks", "value": str(len(chunks)), "body": "Retrieved with local keyword/BM25 matching over uploaded files."},
    ]
    for index, chunk in enumerate(chunks[: max(1, count - 2)], start=1):
        panels.append({
            "label": f"Signal {index}",
            "value": chunk_filename(chunk).split("_", 1)[0][:12],
            "body": excerpt(chunk.get("text", ""), 220),
            "source_hint": chunk_label(chunk, index),
        })
    result["panels"] = panels[:count]
    return result


def generate_artifact(
    tenant_id: str,
    artifact_type: str,
    focus: str = "",
    style: str = "default",
    count: int = 6,
    language: str = "en",
) -> Dict:
    if artifact_type == "audio_overview":
        return generate_audio_overview(tenant_id, focus, style, count, language)
    if artifact_type == "video_overview":
        return generate_video_overview(tenant_id, focus, count, language)
    if artifact_type == "slide_deck":
        return generate_slide_deck(tenant_id, focus, count, language)
    if artifact_type == "flashcards":
        return generate_flashcards(tenant_id, focus, count, language)
    if artifact_type == "infographic":
        return generate_infographic(tenant_id, focus, count, language)
    raise ValueError(f"Unsupported artifact type: {artifact_type}")
