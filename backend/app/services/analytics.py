import re
from collections import Counter, defaultdict
from statistics import mean, pstdev
from typing import Dict, List

from app.services.audit_log import read_audit_events
from app.services.storage import list_document_analyses
from app.services.vector_store import list_documents

AMOUNT_RE = re.compile(r"(?<![A-Za-z0-9])(?:USD|EUR|GBP|INR|\$)?\s*(-?\d[\d,]*(?:\.\d{1,2})?)")
DATE_RE = re.compile(r"\b(?:\d{4}-\d{1,2}-\d{1,2}|\d{1,2}[/-]\d{1,2}[/-]\d{2,4})\b")
TICKET_RE = re.compile(r"\b[A-Z][A-Z0-9]{1,9}-\d+\b")
METRIC_RE = re.compile(
    r"\b(?:p95|p99|latency|traffic|engagement|uptime|error rate|conversion|cpu|memory|"
    r"database|db|queries|requests|users|sessions|deployments|incidents|sla|slo)\b"
)

RISK_WORDS = (
    "risk",
    "issue",
    "incident",
    "outage",
    "error",
    "failure",
    "failed",
    "failing",
    "regression",
    "bug",
    "defect",
    "hotfix",
    "variance",
    "anomaly",
    "escalation",
    "delayed",
    "overdue",
    "missing",
    "slow",
    "latency",
)
BLOCKER_WORDS = (
    "blocker",
    "blocked",
    "stuck",
    "waiting",
    "dependency",
    "cannot proceed",
    "delayed",
    "overdue",
    "unresolved",
    "escalated",
)
DECISION_WORDS = (
    "decision",
    "decided",
    "approved",
    "agreed",
    "owner",
    "action item",
    "next step",
    "follow-up",
    "todo",
    "resolved",
)
HEALTHY_WORDS = (
    "healthy",
    "green",
    "stable",
    "resolved",
    "complete",
    "completed",
    "passed",
    "shipped",
    "released",
    "deployed",
    "on track",
)
TICKET_WORDS = ("ticket", "story", "task", "bug", "epic", "sprint", "backlog", "jira", "linear")

SOURCE_MARKERS = (
    ("Work Tracking", ("jira", "linear", "ticket", "story", "task", "epic", "sprint", "backlog")),
    ("Chat & Decisions", ("slack", "teams", "chat", "conversation", "standup", "decision", "action item")),
    ("Code & Release", ("github", "gitlab", "pull request", "pr ", "commit", "branch", "release", "deploy")),
    ("Product Analytics", ("traffic", "engagement", "conversion", "funnel", "users", "sessions", "retention")),
    ("Observability", ("latency", "error rate", "uptime", "p95", "p99", "cpu", "memory", "requests")),
    ("Database Health", ("database", "db ", "query", "queries", "replication", "connections", "storage")),
    ("Incident & Support", ("incident", "outage", "pagerduty", "support", "zendesk", "customer")),
    ("Documentation & KT", ("runbook", "architecture", "onboarding", "kt", "knowledge transfer", "readme", "docs")),
    ("Financial & Spend", ("invoice", "expense", "cost", "budget", "spend", "revenue")),
)

LANGUAGE_MARKERS = {
    "en": ("the", "and", "project", "ticket", "service", "deployment"),
    "es": ("el", "la", "proyecto", "tarea", "servicio", "despliegue"),
    "fr": ("le", "la", "projet", "tache", "service", "deploiement"),
    "de": ("der", "die", "projekt", "aufgabe", "dienst", "bereitstellung"),
}
LANGUAGE_NAMES = {
    "en": "English",
    "es": "Spanish",
    "fr": "French",
    "de": "German",
    "hi": "Hindi",
    "unknown": "Unknown",
}


def _overlaps_ignored_span(start: int, end: int, ignored_spans: List[tuple]) -> bool:
    return any(start < span_end and end > span_start for span_start, span_end in ignored_spans)


