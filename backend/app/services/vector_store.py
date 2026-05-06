import chromadb
from chromadb.utils import embedding_functions
from app.core.config import get_settings
from app.services.storage import read_json, write_json
from typing import List, Dict, Any
import re
import uuid

settings = get_settings()


def get_chroma_client():
    return chromadb.PersistentClient(path=settings.chroma_persist_dir)


def get_or_create_collection(tenant_id: str):
    client = get_chroma_client()
    ef = embedding_functions.OpenAIEmbeddingFunction(
        api_key=settings.openai_api_key,
        model_name=settings.embedding_model
    )
    collection_name = f"tenant_{tenant_id}"
    return client.get_or_create_collection(
        name=collection_name,
        embedding_function=ef,
        metadata={"hnsw:space": "cosine"}
    )


def _fallback_chunks(tenant_id: str) -> List[Dict[str, Any]]:
    return read_json(tenant_id, "keyword_chunks", [])


def _write_fallback_chunks(tenant_id: str, chunks: List[Dict[str, Any]]) -> None:
    write_json(tenant_id, "keyword_chunks", chunks)


def _keyword_score(query: str, text: str) -> float:
    terms = set(re.findall(r"[a-zA-Z0-9]{3,}", query.lower()))
    if not terms:
        return 0
    haystack = text.lower()
    hits = sum(1 for term in terms if term in haystack)
    return round(hits / len(terms), 4)


def _list_documents_from_metadatas(metadatas: List[Dict]) -> List[Dict]:
    seen = {}
    for meta in metadatas:
        doc_id = meta.get("document_id", "unknown")
        if doc_id not in seen:
            seen[doc_id] = {
                "document_id": doc_id,
                "filename": meta.get("filename", "unknown"),
                "uploaded_at": meta.get("uploaded_at", ""),
                "chunk_count": 0
            }
        seen[doc_id]["chunk_count"] += 1
    return list(seen.values())


def add_chunks(tenant_id: str, chunks: List[str], metadatas: List[Dict[str, Any]]):
    ids = [str(uuid.uuid4()) for _ in chunks]
    try:
        collection = get_or_create_collection(tenant_id)
        collection.add(documents=chunks, metadatas=metadatas, ids=ids)
    except Exception:
        stored = _fallback_chunks(tenant_id)
        stored.extend(
            {"id": chunk_id, "text": chunk, "metadata": metadata}
            for chunk_id, chunk, metadata in zip(ids, chunks, metadatas)
        )
        _write_fallback_chunks(tenant_id, stored)
    return ids


def search_chunks(tenant_id: str, query: str, k: int = None) -> List[Dict]:
    k = k or settings.retrieval_k
    try:
        collection = get_or_create_collection(tenant_id)
        results = collection.query(
            query_texts=[query],
            n_results=min(k, collection.count() or 1)
        )
        chunks = []
        if results["documents"] and results["documents"][0]:
            for doc, meta, dist in zip(
                results["documents"][0],
                results["metadatas"][0],
                results["distances"][0]
            ):
                chunks.append({
                    "text": doc,
                    "metadata": meta,
                    "score": round(1 - dist, 4)
                })
        return chunks
    except Exception:
        scored = []
        for chunk in _fallback_chunks(tenant_id):
            score = _keyword_score(query, chunk.get("text", ""))
            if score > 0:
                scored.append({
                    "text": chunk.get("text", ""),
                    "metadata": chunk.get("metadata", {}),
                    "score": score,
                })
        return sorted(scored, key=lambda item: item["score"], reverse=True)[:k]


def list_documents(tenant_id: str) -> List[Dict]:
    try:
        collection = get_or_create_collection(tenant_id)
        results = collection.get()
        return _list_documents_from_metadatas(results.get("metadatas", []))
    except Exception:
        return _list_documents_from_metadatas([
            chunk.get("metadata", {}) for chunk in _fallback_chunks(tenant_id)
        ])


def delete_document(tenant_id: str, document_id: str):
    try:
        collection = get_or_create_collection(tenant_id)
        results = collection.get(where={"document_id": document_id})
        if results["ids"]:
            collection.delete(ids=results["ids"])
        return len(results["ids"])
    except Exception:
        stored = _fallback_chunks(tenant_id)
        kept = [
            chunk for chunk in stored
            if chunk.get("metadata", {}).get("document_id") != document_id
        ]
        _write_fallback_chunks(tenant_id, kept)
        return len(stored) - len(kept)
