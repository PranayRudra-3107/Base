from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import ingest, query, documents, analytics, projects

app = FastAPI(
    title="Base Platform API",
    description="Project Intelligence & KT Copilot API",
    version="0.1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://yourdomain.vercel.app", "http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(ingest.router, prefix="/api/ingest", tags=["Ingestion"])
app.include_router(query.router, prefix="/api/query", tags=["Query"])
app.include_router(documents.router, prefix="/api/documents", tags=["Documents"])
app.include_router(analytics.router, prefix="/api/analytics", tags=["Analytics"])
app.include_router(projects.router, prefix="/api/projects", tags=["Projects"])

@app.get("/health")
def health():
    return {"status": "ok"}