def _amounts(text: str) -> List[float]:
    ignored_spans = [match.span() for match in DATE_RE.finditer(text)]
    ignored_spans.extend(match.span() for match in TICKET_RE.finditer(text.upper()))
    values = []
    for match in AMOUNT_RE.finditer(text):
        if _overlaps_ignored_span(match.start(), match.end(), ignored_spans):
            continue
        raw = match.group(1).replace(",", "")
        try:
            value = float(raw)
        except ValueError:
            continue
        if abs(value) >= 1:
            values.append(value)
    return values


def _line_hits(lines: List[str], words: tuple) -> List[str]:
    return [
        line
        for line in lines
        if any(word in line.lower() for word in words)
    ]


def _category(filename: str, text: str) -> str:
    haystack = f"{filename} {text[:2500]}".lower()
    for category, markers in SOURCE_MARKERS:
        if any(marker in haystack for marker in markers):
            return category
    return "General Project Data"


def _language(text: str) -> Dict:
    haystack = f" {text[:4000].lower()} "
    if re.search(r"[\u0900-\u097F]", haystack):
        return {"code": "hi", "name": LANGUAGE_NAMES["hi"], "confidence": 0.92}

    scores = {
        code: sum(1 for marker in markers if f" {marker} " in haystack)
        for code, markers in LANGUAGE_MARKERS.items()
    }
    code, score = max(scores.items(), key=lambda item: item[1])
    if score == 0:
        return {"code": "unknown", "name": LANGUAGE_NAMES["unknown"], "confidence": 0}
    return {
        "code": code,
        "name": LANGUAGE_NAMES.get(code, code),
        "confidence": round(min(0.95, 0.45 + score * 0.12), 2),
    }


def _metric_outliers(values: List[float]) -> List[Dict]:
    if len(values) < 4:
        return []

    avg = mean(values)
    spread = pstdev(values)
    if spread == 0:
        return []

    outliers = []
    for value in values:
        z_score = (value - avg) / spread
        if abs(z_score) >= 2:
            outliers.append({
                "amount": round(value, 2),
                "z_score": round(z_score, 2),
                "reason": "Numeric metric is more than two standard deviations from the document average.",
            })
    return outliers[:10]


def _time_bucket(item: Dict) -> str:
    dates = item.get("dates_detected") or []
    raw = dates[0] if dates else item.get("uploaded_at", "")
    match = re.search(r"(\d{4})[-/](\d{1,2})", raw)
    if match:
        return f"{match.group(1)}-{int(match.group(2)):02d}"
    return (item.get("uploaded_at", "")[:7] or "Unknown")


def _project_health_score(
    risk_count: int,
    blocker_count: int,
    validation_count: int,
    healthy_count: int,
    word_count: int,
) -> float:
    score = 100 - (risk_count * 3) - (blocker_count * 7) - (validation_count * 5)
    score += min(8, healthy_count)
    if word_count < 25:
        score -= 10
    return round(max(0, min(100, score)), 1)


def _risk_count(item: Dict) -> int:
    return int(item.get("risk_count", item.get("exception_count", 0)) or 0)


def _blocker_count(item: Dict) -> int:
    return int(item.get("blocker_count", 0) or 0)


def _ticket_count(item: Dict) -> int:
    return int(item.get("ticket_count", 0) or 0)


def _decision_count(item: Dict) -> int:
    return int(item.get("decision_count", 0) or 0)


def _metric_value(item: Dict) -> float:
    return float(item.get("total_metric_value", item.get("total_amount", 0)) or 0)


def _health_score(item: Dict) -> float:
    if "project_health_score" in item:
        return float(item.get("project_health_score") or 0)
    return round(float(item.get("compliance_ratio", 0) or 0) * 100, 1)


def _entity_type(entity_id: str) -> str:
    if entity_id.startswith("PD-"):
        return "incident"
    if entity_id.startswith("PR-"):
        return "pull_request"
    if entity_id.startswith("REL-"):
        return "release"
    return "ticket"


