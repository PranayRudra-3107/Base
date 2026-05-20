from urllib.parse import urlparse

from openai import OpenAI
from app.core.config import get_settings
from app.services.vector_store import search_chunks
from typing import Callable, Dict, List, Optional

settings = get_settings()
client = OpenAI(api_key=settings.openai_api_key)

SYSTEM_PROMPT = """You are a helpful project intelligence and KT assistant.
Answer questions based ONLY on the provided project sources.
If the context doesn't contain enough information to answer, say so clearly.
Always be concise, accurate, and cite which source document your answer comes from.
Do not make up information.
Response language: {response_language}.
All user-facing prose must be written in {response_language}.
Keep source filenames, ticket IDs, PR IDs, release IDs, service names, metrics, URLs, and code terms unchanged."""

WEB_SYSTEM_PROMPT = """You are a helpful project intelligence and general research assistant.
Use live web search when answering general or current questions.
Answer in {response_language}.
Be concise, accurate, and include the most relevant source citations.
Do not invent facts. If the web results are insufficient or conflicting, say that clearly."""

LANGUAGE_NAMES = {
    "en": "English",
    "es": "Spanish",
    "fr": "French",
    "de": "German",
    "hi": "Hindi",
}

NO_SOURCE_MESSAGES = {
    "en": "No relevant project sources found. Please upload sources first.",
    "es": "No se encontraron fuentes relevantes del proyecto. Primero sube fuentes.",
    "fr": "Aucune source de projet pertinente n'a ete trouvee. Veuillez d'abord importer des sources.",
    "de": "Keine relevanten Projektquellen gefunden. Bitte lade zuerst Quellen hoch.",
    "hi": "\u0915\u094b\u0908 \u0938\u0902\u092c\u0902\u0927\u093f\u0924 \u092a\u094d\u0930\u094b\u091c\u0947\u0915\u094d\u091f \u0938\u094d\u0930\u094b\u0924 \u0928\u0939\u0940\u0902 \u092e\u093f\u0932\u093e\u0964 \u0915\u0943\u092a\u092f\u093e \u092a\u0939\u0932\u0947 \u0938\u094d\u0930\u094b\u0924 \u0905\u092a\u0932\u094b\u0921 \u0915\u0930\u0947\u0902\u0964",
}

LANGUAGE_ALIASES = {
    "english": "en",
    "spanish": "es",
    "espanol": "es",
    "espa\xf1ol": "es",
    "french": "fr",
    "francais": "fr",
    "fran\xe7ais": "fr",
    "german": "de",
    "deutsch": "de",
    "hindi": "hi",
}

EXPLICIT_WEB_TERMS = (
    "internet",
    "web",
    "online",
    "search the web",
    "google",
    "today",
    "latest",
    "recent",
    "news",
    "price",
    "weather",
)


def normalize_language(language: str = "en") -> str:
    raw = (language or "en").strip().lower().replace("_", "-")
    if raw in LANGUAGE_NAMES:
        return raw
    if "-" in raw and raw.split("-", 1)[0] in LANGUAGE_NAMES:
        return raw.split("-", 1)[0]
    return LANGUAGE_ALIASES.get(raw, "en")


def build_context(chunks: List[Dict]) -> str:
    context_parts = []
    for i, chunk in enumerate(chunks):
        filename = chunk["metadata"].get("filename", "Unknown")
        context_parts.append(f"[Source {i+1}: {filename}]\n{chunk['text']}")
    return "\n\n---\n\n".join(context_parts)


def emit_progress(progress_callback: Optional[Callable[[Dict], None]], stage: str, message: str, detail: str = "") -> None:
    if progress_callback:
        progress_callback({
            "stage": stage,
            "message": message,
            "detail": detail,
        })


def chunk_top_score(chunks: List[Dict]) -> float:
    scores = []
    for chunk in chunks:
        try:
            scores.append(float(chunk.get("score", 0) or 0))
        except (TypeError, ValueError):
            continue
    return max(scores, default=0)


def should_use_web_search(question: str, chunks: List[Dict]) -> bool:
    if not settings.web_search_enabled:
        return False
    if not chunks:
        return True
    question_lower = question.lower()
    if any(term in question_lower for term in EXPLICIT_WEB_TERMS):
        return True
    return chunk_top_score(chunks) < settings.web_search_min_relevance


