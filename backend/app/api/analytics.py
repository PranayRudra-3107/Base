import csv
import io

from fastapi import APIRouter, Header, Response

from app.services.analytics import build_bi_dataset, build_dashboard, build_knowledge_graph
from app.services.audit_log import read_audit_events, write_audit_event
from app.services.storage import list_document_analyses

router = APIRouter()


@router.get("/dashboard")
async def dashboard(x_tenant_id: str = Header(default="default")):
    """Return project health KPIs, chart series, validation issues, and recent events."""
    write_audit_event(x_tenant_id, "analytics.dashboard.viewed")
    return build_dashboard(x_tenant_id)


@router.get("/audit-log")
async def audit_log(x_tenant_id: str = Header(default="default")):
    """Return recent activity events for a tenant."""
    return read_audit_events(x_tenant_id)


@router.get("/insights")
async def insights(x_tenant_id: str = Header(default="default")):
    """Return generated project insight cards."""
    dashboard_data = build_dashboard(x_tenant_id)
    write_audit_event(x_tenant_id, "analytics.insights.viewed")
    return dashboard_data["insights"]


@router.get("/anomalies")
async def anomalies(x_tenant_id: str = Header(default="default")):
    """Return anomaly detection signals."""
    dashboard_data = build_dashboard(x_tenant_id)
    write_audit_event(x_tenant_id, "analytics.anomalies.viewed")
    return dashboard_data["anomalies"]


@router.get("/knowledge-graph")
async def knowledge_graph(x_tenant_id: str = Header(default="default")):
    """Return an Obsidian-style graph of project sources and extracted entities."""
    graph = build_knowledge_graph(x_tenant_id)
    write_audit_event(
        x_tenant_id,
        "analytics.knowledge_graph.viewed",
        details={"nodes": graph["stats"]["nodes"], "edges": graph["stats"]["edges"]},
    )
    return graph


@router.get("/export.csv")
async def export_csv(x_tenant_id: str = Header(default="default")):
    """Export extracted project intelligence analytics as CSV."""
    rows = list_document_analyses(x_tenant_id)
    headers = [
        "document_id",
        "filename",
        "uploaded_at",
        "source_type",
        "project_health_score",
        "ticket_count",
        "risk_count",
        "blocker_count",
        "decision_count",
        "metric_signal_count",
        "total_metric_value",
        "language",
        "validation_issue_count",
    ]
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(headers)
    for row in rows:
        health_score = row.get("project_health_score", round((row.get("compliance_ratio", 0) or 0) * 100, 1))
        writer.writerow([
            row.get("document_id", ""),
            row.get("filename", ""),
            row.get("uploaded_at", ""),
            row.get("category", ""),
            str(health_score),
            str(row.get("ticket_count", 0)),
            str(row.get("risk_count", row.get("exception_count", 0))),
            str(row.get("blocker_count", 0)),
            str(row.get("decision_count", 0)),
            str(row.get("metric_signal_count", len(row.get("amounts", [])))),
            str(row.get("total_metric_value", row.get("total_amount", 0))),
            (row.get("language") or {}).get("name", "Unknown"),
            str(len(row.get("validation_issues", []))),
        ])

    write_audit_event(
        x_tenant_id,
        "report.exported",
        details={"format": "csv", "rows": len(rows)},
    )
    return Response(
        output.getvalue(),
        media_type="text/csv",
        headers={"Content-Disposition": "attachment; filename=project-intelligence.csv"},
    )


@router.get("/export.tableau.json")
async def export_tableau(x_tenant_id: str = Header(default="default")):
    """Export a Tableau-friendly JSON dataset."""
    payload = build_bi_dataset(x_tenant_id)
    write_audit_event(
        x_tenant_id,
        "report.exported",
        details={"format": "tableau-json", "rows": len(payload["tables"]["documents"])},
    )
    return payload


@router.get("/export.powerbi.json")
async def export_powerbi(x_tenant_id: str = Header(default="default")):
    """Export a PowerBI-friendly JSON dataset."""
    payload = build_bi_dataset(x_tenant_id)
    write_audit_event(
        x_tenant_id,
        "report.exported",
        details={"format": "powerbi-json", "rows": len(payload["tables"]["documents"])},
    )
    return payload