def _signal_node_id(signal_type: str) -> str:
    return f"signal:{signal_type}"


def analyze_document(document_id: str, filename: str, text: str, uploaded_at: str, storage_path: str = "") -> Dict:
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    amounts = _amounts(text)
    metric_outliers = _metric_outliers(amounts)
    ticket_ids = sorted(set(TICKET_RE.findall(text.upper())))[:100]
    ticket_hint_lines = _line_hits(lines, TICKET_WORDS)
    risk_lines = _line_hits(lines, RISK_WORDS)
    blocker_lines = _line_hits(lines, BLOCKER_WORDS)
    decision_lines = _line_hits(lines, DECISION_WORDS)
    healthy_lines = _line_hits(lines, HEALTHY_WORDS)
    metric_lines = [line for line in lines if METRIC_RE.search(line.lower())]
    validation_issues = []
    word_count = len(text.split())

    if not DATE_RE.search(text):
        validation_issues.append("No project dates or timestamps were detected.")
    if word_count < 25:
        validation_issues.append("Document text is very short; KT and metric extraction may be incomplete.")
    if not any((ticket_ids, risk_lines, blocker_lines, decision_lines, metric_lines, amounts)):
        validation_issues.append("No tickets, decisions, risks, operational metrics, or numeric values were detected.")
    if metric_outliers:
        validation_issues.append(f"{len(metric_outliers)} unusual numeric metric value(s) detected.")

    ticket_count = len(ticket_ids) or len(ticket_hint_lines)
    risk_count = len(risk_lines)
    blocker_count = len(blocker_lines)
    decision_count = len(decision_lines)
    metric_signal_count = len(metric_lines) + len(amounts)
    health_score = _project_health_score(
        risk_count=risk_count,
        blocker_count=blocker_count,
        validation_count=len(validation_issues),
        healthy_count=len(healthy_lines),
        word_count=word_count,
    )

    return {
        "document_id": document_id,
        "filename": filename,
        "uploaded_at": uploaded_at,
        "storage_path": storage_path,
        "category": _category(filename, text),
        "line_count": len(lines),
        "word_count": word_count,
        "dates_detected": DATE_RE.findall(text),
        "language": _language(text),
        "ticket_ids": ticket_ids,
        "ticket_count": ticket_count,
        "risk_count": risk_count,
        "risk_samples": risk_lines[:5],
        "blocker_count": blocker_count,
        "blocker_samples": blocker_lines[:5],
        "decision_count": decision_count,
        "decision_samples": decision_lines[:5],
        "metric_signal_count": metric_signal_count,
        "metric_lines": metric_lines[:5],
        "amounts": amounts[:250],
        "metric_outliers": metric_outliers,
        "total_metric_value": round(sum(amounts), 2),
        "average_metric_value": round(sum(amounts) / len(amounts), 2) if amounts else 0,
        "project_health_score": health_score,
        "kt_readiness_score": round(min(100, (word_count / 8) + (decision_count * 4) + (ticket_count * 2)), 1),
        "validation_issues": validation_issues,
        # Legacy aliases keep old stored data/export consumers from breaking.
        "total_amount": round(sum(amounts), 2),
        "average_amount": round(sum(amounts) / len(amounts), 2) if amounts else 0,
        "exception_count": risk_count,
        "exception_samples": risk_lines[:5],
        "compliance_ratio": round(health_score / 100, 4),
    }


