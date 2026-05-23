from fastapi import APIRouter, Header, HTTPException
from pydantic import BaseModel
from typing import List
from app.services.audit_log import write_audit_event
from app.services.projects import touch_project
from app.services.storage import delete_document_analysis, delete_raw_document, list_document_analyses
from app.services.vector_store import list_documents, delete_document

router = APIRouter()


class DocumentInfo(BaseModel):
    document_id: str
    filename: str
    uploaded_at: str
    chunk_count: int


class DeleteResponse(BaseModel):
    message: str
    chunks_deleted: int


def merge_indexed_documents_with_analyses(indexed_docs: List[dict], analyses: List[dict]) -> List[dict]:
    docs_by_id = {doc.get("document_id"): doc for doc in indexed_docs}

    for analysis in analyses:
        document_id = analysis.get("document_id")
        if not document_id or document_id in docs_by_id:
            continue
        docs_by_id[document_id] = {
            "document_id": document_id,
            "filename": analysis.get("filename", "unknown"),
            "uploaded_at": analysis.get("uploaded_at", ""),
            "chunk_count": analysis.get("chunk_count", 0),
        }

    return sorted(
        docs_by_id.values(),
        key=lambda item: item.get("uploaded_at", ""),
        reverse=True,
    )


@router.get("/", response_model=List[DocumentInfo])
async def get_documents(x_tenant_id: str = Header(default="default")):
    """List all project sources indexed for this tenant."""
    try:
        docs = list_documents(x_tenant_id)
        analyses = list_document_analyses(x_tenant_id)
        return merge_indexed_documents_with_analyses(docs, analyses)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/{document_id}", response_model=DeleteResponse)
async def delete_doc(
    document_id: str,
    x_tenant_id: str = Header(default="default")
):
    """Delete a project source and all its chunks from the index."""
    try:
        analyses = list_document_analyses(x_tenant_id)
        analysis = next((item for item in analyses if item.get("document_id") == document_id), None)
        count = delete_document(x_tenant_id, document_id)
        analysis_deleted = delete_document_analysis(x_tenant_id, document_id)
        raw_deleted = False
        if analysis:
            raw_deleted = delete_raw_document(analysis.get("storage_path", ""))
        if count == 0 and not analysis_deleted:
            raise HTTPException(status_code=404, detail="Document not found.")
        touch_project(x_tenant_id)
        write_audit_event(
            tenant_id=x_tenant_id,
            action="document.deleted",
            details={"document_id": document_id, "chunks_deleted": count, "raw_deleted": raw_deleted},
        )
        return DeleteResponse(
            message="Project source deleted successfully.",
            chunks_deleted=count
        )
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
