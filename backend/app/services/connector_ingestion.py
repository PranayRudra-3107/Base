from typing import Any, Dict

from app.services.analytics import analyze_document
from app.services.audit_log import write_audit_event
from app.services.ingestion import process_file_details
from app.services.projects import touch_project
from app.services.storage import save_raw_document, upsert_document_analysis
from app.services.vector_store import add_chunks


def ingest_connector_text(
    tenant_id: str,
    connector_id: str,
    connector_name: str,
    filename: str,
    text: str,
    metadata: Dict[str, Any] = None,
) -> Dict[str, Any]:
    """Index connector output through the same path used by uploaded files."""
    if not text.strip():
        raise ValueError("Connector returned no text to index.")

    safe_filename = filename if filename.lower().endswith((".md", ".txt", ".csv")) else f"{filename}.md"
    file_bytes = text.encode("utf-8")
    details = process_file_details(safe_filename, file_bytes)
    extra_metadata = {
        "source": "connector",
        "connector_id": connector_id,
        "connector_name": connector_name,
        **(metadata or {}),
    }
    metadatas = [{**item, **extra_metadata} for item in details["metadatas"]]

    chunk_ids = add_chunks(
        tenant_id=tenant_id,
        chunks=details["chunks"],
        metadatas=metadatas,
    )
    document_id = details["document_id"]
    storage_path = save_raw_document(tenant_id, document_id, safe_filename, file_bytes)
    analysis = analyze_document(
        document_id=document_id,
        filename=safe_filename,
        text=details["text"],
        uploaded_at=details["uploaded_at"],
        storage_path=storage_path,
    )
    analysis["chunk_count"] = len(chunk_ids)
    analysis["source"] = "connector"
    analysis["connector_id"] = connector_id
    analysis["connector_name"] = connector_name
    upsert_document_analysis(tenant_id, analysis)
    touch_project(tenant_id)
    write_audit_event(
        tenant_id=tenant_id,
        action="connector.synced",
        details={
            "connector_id": connector_id,
            "connector_name": connector_name,
            "document_id": document_id,
            "filename": safe_filename,
            "chunks_created": len(chunk_ids),
            "validation_issues": len(analysis["validation_issues"]),
        },
    )
    return {
        "document_id": document_id,
        "filename": safe_filename,
        "chunks_created": len(chunk_ids),
        "analysis": analysis,
    }