def detect_anomalies(analyses: List[Dict]) -> List[Dict]:
    anomalies = []
    totals = [_metric_value(item) for item in analyses if _metric_value(item) > 0]
    avg_total = mean(totals) if totals else 0
    total_spread = pstdev(totals) if len(totals) > 1 else 0

    for item in analyses:
        doc_id = item.get("document_id")
        filename = item.get("filename", "Unknown")
        total = _metric_value(item)
        risk_count = _risk_count(item)
        blocker_count = _blocker_count(item)
        health = _health_score(item)
        z_score = (total - avg_total) / total_spread if total_spread else 0

        if blocker_count >= 2:
            anomalies.append({
                "type": "blocker_cluster",
                "severity": "high",
                "document_id": doc_id,
                "filename": filename,
                "metric": "blocker_count",
                "value": blocker_count,
                "score": blocker_count,
                "description": "Multiple blocker or dependency signals were detected in this source.",
            })

        if risk_count >= 5:
            anomalies.append({
                "type": "risk_cluster",
                "severity": "high" if risk_count >= 8 else "medium",
                "document_id": doc_id,
                "filename": filename,
                "metric": "risk_count",
                "value": risk_count,
                "score": risk_count,
                "description": "This source contains a high concentration of risk, issue, incident, or error signals.",
            })

        if health and health < 70:
            anomalies.append({
                "type": "low_project_health",
                "severity": "high" if health < 50 else "medium",
                "document_id": doc_id,
                "filename": filename,
                "metric": "project_health_score",
                "value": health,
                "score": round(100 - health, 2),
                "description": "Project health score is below the review threshold for this source.",
            })

        if total_spread and abs(z_score) >= 2:
            anomalies.append({
                "type": "metric_value_outlier",
                "severity": "high" if abs(z_score) >= 3 else "medium",
                "document_id": doc_id,
                "filename": filename,
                "metric": "total_metric_value",
                "value": round(total, 2),
                "score": round(z_score, 2),
                "description": "Numeric metric total is statistically unusual compared with other uploaded sources.",
            })

        for outlier in item.get("metric_outliers", item.get("amount_outliers", [])):
            anomalies.append({
                "type": "line_metric_outlier",
                "severity": "medium",
                "document_id": doc_id,
                "filename": filename,
                "metric": "numeric_value",
                "value": outlier.get("amount"),
                "score": outlier.get("z_score"),
                "description": outlier.get("reason"),
            })

    return sorted(anomalies, key=lambda a: (a.get("severity") != "high", -abs(a.get("score") or 0)))[:50]


def build_insights(analyses: List[Dict], anomalies: List[Dict], validation_issues: List[Dict]) -> List[Dict]:
    insights = []
    total_blockers = sum(_blocker_count(item) for item in analyses)
    total_risks = sum(_risk_count(item) for item in analyses)

    if total_blockers:
        insights.append({
            "type": "blocker_focus",
            "severity": "high",
            "title": f"{total_blockers} blocker signal(s) need attention",
            "description": "Some sources mention blocked work, unresolved dependencies, or delayed execution.",
            "action": "Review the blocker queue before planning the next handoff or sprint update.",
        })

    if anomalies:
        high_count = sum(1 for item in anomalies if item.get("severity") == "high")
        insights.append({
            "type": "project_health",
            "severity": "high" if high_count else "medium",
            "title": f"{len(anomalies)} project health signal(s) detected",
            "description": "Review sources with clustered blockers, concentrated risks, low health score, or unusual metric values.",
            "action": "Use the source documents and AI chat to validate root cause and next action.",
        })

    if validation_issues:
        insights.append({
            "type": "data_quality",
            "severity": "medium",
            "title": f"{len(validation_issues)} data quality issue(s) need review",
            "description": "Some uploaded sources are missing dates, project signals, or enough extracted text.",
            "action": "Upload richer project exports, runbooks, chats, tickets, or metrics reports.",
        })

    if analyses:
        riskiest = max(analyses, key=lambda item: (_risk_count(item), _blocker_count(item)))
        if total_risks:
            insights.append({
                "type": "risk_focus",
                "severity": "info",
                "title": f"Riskiest source: {riskiest.get('filename', 'Unknown')}",
                "description": f"This source contains {_risk_count(riskiest)} risk signal(s) and {_blocker_count(riskiest)} blocker signal(s).",
                "action": "Ask the AI chat to summarize this source before handoff.",
                "document_id": riskiest.get("document_id"),
            })

        source_types = Counter(item.get("category", "General Project Data") for item in analyses)
        insights.append({
            "type": "kt_readiness",
            "severity": "info",
            "title": f"KT base spans {len(source_types)} source type(s)",
            "description": "Base can generate a stronger KT brief when docs, tickets, chats, incidents, and metrics are uploaded together.",
            "action": "Open the KT Brief view to generate onboarding or handoff context.",
        })

        languages = Counter((item.get("language") or {}).get("name", "Unknown") for item in analyses)
        if len(languages) > 1:
            insights.append({
                "type": "multi_language",
                "severity": "info",
                "title": f"{len(languages)} document languages detected",
                "description": "AI responses can be requested in multiple languages from the top bar.",
                "action": "Use the chat language selector when preparing localized KT summaries.",
            })

    if not insights:
        insights.append({
            "type": "baseline",
            "severity": "info",
            "title": "No project signals detected yet",
            "description": "Upload project docs, Jira exports, chats, runbooks, incidents, or metrics reports to build a KT baseline.",
            "action": "Start with an architecture doc plus recent tickets or sprint notes.",
        })

    return insights


