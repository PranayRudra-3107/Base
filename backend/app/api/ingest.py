from fastapi import APIRouter, UploadFile, File, Header, HTTPException
from app.services.analytics import analyze_document
from app.services.audit_log import write_audit_event
from app.services.ingestion import process_file_details
from app.services.projects import touch_project
from app.services.storage import save_raw_document, upsert_document_analysis
from app.services.vector_store import add_chunks
from pydantic import BaseModel
from typing import List

router = APIRouter()


class IngestResponse(BaseModel):
    message: str
    document_id: str
    filename: str
    chunks_created: int
    validation_issues: List[str]
    kpis: dict


@router.post("/", response_model=IngestResponse)
async def ingest_document(
    file: UploadFile = File(...),
    x_tenant_id: str = Header(default="default")
):
    """Upload and index a project source for a tenant."""
    if not file.filename:
        raise HTTPException(status_code=400, detail="No filename provided.")

    ext = file.filename.lower().split(".")[-1]
    if ext not in ["pdf", "txt", "md", "csv"]:
        raise HTTPException(
            status_code=400,
            detail="Unsupported file type. Use PDF, TXT, MD, or CSV."
        )

    file_bytes = await file.read()

    if len(file_bytes) > 10 * 1024 * 1024:  # 10MB limit
        raise HTTPException(status_code=400, detail="File too large. Max 10MB.")

    try:
        details = process_file_details(file.filename, file_bytes)
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))

    ids = add_chunks(
        tenant_id=x_tenant_id,
        chunks=details["chunks"],
        metadatas=details["metadatas"],
    )
    document_id = details["document_id"]
    storage_path = save_raw_document(x_tenant_id, document_id, file.filename, file_bytes)
    analysis = analyze_document(
        document_id=document_id,
        filename=file.filename,
        text=details["text"],
        uploaded_at=details["uploaded_at"],
        storage_path=storage_path,
    )
    analysis["chunk_count"] = len(ids)
    upsert_document_analysis(x_tenant_id, analysis)
    touch_project(x_tenant_id)
    write_audit_event(
        tenant_id=x_tenant_id,
        action="document.ingested",
        details={
            "document_id": document_id,
            "filename": file.filename,
            "chunks_created": len(ids),
            "validation_issues": len(analysis["validation_issues"]),
            "risks": analysis["risk_count"],
            "blockers": analysis["blocker_count"],
            "tickets": analysis["ticket_count"],
        },
    )

    return IngestResponse(
        message="Project source ingested successfully.",
        document_id=document_id,
        filename=file.filename,
        chunks_created=len(ids),
        validation_issues=analysis["validation_issues"],
        kpis={
            "project_health_score": analysis["project_health_score"],
            "risk_count": analysis["risk_count"],
            "blocker_count": analysis["blocker_count"],
            "ticket_count": analysis["ticket_count"],
            "decision_count": analysis["decision_count"],
            "total_metric_value": analysis["total_metric_value"],
            "kt_readiness_score": analysis["kt_readiness_score"],
            # Legacy aliases for older clients.
            "total_amount": analysis["total_amount"],
            "exception_count": analysis["exception_count"],
            "compliance_ratio": analysis["compliance_ratio"],
        },
    )