def web_tool_config() -> Dict:
    context_size = settings.web_search_context_size
    if context_size not in {"low", "medium", "high"}:
        context_size = "medium"
    tool_type = settings.web_search_tool if settings.web_search_tool in {"web_search", "web_search_preview"} else "web_search"
    return {
        "type": tool_type,
        "search_context_size": context_size,
    }


def response_output_text(response) -> str:
    output_text = getattr(response, "output_text", "")
    if output_text:
        return output_text

    parts = []
    for item in getattr(response, "output", []) or []:
        if getattr(item, "type", "") != "message":
            continue
        for content in getattr(item, "content", []) or []:
            if getattr(content, "type", "") == "output_text":
                parts.append(getattr(content, "text", ""))
    return "\n".join(part for part in parts if part).strip()


def source_title_from_url(url: str) -> str:
    host = urlparse(url).netloc
    return host.replace("www.", "") or url


def add_web_source(sources: List[Dict], seen: set, url: str, title: str = "") -> None:
    if not url or url in seen:
        return
    seen.add(url)
    sources.append({
        "filename": title or source_title_from_url(url),
        "document_id": url,
        "relevance_score": 1,
        "source_type": "web",
        "url": url,
    })


def extract_web_sources(response) -> List[Dict]:
    sources = []
    seen = set()
    for item in getattr(response, "output", []) or []:
        if getattr(item, "type", "") == "message":
            for content in getattr(item, "content", []) or []:
                for annotation in getattr(content, "annotations", []) or []:
                    if getattr(annotation, "type", "") == "url_citation":
                        add_web_source(
                            sources,
                            seen,
                            getattr(annotation, "url", ""),
                            getattr(annotation, "title", ""),
                        )
        if getattr(item, "type", "") == "web_search_call":
            action = getattr(item, "action", None)
            for source in getattr(action, "sources", []) or []:
                add_web_source(sources, seen, getattr(source, "url", ""))
    return sources[:8]


def build_web_input(question: str, chat_history: List[Dict] = None) -> str:
    history_lines = []
    for msg in (chat_history or [])[-6:]:
        role = msg.get("role", "user")
        content = msg.get("content", "")
        if content:
            history_lines.append(f"{role}: {content}")
    history = "\n".join(history_lines)
    if history:
        return f"Recent conversation:\n{history}\n\nQuestion:\n{question}"
    return question


def query_web(
    question: str,
    chat_history: List[Dict] = None,
    language: str = "en",
    progress_callback: Optional[Callable[[Dict], None]] = None,
) -> Dict:
    language_code = normalize_language(language)
    response_language = LANGUAGE_NAMES[language_code]
    emit_progress(
        progress_callback,
        "web",
        "Agent is searching the internet for this question.",
        "Using OpenAI web search to gather current public sources.",
    )
    response = client.responses.create(
        model=settings.web_search_model,
        instructions=WEB_SYSTEM_PROMPT.format(response_language=response_language),
        input=build_web_input(question, chat_history),
        tools=[web_tool_config()],
        tool_choice="auto",
        include=["web_search_call.action.sources"],
        max_output_tokens=1000,
    )
    emit_progress(
        progress_callback,
        "web_sources",
        "Agent is reviewing web citations.",
        "Extracting URLs and titles from the web search response.",
    )
    answer = response_output_text(response)
    sources = extract_web_sources(response)
    usage = getattr(response, "usage", None)
    return {
        "answer": answer or "I could not produce an internet answer from the available web results.",
        "sources": sources,
        "chunks_used": 0,
        "tokens_used": usage.total_tokens if usage else None,
        "answer_mode": "web",
    }


