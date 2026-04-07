import chromadb
from chromadb.utils import embedding_functions
from app.core.config import get_settings
from typing import List, Dict, Any
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


def add_chunks(tenant_id: str, chunks: List[str], metadatas: List[Dict[str, Any]]):
    collection = get_or_create_collection(tenant_id)
    ids = [str(uuid.uuid4()) for _ in chunks]
    collection.add(documents=chunks, metadatas=metadatas, ids=ids)
    return ids


def search_chunks(tenant_id: str, query: str, k: int = None) -> List[Dict]:
    k = k or settings.retrieval_k
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


def list_documents(tenant_id: str) -> List[Dict]:
    collection = get_or_create_collection(tenant_id)
    results = collection.get()
    seen = {}
    for meta in results.get("metadatas", []):
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


def delete_document(tenant_id: str, document_id: str):
    collection = get_or_create_collection(tenant_id)
    results = collection.get(where={"document_id": document_id})
    if results["ids"]:
        collection.delete(ids=results["ids"])
    return len(results["ids"])
