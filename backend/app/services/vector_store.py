import chromadb
from openai import OpenAI
from chromadb.utils import embedding_functions
from app.core.config import get_settings
from app.services.database import delete_tenant_vectors, pgvector_enabled, vector_connection
from app.services.ingestion import chunk_text, extract_text
from app.services.storage import list_document_analyses, read_json, read_raw_document, write_json
from typing import List, Dict, Any
from collections import Counter
from pathlib import Path
import re
import uuid
import math

settings = get_settings()

TOKEN_RE = re.compile(r"[a-zA-Z0-9][a-zA-Z0-9_.:/#-]{1,}")
SEMANTIC_WEIGHT = 0.68
KEYWORD_WEIGHT = 0.32
IDENTIFIER_MATCH_BOOST = 0.4
STOP_WORDS = {
    "a", "an", "and", "are", "as", "at", "be", "by", "can", "did", "do",
    "does", "for", "from", "had", "has", "have", "how", "i", "in", "is",
    "it", "of", "on", "or", "our", "show", "that", "the", "this", "to",
    "was", "were", "what", "when", "where", "which", "who", "why", "with",
}


def _collection_name(tenant_id: str) -> str:
    safe_tenant = re.sub(r"[^a-zA-Z0-9_-]", "_", tenant_id or "default")
    safe_tenant = safe_tenant.strip("_-") or "default"
    return f"tenant_{safe_tenant}"[:63].rstrip("_-")


def get_chroma_client():
    return chromadb.PersistentClient(path=settings.chroma_persist_dir)


def get_or_create_collection(tenant_id: str):
    client = get_chroma_client()
    ef = embedding_functions.OpenAIEmbeddingFunction(
        api_key=settings.openai_api_key,
        model_name=settings.embedding_model
    )
    collection_name = _collection_name(tenant_id)
    return client.get_or_create_collection(
        name=collection_name,
        embedding_function=ef,
        metadata={"hnsw:space": "cosine"}
    )


def _vector_literal(values: List[float]) -> str:
    return "[" + ",".join(f"{float(value):.8f}" for value in values) + "]"


def _embed_texts(texts: List[str]) -> List[List[float]]:
    if not texts:
        return []
    client = OpenAI(api_key=settings.openai_api_key)
    embeddings = []
    batch_size = 64
    for start in range(0, len(texts), batch_size):
        batch = texts[start:start + batch_size]
        response = client.embeddings.create(
            model=settings.embedding_model,
            input=batch,
        )
        ordered = sorted(response.data, key=lambda item: item.index)
        embeddings.extend(item.embedding for item in ordered)
    return embeddings


def _fallback_chunks(tenant_id: str) -> List[Dict[str, Any]]:
    return read_json(tenant_id, "keyword_chunks", [])


def _write_fallback_chunks(tenant_id: str, chunks: List[Dict[str, Any]]) -> None:
    write_json(tenant_id, "keyword_chunks", chunks)


def _append_keyword_chunks(tenant_id: str, rows: List[Dict[str, Any]]) -> None:
    stored = _fallback_chunks(tenant_id)
    stored.extend(rows)
    _write_fallback_chunks(tenant_id, stored)


def _delete_keyword_document(tenant_id: str, document_id: str) -> int:
    stored = _fallback_chunks(tenant_id)
    kept = [
        chunk for chunk in stored
        if chunk.get("metadata", {}).get("document_id") != document_id
    ]
    _write_fallback_chunks(tenant_id, kept)
    return len(stored) - len(kept)


def _resolve_storage_path(storage_path: str) -> Path:
    path = Path(storage_path or "")
    if path.exists():
        return path
    backend_root = Path(__file__).resolve().parents[2]
    candidate = backend_root / storage_path
    return candidate