def query_rag(
    tenant_id: str,
    question: str,
    chat_history: List[Dict] = None,
    language: str = "en",
    progress_callback: Optional[Callable[[Dict], None]] = None,
    allow_web_search: bool = True,
) -> Dict:
    language_code = normalize_language(language)
    response_language = LANGUAGE_NAMES[language_code]

    # 1. Retrieve relevant chunks
    emit_progress(
        progress_callback,
        "prepare",
        "Agent is reading your question and preparing the retrieval plan.",
        "Checking the selected project workspace and response language.",
    )
    emit_progress(
        progress_callback,
        "retrieve",
        "Agent is gathering information related to this question.",
        "Running hybrid retrieval: semantic vector search plus rg-like keyword matching.",
    )
    chunks = search_chunks(tenant_id, question)

    if allow_web_search and should_use_web_search(question, chunks):
        reason = "No strong matching project source was found." if not chunks else "The strongest project match looked weak or the question requested current web context."
        emit_progress(
            progress_callback,
            "route",
            "Agent is switching to internet search.",
            reason,
        )
        try:
            return query_web(question, chat_history, language, progress_callback)
        except Exception as exc:
            emit_progress(
                progress_callback,
                "web_error",
                "Internet search failed.",
                str(exc),
            )
            if not chunks:
                return {
                    "answer": f"I could not search the internet for this question: {str(exc)}",
                    "sources": [],
                    "chunks_used": 0,
                    "tokens_used": None,
                    "answer_mode": "web_error",
                }

    if not chunks:
        emit_progress(
            progress_callback,
            "complete",
            "Agent could not find matching project sources.",
            "The answer will explain that more sources are needed.",
        )
        return {
            "answer": NO_SOURCE_MESSAGES[language_code],
            "sources": [],
            "chunks_used": 0
        }

    # 2. Build context from retrieved chunks
    filenames = []
    for chunk in chunks:
        filename = chunk["metadata"].get("filename", "Unknown")
        if filename not in filenames:
            filenames.append(filename)

    emit_progress(
        progress_callback,
        "context",
        f"Agent found {len(chunks)} relevant chunk(s) from {len(filenames)} source file(s).",
        "Merging semantic matches with exact keyword, ID, ticket, PR, and error-code matches.",
    )
    for filename in filenames[:4]:
        emit_progress(
            progress_callback,
            "document",
            f"Agent is going through {filename}.",
            "Extracting the most relevant facts, IDs, metrics, and decisions.",
        )
    if len(filenames) > 4:
        emit_progress(
            progress_callback,
            "document",
            f"Agent is also checking {len(filenames) - 4} additional source file(s).",
            "Keeping the context focused on the strongest matches.",
        )

    context = build_context(chunks)

    # 3. Build messages
    messages = [{"role": "system", "content": SYSTEM_PROMPT.format(response_language=response_language)}]

    # Include recent chat history for multi-turn conversations
    if chat_history:
        for msg in chat_history[-6:]:  # last 3 exchanges
            messages.append(msg)

    messages.append({
        "role": "user",
        "content": f"""Context project sources:
{context}

Question: {question}

Answer based on the context above. Respond only in {response_language}."""
    })

    # 4. Call LLM
    emit_progress(
        progress_callback,
        "generate",
        f"Agent is generating a source-grounded answer in {response_language}.",
        "Using only the retrieved project context and preserving source IDs.",
    )
    response = client.chat.completions.create(
        model=settings.llm_model,
        messages=messages,
        temperature=0.1,
        max_tokens=1000
    )

    answer = response.choices[0].message.content

    # 5. Build source citations
    emit_progress(
        progress_callback,
        "cite",
        "Agent is attaching source citations and confidence signals.",
        "Preparing filenames, document IDs, and relevance scores.",
    )
    sources = []
    seen_docs = set()
    for chunk in chunks:
        doc_id = chunk["metadata"].get("document_id")
        filename = chunk["metadata"].get("filename", "Unknown")
        if doc_id not in seen_docs:
            seen_docs.add(doc_id)
            sources.append({
                "filename": filename,
                "document_id": doc_id,
                "relevance_score": chunk["score"],
                "source_type": "project",
                "url": None,
                "retrieval_mode": chunk.get("retrieval_mode", "semantic"),
                "semantic_score": chunk.get("semantic_score", 0),
                "keyword_score": chunk.get("keyword_score", 0),
                "matched_terms": chunk.get("matched_terms", []),
            })

    usage = getattr(response, "usage", None)

    return {
        "answer": answer,
        "sources": sources,
        "chunks_used": len(chunks),
        "tokens_used": usage.total_tokens if usage else None,
        "answer_mode": "project",
    }