def build_pivot(analyses: List[Dict]) -> Dict:
    categories = sorted({item.get("category", "General Project Data") for item in analyses})
    periods = sorted({_time_bucket(item) for item in analyses})
    metric_cells = defaultdict(float)
    risk_cells = defaultdict(int)
    blocker_cells = defaultdict(int)
    ticket_cells = defaultdict(int)

    for item in analyses:
        key = (item.get("category", "General Project Data"), _time_bucket(item))
        metric_cells[key] += _metric_value(item)
        risk_cells[key] += _risk_count(item)
        blocker_cells[key] += _blocker_count(item)
        ticket_cells[key] += _ticket_count(item)

    metric_rows = [
        {
            "category": category,
            "values": [round(metric_cells[(category, period)], 2) for period in periods],
        }
        for category in categories
    ]

    return {
        "rows": categories,
        "columns": periods,
        "metric_values": metric_rows,
        "amounts": metric_rows,
        "risks": [
            {
                "category": category,
                "values": [risk_cells[(category, period)] for period in periods],
            }
            for category in categories
        ],
        "blockers": [
            {
                "category": category,
                "values": [blocker_cells[(category, period)] for period in periods],
            }
            for category in categories
        ],
        "tickets": [
            {
                "category": category,
                "values": [ticket_cells[(category, period)] for period in periods],
            }
            for category in categories
        ],
    }


def build_multi_axis_trends(analyses: List[Dict]) -> List[Dict]:
    by_period = defaultdict(lambda: {
        "metric_value": 0,
        "risks": 0,
        "blockers": 0,
        "tickets": 0,
        "health_sum": 0,
        "documents": 0,
    })
    for item in analyses:
        bucket = by_period[_time_bucket(item)]
        bucket["metric_value"] += _metric_value(item)
        bucket["risks"] += _risk_count(item)
        bucket["blockers"] += _blocker_count(item)
        bucket["tickets"] += _ticket_count(item)
        bucket["health_sum"] += _health_score(item)
        bucket["documents"] += 1

    rows = []
    for period, values in sorted(by_period.items()):
        docs = values["documents"] or 1
        health = round(values["health_sum"] / docs, 1)
        rows.append({
            "period": period,
            "metric_value": round(values["metric_value"], 2),
            "risks": values["risks"],
            "blockers": values["blockers"],
            "tickets": values["tickets"],
            "project_health_score": health,
            "documents": docs,
            # Legacy aliases.
            "amount": round(values["metric_value"], 2),
            "exceptions": values["risks"],
            "compliance_ratio": round(health / 100, 4),
        })
    return rows