def _keyword_cache_chunks(tenant_id: str) -> List[Dict[str, Any]]:
    stored = _fallback_chunks(tenant_id)
    cached_docs = {
        chunk.get("metadata", {}).get("document_id")
        for chunk in stored
        if chunk.get("metadata", {}).get("document_id")
    }
    backfilled = []
    for analysis in list_document_analyses(tenant_id):
        document_id = analysis.get("document_id")
        filename = analysis.get("filename", "unknown")
        if not document_id or document_id in cached_docs:
            continue
        try:
            storage_path = analysis.get("storage_path", "")
            if storage_path and not storage_path.startswith("s3://"):
                path = _resolve_storage_path(storage_path)
                if not path.exists():
                    continue
                file_bytes = path.read_bytes()
            else:
                file_bytes = read_raw_document(storage_path)
            text = extract_text(filename, file_bytes)
            chunks = chunk_text(text)
        except Exception:
            continue
        for index, chunk in enumerate(chunks):
            backfilled.append({
                "id": str(uuid.uuid4()),
                "text": chunk,
                "metadata": {
                    "document_id": document_id,
                    "filename": filename,
                    "chunk_index": index,
                    "total_chunks": len(chunks),
                    "uploaded_at": analysis.get("uploaded_at", ""),
                },
            })
        cached_docs.add(document_id)
    if backfilled:
        stored = [*stored, *backfilled]
        _write_fallback_chunks(tenant_id, stored)
    return stored


def _tokenize(value: str) -> List[str]:
    return [token.lower() for token in TOKEN_RE.findall(value or "")]


def _looks_like_identifier(token: str) -> bool:
    return any(char.isdigit() for char in token) or any(char in token for char in "-_:/#.")


def _query_tokens(value: str) -> List[str]:
    return [
        token for token in _tokenize(value)
        if token not in STOP_WORDS or _looks_like_identifier(token)
    ]


def _chunk_key(chunk: Dict[str, Any]) -> str:
    metadata = chunk.get("metadata", {}) or {}
    return chunk.get("id") or "|".join([
        metadata.get("document_id", "unknown"),
        str(metadata.get("chunk_index", "")),
        chunk.get("text", "")[:80],
    ])


def _normalize_score(score: Any) -> float:
    try:
        return max(0.0, min(1.0, float(score)))
    except (TypeError, ValueError):
        return 0.0


def _metadata_from_row(row: Dict[str, Any]) -> Dict[str, Any]:
    metadata = dict(row.get("metadata") or {})
    metadata.update({
        "document_id": row.get("document_id", metadata.get("document_id", "")),
        "filename": row.get("filename", metadata.get("filename", "unknown")),
        "chunk_index": row.get("chunk_index", metadata.get("chunk_index", 0)),
        "total_chunks": row.get("total_chunks", metadata.get("total_chunks", 0)),
        "uploaded_at": row.get("uploaded_at", metadata.get("uploaded_at", "")),
    })
    return metadata


def _pgvector_add_chunks(tenant_id: str, chunks: List[str], metadatas: List[Dict[str, Any]], ids: List[str]) -> None:
    from psycopg.types.json import Jsonb

    embeddings = _embed_texts(chunks)
    with vector_connection() as conn:
        with conn.cursor() as cur:
            for chunk_id, chunk, metadata, embedding in zip(ids, chunks, metadatas, embeddings):
                cur.execute(
                    """
                    INSERT INTO base_vector_chunks (
                        id, tenant_id, document_id, filename, chunk_index, total_chunks,
                        uploaded_at, text, metadata, embedding
                    )
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s::vector)
                    ON CONFLICT (id) DO UPDATE SET
                        text = EXCLUDED.text,
                        metadata = EXCLUDED.metadata,
                        embedding = EXCLUDED.embedding
                    """,
                    (
                        chunk_id,
                        tenant_id,
                        metadata.get("document_id", ""),
                        metadata.get("filename", "unknown"),
                        int(metadata.get("chunk_index", 0)),
                        int(metadata.get("total_chunks", len(chunks))),
                        metadata.get("uploaded_at", ""),
                        chunk,
                        Jsonb(metadata),
                        _vector_literal(embedding),
                    ),
                )
        conn.commit()


