from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import ingest, query, documents, analytics, projects
from app.core.config import get_settings, parse_csv_setting
from app.services.database import init_metadata_schema, init_vector_schema, postgres_enabled, pgvector_enabled

settings = get_settings()

app = FastAPI(
    title="Base Platform API",
    description="Project Intelligence & KT Copilot API",
    version="0.1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=parse_csv_setting(settings.cors_origins),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(ingest.router, prefix="/api/ingest", tags=["Ingestion"])
app.include_router(query.router, prefix="/api/query", tags=["Query"])
app.include_router(documents.router, prefix="/api/documents", tags=["Documents"])
app.include_router(analytics.router, prefix="/api/analytics", tags=["Analytics"])
app.include_router(projects.router, prefix="/api/projects", tags=["Projects"])


@app.on_event("startup")
def startup_checks():
    if postgres_enabled():
        init_metadata_schema()
    if pgvector_enabled():
        init_vector_schema()


@app.get("/health")
def health():
    return {
        "status": "ok",
        "environment": settings.environment,
        "metadata_backend": settings.metadata_backend,
        "document_storage_backend": settings.document_storage_backend,
        "vector_backend": settings.vector_backend,
    }