def build_bi_dataset(tenant_id: str) -> Dict:
    analyses = list_document_analyses(tenant_id)
    dashboard = build_dashboard(tenant_id)
    return {
        "tenant_id": tenant_id,
        "dataset": "project_intelligence",
        "version": "3.0",
        "tables": {
            "documents": analyses,
            "anomalies": dashboard["anomalies"],
            "insights": dashboard["insights"],
            "pivot_metric_values": dashboard["charts"]["pivot_table"]["metric_values"],
            "multi_axis_trends": dashboard["charts"]["multi_axis_trends"],
        },
    }


def build_knowledge_graph(tenant_id: str) -> Dict:
    analyses = list_document_analyses(tenant_id)
    nodes = {}
    edge_weights = defaultdict(float)
    edge_details = {}

    def add_node(node_id: str, label: str, node_type: str, weight: float = 1, metadata: Dict = None) -> None:
        existing = nodes.get(node_id)
        if existing:
            existing["weight"] = max(existing["weight"], round(weight, 2))
            if metadata:
                existing.setdefault("metadata", {}).update(metadata)
            return
        nodes[node_id] = {
            "id": node_id,
            "label": label,
            "type": node_type,
            "weight": round(weight, 2),
            "metadata": metadata or {},
        }

    def add_edge(
        source: str,
        target: str,
        edge_type: str,
        weight: float = 1,
        description: str = "",
        metadata: Dict = None,
    ) -> None:
        if source == target:
            return
        key = (source, target, edge_type)
        edge_weights[key] += max(1, weight)
        if key not in edge_details:
            edge_details[key] = {"description": description, "metadata": metadata or {}}

    add_node(
        "project",
        "Project",
        "project",
        max(4, len(analyses)),
        {"description": "The selected project workspace. It connects every uploaded source and the entities extracted from those sources."},
    )
    for signal_type, label in (
        ("risks", "Risks"),
        ("blockers", "Blockers"),
        ("decisions", "Decisions"),
        ("metrics", "Metrics"),
    ):
        add_node(
            _signal_node_id(signal_type),
            label,
            "signal",
            2,
            {"description": f"Aggregated {label.lower()} extracted from uploaded project sources."},
        )

    for item in analyses:
        document_id = item.get("document_id") or item.get("filename", "unknown")
        doc_node_id = f"doc:{document_id}"
        filename = item.get("filename", "Unknown")
        category = item.get("category", "General Project Data")
        period = _time_bucket(item)
        language = (item.get("language") or {}).get("name", "Unknown")
        risk_count = _risk_count(item)
        blocker_count = _blocker_count(item)
        decision_count = _decision_count(item)
        metric_count = int(item.get("metric_signal_count", len(item.get("amounts", []))) or 0)

        add_node(
            doc_node_id,
            filename,
            "document",
            max(4, min(18, item.get("chunk_count", 1) + risk_count + blocker_count + 1)),
            {
                "document_id": document_id,
                "filename": filename,
                "source_type": category,
                "uploaded_at": item.get("uploaded_at", ""),
                "health": _health_score(item),
                "risks": risk_count,
                "blockers": blocker_count,
                "tickets": _ticket_count(item),
                "decisions": decision_count,
                "metrics": metric_count,
                "description": (
                    f"{filename} is an uploaded {category} source. "
                    f"It contributed {_ticket_count(item)} ticket/entity references, "
                    f"{risk_count} risk signals, {blocker_count} blocker signals, "
                    f"{decision_count} decision signals, and {metric_count} metric signals."
                ),
            },
        )
        add_edge(
            "project",
            doc_node_id,
            "contains",
            2,
            f"Project contains the uploaded source {filename}.",
            {"evidence": filename},
        )

        category_node_id = f"source:{category}"
        add_node(
            category_node_id,
            category,
            "source_type",
            3,
            {"description": f"Source type bucket assigned from content markers. Documents connected here are classified as {category}."},
        )
        add_edge(
            doc_node_id,
            category_node_id,
            "source_type",
            2,
            f"{filename} was classified as {category}.",
        )

        period_node_id = f"period:{period}"
        add_node(
            period_node_id,
            period,
            "period",
            2,
            {"description": f"Time bucket {period} based on the source's detected dates or upload date."},
        )
        add_edge(
            doc_node_id,
            period_node_id,
            "uploaded_or_detected",
            1,
            f"{filename} is associated with the {period} time bucket.",
        )

        language_node_id = f"language:{language}"
        add_node(language_node_id, language, "language", 1, {"description": f"Detected source language: {language}."})
        add_edge(doc_node_id, language_node_id, "language", 1, f"{filename} was detected as {language}.")

        if risk_count:
            signal_id = _signal_node_id("risks")
            add_node(signal_id, "Risks", "signal", min(16, risk_count))
            add_edge(
                doc_node_id,
                signal_id,
                "risk_signal",
                risk_count,
                f"{filename} contains {risk_count} risk-related line(s).",
                {"samples": item.get("risk_samples", [])},
            )
        if blocker_count:
            signal_id = _signal_node_id("blockers")
            add_node(signal_id, "Blockers", "signal", min(16, blocker_count))
            add_edge(
                doc_node_id,
                signal_id,
                "blocker_signal",
                blocker_count,
                f"{filename} contains {blocker_count} blocker/dependency line(s).",
                {"samples": item.get("blocker_samples", [])},
            )
        if decision_count:
            signal_id = _signal_node_id("decisions")
            add_node(signal_id, "Decisions", "signal", min(16, decision_count))
            add_edge(
                doc_node_id,
                signal_id,
                "decision_signal",
                decision_count,
                f"{filename} contains {decision_count} decision/action line(s).",
                {"samples": item.get("decision_samples", [])},
            )
        if metric_count:
            signal_id = _signal_node_id("metrics")
            add_node(signal_id, "Metrics", "signal", min(16, metric_count))
            add_edge(
                doc_node_id,
                signal_id,
                "metric_signal",
                min(metric_count, 25),
                f"{filename} contains {metric_count} metric/numeric signal(s).",
                {"samples": item.get("metric_lines", [])},
            )

        for ticket_id in item.get("ticket_ids", [])[:100]:
            node_type = _entity_type(ticket_id)
            entity_node_id = f"{node_type}:{ticket_id}"
            add_node(
                entity_node_id,
                ticket_id,
                node_type,
                2,
                {"description": f"{ticket_id} is a {node_type.replace('_', ' ')} reference mentioned by one or more uploaded sources."},
            )
            nodes[entity_node_id].setdefault("metadata", {})["mentions"] = nodes[entity_node_id].get("metadata", {}).get("mentions", 0) + 1
            add_edge(
                doc_node_id,
                entity_node_id,
                "mentions",
                2 if node_type in {"incident", "ticket"} else 1,
                f"{filename} mentions {ticket_id}.",
                {"evidence": filename},
            )

    edges = [
        {
            "source": source,
            "target": target,
            "type": edge_type,
            "weight": round(weight, 2),
            "description": edge_details.get((source, target, edge_type), {}).get("description", ""),
            "metadata": edge_details.get((source, target, edge_type), {}).get("metadata", {}),
        }
        for (source, target, edge_type), weight in edge_weights.items()
    ]

    node_values = list(nodes.values())
    return {
        "nodes": node_values,
        "edges": edges,
        "stats": {
            "documents": len(analyses),
            "nodes": len(node_values),
            "edges": len(edges),
            "tickets": sum(1 for node in node_values if node["type"] == "ticket"),
            "incidents": sum(1 for node in node_values if node["type"] == "incident"),
            "pull_requests": sum(1 for node in node_values if node["type"] == "pull_request"),
        },
    }


