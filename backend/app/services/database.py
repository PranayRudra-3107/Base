from datetime import datetime
from typing import Any, Dict, List

from app.core.config import get_settings

settings = get_settings()
_metadata_schema_ready = False
_vector_schema_ready = False


def postgres_enabled() -> bool:
    return bool(settings.database_url) and settings.metadata_backend.lower() == "postgres"


def pgvector_enabled() -> bool:
    return bool(settings.database_url) and settings.vector_backend.lower() == "pgvector"


def _connect(row_factory=None):
    if not settings.database_url:
        raise RuntimeError("DATABASE_URL is required for Postgres-backed storage.")

    import psycopg
    from psycopg.rows import dict_row

    return psycopg.connect(settings.database_url, row_factory=row_factory or dict_row)


def _jsonb(value: Any):
    from psycopg.types.json import Jsonb

    return Jsonb(value)


def init_metadata_schema() -> None:
    global _metadata_schema_ready
    if _metadata_schema_ready:
        return
    if not postgres_enabled():
        return
    with _connect() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                CREATE TABLE IF NOT EXISTS base_json_store (
                    tenant_id TEXT NOT NULL,
                    name TEXT NOT NULL,
                    payload JSONB NOT NULL,
                    updated_at TIMESTAMPTZ NOT NULL DEFAULT now(),
                    PRIMARY KEY (tenant_id, name)
                );

                CREATE TABLE IF NOT EXISTS base_audit_events (
                    id BIGSERIAL PRIMARY KEY,
                    timestamp TEXT NOT NULL,
                    tenant_id TEXT NOT NULL,
                    actor TEXT NOT NULL,
                    action TEXT NOT NULL,
                    details JSONB NOT NULL DEFAULT '{}'::jsonb
                );

                CREATE INDEX IF NOT EXISTS base_audit_events_tenant_time_idx
                    ON base_audit_events (tenant_id, id DESC);
                """
            )
        conn.commit()
    _metadata_schema_ready = True


def read_json_record(tenant_id: str, name: str, default: Any) -> Any:
    init_metadata_schema()
    with _connect() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT payload
                FROM base_json_store
                WHERE tenant_id = %s AND name = %s
                """,
                (tenant_id, name),
            )
            row = cur.fetchone()
    return row["payload"] if row else default


def write_json_record(tenant_id: str, name: str, data: Any) -> None:
    init_metadata_schema()
    with _connect() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO base_json_store (tenant_id, name, payload, updated_at)
                VALUES (%s, %s, %s, now())
                ON CONFLICT (tenant_id, name)
                DO UPDATE SET payload = EXCLUDED.payload, updated_at = now()
                """,
                (tenant_id, name, _jsonb(data)),
            )
        conn.commit()


def write_audit_record(tenant_id: str, action: str, actor: str, details: Dict = None) -> Dict:
    init_metadata_schema()
    event = {
        "timestamp": datetime.utcnow().isoformat(),
        "tenant_id": tenant_id,
        "actor": actor,
        "action": action,
        "details": details or {},
    }
    with _connect() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO base_audit_events (timestamp, tenant_id, actor, action, details)
                VALUES (%s, %s, %s, %s, %s)
                """,
                (
                    event["timestamp"],
                    event["tenant_id"],
                    event["actor"],
                    event["action"],
                    _jsonb(event["details"]),
                ),
            )
        conn.commit()
    return event


def read_audit_records(tenant_id: str, limit: int = 100) -> List[Dict]:
    init_metadata_schema()
    with _connect() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT timestamp, tenant_id, actor, action, details
                FROM base_audit_events
                WHERE tenant_id = %s
                ORDER BY id DESC
                LIMIT %s
                """,
                (tenant_id, limit),
            )
            rows = cur.fetchall()
    return rows


def delete_tenant_records(tenant_id: str) -> Dict[str, int]:
    """Delete project-scoped metadata and audit rows from Postgres."""
    init_metadata_schema()
    with _connect() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "DELETE FROM base_json_store WHERE tenant_id = %s RETURNING name",
                (tenant_id,),
            )
            metadata_deleted = len(cur.fetchall())
            cur.execute(
                "DELETE FROM base_audit_events WHERE tenant_id = %s RETURNING id",
                (tenant_id,),
            )
            audit_deleted = len(cur.fetchall())
        conn.commit()
    return {
        "metadata_records_deleted": metadata_deleted,
        "audit_events_deleted": audit_deleted,
    }


def init_vector_schema() -> None:
    global _vector_schema_ready
    if _vector_schema_ready:
        return
    if not pgvector_enabled():
        return
    with _connect() as conn:
        with conn.cursor() as cur:
            cur.execute("CREATE EXTENSION IF NOT EXISTS vector;")
            cur.execute(
                f"""
                CREATE TABLE IF NOT EXISTS base_vector_chunks (
                    id TEXT PRIMARY KEY,
                    tenant_id TEXT NOT NULL,
                    document_id TEXT NOT NULL,
                    filename TEXT NOT NULL,
                    chunk_index INTEGER NOT NULL,
                    total_chunks INTEGER NOT NULL,
                    uploaded_at TEXT NOT NULL,
                    text TEXT NOT NULL,
                    metadata JSONB NOT NULL DEFAULT '{{}}'::jsonb,
                    embedding vector({settings.embedding_dimensions}) NOT NULL,
                    created_at TIMESTAMPTZ NOT NULL DEFAULT now()
                );

                CREATE INDEX IF NOT EXISTS base_vector_chunks_tenant_idx
                    ON base_vector_chunks (tenant_id);

                CREATE INDEX IF NOT EXISTS base_vector_chunks_document_idx
                    ON base_vector_chunks (tenant_id, document_id);
                """
            )
        conn.commit()
    try:
        with _connect() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    CREATE INDEX IF NOT EXISTS base_vector_chunks_embedding_hnsw_idx
                        ON base_vector_chunks
                        USING hnsw (embedding vector_cosine_ops);
                    """
                )
            conn.commit()
    except Exception:
        with _connect() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    CREATE INDEX IF NOT EXISTS base_vector_chunks_embedding_ivfflat_idx
                        ON base_vector_chunks
                        USING ivfflat (embedding vector_cosine_ops)
                        WITH (lists = 100);
                    """
                )
            conn.commit()
    _vector_schema_ready = True


def vector_connection():
    init_vector_schema()
    return _connect()


def delete_tenant_vectors(tenant_id: str) -> int:
    """Delete all pgvector chunks owned by one project."""
    init_vector_schema()
    with _connect() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "DELETE FROM base_vector_chunks WHERE tenant_id = %s RETURNING id",
                (tenant_id,),
            )
            deleted = len(cur.fetchall())
        conn.commit()
    return deleted
