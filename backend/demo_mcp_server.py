"""Open-source enterprise MCP server used for Base interview demonstrations."""

import json
from datetime import datetime, timezone
from typing import Any, Dict, List

from mcp.server.fastmcp import FastMCP
from mcp.server.transport_security import TransportSecuritySettings


server = FastMCP(
    name="Acme Enterprise Systems",
    instructions=(
        "Demo enterprise registry server exposing Jira-like delivery records, "
        "Confluence-like runbooks, incidents, and controlled handoff-note writes."
    ),
    host="0.0.0.0",
    port=8100,
    streamable_http_path="/mcp",
    stateless_http=True,
    json_response=True,
    transport_security=TransportSecuritySettings(
        enable_dns_rebinding_protection=True,
        allowed_hosts=["enterprise-mcp:*", "127.0.0.1:*", "localhost:*"],
        allowed_origins=["http://enterprise-mcp:*", "http://127.0.0.1:*", "http://localhost:*"],
    ),
)

RECORDS: List[Dict[str, Any]] = [
    {
        "id": "BASE-431",
        "source": "jira",
        "title": "Checkout API latency after pricing rollout",
        "status": "In Progress",
        "owner": "Maya Chen",
        "severity": "high",
        "updated_at": "2026-07-11T14:20:00Z",
        "text": "p95 latency rose from 185ms to 418ms after pricing-service 2.8. Rollback is approved if p95 remains above 350ms for 15 minutes.",
    },
    {
        "id": "BASE-447",
        "source": "jira",
        "title": "Add idempotency keys to payment retries",
        "status": "Ready for Review",
        "owner": "Luis Romero",
        "severity": "medium",
        "updated_at": "2026-07-12T09:10:00Z",
        "text": "PR 1842 adds idempotency keys and replay protection. Database migration is backward compatible.",
    },
    {
        "id": "PD-102",
        "source": "pagerduty",
        "title": "Elevated checkout failures in eu-central-1",
        "status": "Resolved",
        "owner": "Payments On-call",
        "severity": "sev-2",
        "updated_at": "2026-07-10T18:42:00Z",
        "text": "Connection pool exhaustion caused 7.4% checkout failures for 23 minutes. Pool size was raised and a saturation alert was added.",
    },
    {
        "id": "ADR-42",
        "source": "confluence",
        "title": "Checkout service ownership and rollback policy",
        "status": "Approved",
        "owner": "Platform Architecture",
        "severity": "information",
        "updated_at": "2026-07-09T11:00:00Z",
        "text": "Checkout API owns orchestration; pricing owns quote calculation; payments owns authorization. The release captain can trigger rollback after SLO breach confirmation.",
    },
]

RUNBOOKS = {
    "checkout": """# Checkout Rollback Runbook

Owner: Payments On-call
Escalation: #incident-checkout

1. Confirm p95 latency above 350ms for 15 minutes or error rate above 5%.
2. Pause the pricing rollout in eu-central-1.
3. Roll checkout-api back to release 2.7.4.
4. Validate payment authorization, database pool saturation, and queue depth.
5. Update BASE-431 and attach the Grafana snapshot before resolving the incident.
""",
    "database": """# Database Saturation Runbook

Owner: Data Platform

Check active connections, waiting queries, lock duration, and replica lag. At 80% pool saturation, stop nonessential batch workers. At 90%, page Data Platform and fail over only after confirming replica health.
""",
}

HANDOFF_NOTES: List[Dict[str, str]] = []


def _matches(record: Dict[str, Any], query: str, source: str) -> bool:
    source_match = source == "all" or record["source"] == source.lower()
    haystack = " ".join(str(value) for value in record.values()).lower()
    terms = [term for term in query.lower().split() if term]
    return source_match and (not terms or all(term in haystack for term in terms))


@server.tool()
def search_enterprise(query: str, source: str = "all", limit: int = 5) -> List[Dict[str, Any]]:
    """Search delivery, documentation, and incident records in the demo enterprise system."""
    limit = max(1, min(int(limit), 20))
    return [record for record in RECORDS if _matches(record, query, source)][:limit]


@server.tool()
def get_record(record_id: str) -> Dict[str, Any]:
    """Get one enterprise record by ticket, incident, or architecture-decision ID."""
    record_id = record_id.strip().upper()
    record = next((item for item in RECORDS if item["id"].upper() == record_id), None)
    if not record:
        raise ValueError(f"Unknown enterprise record: {record_id}")
    return record


@server.tool()
def create_handoff_note(project: str, summary: str, owner: str = "Unassigned") -> Dict[str, str]:
    """Write a controlled handoff note and return its generated identifier."""
    if not project.strip() or not summary.strip():
        raise ValueError("project and summary are required")
    note = {
        "id": f"HANDOFF-{len(HANDOFF_NOTES) + 1:03d}",
        "project": project.strip(),
        "summary": summary.strip(),
        "owner": owner.strip() or "Unassigned",
        "created_at": datetime.now(timezone.utc).isoformat(),
    }
    HANDOFF_NOTES.append(note)
    return note


@server.tool()
def list_handoff_notes(project: str = "") -> List[Dict[str, str]]:
    """List handoff notes written through the MCP server."""
    return [note for note in HANDOFF_NOTES if not project or note["project"].lower() == project.lower()]


@server.resource("acme://catalog", mime_type="application/json")
def enterprise_catalog() -> str:
    """Describe the enterprise datasets exposed by this demo server."""
    return json.dumps(
        {
            "systems": ["Jira", "Confluence", "PagerDuty"],
            "record_count": len(RECORDS),
            "runbooks": sorted(RUNBOOKS),
            "write_capability": "create_handoff_note",
        },
        indent=2,
    )


@server.resource("acme://runbooks/{name}", mime_type="text/markdown")
def runbook(name: str) -> str:
    """Read one operational runbook by name."""
    content = RUNBOOKS.get(name.lower())
    if not content:
        raise ValueError(f"Unknown runbook: {name}")
    return content


@server.prompt()
def incident_handoff(service: str = "checkout") -> str:
    """Provide a reusable prompt for an incident-to-handoff workflow."""
    return (
        f"Review incidents, delivery tickets, and runbooks for {service}. "
        "Return impact, root cause, owner, rollback criteria, and the next three actions."
    )


def main() -> None:
    server.run(transport="streamable-http")


if __name__ == "__main__":
    main()