def merge_analyses_with_indexed_documents(tenant_id: str, analyses: List[Dict]) -> List[Dict]:
    merged = list(analyses)
    analysed_ids = {
        item.get("document_id")
        for item in analyses
        if item.get("document_id")
    }
    for doc in list_documents(tenant_id):
        document_id = doc.get("document_id")
        if not document_id or document_id in analysed_ids:
            continue
        merged.append({
            "document_id": document_id,
            "filename": doc.get("filename", "unknown"),
            "uploaded_at": doc.get("uploaded_at", ""),
            "chunk_count": doc.get("chunk_count", 0),
            "category": "Indexed Source",
            "language": {"name": "Unknown"},
            "validation_issues": [],
            "risk_count": 0,
            "blocker_count": 0,
            "ticket_count": 0,
            "decision_count": 0,
            "total_metric_value": 0,
            "project_health_score": 0,
            "kt_readiness_score": 0,
            "summary": "Indexed source available in the vector store; detailed analytics were not recorded for this upload.",
        })
        analysed_ids.add(document_id)
    return merged


def build_dashboard(tenant_id: str) -> Dict:
    analyses = merge_analyses_with_indexed_documents(tenant_id, list_document_analyses(tenant_id))
    doc_count = len(analyses)
    total_metric_value = round(sum(_metric_value(item) for item in analyses), 2)
    total_risks = sum(_risk_count(item) for item in analyses)
    total_blockers = sum(_blocker_count(item) for item in analyses)
    total_tickets = sum(_ticket_count(item) for item in analyses)
    total_decisions = sum(_decision_count(item) for item in analyses)
    avg_health = (
        round(sum(_health_score(item) for item in analyses) / doc_count, 1)
        if doc_count
        else 0
    )
    source_totals = Counter()
    metric_totals = Counter()
    risk_totals = Counter()
    blocker_totals = Counter()
    language_totals = Counter()
    validation_issues = []

    for item in analyses:
        category = item.get("category", "General Project Data")
        source_totals[category] += 1
        metric_totals[category] += _metric_value(item)
        risk_totals[category] += _risk_count(item)
        blocker_totals[category] += _blocker_count(item)
        language = (item.get("language") or {}).get("name", "Unknown")
        language_totals[language] += 1
        for issue in item.get("validation_issues", []):
            validation_issues.append({
                "document_id": item.get("document_id"),
                "filename": item.get("filename"),
                "issue": issue,
            })

    anomalies = detect_anomalies(analyses)
    insights = build_insights(analyses, anomalies, validation_issues)

    return {
        "kpis": {
            "documents": doc_count,
            "project_health_score": avg_health,
            "risks": total_risks,
            "blockers": total_blockers,
            "tickets": total_tickets,
            "decisions": total_decisions,
            "total_metric_value": total_metric_value,
            "validation_issues": len(validation_issues),
            "anomalies": len(anomalies),
            # Legacy aliases.
            "total_audited_amount": total_metric_value,
            "exceptions": total_risks,
            "compliance_ratio": round(avg_health / 100, 4) if avg_health else 0,
        },
        "charts": {
            "documents_by_source": [
                {"label": label, "value": value}
                for label, value in source_totals.items()
            ],
            "metric_value_by_source": [
                {"label": label, "value": round(value, 2)}
                for label, value in metric_totals.items()
            ],
            "risks_by_source": [
                {"label": label, "value": value}
                for label, value in risk_totals.items()
            ],
            "blockers_by_source": [
                {"label": label, "value": value}
                for label, value in blocker_totals.items()
            ],
            "documents_over_time": [
                {"label": item.get("uploaded_at", "")[:10] or "Unknown", "value": 1}
                for item in analyses
            ],
            "languages": [
                {"label": label, "value": value}
                for label, value in language_totals.items()
            ],
            "pivot_table": build_pivot(analyses),
            "multi_axis_trends": build_multi_axis_trends(analyses),
            # Legacy aliases for existing UI/export consumers.
            "amount_by_category": [
                {"label": label, "value": round(value, 2)}
                for label, value in metric_totals.items()
            ],
            "exceptions_by_category": [
                {"label": label, "value": value}
                for label, value in risk_totals.items()
            ],
        },
        "insights": insights,
        "anomalies": anomalies,
        "documents": analyses,
        "validation_issues": validation_issues[:50],
        "audit_events": read_audit_events(tenant_id, limit=20),
    }
