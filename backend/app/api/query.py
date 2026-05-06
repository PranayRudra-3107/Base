from fastapi import APIRouter, Header, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from app.services.audit_log import write_audit_event
from app.services.rag import query_rag

router = APIRouter()


class ChatMessage(BaseModel):
    role: str  # "user" or "assistant"
    content: str


class QueryRequest(BaseModel):
    question: str
    chat_history: Optional[List[ChatMessage]] = []
    language: str = "en"


class Source(BaseModel):
    filename: str
    document_id: str
    relevance_score: float


class QueryResponse(BaseModel):
    answer: str
    sources: List[Source]
    chunks_used: int
    tokens_used: Optional[int] = None


@router.post("/", response_model=QueryResponse)
async def query_documents(
    request: QueryRequest,
    x_tenant_id: str = Header(default="default")
):
    """Ask a question against the tenant's indexed documents."""
    if not request.question.strip():
        raise HTTPException(status_code=400, detail="Question cannot be empty.")

    if len(request.question) > 2000:
        raise HTTPException(status_code=400, detail="Question too long. Max 2000 chars.")

    history = [{"role": m.role, "content": m.content} for m in (request.chat_history or [])]

    try:
        result = query_rag(
            tenant_id=x_tenant_id,
            question=request.question,
            chat_history=history,
            language=request.language,
        )
        write_audit_event(
            tenant_id=x_tenant_id,
            action="rag.query",
            details={
                "question_length": len(request.question),
                "chunks_used": result.get("chunks_used", 0),
                "language": request.language,
            },
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Query failed: {str(e)}")

    return QueryResponse(**result)
