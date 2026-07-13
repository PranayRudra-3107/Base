import json
from typing import Any, Dict, List

from mcp.server.fastmcp import FastMCP
from mcp.server.transport_security import TransportSecuritySettings

from app.core.config import get_settings, parse_csv_setting
from app.services.analytics import build_dashboard, build_knowledge_graph
from app.services.audit_log import write_audit_event
from app.services.multi_agent import run_project_review_board
from app.services.projects import get_project, list_projects
from app.services.rag import query_rag
from app.services.storage import list_document_analyses
from app.services.vector_store import list_documents, search_chunks

settings = get_settings()

base_mcp = FastMCP(
    name="Base Project Intelligence",
    instructions=(
        "Access project-scoped Base sources, hybrid search, knowledge graphs, "
        "analytics, RAG answers, and multi-agent project reviews. Pass a project_id "
        "to every project tool and preserve source identifiers in downstream answers."
    ),
    streamable_http_path="/mcp",
    stateless_http=True,
    json_response=True,
    transport_security=TransportSecuritySettings(
        enable_dns_rebinding_protection=True,
        allowed_hosts=parse_csv_setting(settings.mcp_allowed_hosts),
        allowed_origins=parse_csv_setting(settings.mcp_allowed_origins),
    ),
)


def _allowed_project_ids() -> set[str]:
    return set(parse_csv_setting(settings.mcp_exposed_project_ids))


def _require_project(project_id: str) -> Dict[str, Any]:
    project_id = (project_id or "").strip()
    if not project_id:
        raise ValueError("project_id is required.")
    allowed = _allowed_project_ids()
    if allowed and project_id not in allowed:
        raise PermissionError(f"Project '{project_id}' is not exposed through MCP.")
    try:
        return get_project(project_id)
    except KeyError as exc:
        raise ValueError(f"Unknown project_id: {project_id}") from exc


def _project_catalog() -> List[Dict[str, Any]]:
    allowed = _allowed_project_ids()
    projects = list_projects()
    if allowed:
        projects = [item for item in projects if item.get("project_id") in allowed]
    return projects


def _project_sources(project_id: str) -> List[Dict[str, Any]]:
    _require_project(project_id)
    indexed = {
        item.get("document_id"): item
        for item in list_documents(project_id)
        if item.get("document_id")
    }
    for analysis in list_document_analyses(project_id):
        document_id = analysis.get("document_id")
        if not document_id:
            continue
        indexed[document_id] = {
            **indexed.get(document_id, {}),
            "document_id": document_id,
            "filename": analysis.get("filename", indexed.get(document_id, {}).get("filename", "unknown")),
            "uploaded_at": analysis.get("uploaded_at", indexed.get(document_id, {}).get("uploaded_at", "")),
            "chunk_count": analysis.get("chunk_count", indexed.get(document_id, {}).get("chunk_count", 0)),
            "source_type": analysis.get("category", "General Project Data"),
            "source": analysis.get("source", "upload"),
        }
    return sorted(indexed.values(), key=lambda item: item.get("uploaded_at", ""), reverse=True)


def _dashboard_summary(project_id: str) -> Dict[str, Any]:
    _require_project(project_id)
    dashboard = build_dashboard(project_id)
    return {
        "kpis": dashboard.get("kpis", {}),
        "charts": dashboard.get("charts", {}),
        "insights": dashboard.get("insights", []),
        "anomalies": dashboard.get("anomalies", []),
        "validation_issues": dashboard.get("validation_issues", []),
    }


def _json_resource(value: Any) -> str:
    return json.dumps(value, indent=2, ensure_ascii=True, default=str)


@base_mcp.resource("base://projects", mime_type="application/json")
def project_catalog_resource() -> str:
    """List Base projects currently exposed through MCP."""
    return _json_resource(_project_catalog())


@base_mcp.resource("base://projects/{project_id}/summary", mime_type="application/json")
def project_summary_resource(project_id: str) -> str:
    """Read one project workspace summary."""
    return _json_resource(_require_project(project_id))


@base_mcp.resource("base://projects/{project_id}/sources", mime_type="application/json")
def project_sources_resource(project_id: str) -> str:
    """List indexed sources for one Base project."""
    return _json_resource(_project_sources(project_id))


