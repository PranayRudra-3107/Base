import re
from collections import Counter, defaultdict
from statistics import mean, pstdev
from typing import Dict, List

from app.services.audit_log import read_audit_events
from app.services.storage import list_document_analyses

AMOUNT_RE = re.compile(r"(?<![A-Za-z0-9])(?:USD|EUR|GBP|INR|\$|€|£)?\s*(-?\d[\d,]*(?:\.\d{1,2})?)")
DATE_RE = re.compile(r"\b(?:\d{4}-\d{1,2}-\d{1,2}|\d{1,2}[/-]\d{1,2}[/-]\d{2,4})\b")
EXCEPTION_WORDS = ("exception", "finding", "issue", "variance", "anomaly", "deficiency", "failed", "missing")
COMPLIANCE_WORDS = ("compliant", "compliance", "approved", "passed", "complete")
LANGUAGE_MARKERS = {
    "en": ("the", "and", "audit", "invoice", "control", "compliance"),
    "es": ("el", "la", "auditoria", "factura", "control", "cumplimiento"),
    "fr": ("le", "la", "audit", "facture", "controle", "conformite"),
    "de": ("der", "die", "prüfung", "rechnung", "kontrolle", "konformität"),
    "hi": ("लेखा", "चालान", "अनुपालन", "नियंत्रण", "रिपोर्ट"),
}
LANGUAGE_NAMES = {
    "en": "English",
    "es": "Spanish",
    "fr": "French",
    "de": "German",
    "hi": "Hindi",
    "unknown": "Unknown",
}


def _amounts(text: str) -> List[float]:
    values = []
    for match in AMOUNT_RE.finditer(text):
        raw = match.group(1).replace(",", "")
        try:
            value = float(raw)
        except ValueError:
            continue
        if abs(value) >= 1:
            values.append(value)
    return values


def _category(filename: str, text: str) -> str:
    haystack = f"{filename} {text[:1000]}".lower()
    if any(word in haystack for word in ("invoice", "expense", "cost", "spend")):
        return "Spend"
    if any(word in haystack for word in ("control", "policy", "compliance", "risk")):
        return "Compliance"
    if any(word in haystack for word in ("payroll", "salary", "employee")):
        return "Payroll"
    if any(word in haystack for word in ("vendor", "procurement", "purchase")):
        return "Procurement"
    return "General Audit"


def _language(text: str) -> Dict:
    haystack = f" {text[:4000].lower()} "
    if re.search(r"[\u0900-\u097F]", haystack):
        return {"code": "hi", "name": LANGUAGE_NAMES["hi"], "confidence": 0.92}

    scores = {}
    for code, markers in LANGUAGE_MARKERS.items():
        scores[code] = sum(1 for marker in markers if f" {marker} " in haystack)

    code, score = max(scores.items(), key=lambda item: item[1])
    if score == 0:
        return {"code": "unknown", "name": LANGUAGE_NAMES["unknown"], "confidence": 0}
    return {
        "code": code,
        "name": LANGUAGE_NAMES.get(code, code),
        "confidence": round(min(0.95, 0.45 + score * 0.12), 2),
    }


def _amount_outliers(amounts: List[float]) -> List[Dict]:
    if len(amounts) < 4:
        return []

    avg = mean(amounts)
    spread = pstdev(amounts)
    if spread == 0:
        return []

    outliers = []
    for value in amounts:
        z_score = (value - avg) / spread
        if abs(z_score) >= 2:
            outliers.append({
                "amount": round(value, 2),
                "z_score": round(z_score, 2),
                "reason": "Amount is more than two standard deviations from the document average.",
            })
    return outliers[:10]


def _time_bucket(item: Dict) -> str:
    dates = item.get("dates_detected") or []
    raw = dates[0] if dates else item.get("uploaded_at", "")
    match = re.search(r"(\d{4})[-/](\d{1,2})", raw)
    if match:
        return f"{match.group(1)}-{int(match.group(2)):02d}"
    return (item.get("uploaded_at", "")[:7] or "Unknown")


