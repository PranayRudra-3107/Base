import json
import os
import re
import uuid
from datetime import datetime
from typing import Dict, List

from app.core.config import get_settings
from app.services.database import postgres_enabled
from app.services.analytics import build_dashboard
from app.services.storage import read_json, write_json

settings = get_settings()


def _projects_path() -> str:
    os.makedirs(settings.data_dir, exist_ok=True)
    return os.path.join(settings.data_dir, "projects.json")


def _now() -> str:
    return datetime.utcnow().isoformat()


def _project_slug(name: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", name.lower()).strip("-")
    return (slug or "project")[:40].strip("-") or "project"


def _read_projects() -> List[Dict]:
    if postgres_enabled():
        return read_json("_global", "projects", [])

    path = _projects_path()
    if not os.path.exists(path):
        legacy_path = os.path.join(settings.data_dir, "default", "analyses.json")
        if os.path.exists(legacy_path):
            now = _now()
            legacy_project = {
                "project_id": "default",
                "name": "Default Project",
                "description": "Legacy workspace created before project selection was added.",
                "created_at": now,
                "updated_at": now,
            }
            _write_projects([legacy_project])
            return [legacy_project]
        return []
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def _write_projects(projects: List[Dict]) -> None:
    if postgres_enabled():
        write_json("_global", "projects", projects)
        return

    with open(_projects_path(), "w", encoding="utf-8") as f:
        json.dump(projects, f, indent=2)


def _project_summary(project_id: str) -> Dict:
    dashboard = build_dashboard(project_id)
    kpis = dashboard.get("kpis", {})
    return {
        "document_count": kpis.get("documents", 0),
        "project_health_score": kpis.get("project_health_score", 0),
        "risk_count": kpis.get("risks", kpis.get("exceptions", 0)),
        "blocker_count": kpis.get("blockers", 0),
        "ticket_count": kpis.get("tickets", 0),
        "decision_count": kpis.get("decisions", 0),
        "last_activity_at": (dashboard.get("audit_events") or [{}])[0].get("timestamp", ""),
    }


def list_projects() -> List[Dict]:
    projects = _read_projects()
    enriched = []
    for project in projects:
        enriched.append({**project, **_project_summary(project["project_id"])})
    return sorted(enriched, key=lambda item: item.get("updated_at", ""), reverse=True)


def create_project(name: str, description: str = "") -> Dict:
    name = name.strip()
    description = description.strip()
    if not name:
        raise ValueError("Project name is required.")
    if len(name) > 120:
        raise ValueError("Project name must be 120 characters or fewer.")
    if len(description) > 500:
        raise ValueError("Project description must be 500 characters or fewer.")

    projects = _read_projects()
    now = _now()
    project = {
        "project_id": f"{_project_slug(name)}-{uuid.uuid4().hex[:8]}",
        "name": name,
        "description": description,
        "created_at": now,
        "updated_at": now,
    }
    projects.append(project)
    _write_projects(projects)
    return {**project, **_project_summary(project["project_id"])}


def get_project(project_id: str) -> Dict:
    for project in _read_projects():
        if project.get("project_id") == project_id:
            return {**project, **_project_summary(project_id)}
    raise KeyError(project_id)


def touch_project(project_id: str) -> None:
    projects = _read_projects()
    changed = False
    for project in projects:
        if project.get("project_id") == project_id:
            project["updated_at"] = _now()
            changed = True
            break
    if changed:
        _write_projects(projects)