def _pgvector_all_chunks(tenant_id: str) -> List[Dict[str, Any]]:
    with vector_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT id, document_id, filename, chunk_index, total_chunks, uploaded_at, text, metadata
                FROM base_vector_chunks
                WHERE tenant_id = %s
                ORDER BY document_id, chunk_index
                """,
                (tenant_id,),
            )
            rows = cur.fetchall()
    return [
        {
            "id": row["id"],
            "text": row["text"] or "",
            "metadata": _metadata_from_row(row),
        }
        for row in rows
    ]


def _pgvector_search_chunks(tenant_id: str, query: str, k: int) -> List[Dict[str, Any]]:
    query_embedding = _embed_texts([query])[0]
    vector = _vector_literal(query_embedding)
    with vector_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT
                    id,
                    document_id,
                    filename,
                    chunk_index,
                    total_chunks,
                    uploaded_at,
                    text,
                    metadata,
                    embedding <=> %s::vector AS distance
                FROM base_vector_chunks
                WHERE tenant_id = %s
                ORDER BY embedding <=> %s::vector
                LIMIT %s
                """,
                (vector, tenant_id, vector, k),
            )
            rows = cur.fetchall()
    chunks = []
    for row in rows:
        score = _normalize_score(1 - float(row["distance"]))
        chunks.append({
            "id": row["id"],
            "text": row["text"] or "",
            "metadata": _metadata_from_row(row),
            "score": score,
            "semantic_score": score,
            "keyword_score": 0,
            "retrieval_mode": "semantic",
        })
    return chunks


def _pgvector_list_documents(tenant_id: str) -> List[Dict]:
    with vector_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT
                    document_id,
                    MIN(filename) AS filename,
                    MIN(uploaded_at) AS uploaded_at,
                    COUNT(*) AS chunk_count
                FROM base_vector_chunks
                WHERE tenant_id = %s
                GROUP BY document_id
                ORDER BY uploaded_at DESC
                """,
                (tenant_id,),
            )
            rows = cur.fetchall()
    return [dict(row) for row in rows]


def _pgvector_delete_document(tenant_id: str, document_id: str) -> int:
    with vector_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                DELETE FROM base_vector_chunks
                WHERE tenant_id = %s AND document_id = %s
                RETURNING id
                """,
                (tenant_id, document_id),
            )
            deleted = cur.fetchall()
        conn.commit()
    return len(deleted)


def _all_indexed_chunks(tenant_id: str) -> List[Dict[str, Any]]:
    if pgvector_enabled():
        try:
            chunks = _pgvector_all_chunks(tenant_id)
            return chunks or _keyword_cache_chunks(tenant_id)
        except Exception:
            return _keyword_cache_chunks(tenant_id)

    try:
        collection = get_or_create_collection(tenant_id)
        results = collection.get(include=["documents", "metadatas"])
        chunks = [
            {
                "id": chunk_id,
                "text": doc or "",
                "metadata": meta or {},
            }
            for chunk_id, doc, meta in zip(
                results.get("ids", []),
                results.get("documents", []),
                results.get("metadatas", []),
            )
        ]
        return chunks or _keyword_cache_chunks(tenant_id)
    except Exception:
        return _keyword_cache_chunks(tenant_id)


def _semantic_search_chunks(tenant_id: str, query: str, k: int) -> List[Dict[str, Any]]:
    if pgvector_enabled():
        return _pgvector_search_chunks(tenant_id, query, k)

    collection = get_or_create_collection(tenant_id)
    count = collection.count()
    if count <= 0:
        return []
    results = collection.query(
        query_texts=[query],
        n_results=min(k, count)
    )
    chunks = []
    if results["documents"] and results["documents"][0]:
        for chunk_id, doc, meta, dist in zip(
            results["ids"][0],
            results["documents"][0],
            results["metadatas"][0],
            results["distances"][0],
        ):
            score = _normalize_score(1 - dist)
            chunks.append({
                "id": chunk_id,
                "text": doc,
                "metadata": meta,
                "score": score,
                "semantic_score": score,
                "keyword_score": 0,
                "retrieval_mode": "semantic",
            })
    return chunks