def analyze_document(document_id: str, filename: str, text: str, uploaded_at: str, storage_path: str = "") -> Dict:
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    lower_lines = [line.lower() for line in lines]
    amounts = _amounts(text)
    amount_outliers = _amount_outliers(amounts)
    exception_lines = [
        lines[i]
        for i, line in enumerate(lower_lines)
        if any(word in line for word in EXCEPTION_WORDS)
    ]
    compliance_hits = sum(1 for line in lower_lines if any(word in line for word in COMPLIANCE_WORDS))
    validation_issues = []

    if not amounts:
        validation_issues.append("No numeric audit amounts were detected.")
    if not DATE_RE.search(text):
        validation_issues.append("No audit dates were detected.")
    if len(text.split()) < 25:
        validation_issues.append("Document text is very short; extraction may be incomplete.")
    if amount_outliers:
        validation_issues.append(f"{len(amount_outliers)} unusually large or small amount(s) detected.")

    total_checks = max(len(lines), 1)
    exception_count = len(exception_lines)
    compliance_ratio = max(0, min(1, (compliance_hits + total_checks - exception_count) / total_checks))

    return {
        "document_id": document_id,
        "filename": filename,
        "uploaded_at": uploaded_at,
        "storage_path": storage_path,
        "category": _category(filename, text),
        "line_count": len(lines),
        "word_count": len(text.split()),
        "dates_detected": DATE_RE.findall(text),
        "language": _language(text),
        "amounts": amounts[:250],
        "amount_outliers": amount_outliers,
        "total_amount": round(sum(amounts), 2),
        "average_amount": round(sum(amounts) / len(amounts), 2) if amounts else 0,
        "exception_count": exception_count,
        "exception_samples": exception_lines[:5],
        "compliance_ratio": round(compliance_ratio, 4),
        "validation_issues": validation_issues,
    }


def detect_anomalies(analyses: List[Dict]) -> List[Dict]:
    anomalies = []
    totals = [item.get("total_amount", 0) for item in analyses if item.get("total_amount", 0) > 0]
    avg_total = mean(totals) if totals else 0
    total_spread = pstdev(totals) if len(totals) > 1 else 0

    for item in analyses:
        doc_id = item.get("document_id")
        filename = item.get("filename", "Unknown")
        total = item.get("total_amount", 0)
        z_score = (total - avg_total) / total_spread if total_spread else 0

        if total_spread and abs(z_score) >= 2:
            anomalies.append({
                "type": "amount_outlier",
                "severity": "high" if abs(z_score) >= 3 else "medium",
                "document_id": doc_id,
                "filename": filename,
                "metric": "total_amount",
                "value": round(total, 2),
                "score": round(z_score, 2),
                "description": "Document total is statistically unusual compared with other uploaded documents.",
            })

        if item.get("exception_count", 0) >= 3:
            anomalies.append({
                "type": "exception_cluster",
                "severity": "high",
                "document_id": doc_id,
                "filename": filename,
                "metric": "exception_count",
                "value": item.get("exception_count", 0),
                "score": item.get("exception_count", 0),
                "description": "Multiple exception or finding lines were detected in this document.",
            })

        if item.get("compliance_ratio", 1) < 0.8:
            anomalies.append({
                "type": "low_compliance",
                "severity": "medium",
                "document_id": doc_id,
                "filename": filename,
                "metric": "compliance_ratio",
                "value": item.get("compliance_ratio", 0),
                "score": round(1 - item.get("compliance_ratio", 0), 2),
                "description": "Compliance ratio is below the configured review threshold.",
            })

        for outlier in item.get("amount_outliers", []):
            anomalies.append({
                "type": "line_amount_outlier",
                "severity": "medium",
                "document_id": doc_id,
                "filename": filename,
                "metric": "amount",
                "value": outlier.get("amount"),
                "score": outlier.get("z_score"),
                "description": outlier.get("reason"),
            })

    return sorted(anomalies, key=lambda a: (a.get("severity") != "high", -abs(a.get("score") or 0)))[:50]


def build_insights(analyses: List[Dict], anomalies: List[Dict], validation_issues: List[Dict]) -> List[Dict]:
    insights = []
    if anomalies:
        high_count = sum(1 for item in anomalies if item.get("severity") == "high")
        insights.append({
            "type": "anomaly_detection",
            "severity": "high" if high_count else "medium",
            "title": f"{len(anomalies)} anomaly signal(s) detected",
            "description": "Review documents with unusual totals, clustered exceptions, low compliance, or line-level outlier amounts.",
            "action": "Open the anomaly queue and validate source documents before reporting.",
        })

    if validation_issues:
        insights.append({
            "type": "data_quality",
            "severity": "medium",
            "title": f"{len(validation_issues)} validation issue(s) need review",
            "description": "Some uploaded documents are missing dates, numeric audit amounts, or sufficient extracted text.",
            "action": "Use the validation queue to correct source data or re-upload higher quality documents.",
        })

    if analyses:
        highest = max(analyses, key=lambda item: item.get("total_amount", 0))
        insights.append({
            "type": "spend_focus",
            "severity": "info",
            "title": f"Largest audited amount: {highest.get('filename', 'Unknown')}",
            "description": f"This document contributes {round(highest.get('total_amount', 0), 2)} to the audited total.",
            "action": "Prioritize review if materiality thresholds apply.",
            "document_id": highest.get("document_id"),
        })

        languages = Counter((item.get("language") or {}).get("name", "Unknown") for item in analyses)
        if len(languages) > 1:
            insights.append({
                "type": "multi_language",
                "severity": "info",
                "title": f"{len(languages)} document languages detected",
                "description": "Analytics and RAG query responses can be filtered or requested by language.",
                "action": "Use the chat language selector when preparing localized summaries.",
            })

    if not insights:
        insights.append({
            "type": "baseline",
            "severity": "info",
            "title": "No high-risk signals detected yet",
            "description": "Upload more audit documents to build a richer anomaly and trend baseline.",
            "action": "Add reports, invoices, control logs, or CSV extracts.",
        })

    return insights


