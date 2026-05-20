import json
from queue import Queue
from threading import Thread

from fastapi import APIRouter, Header, HTTPException
from pydantic import BaseModel, Field
from starlette.responses import StreamingResponse
from typing import List, Literal, Optional
from app.services.audit_log import write_audit_event
from app.services.rag import query_rag
from app.services.studio import generate_artifact, generate_conversation, generate_quiz

router = APIRouter()


class ChatMessage(BaseModel):
    role: Literal["user", "assistant"]
    content: str


class QueryRequest(BaseModel):
    question: str
    chat_history: Optional[List[ChatMessage]] = Field(default_factory=list)
    language: Literal["en", "es", "fr", "de", "hi"] = "en"
    allow_web_search: bool = True


class KTRequest(BaseModel):
    focus: str = "project"
    audience: str = "new team member"
    language: Literal["en", "es", "fr", "de", "hi"] = "en"


class QuizRequest(BaseModel):
    focus: str = "project onboarding, risks, incidents, tickets, PRs, decisions, and metrics"
    difficulty: Literal["easy", "medium", "hard"] = "medium"
    count: int = Field(default=6, ge=3, le=12)
    language: Literal["en", "es", "fr", "de", "hi"] = "en"


class ConversationRequest(BaseModel):
    focus: str = "overall project overview, recent changes, risks, metrics, incidents, and handoff context"
    format: Literal["deep_dive", "brief", "critique", "debate"] = "deep_dive"
    length: Literal["short", "default", "long"] = "default"
    language: Literal["en", "es", "fr", "de", "hi"] = "en"


class StudioArtifactRequest(BaseModel):
    artifact_type: Literal["audio_overview", "video_overview", "slide_deck", "flashcards", "infographic"]
    focus: str = "overall project overview, recent changes, risks, metrics, incidents, and handoff context"
    style: Literal["default", "deep_dive", "brief", "critique", "debate"] = "default"
    count: int = Field(default=6, ge=3, le=12)
    language: Literal["en", "es", "fr", "de", "hi"] = "en"


class Source(BaseModel):
    filename: str
    document_id: str
    relevance_score: float
    source_type: str = "project"
    url: Optional[str] = None
    retrieval_mode: Optional[str] = None
    semantic_score: Optional[float] = None
    keyword_score: Optional[float] = None
    matched_terms: Optional[List[str]] = None


class QueryResponse(BaseModel):
    answer: str
    sources: List[Source]
    chunks_used: int
    tokens_used: Optional[int] = None


class QuizQuestion(BaseModel):
    id: str
    question: str
    options: List[str]
    answer_index: int
    hint: str = ""
    explanation: str = ""
    source_hint: str = ""


class QuizResponse(BaseModel):
    title: str
    difficulty: str
    questions: List[QuizQuestion]
    sources: List[Source]
    chunks_used: int
    tokens_used: Optional[int] = None


class ConversationTurn(BaseModel):
    speaker: str
    text: str


class ConversationResponse(BaseModel):
    title: str
    format: str
    turns: List[ConversationTurn]
    takeaways: List[str] = Field(default_factory=list)
    sources: List[Source]
    chunks_used: int
    tokens_used: Optional[int] = None


class StudioArtifactResponse(BaseModel):
    artifact_type: str
    title: str
    summary: str = ""
    cards: List[dict] = Field(default_factory=list)
    turns: List[dict] = Field(default_factory=list)
    scenes: List[dict] = Field(default_factory=list)
    slides: List[dict] = Field(default_factory=list)
    panels: List[dict] = Field(default_factory=list)
    sources: List[Source]
    chunks_used: int
    tokens_used: Optional[int] = None


def validate_question(request: QueryRequest) -> None:
    if not request.question.strip():
        raise HTTPException(status_code=400, detail="Question cannot be empty.")

    if len(request.question) > 2000:
        raise HTTPException(status_code=400, detail="Question too long. Max 2000 chars.")


def request_history(request: QueryRequest) -> List[dict]:
    return [{"role": m.role, "content": m.content} for m in (request.chat_history or [])]


def sse_event(event: str, data: dict) -> str:
    return f"event: {event}\ndata: {json.dumps(data)}\n\n"


