from fastapi import APIRouter, Header, HTTPException
from pydantic import BaseModel
from typing import List
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


@router.get("/", response_model=List[DocumentInfo])
async def get_documents(x_tenant_id: str = Header(default="default")):
    """List all documents indexed for this tenant."""
    try:
        docs = list_documents(x_tenant_id)
        return docs
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/{document_id}", response_model=DeleteResponse)
async def delete_doc(
    document_id: str,
    x_tenant_id: str = Header(default="default")
):
    """Delete a document and all its chunks from the index."""
    try:
        count = delete_document(x_tenant_id, document_id)
        if count == 0:
            raise HTTPException(status_code=404, detail="Document not found.")
        return DeleteResponse(
            message="Document deleted successfully.",
            chunks_deleted=count
        )
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