def _bm25_search_chunks(query: str, chunks: List[Dict[str, Any]], k: int) -> List[Dict[str, Any]]:
    query_terms = _query_tokens(query)
    if not query_terms or not chunks:
        return []

    query_counts = Counter(query_terms)
    identifier_terms = {term for term in query_counts if _looks_like_identifier(term)}
    chunk_terms = []
    document_frequency = Counter()
    for chunk in chunks:
        counts = Counter(_tokenize(chunk.get("text", "")))
        chunk_terms.append(counts)
        document_frequency.update(counts.keys())

    total_chunks = len(chunks)
    avg_len = sum(sum(counts.values()) for counts in chunk_terms) / total_chunks if total_chunks else 0
    if avg_len <= 0:
        return []

    k1 = 1.5
    b = 0.75
    exact_phrase = (query or "").strip().lower()
    scored = []

    for chunk, counts in zip(chunks, chunk_terms):
        doc_len = sum(counts.values())
        if doc_len <= 0:
            continue
        score = 0.0
        matched_terms = []
        for term, query_count in query_counts.items():
            frequency = counts.get(term, 0)
            if frequency <= 0:
                continue
            df = document_frequency.get(term, 0)
            idf = math.log(1 + ((total_chunks - df + 0.5) / (df + 0.5)))
            numerator = frequency * (k1 + 1)
            denominator = frequency + k1 * (1 - b + b * (doc_len / avg_len))
            score += idf * (numerator / denominator) * min(query_count, 2)
            matched_terms.append(term)

        text_lower = chunk.get("text", "").lower()
        if exact_phrase and len(exact_phrase) >= 4 and exact_phrase in text_lower:
            score += 1.5
        matched_identifiers = [term for term in matched_terms if term in identifier_terms]
        if matched_identifiers:
            score += IDENTIFIER_MATCH_BOOST * len(matched_identifiers)

        if score > 0:
            scored.append({
                "id": _chunk_key(chunk),
                "text": chunk.get("text", ""),
                "metadata": chunk.get("metadata", {}),
                "score": score,
                "semantic_score": 0,
                "keyword_score": score,
                "retrieval_mode": "keyword",
                "matched_terms": matched_terms[:8],
                "exact_identifier_match": bool(matched_identifiers),
            })

    return sorted(scored, key=lambda item: item["score"], reverse=True)[:k]


def _merge_hybrid_results(semantic_chunks: List[Dict[str, Any]], keyword_chunks: List[Dict[str, Any]], k: int) -> List[Dict[str, Any]]:
    merged: Dict[str, Dict[str, Any]] = {}
    max_keyword = max((chunk.get("keyword_score", 0) for chunk in keyword_chunks), default=0) or 1

    for chunk in semantic_chunks:
        key = _chunk_key(chunk)
        semantic_score = _normalize_score(chunk.get("semantic_score", chunk.get("score", 0)))
        merged[key] = {
            **chunk,
            "score": semantic_score * SEMANTIC_WEIGHT,
            "semantic_score": semantic_score,
            "keyword_score": 0,
            "retrieval_mode": "semantic",
        }

    for chunk in keyword_chunks:
        key = _chunk_key(chunk)
        keyword_score = _normalize_score(chunk.get("keyword_score", 0) / max_keyword)
        identifier_boost = IDENTIFIER_MATCH_BOOST if chunk.get("exact_identifier_match") else 0
        existing = merged.get(key)
        if existing:
            existing["keyword_score"] = keyword_score
            existing["score"] = round(min(1.0, existing["semantic_score"] * SEMANTIC_WEIGHT + keyword_score * KEYWORD_WEIGHT + identifier_boost), 4)
            existing["retrieval_mode"] = "hybrid"
            if chunk.get("matched_terms"):
                existing["matched_terms"] = chunk["matched_terms"]
            if chunk.get("exact_identifier_match"):
                existing["exact_identifier_match"] = True
        else:
            merged[key] = {
                **chunk,
                "keyword_score": keyword_score,
                "score": round(min(1.0, keyword_score * KEYWORD_WEIGHT + identifier_boost), 4),
                "retrieval_mode": "keyword",
            }

    return sorted(merged.values(), key=lambda item: item["score"], reverse=True)[:k]


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
    keyword_rows = [
        {"id": chunk_id, "text": chunk, "metadata": metadata}
        for chunk_id, chunk, metadata in zip(ids, chunks, metadatas)
    ]
    if pgvector_enabled():
        _pgvector_add_chunks(tenant_id, chunks, metadatas, ids)
        _append_keyword_chunks(tenant_id, keyword_rows)
        return ids

    _append_keyword_chunks(tenant_id, keyword_rows)
    try:
        collection = get_or_create_collection(tenant_id)
        collection.add(documents=chunks, metadatas=metadatas, ids=ids)
    except Exception:
        pass
    return ids


