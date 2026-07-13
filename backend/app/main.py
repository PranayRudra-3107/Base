import secrets
from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from app.api import analytics, connectors, documents, ingest, mcp_bridge, projects, query
from app.core.config import get_settings, parse_csv_setting
from app.mcp_server import base_mcp
from app.services.database import init_metadata_schema, init_vector_schema, postgres_enabled, pgvector_enabled

settings = get_settings()


@asynccontextmanager
async def lifespan(_: FastAPI):
    if postgres_enabled():
        init_metadata_schema()
    if pgvector_enabled():
        init_vector_schema()
    async with base_mcp.session_manager.run():
        yield


app = FastAPI(
    title="Base Platform API",
    description="Project Intelligence & KT Copilot API",
    version="0.2.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=parse_csv_setting(settings.cors_origins),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["Mcp-Session-Id"],
)


@app.middleware("http")
async def protect_mcp_endpoint(request: Request, call_next):
    expected = settings.mcp_api_key.strip()
    is_mcp_request = request.url.path.startswith("/mcp")
    is_production = settings.environment.strip().lower() == "production"
    if request.method != "OPTIONS" and is_mcp_request and is_production and not expected:
        return JSONResponse(
            status_code=503,
            content={"detail": "MCP is unavailable because MCP_API_KEY is not configured."},
        )
    if request.method != "OPTIONS" and is_mcp_request and expected:
        authorization = request.headers.get("Authorization", "")
        bearer = authorization[7:].strip() if authorization.lower().startswith("bearer ") else ""
        supplied = request.headers.get("X-MCP-API-Key", "").strip() or bearer
        if not supplied or not secrets.compare_digest(supplied, expected):
            return JSONResponse(
                status_code=401,
                content={"detail": "A valid MCP API key is required."},
                headers={"WWW-Authenticate": "Bearer"},
            )
    return await call_next(request)

app.include_router(ingest.router, prefix="/api/ingest", tags=["Ingestion"])
app.include_router(query.router, prefix="/api/query", tags=["Query"])
app.include_router(documents.router, prefix="/api/documents", tags=["Documents"])
app.include_router(analytics.router, prefix="/api/analytics", tags=["Analytics"])
app.include_router(projects.router, prefix="/api/projects", tags=["Projects"])
app.include_router(connectors.router, prefix="/api/connectors", tags=["Connectors"])
app.include_router(mcp_bridge.router, prefix="/api/mcp", tags=["MCP"])


@app.get("/health")
def health():
    mcp_key_configured = bool(settings.mcp_api_key.strip())
    mcp_available = settings.environment.strip().lower() != "production" or mcp_key_configured
    return {
        "status": "ok",
        "environment": settings.environment,
        "metadata_backend": settings.metadata_backend,
        "document_storage_backend": settings.document_storage_backend,
        "vector_backend": settings.vector_backend,
        "mcp_endpoint": "/mcp",
        "mcp_available": mcp_available,
        "mcp_authentication_required": mcp_key_configured,
    }


# Keep this catch-all mount last so FastAPI routes remain authoritative and MCP is served at /mcp.
app.mount("/", base_mcp.streamable_http_app())
