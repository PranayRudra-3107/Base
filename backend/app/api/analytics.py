from fastapi import APIRouter, Header, Response

from app.services.analytics import build_bi_dataset, build_dashboard
from app.services.audit_log import read_audit_events, write_audit_event
from app.services.storage import list_document_analyses

router = APIRouter()


@router.get("/dashboard")
async def dashboard(x_tenant_id: str = Header(default="default")):
    """Return audit KPIs, chart series, validation issues, and recent audit events."""
    write_audit_event(x_tenant_id, "analytics.dashboard.viewed")
    return build_dashboard(x_tenant_id)


@router.get("/audit-log")
async def audit_log(x_tenant_id: str = Header(default="default")):
    """Return recent audit trail events for a tenant."""
    return read_audit_events(x_tenant_id)


@router.get("/insights")
async def insights(x_tenant_id: str = Header(default="default")):
    """Return generated audit insight cards."""
    dashboard_data = build_dashboard(x_tenant_id)
    write_audit_event(x_tenant_id, "analytics.insights.viewed")
    return dashboard_data["insights"]


@router.get("/anomalies")
async def anomalies(x_tenant_id: str = Header(default="default")):
    """Return anomaly detection signals."""
    dashboard_data = build_dashboard(x_tenant_id)
    write_audit_event(x_tenant_id, "analytics.anomalies.viewed")
    return dashboard_data["anomalies"]


@router.get("/export.csv")
async def export_csv(x_tenant_id: str = Header(default="default")):
    """Export extracted audit analytics as CSV."""
    rows = list_document_analyses(x_tenant_id)
    headers = [
        "document_id",
        "filename",
        "uploaded_at",
        "category",
        "total_amount",
        "average_amount",
        "exception_count",
        "compliance_ratio",
        "language",
        "amount_outlier_count",
        "validation_issue_count",
    ]
    lines = [",".join(headers)]
    for row in rows:
        values = [
            row.get("document_id", ""),
            row.get("filename", "").replace(",", " "),
            row.get("uploaded_at", ""),
            row.get("category", ""),
            str(row.get("total_amount", 0)),
            str(row.get("average_amount", 0)),
            str(row.get("exception_count", 0)),
            str(row.get("compliance_ratio", 0)),
            (row.get("language") or {}).get("name", "Unknown"),
            str(len(row.get("amount_outliers", []))),
            str(len(row.get("validation_issues", []))),
        ]
        lines.append(",".join(values))

    write_audit_event(
        x_tenant_id,
        "report.exported",
        details={"format": "csv", "rows": len(rows)},
    )
    return Response(
        "\n".join(lines),
        media_type="text/csv",
        headers={"Content-Disposition": "attachment; filename=audit-analytics.csv"},
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