def search_chunks(tenant_id: str, query: str, k: int = None) -> List[Dict]:
    k = k or settings.retrieval_k
    semantic_chunks = []
    try:
        semantic_chunks = _semantic_search_chunks(tenant_id, query, k * 2)
    except Exception:
        semantic_chunks = []
    keyword_chunks = _bm25_search_chunks(query, _all_indexed_chunks(tenant_id), k * 2)
    return _merge_hybrid_results(semantic_chunks, keyword_chunks, k)


def keyword_search_chunks(tenant_id: str, query: str, k: int = None) -> List[Dict]:
    k = k or settings.retrieval_k
    return _bm25_search_chunks(query, _keyword_cache_chunks(tenant_id), k)


def list_documents(tenant_id: str) -> List[Dict]:
    if pgvector_enabled():
        try:
            docs = _pgvector_list_documents(tenant_id)
            return docs or _list_documents_from_metadatas([
                chunk.get("metadata", {}) for chunk in _keyword_cache_chunks(tenant_id)
            ])
        except Exception:
            return _list_documents_from_metadatas([
                chunk.get("metadata", {}) for chunk in _keyword_cache_chunks(tenant_id)
            ])

    try:
        collection = get_or_create_collection(tenant_id)
        results = collection.get()
        return _list_documents_from_metadatas(results.get("metadatas", []))
    except Exception:
        return _list_documents_from_metadatas([
            chunk.get("metadata", {}) for chunk in _keyword_cache_chunks(tenant_id)
        ])


def delete_document(tenant_id: str, document_id: str):
    if pgvector_enabled():
        deleted = _pgvector_delete_document(tenant_id, document_id)
        keyword_deleted = _delete_keyword_document(tenant_id, document_id)
        return deleted or keyword_deleted

    try:
        collection = get_or_create_collection(tenant_id)
        results = collection.get(where={"document_id": document_id})
        if results["ids"]:
            collection.delete(ids=results["ids"])
        deleted = len(results["ids"])
        _delete_keyword_document(tenant_id, document_id)
        return deleted
    except Exception:
        return _delete_keyword_document(tenant_id, document_id)


def delete_project_index(tenant_id: str) -> int:
    """Delete every vector chunk associated with one project."""
    if pgvector_enabled():
        return delete_tenant_vectors(tenant_id)

    fallback_count = len(_fallback_chunks(tenant_id))
    client = get_chroma_client()
    collection_name = _collection_name(tenant_id)
    try:
        collection = client.get_collection(collection_name)
        deleted = collection.count()
    except Exception:
        deleted = 0
    try:
        client.delete_collection(collection_name)
    except Exception:
        pass
    return deleted or fallback_count