def validate_kt_request(request: KTRequest) -> tuple[str, str]:
    focus = request.focus.strip() or "project"
    audience = request.audience.strip() or "new team member"

    if len(focus) > 500:
        raise HTTPException(status_code=400, detail="Focus too long. Max 500 chars.")
    if len(audience) > 200:
        raise HTTPException(status_code=400, detail="Audience too long. Max 200 chars.")

    return focus, audience


def validate_studio_focus(focus: str, label: str = "Focus") -> str:
    clean = focus.strip() or "project"
    if len(clean) > 500:
        raise HTTPException(status_code=400, detail=f"{label} too long. Max 500 chars.")
    return clean


def build_kt_question(focus: str, audience: str) -> str:
    return f"""Create a practical KT brief for {audience} focused on: {focus}.

Use only the uploaded project sources. Structure the brief with:
1. Project or module purpose
2. Important systems, components, and workflows
3. Current priorities, tickets, releases, or recent changes
4. Risks, blockers, incidents, and unresolved questions
5. Key metrics or health signals
6. Decisions, owners, and action items
7. First-week checklist for the audience

If a section is not supported by the sources, say what is missing."""


@router.post("/", response_model=QueryResponse)
async def query_documents(
    request: QueryRequest,
    x_tenant_id: str = Header(default="default")
):
    """Ask a question against the tenant's indexed project sources."""
    validate_question(request)
    history = request_history(request)

    try:
        result = query_rag(
            tenant_id=x_tenant_id,
            question=request.question,
            chat_history=history,
            language=request.language,
            allow_web_search=request.allow_web_search,
        )
        write_audit_event(
            tenant_id=x_tenant_id,
            action="rag.query",
            details={
                "question_length": len(request.question),
                "chunks_used": result.get("chunks_used", 0),
                "language": request.language,
                "answer_mode": result.get("answer_mode", "project"),
            },
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Query failed: {str(e)}")

    return QueryResponse(**result)


@router.post("/quiz", response_model=QuizResponse)
async def generate_project_quiz(
    request: QuizRequest,
    x_tenant_id: str = Header(default="default")
):
    """Generate an interactive source-grounded quiz from indexed project sources."""
    focus = validate_studio_focus(request.focus)
    try:
        result = generate_quiz(
            tenant_id=x_tenant_id,
            focus=focus,
            difficulty=request.difficulty,
            count=request.count,
            language=request.language,
        )
        write_audit_event(
            tenant_id=x_tenant_id,
            action="studio.quiz.generated",
            details={
                "focus_length": len(focus),
                "difficulty": request.difficulty,
                "count": request.count,
                "chunks_used": result.get("chunks_used", 0),
                "language": request.language,
            },
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Quiz generation failed: {str(e)}")
    return QuizResponse(**result)


@router.post("/conversation", response_model=ConversationResponse)
async def generate_project_conversation(
    request: ConversationRequest,
    x_tenant_id: str = Header(default="default")
):
    """Generate a NotebookLM-style source-grounded conversation transcript."""
    focus = validate_studio_focus(request.focus)
    try:
        result = generate_conversation(
            tenant_id=x_tenant_id,
            focus=focus,
            format_name=request.format,
            length=request.length,
            language=request.language,
        )
        write_audit_event(
            tenant_id=x_tenant_id,
            action="studio.conversation.generated",
            details={
                "focus_length": len(focus),
                "format": request.format,
                "length": request.length,
                "chunks_used": result.get("chunks_used", 0),
                "language": request.language,
            },
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Conversation generation failed: {str(e)}")
    return ConversationResponse(**result)


@router.post("/artifact", response_model=StudioArtifactResponse)
async def generate_studio_artifact(
    request: StudioArtifactRequest,
    x_tenant_id: str = Header(default="default")
):
    """Generate source-grounded Studio artifacts such as audio/video overviews, slides, flashcards, or infographics."""
    focus = validate_studio_focus(request.focus)
    try:
        result = generate_artifact(
            tenant_id=x_tenant_id,
            artifact_type=request.artifact_type,
            focus=focus,
            style=request.style,
            count=request.count,
            language=request.language,
        )
        write_audit_event(
            tenant_id=x_tenant_id,
            action="studio.artifact.generated",
            details={
                "artifact_type": request.artifact_type,
                "focus_length": len(focus),
                "style": request.style,
                "count": request.count,
                "chunks_used": result.get("chunks_used", 0),
                "language": request.language,
            },
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Artifact generation failed: {str(e)}")
    return StudioArtifactResponse(**result)


@router.post("/stream")
async def stream_query_documents(
    request: QueryRequest,
    x_tenant_id: str = Header(default="default")
):
    """Ask a question and stream backend progress events before the final answer."""
    validate_question(request)
    history = request_history(request)
    events: Queue = Queue()

    def progress_callback(payload: dict) -> None:
        events.put(("progress", payload))

    def worker() -> None:
        try:
            result = query_rag(
                tenant_id=x_tenant_id,
                question=request.question,
                chat_history=history,
                language=request.language,
                progress_callback=progress_callback,
                allow_web_search=request.allow_web_search,
            )
            write_audit_event(
                tenant_id=x_tenant_id,
                action="rag.query",
                details={
                    "question_length": len(request.question),
                    "chunks_used": result.get("chunks_used", 0),
                    "language": request.language,
                    "streamed": True,
                    "answer_mode": result.get("answer_mode", "project"),
                },
            )
            events.put(("final", result))
        except Exception as e:
            events.put(("error", {"detail": f"Query failed: {str(e)}"}))
        finally:
            events.put((None, None))

    def event_stream():
        thread = Thread(target=worker, daemon=True)
        thread.start()
        yield sse_event("progress", {
            "stage": "start",
            "message": "Agent is starting the backend reasoning flow.",
            "detail": "Opening a live progress stream for this question.",
        })
        while True:
            event, payload = events.get()
            if event is None:
                break
            yield sse_event(event, payload)

    return StreamingResponse(
        event_stream(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "X-Accel-Buffering": "no",
        },
    )


@router.post("/kt/stream")
async def stream_kt_brief(
    request: KTRequest,
    x_tenant_id: str = Header(default="default")
):
    """Generate a KT brief and stream backend progress events before the final brief."""
    focus, audience = validate_kt_request(request)
    question = build_kt_question(focus, audience)
    events: Queue = Queue()

    def progress_callback(payload: dict) -> None:
        events.put(("progress", payload))

    def worker() -> None:
        try:
            result = query_rag(
                tenant_id=x_tenant_id,
                question=question,
                chat_history=[],
                language=request.language,
                progress_callback=progress_callback,
                allow_web_search=False,
            )
            write_audit_event(
                tenant_id=x_tenant_id,
                action="kt.brief.generated",
                details={
                    "focus_length": len(focus),
                    "audience": audience,
                    "chunks_used": result.get("chunks_used", 0),
                    "language": request.language,
                    "streamed": True,
                },
            )
            events.put(("final", result))
        except Exception as e:
            events.put(("error", {"detail": f"KT generation failed: {str(e)}"}))
        finally:
            events.put((None, None))

    def event_stream():
        thread = Thread(target=worker, daemon=True)
        thread.start()
        yield sse_event("progress", {
            "stage": "start",
            "message": "Agent is starting the KT brief workflow.",
            "detail": "Opening a live progress stream for onboarding and handoff synthesis.",
        })
        while True:
            event, payload = events.get()
            if event is None:
                break
            yield sse_event(event, payload)

    return StreamingResponse(
        event_stream(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "X-Accel-Buffering": "no",
        },
    )


@router.post("/kt", response_model=QueryResponse)
async def generate_kt_brief(
    request: KTRequest,
    x_tenant_id: str = Header(default="default")
):
    """Generate a source-grounded KT brief from indexed project sources."""
    focus, audience = validate_kt_request(request)
    question = build_kt_question(focus, audience)

    try:
        result = query_rag(
            tenant_id=x_tenant_id,
            question=question,
            chat_history=[],
            language=request.language,
            allow_web_search=False,
        )
        write_audit_event(
            tenant_id=x_tenant_id,
            action="kt.brief.generated",
            details={
                "focus_length": len(focus),
                "audience": audience,
                "chunks_used": result.get("chunks_used", 0),
                "language": request.language,
            },
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"KT generation failed: {str(e)}")

    return QueryResponse(**result)