def build_pivot(analyses: List[Dict]) -> Dict:
    categories = sorted({item.get("category", "General Audit") for item in analyses})
    periods = sorted({_time_bucket(item) for item in analyses})
    amount_cells = defaultdict(float)
    exception_cells = defaultdict(int)

    for item in analyses:
        key = (item.get("category", "General Audit"), _time_bucket(item))
        amount_cells[key] += item.get("total_amount", 0)
        exception_cells[key] += item.get("exception_count", 0)

    return {
        "rows": categories,
        "columns": periods,
        "amounts": [
            {
                "category": category,
                "values": [round(amount_cells[(category, period)], 2) for period in periods],
            }
            for category in categories
        ],
        "exceptions": [
            {
                "category": category,
                "values": [exception_cells[(category, period)] for period in periods],
            }
            for category in categories
        ],
    }


def build_multi_axis_trends(analyses: List[Dict]) -> List[Dict]:
    by_period = defaultdict(lambda: {"amount": 0, "exceptions": 0, "compliance_sum": 0, "documents": 0})
    for item in analyses:
        bucket = by_period[_time_bucket(item)]
        bucket["amount"] += item.get("total_amount", 0)
        bucket["exceptions"] += item.get("exception_count", 0)
        bucket["compliance_sum"] += item.get("compliance_ratio", 0)
        bucket["documents"] += 1

    rows = []
    for period, values in sorted(by_period.items()):
        docs = values["documents"] or 1
        rows.append({
            "period": period,
            "amount": round(values["amount"], 2),
            "exceptions": values["exceptions"],
            "compliance_ratio": round(values["compliance_sum"] / docs, 4),
            "documents": docs,
        })
    return rows


def build_bi_dataset(tenant_id: str) -> Dict:
    analyses = list_document_analyses(tenant_id)
    dashboard = build_dashboard(tenant_id)
    return {
        "tenant_id": tenant_id,
        "dataset": "audit_analytics",
        "version": "2.0",
        "tables": {
            "documents": analyses,
            "anomalies": dashboard["anomalies"],
            "insights": dashboard["insights"],
            "pivot_amounts": dashboard["charts"]["pivot_table"]["amounts"],
            "multi_axis_trends": dashboard["charts"]["multi_axis_trends"],
        },
    }


def build_dashboard(tenant_id: str) -> Dict:
    analyses = list_document_analyses(tenant_id)
    doc_count = len(analyses)
    total_amount = round(sum(item.get("total_amount", 0) for item in analyses), 2)
    total_exceptions = sum(item.get("exception_count", 0) for item in analyses)
    avg_compliance = (
        round(sum(item.get("compliance_ratio", 0) for item in analyses) / doc_count, 4)
        if doc_count
        else 0
    )
    category_totals = Counter()
    exception_totals = Counter()
    language_totals = Counter()
    validation_issues = []

    for item in analyses:
        category = item.get("category", "General Audit")
        category_totals[category] += item.get("total_amount", 0)
        exception_totals[category] += item.get("exception_count", 0)
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
            "total_audited_amount": total_amount,
            "exceptions": total_exceptions,
            "compliance_ratio": avg_compliance,
            "validation_issues": len(validation_issues),
            "anomalies": len(anomalies),
        },
        "charts": {
            "amount_by_category": [
                {"label": label, "value": round(value, 2)}
                for label, value in category_totals.items()
            ],
            "exceptions_by_category": [
                {"label": label, "value": value}
                for label, value in exception_totals.items()
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
        },
        "insights": insights,
        "anomalies": anomalies,
        "documents": analyses,
        "validation_issues": validation_issues[:50],
        "audit_events": read_audit_events(tenant_id, limit=20),
    }
