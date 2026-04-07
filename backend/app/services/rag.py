from openai import OpenAI
from app.core.config import get_settings
from app.services.vector_store import search_chunks
from typing import List, Dict

settings = get_settings()
client = OpenAI(api_key=settings.openai_api_key)

SYSTEM_PROMPT = """You are a helpful enterprise knowledge assistant.
Answer questions based ONLY on the provided context documents.
If the context doesn't contain enough information to answer, say so clearly.
Always be concise, accurate, and cite which document your answer comes from.
Do not make up information."""


def build_context(chunks: List[Dict]) -> str:
    context_parts = []
    for i, chunk in enumerate(chunks):
        filename = chunk["metadata"].get("filename", "Unknown")
        context_parts.append(f"[Source {i+1}: {filename}]\n{chunk['text']}")
    return "\n\n---\n\n".join(context_parts)


def query_rag(tenant_id: str, question: str, chat_history: List[Dict] = None) -> Dict:
    # 1. Retrieve relevant chunks
    chunks = search_chunks(tenant_id, question)

    if not chunks:
        return {
            "answer": "No relevant documents found. Please upload documents first.",
            "sources": [],
            "chunks_used": 0
        }

    # 2. Build context from retrieved chunks
    context = build_context(chunks)

    # 3. Build messages
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]

    # Include recent chat history for multi-turn conversations
    if chat_history:
        for msg in chat_history[-6:]:  # last 3 exchanges
            messages.append(msg)

    messages.append({
        "role": "user",
        "content": f"""Context documents:
{context}

Question: {question}

Answer based on the context above:"""
    })

    # 4. Call LLM
    response = client.chat.completions.create(
        model=settings.llm_model,
        messages=messages,
        temperature=0.1,
        max_tokens=1000
    )

    answer = response.choices[0].message.content

    # 5. Build source citations
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
                "relevance_score": chunk["score"]
            })

    return {
        "answer": answer,
        "sources": sources,
        "chunks_used": len(chunks),
        "tokens_used": response.usage.total_tokens
    }
