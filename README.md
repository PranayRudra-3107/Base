# Base Platform — MVP

Enterprise GenAI Knowledge & Workflow Platform

## What this does
- Upload PDF, TXT, Markdown documents
- Ask questions → grounded answers via RAG
- Source citations with relevance scores
- Multi-tenant by design

---

## Quick Start

### 1. Backend

```bash
cd backend
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env            # Then add your OPENAI_API_KEY
uvicorn app.main:app --reload --port 8000
```

API live at: http://localhost:8000
Swagger docs: http://localhost:8000/docs

### 2. Frontend

```bash
cd frontend
# Option A: open directly
open index.html
# Option B: local server
python -m http.server 3000
# Then visit http://localhost:3000
```

---

## Project Structure

```
base-platform/
├── backend/
│   ├── app/
│   │   ├── main.py              # FastAPI app
│   │   ├── core/config.py       # Settings from .env
│   │   ├── api/
│   │   │   ├── ingest.py        # POST /api/ingest/
│   │   │   ├── query.py         # POST /api/query/
│   │   │   └── documents.py     # GET/DELETE /api/documents/
│   │   └── services/
│   │       ├── ingestion.py     # File parsing + chunking
│   │       ├── vector_store.py  # ChromaDB operations
│   │       └── rag.py           # RAG pipeline
│   ├── requirements.txt
│   └── .env.example
└── frontend/
    └── index.html               # Complete single-file UI
```

---

## API Reference

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /api/ingest/ | Upload & index a document |
| POST | /api/query/ | Ask a question |
| GET | /api/documents/ | List documents |
| DELETE | /api/documents/{id} | Delete a document |

All endpoints accept x-tenant-id header (default: "default").

---

## .env Config

```
OPENAI_API_KEY=sk-...
LLM_MODEL=gpt-4o
EMBEDDING_MODEL=text-embedding-3-small
CHUNK_SIZE=500
CHUNK_OVERLAP=50
RETRIEVAL_K=5
```

---

## Deployment

Backend → Railway.app ($5/mo)
Frontend → Vercel (free) — update API_BASE in index.html

Estimated cost for early users: < $10/month