@base_mcp.resource("base://projects/{project_id}/knowledge-graph", mime_type="application/json")
def project_graph_resource(project_id: str) -> str:
    """Read the nodes, edges, and evidence metadata in a project's knowledge graph."""
    _require_project(project_id)
    return _json_resource(build_knowledge_graph(project_id))


@base_mcp.tool()
def base_list_projects() -> List[Dict[str, Any]]:
    """List project workspaces exposed by Base, including high-level health statistics."""
    return _project_catalog()


@base_mcp.tool()
def base_list_sources(project_id: str) -> List[Dict[str, Any]]:
    """List the indexed source documents available in a Base project."""
    sources = _project_sources(project_id)
    write_audit_event(project_id, "mcp.sources.listed", actor="mcp")
    return sources


@base_mcp.tool()
def base_search_project(project_id: str, query: str, limit: int = 5) -> List[Dict[str, Any]]:
    """Hybrid-search one project and return source-grounded text chunks with relevance metadata."""
    _require_project(project_id)
    query = (query or "").strip()
    if not query:
        raise ValueError("query is required.")
    limit = max(1, min(int(limit), 20))
    matches = search_chunks(project_id, query, k=limit)
    result = [
        {
            "chunk_id": item.get("id"),
            "text": (item.get("text") or "")[:6000],
            "document_id": item.get("metadata", {}).get("document_id"),
            "filename": item.get("metadata", {}).get("filename", "Unknown"),
            "chunk_index": item.get("metadata", {}).get("chunk_index"),
            "relevance_score": item.get("score", 0),
            "retrieval_mode": item.get("retrieval_mode"),
            "semantic_score": item.get("semantic_score"),
            "keyword_score": item.get("keyword_score"),
            "matched_terms": item.get("matched_terms", []),
        }
        for item in matches
    ]
    write_audit_event(
        project_id,
        "mcp.project.searched",
        actor="mcp",
        details={"query": query[:200], "matches": len(result)},
    )
    return result


@base_mcp.tool()
def base_get_dashboard(project_id: str) -> Dict[str, Any]:
    """Return health KPIs, trends, risks, anomalies, and validation issues for one project."""
    result = _dashboard_summary(project_id)
    write_audit_event(project_id, "mcp.dashboard.read", actor="mcp")
    return result


@base_mcp.tool()
def base_get_knowledge_graph(project_id: str) -> Dict[str, Any]:
    """Return the evidence graph connecting sources, tickets, PRs, incidents, risks, and decisions."""
    _require_project(project_id)
    result = build_knowledge_graph(project_id)
    write_audit_event(
        project_id,
        "mcp.knowledge_graph.read",
        actor="mcp",
        details=result.get("stats", {}),
    )
    return result


@base_mcp.tool()
def base_ask_project(
    project_id: str,
    question: str,
    language: str = "en",
    allow_web_search: bool = False,
) -> Dict[str, Any]:
    """Ask Base a source-grounded project question; internet fallback is disabled unless explicitly enabled."""
    _require_project(project_id)
    question = (question or "").strip()
    if not question:
        raise ValueError("question is required.")
    result = query_rag(
        tenant_id=project_id,
        question=question,
        language=language,
        allow_web_search=allow_web_search,
    )
    write_audit_event(
        project_id,
        "mcp.project.asked",
        actor="mcp",
        details={"question": question[:200], "chunks_used": result.get("chunks_used", 0)},
    )
    return result


@base_mcp.tool()
def base_run_project_review(
    project_id: str,
    focus: str = "overall project health, risk, release readiness, incidents, metrics, and KT",
    language: str = "en",
) -> Dict[str, Any]:
    """Run Base's LangGraph multi-agent review board over one project's evidence."""
    _require_project(project_id)
    result = run_project_review_board(project_id, focus=focus, language=language)
    write_audit_event(
        project_id,
        "mcp.multi_agent_review.completed",
        actor="mcp",
        details={"focus": focus[:200], "chunks_used": result.get("chunks_used", 0)},
    )
    return result


def main() -> None:
    """Run Base as a local stdio MCP server."""
    base_mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
