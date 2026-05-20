from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

from app.services.projects import create_project, get_project, list_projects

router = APIRouter()


class ProjectCreate(BaseModel):
    name: str
    description: str = ""


class ProjectInfo(BaseModel):
    project_id: str
    name: str
    description: str
    created_at: str
    updated_at: str
    document_count: int
    project_health_score: float
    risk_count: int
    blocker_count: int
    ticket_count: int
    decision_count: int
    last_activity_at: str = ""


@router.get("/", response_model=List[ProjectInfo])
async def get_projects():
    """List available projects and lightweight dashboard summaries."""
    return list_projects()


@router.post("/", response_model=ProjectInfo)
async def add_project(request: ProjectCreate):
    """Create a project workspace for uploads, RAG, analytics, and activity."""
    try:
        return create_project(request.name, request.description)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/{project_id}", response_model=ProjectInfo)
async def get_project_details(project_id: str):
    """Return one project and its lightweight dashboard summary."""
    try:
        return get_project(project_id)
    except KeyError:
        raise HTTPException(status_code=404, detail="Project not found.")
