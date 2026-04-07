from fastapi import APIRouter, UploadFile, File, Header, HTTPException
from app.services.ingestion import process_file
from app.services.vector_store import add_chunks
from pydantic import BaseModel

router = APIRouter()


class IngestResponse(BaseModel):
    message: str
    document_id: str
    filename: str
    chunks_created: int


@router.post("/", response_model=IngestResponse)
async def ingest_document(
    file: UploadFile = File(...),
    x_tenant_id: str = Header(default="default")
):
    """Upload and index a document for a tenant."""
    if not file.filename:
        raise HTTPException(status_code=400, detail="No filename provided.")

    ext = file.filename.lower().split(".")[-1]
    if ext not in ["pdf", "txt", "md"]:
        raise HTTPException(
            status_code=400,
            detail="Unsupported file type. Use PDF, TXT, or MD."
        )

    file_bytes = await file.read()

    if len(file_bytes) > 10 * 1024 * 1024:  # 10MB limit
        raise HTTPException(status_code=400, detail="File too large. Max 10MB.")

    try:
        chunks, metadatas = process_file(file.filename, file_bytes)
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))

    ids = add_chunks(tenant_id=x_tenant_id, chunks=chunks, metadatas=metadatas)
    document_id = metadatas[0]["document_id"]

    return IngestResponse(
        message="Document ingested successfully.",
        document_id=document_id,
        filename=file.filename,
        chunks_created=len(ids)
    )
