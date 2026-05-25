import base64
import html
import json
import re
import uuid
from datetime import datetime, timedelta
from typing import Any, Awaitable, Callable, Dict, List, Tuple
from urllib.parse import quote, urlencode

import httpx

from app.core.config import get_settings
from app.services.audit_log import write_audit_event
from app.services.connector_ingestion import ingest_connector_text
from app.services.storage import read_json, write_json

settings = get_settings()

CONNECTIONS_KEY = "connector_connections"
OAUTH_STATES_KEY = "connector_oauth_states"
SECRET_FIELD_HINTS = ("token", "secret", "password", "key", "pat", "database_url", "access_token", "refresh_token")
SOURCE_CODE_EXTENSIONS = {
    ".cfg",
    ".conf",
    ".css",
    ".go",
    ".graphql",
    ".hcl",
    ".html",
    ".ini",
    ".java",
    ".js",
    ".json",
    ".jsx",
    ".kt",
    ".md",
    ".php",
    ".properties",
    ".proto",
    ".py",
    ".rb",
    ".rs",
    ".scala",
    ".sh",
    ".sql",
    ".swift",
    ".toml",
    ".ts",
    ".tsx",
    ".txt",
    ".xml",
    ".yaml",
    ".yml",
}
SOURCE_CODE_FILENAMES = {
    "dockerfile",
    "makefile",
    "procfile",
    "requirements.txt",
    "pyproject.toml",
    "package.json",
    "package-lock.json",
    "pnpm-lock.yaml",
    "yarn.lock",
    "vite.config.js",
    "vite.config.ts",
    "next.config.js",
    "next.config.ts",
    "tsconfig.json",
}
SOURCE_SKIP_DIRS = {
    ".cache",
    ".git",
    ".next",
    ".serverless",
    ".terraform",
    ".venv",
    "__pycache__",
    "build",
    "chroma_db",
    "coverage",
    "data",
    "dist",
    "node_modules",
    "logs",
    "synthetic data",
    "synthetic_data",
    "target",
    "tmp",
    "vendor",
    "venv",
}
SOURCE_SKIP_EXTENSIONS = {
    ".7z",
    ".avif",
    ".db",
    ".dll",
    ".dylib",
    ".exe",
    ".gif",
    ".gz",
    ".ico",
    ".jpeg",
    ".jpg",
    ".lockb",
    ".mov",
    ".mp3",
    ".mp4",
    ".pdf",
    ".png",
    ".pyc",
    ".sqlite",
    ".sqlite3",
    ".tar",
    ".webp",
    ".woff",
    ".woff2",
    ".zip",
}
MAX_SOURCE_FILES = 120
MAX_SOURCE_FILE_BYTES = 120_000
MAX_SOURCE_FILE_CHARS = 24_000
MAX_SOURCE_TOTAL_CHARS = 420_000


def _field(
    name: str,
    label: str,
    secret: bool = False,
    required: bool = True,
    placeholder: str = "",
    help_text: str = "",
) -> Dict[str, Any]:
    return {
        "name": name,
        "label": label,
        "secret": secret,
        "required": required,
        "placeholder": placeholder,
        "help": help_text,
    }


CONNECTOR_CATALOG: List[Dict[str, Any]] = [
    {
        "id": "jira",
        "name": "Jira",
        "group": "Project Work",
        "description": "Issues, epics, sprint movement, blockers, owners, and comments.",
        "keywords": ["jira", "ticket", "story", "sprint", "epic", "backlog"],
        "auth_type": "atlassian_oauth_or_api_token",
        "oauth_provider": "atlassian",
        "fields": [
            _field("site_url", "Jira site URL", required=False, placeholder="https://company.atlassian.net"),
            _field("email", "Atlassian email", required=False),
            _field("api_token", "Atlassian API token", secret=True, required=False),
            _field("jql", "JQL", required=False, placeholder="project = BASE ORDER BY updated DESC"),
        ],
    },
    {
        "id": "linear",
        "name": "Linear",
        "group": "Project Work",
        "description": "Issues, owners, states, cycles, priorities, and delivery signals.",
        "keywords": ["linear", "issue", "cycle", "team", "priority"],
        "auth_type": "api_key",
        "fields": [
            _field("api_key", "Linear API key", secret=True),
            _field("query", "Issue search", required=False, placeholder="team.key = BASE"),
        ],
    },
    {
        "id": "azure_boards",
        "name": "Azure Boards",
        "group": "Project Work",
        "description": "Work items, states, assignments, blockers, and sprint status.",
        "keywords": ["azure boards", "work item", "wiql", "sprint"],
        "auth_type": "personal_access_token",
        "fields": [
            _field("organization", "Azure DevOps organization"),
            _field("project", "Project"),
            _field("pat", "Personal access token", secret=True),
            _field("wiql", "WIQL", required=False, placeholder="SELECT [System.Id] FROM WorkItems ORDER BY [System.ChangedDate] DESC"),
        ],
    },
    {
        "id": "slack",
        "name": "Slack",
        "group": "Communication",
        "description": "Channel decisions, standups, incident rooms, and coordination history.",
        "keywords": ["slack", "channel", "standup", "conversation"],
        "auth_type": "bot_or_user_token",
        "fields": [
            _field("bot_token", "Slack bot/user token", secret=True),
            _field("channel_id", "Conversation/channel ID", placeholder="C0123456789"),
        ],
    },
    {
        "id": "teams",
        "name": "Microsoft Teams",
        "group": "Communication",
        "description": "Team channels, chat context, handoff notes, and decisions through Microsoft Graph.",
        "keywords": ["teams", "chat", "standup", "conversation"],
        "auth_type": "microsoft_oauth_or_access_token",
        "oauth_provider": "microsoft",
        "fields": [
            _field("access_token", "Microsoft Graph access token", secret=True, required=False),
            _field("team_id", "Team ID", required=False),
            _field("channel_id", "Channel ID", required=False),
            _field("chat_id", "Chat ID", required=False),
        ],
    },
    {
        "id": "email",
        "name": "Email",
        "group": "Communication",
        "description": "Stakeholder decisions, approvals, escalations, and long-form project context.",
        "keywords": ["email", "mail", "inbox", "subject"],
        "auth_type": "microsoft_oauth_or_access_token",
        "oauth_provider": "microsoft",
        "fields": [
            _field("access_token", "Microsoft Graph access token", secret=True, required=False),
            _field("search", "Mail search", required=False, placeholder="subject:project OR project-name"),
        ],
    },
    {
        "id": "github",
        "name": "GitHub",
        "group": "Development",
        "description": "PRs, commits, branches, releases, reviewers, and bounded source-code snapshots.",
        "keywords": ["github", "pull request", "pr-", "commit", "branch", "release", "source code", "repository"],
        "auth_type": "token_optional",
        "fields": [
            _field("owner", "Repository owner"),
            _field("repo", "Repository name"),
            _field("token", "GitHub token", secret=True, required=False),
            _field("ref", "Branch or ref", required=False, placeholder="main"),
            _field("code_paths", "Code paths", required=False, placeholder="backend/app, frontend/index.html, README.md"),
            _field(
                "include_code",
                "Index source code",
                required=False,
                placeholder="true",
                help_text="Leave blank or use true to index a safe source snapshot. Use false for PR/commit metadata only.",
            ),
        ],
    },
    {
        "id": "gitlab",
        "name": "GitLab",
        "group": "Development",
        "description": "Merge requests, commits, branches, releases, and deployment context.",
        "keywords": ["gitlab", "merge request", "commit", "branch", "release"],
        "auth_type": "access_token",
        "fields": [
            _field("base_url", "GitLab URL", required=False, placeholder="https://gitlab.com"),
            _field("project_id", "Project ID or URL-encoded path"),
            _field("token", "GitLab token", secret=True, required=False),
        ],
    },
    {
        "id": "bitbucket",
        "name": "Bitbucket",
        "group": "Development",
        "description": "Pull requests, commits, branches, and release context from Bitbucket Cloud.",
        "keywords": ["bitbucket", "pull request", "commit", "branch"],
        "auth_type": "app_password_or_token",
        "fields": [
            _field("workspace", "Workspace"),
            _field("repo_slug", "Repository slug"),
            _field("username", "Username", required=False),
            _field("app_password", "App password", secret=True, required=False),
            _field("access_token", "OAuth access token", secret=True, required=False),
        ],
    },
    {
        "id": "mixpanel",
        "name": "Mixpanel",
        "group": "Product Analytics",
        "description": "Product events, funnels, usage movement, and engagement context.",
        "keywords": ["mixpanel", "event", "funnel", "retention"],
        "auth_type": "service_account_or_export_url",
        "fields": [
            _field("service_account_username", "Service account username", required=False),
            _field("service_account_secret", "Service account secret", secret=True, required=False),
            _field("event", "Event name", required=False),
            _field("from_date", "From date", required=False, placeholder="2026-01-01"),
            _field("to_date", "To date", required=False, placeholder="2026-05-24"),
            _field("export_url", "Prebuilt export URL", required=False),
        ],
    },
    {
        "id": "amplitude",
        "name": "Amplitude",
        "group": "Product Analytics",
        "description": "Event taxonomy, product usage, retention, and growth signals.",
        "keywords": ["amplitude", "event", "retention", "analytics"],
        "auth_type": "api_key_secret",
        "fields": [
            _field("api_key", "Amplitude API key"),
            _field("secret_key", "Amplitude secret key", secret=True),
        ],
    },
    {
        "id": "ga4",
        "name": "Google Analytics 4",
        "group": "Product Analytics",
        "description": "Traffic, engagement, sessions, conversions, and channel metrics.",
        "keywords": ["ga4", "google analytics", "sessions", "conversion"],
        "auth_type": "access_token",
        "fields": [
            _field("property_id", "GA4 property ID"),
            _field("access_token", "Google OAuth access token", secret=True),
        ],
    },
    {
        "id": "posthog",
        "name": "PostHog",
        "group": "Product Analytics",
        "description": "Events, feature flags, insights, funnels, and product behavior.",
        "keywords": ["posthog", "event", "feature flag", "insight"],
        "auth_type": "personal_api_key",
        "fields": [
            _field("host", "PostHog host", required=False, placeholder="https://app.posthog.com"),
            _field("project_id", "Project ID"),
            _field("personal_api_key", "Personal API key", secret=True),
        ],
    },
    {
        "id": "custom_events",
        "name": "Custom Event Tables",
        "group": "Product Analytics",
        "description": "A generic JSON endpoint for internal event tables or analytics exports.",
        "keywords": ["custom events", "event table", "analytics"],
        "auth_type": "generic_json_endpoint",
        "fields": [
            _field("endpoint_url", "JSON endpoint URL"),
            _field("api_token", "Bearer token", secret=True, required=False),
        ],
    },
    {
        "id": "datadog",
        "name": "Datadog",
        "group": "Observability",
        "description": "Monitors, dashboards, incidents, latency, errors, and service health.",
        "keywords": ["datadog", "monitor", "latency", "error rate"],
        "auth_type": "api_and_app_key",
        "fields": [
            _field("site", "Datadog site", required=False, placeholder="datadoghq.com"),
            _field("api_key", "API key", secret=True),
            _field("app_key", "Application key", secret=True),
        ],
    },
    {
        "id": "grafana",
        "name": "Grafana / Metrics",
        "group": "Observability",
        "description": "Dashboards, panel queries, traffic, latency, errors, and uptime signals.",
        "keywords": ["grafana", "traffic", "latency", "p95", "p99", "error rate", "requests"],
        "auth_type": "service_account_token",
        "fields": [
            _field("base_url", "Grafana URL", placeholder="https://grafana.company.com"),
            _field("api_token", "Service account token", secret=True),
            _field("dashboard_uid", "Dashboard UID", required=False),
        ],
    },
    {
        "id": "prometheus",
        "name": "Prometheus",
        "group": "Observability",
        "description": "PromQL snapshots for traffic, latency, errors, saturation, and uptime.",
        "keywords": ["prometheus", "promql", "latency", "errors", "requests"],
        "auth_type": "prometheus_http_api",
        "fields": [
            _field("base_url", "Prometheus URL", placeholder="https://prometheus.company.com"),
            _field("bearer_token", "Bearer token", secret=True, required=False),
            _field("queries", "PromQL queries", required=False, placeholder="up, rate(http_requests_total[5m])"),
        ],
    },
    {
        "id": "cloudwatch",
        "name": "CloudWatch",
        "group": "Observability",
        "description": "AWS service metrics and alarms through the task role or AWS credentials.",
        "keywords": ["cloudwatch", "aws", "alarm", "metric"],
        "auth_type": "aws_role",
        "fields": [
            _field("region", "AWS region", required=False, placeholder="eu-central-1"),
            _field("namespace", "Metric namespace", required=False, placeholder="AWS/ECS"),
        ],
    },
    {
        "id": "newrelic",
        "name": "New Relic",
        "group": "Observability",
        "description": "NRQL snapshots, service health, deployments, and error trends.",
        "keywords": ["new relic", "nrql", "latency", "error", "apm"],
        "auth_type": "api_key",
        "fields": [
            _field("api_key", "User API key", secret=True),
            _field("account_id", "Account ID"),
            _field("nrql", "NRQL", required=False, placeholder="SELECT count(*) FROM Transaction SINCE 1 day ago"),
        ],
    },
    {
        "id": "database",
        "name": "Database Health",
        "group": "Observability",
        "description": "PostgreSQL health checks for size, sessions, table bloat hints, and slow-query readiness.",
        "keywords": ["database", "db", "query", "replication", "connections", "storage"],
        "auth_type": "read_only_database_url",
        "fields": [
            _field("database_url", "Read-only PostgreSQL URL", secret=True),
        ],
    },
    {
        "id": "pagerduty",
        "name": "PagerDuty",
        "group": "Support & Incidents",
        "description": "Incidents, urgency, impacted services, on-call context, and follow-up actions.",
        "keywords": ["pagerduty", "incident", "outage", "pd-", "sev"],
        "auth_type": "api_token",
        "fields": [
            _field("api_token", "PagerDuty API token", secret=True),
            _field("since", "Since", required=False, placeholder="2026-01-01T00:00:00Z"),
        ],
    },
    {
        "id": "opsgenie",
        "name": "Opsgenie",
        "group": "Support & Incidents",
        "description": "Alerts, incidents, priorities, owners, and escalation context.",
        "keywords": ["opsgenie", "alert", "incident", "escalation"],
        "auth_type": "api_key",
        "fields": [
            _field("api_key", "Opsgenie API key", secret=True),
            _field("region", "Region", required=False, placeholder="us or eu"),
            _field("query", "Alert query", required=False, placeholder="status: open"),
        ],
    },
    {
        "id": "statuspage",
        "name": "Statuspage",
        "group": "Support & Incidents",
        "description": "Public/private incident timelines, components, and customer-facing updates.",
        "keywords": ["statuspage", "incident", "maintenance", "component"],
        "auth_type": "api_key",
        "fields": [
            _field("api_key", "Statuspage API key", secret=True),
            _field("page_id", "Page ID"),
        ],
    },
    {
        "id": "incident_docs",
        "name": "Internal Incident Docs",
        "group": "Support & Incidents",
        "description": "Generic incident-postmortem JSON or Markdown endpoint for internal tools.",
        "keywords": ["postmortem", "incident doc", "rca", "sev"],
        "auth_type": "generic_json_endpoint",
        "fields": [
            _field("endpoint_url", "Incident JSON endpoint URL"),
            _field("api_token", "Bearer token", secret=True, required=False),
        ],
    },
    {
        "id": "notion",
        "name": "Notion",
        "group": "Knowledge",
        "description": "Pages, databases, runbooks, decision records, and onboarding notes.",
        "keywords": ["notion", "runbook", "decision", "onboarding"],
        "auth_type": "integration_token",
        "fields": [
            _field("integration_token", "Integration token", secret=True),
            _field("query", "Search query", required=False),
        ],
    },
    {
        "id": "confluence",
        "name": "Confluence",
        "group": "Knowledge",
        "description": "Architecture docs, runbooks, onboarding pages, and decision records.",
        "keywords": ["confluence", "runbook", "architecture", "docs", "onboarding"],
        "auth_type": "atlassian_oauth_or_api_token",
        "oauth_provider": "atlassian",
        "fields": [
            _field("site_url", "Confluence site URL", required=False, placeholder="https://company.atlassian.net"),
            _field("email", "Atlassian email", required=False),
            _field("api_token", "Atlassian API token", secret=True, required=False),
            _field("cql", "CQL", required=False, placeholder='type = "page" ORDER BY lastmodified DESC'),
        ],
    },
    {
        "id": "google_drive",
        "name": "Google Drive",
        "group": "Knowledge",
        "description": "Docs, Sheets, PDFs, and shared project folders.",
        "keywords": ["google drive", "doc", "sheet", "pdf"],
        "auth_type": "google_access_token",
        "fields": [
            _field("access_token", "Google OAuth access token", secret=True),
            _field("query", "Drive query", required=False, placeholder="trashed = false"),
        ],
    },
    {
        "id": "sharepoint",
        "name": "SharePoint",
        "group": "Knowledge",
        "description": "Microsoft 365 documents, folders, and knowledge libraries through Graph.",
        "keywords": ["sharepoint", "drive", "document", "folder"],
        "auth_type": "microsoft_oauth_or_access_token",
        "oauth_provider": "microsoft",
        "fields": [
            _field("access_token", "Microsoft Graph access token", secret=True, required=False),
            _field("site_id", "Site ID", required=False),
            _field("drive_id", "Drive ID", required=False),
        ],
    },
    {
        "id": "markdown_repo",
        "name": "Markdown Repo",
        "group": "Knowledge",
        "description": "Repository documentation, ADRs, runbooks, and local Markdown source trees.",
        "keywords": ["markdown", "adr", "runbook", "docs"],
        "auth_type": "github_repo_docs",
        "fields": [
            _field("owner", "GitHub owner"),
            _field("repo", "Repository name"),
            _field("path", "Docs path", required=False, placeholder="docs"),
            _field("token", "GitHub token", secret=True, required=False),
        ],
    },
    {
        "id": "pdf",
        "name": "PDFs",
        "group": "Knowledge",
        "description": "Upload PDFs directly from the Sources button; the connector tracks coverage.",
        "keywords": ["pdf", "document", "spec"],
        "auth_type": "upload",
        "fields": [],
        "upload_only": True,
    },
    {
        "id": "zendesk",
        "name": "Zendesk / Support",
        "group": "Customer Support",
        "description": "Support tickets, customer pain, escalations, and recurring issues.",
        "keywords": ["zendesk", "support", "customer", "ticket"],
        "auth_type": "api_token",
        "fields": [
            _field("subdomain", "Zendesk subdomain"),
            _field("email", "Zendesk email"),
            _field("api_token", "Zendesk API token", secret=True),
        ],
    },
    {
        "id": "intercom",
        "name": "Intercom",
        "group": "Customer Support",
        "description": "Customer conversations, support trends, and escalation context.",
        "keywords": ["intercom", "conversation", "customer", "support"],
        "auth_type": "access_token",
        "fields": [
            _field("access_token", "Intercom access token", secret=True),
        ],
    },
    {
        "id": "freshdesk",
        "name": "Freshdesk",
        "group": "Customer Support",
        "description": "Support tickets, customer themes, and operational backlog signals.",
        "keywords": ["freshdesk", "support", "customer", "ticket"],
        "auth_type": "api_key",
        "fields": [
            _field("domain", "Freshdesk domain", placeholder="company.freshdesk.com"),
            _field("api_key", "Freshdesk API key", secret=True),
        ],
    },
    {
        "id": "crm_notes",
        "name": "CRM Notes",
        "group": "Customer Support",
        "description": "Generic CRM notes from Salesforce, HubSpot, or an internal customer API.",
        "keywords": ["crm", "salesforce", "hubspot", "customer notes"],
        "auth_type": "generic_json_endpoint",
        "fields": [
            _field("endpoint_url", "CRM notes JSON endpoint URL"),
            _field("api_token", "Bearer token", secret=True, required=False),
        ],
    },
    {
        "id": "powerbi",
        "name": "Power BI / BI",
        "group": "Analytics",
        "description": "Reports, dashboards, business KPIs, product funnels, and leadership metrics.",
        "keywords": ["power bi", "dashboard", "report", "conversion", "retention"],
        "auth_type": "microsoft_oauth_or_access_token",
        "oauth_provider": "microsoft",
        "fields": [
            _field("access_token", "Power BI access token", secret=True, required=False),
            _field("group_id", "Workspace/group ID", required=False),
        ],
    },
]

CATALOG_BY_ID = {item["id"]: item for item in CONNECTOR_CATALOG}


def _now() -> str:
    return datetime.utcnow().isoformat()


def _read_connections(tenant_id: str) -> Dict[str, Dict[str, Any]]:
    return read_json(tenant_id, CONNECTIONS_KEY, {})


def _write_connections(tenant_id: str, connections: Dict[str, Dict[str, Any]]) -> None:
    write_json(tenant_id, CONNECTIONS_KEY, connections)


def _is_secret_field(name: str) -> bool:
    lowered = name.lower()
    return any(hint in lowered for hint in SECRET_FIELD_HINTS)


def _redact_credentials(credentials: Dict[str, Any]) -> Dict[str, Any]:
    redacted = {}
    for key, value in (credentials or {}).items():
        if _is_secret_field(key):
            redacted[key] = bool(value)
        else:
            redacted[key] = value
    return redacted


def _oauth_redirect_uri(provider: str) -> str:
    if provider == "microsoft" and settings.microsoft_redirect_uri:
        return settings.microsoft_redirect_uri
    if provider == "atlassian" and settings.atlassian_redirect_uri:
        return settings.atlassian_redirect_uri
    base = (settings.public_app_url or "http://localhost:8000").rstrip("/")
    return f"{base}/api/connectors/oauth/{provider}/callback"


def _oauth_available(provider: str) -> bool:
    if provider == "microsoft":
        return bool(settings.microsoft_client_id and settings.microsoft_client_secret)
    if provider == "atlassian":
        return bool(settings.atlassian_client_id and settings.atlassian_client_secret)
    return False


def _connector_status(tenant_id: str, definition: Dict[str, Any], connection: Dict[str, Any] = None) -> Dict[str, Any]:
    connection = connection or {}
    credentials = connection.get("credentials") or {}
    connected = bool(connection.get("connected_at") and credentials)
    oauth_provider = definition.get("oauth_provider", "")
    return {
        **definition,
        "connected": connected,
        "credentials": _redact_credentials(credentials),
        "connected_at": connection.get("connected_at", ""),
        "last_sync_at": connection.get("last_sync_at", ""),
        "last_error": connection.get("last_error", ""),
        "last_document_id": connection.get("last_document_id", ""),
        "last_filename": connection.get("last_filename", ""),
        "sync_count": connection.get("sync_count", 0),
        "oauth_available": _oauth_available(oauth_provider) if oauth_provider else False,
    }


def list_connector_statuses(tenant_id: str) -> Dict[str, Any]:
    connections = _read_connections(tenant_id)
    connectors = [
        _connector_status(tenant_id, definition, connections.get(definition["id"]))
        for definition in CONNECTOR_CATALOG
    ]
    groups = sorted({item["group"] for item in CONNECTOR_CATALOG})
    return {
        "connectors": connectors,
        "groups": groups,
        "connected_count": sum(1 for item in connectors if item["connected"]),
        "total_count": len(connectors),
    }


def save_connector_credentials(tenant_id: str, connector_id: str, credentials: Dict[str, Any]) -> Dict[str, Any]:
    if connector_id not in CATALOG_BY_ID:
        raise KeyError(f"Unknown connector: {connector_id}")

    definition = CATALOG_BY_ID[connector_id]
    if definition.get("upload_only"):
        raise ValueError("This source is upload-only. Use Upload Source to index exported files.")

    cleaned = {
        key: value.strip() if isinstance(value, str) else value
        for key, value in (credentials or {}).items()
        if value not in (None, "")
    }
    connections = _read_connections(tenant_id)
    existing = connections.get(connector_id, {})
    merged_credentials = {**(existing.get("credentials") or {}), **cleaned}
    missing = [
        field["name"]
        for field in definition.get("fields", [])
        if field.get("required") and not merged_credentials.get(field["name"])
    ]
    if missing:
        raise ValueError(f"Missing required connector field(s): {', '.join(missing)}")

    connections[connector_id] = {
        **existing,
        "credentials": merged_credentials,
        "connected_at": existing.get("connected_at") or _now(),
        "last_error": "",
    }
    _write_connections(tenant_id, connections)
    write_audit_event(
        tenant_id,
        "connector.connected",
        details={"connector_id": connector_id, "connector_name": definition["name"]},
    )
    return _connector_status(tenant_id, definition, connections[connector_id])


def disconnect_connector(tenant_id: str, connector_id: str) -> None:
    if connector_id not in CATALOG_BY_ID:
        raise KeyError(f"Unknown connector: {connector_id}")
    connections = _read_connections(tenant_id)
    if connector_id in connections:
        connections.pop(connector_id)
        _write_connections(tenant_id, connections)
    write_audit_event(
        tenant_id,
        "connector.disconnected",
        details={"connector_id": connector_id, "connector_name": CATALOG_BY_ID[connector_id]["name"]},
    )


def start_oauth(tenant_id: str, connector_id: str) -> Dict[str, Any]:
    if connector_id not in CATALOG_BY_ID:
        raise KeyError(f"Unknown connector: {connector_id}")
    definition = CATALOG_BY_ID[connector_id]
    provider = definition.get("oauth_provider")
    if not provider:
        raise ValueError("This connector does not support OAuth sign-in.")
    if not _oauth_available(provider):
        raise ValueError(f"{definition['name']} OAuth is not configured on the backend.")

    state = uuid.uuid4().hex
    states = read_json("_global", OAUTH_STATES_KEY, {})
    states[state] = {
        "tenant_id": tenant_id,
        "connector_id": connector_id,
        "provider": provider,
        "created_at": _now(),
    }
    write_json("_global", OAUTH_STATES_KEY, states)

    redirect_uri = _oauth_redirect_uri(provider)
    if provider == "microsoft":
        tenant = settings.microsoft_tenant_id or "organizations"
        params = {
            "client_id": settings.microsoft_client_id,
            "response_type": "code",
            "redirect_uri": redirect_uri,
            "response_mode": "query",
            "scope": settings.microsoft_connector_scopes,
            "state": state,
            "prompt": "select_account",
        }
        url = f"https://login.microsoftonline.com/{tenant}/oauth2/v2.0/authorize?{urlencode(params)}"
    else:
        params = {
            "audience": "api.atlassian.com",
            "client_id": settings.atlassian_client_id,
            "scope": settings.atlassian_connector_scopes,
            "redirect_uri": redirect_uri,
            "state": state,
            "response_type": "code",
            "prompt": "consent",
        }
        url = f"https://auth.atlassian.com/authorize?{urlencode(params)}"

    return {"authorization_url": url, "state": state, "provider": provider, "redirect_uri": redirect_uri}


async def complete_oauth(provider: str, code: str, state: str) -> Dict[str, Any]:
    states = read_json("_global", OAUTH_STATES_KEY, {})
    pending = states.pop(state, None)
    write_json("_global", OAUTH_STATES_KEY, states)
    if not pending or pending.get("provider") != provider:
        raise ValueError("OAuth state is invalid or expired.")

    tenant_id = pending["tenant_id"]
    connector_id = pending["connector_id"]
    redirect_uri = _oauth_redirect_uri(provider)
    async with httpx.AsyncClient(timeout=settings.connector_timeout_seconds) as client:
        if provider == "microsoft":
            token_url = f"https://login.microsoftonline.com/{settings.microsoft_tenant_id or 'organizations'}/oauth2/v2.0/token"
            response = await client.post(
                token_url,
                data={
                    "client_id": settings.microsoft_client_id,
                    "client_secret": settings.microsoft_client_secret,
                    "grant_type": "authorization_code",
                    "code": code,
                    "redirect_uri": redirect_uri,
                    "scope": settings.microsoft_connector_scopes,
                },
                headers={"Content-Type": "application/x-www-form-urlencoded"},
            )
            response.raise_for_status()
            credentials = response.json()
        else:
            response = await client.post(
                "https://auth.atlassian.com/oauth/token",
                json={
                    "grant_type": "authorization_code",
                    "client_id": settings.atlassian_client_id,
                    "client_secret": settings.atlassian_client_secret,
                    "code": code,
                    "redirect_uri": redirect_uri,
                },
            )
            response.raise_for_status()
            credentials = response.json()
            resources = await client.get(
                "https://api.atlassian.com/oauth/token/accessible-resources",
                headers={"Authorization": f"Bearer {credentials.get('access_token', '')}"},
            )
            if resources.status_code < 400:
                resource_list = resources.json()
                if resource_list:
                    credentials["cloud_id"] = resource_list[0].get("id", "")
                    credentials["site_url"] = resource_list[0].get("url", "")

    save_connector_credentials(tenant_id, connector_id, credentials)
    return {
        "tenant_id": tenant_id,
        "connector_id": connector_id,
        "connector_name": CATALOG_BY_ID[connector_id]["name"],
    }


def _clean_url(url: str) -> str:
    return (url or "").strip().rstrip("/")


def _limit() -> int:
    return max(1, min(int(settings.connector_sync_limit or 50), 200))


def _truthy(value: Any, default: bool = True) -> bool:
    if value in (None, ""):
        return default
    return str(value).strip().lower() not in {"0", "false", "no", "off", "metadata_only"}


def _split_list(value: Any) -> List[str]:
    return [
        item.strip().strip("/")
        for item in re.split(r"[,\n]+", str(value or ""))
        if item.strip().strip("/")
    ]


def _source_path_matches(path: str, filters: List[str]) -> bool:
    if not filters:
        return True
    normalized = path.strip("/")
    return any(normalized == item or normalized.startswith(f"{item.rstrip('/')}/") for item in filters)


def _source_file_allowed(item: Dict[str, Any], filters: List[str]) -> bool:
    path = str(item.get("path") or "")
    if item.get("type") != "blob" or not path or not _source_path_matches(path, filters):
        return False
    if int(item.get("size") or 0) > MAX_SOURCE_FILE_BYTES:
        return False
    lowered = path.lower()
    name = lowered.rsplit("/", 1)[-1]
    if name.startswith(".env") or name.endswith((".pem", ".p12", ".pfx", ".crt", ".key")):
        return False
    parts = set(lowered.split("/")[:-1])
    if parts & SOURCE_SKIP_DIRS:
        return False
    dot = name.rfind(".")
    ext = name[dot:] if dot >= 0 else ""
    if ext in SOURCE_SKIP_EXTENSIONS:
        return False
    return ext in SOURCE_CODE_EXTENSIONS or name in SOURCE_CODE_FILENAMES or name.startswith("readme")


def _language_hint(path: str) -> str:
    name = path.lower().rsplit("/", 1)[-1]
    ext = name.rsplit(".", 1)[-1] if "." in name else ""
    return {
        "css": "css",
        "go": "go",
        "html": "html",
        "java": "java",
        "js": "javascript",
        "json": "json",
        "jsx": "jsx",
        "kt": "kotlin",
        "md": "markdown",
        "php": "php",
        "py": "python",
        "rb": "ruby",
        "rs": "rust",
        "sh": "bash",
        "sql": "sql",
        "swift": "swift",
        "toml": "toml",
        "ts": "typescript",
        "tsx": "tsx",
        "xml": "xml",
        "yaml": "yaml",
        "yml": "yaml",
    }.get(ext, "")


def _require(credentials: Dict[str, Any], *fields: str) -> None:
    missing = [field for field in fields if not credentials.get(field)]
    if missing:
        raise ValueError(f"Missing connector credential(s): {', '.join(missing)}")


def _strip_html(value: str) -> str:
    value = re.sub(r"<(br|/p|/div|/li|/h[1-6])[^>]*>", "\n", str(value or ""), flags=re.I)
    value = re.sub(r"<[^>]+>", " ", value)
    value = html.unescape(value)
    return re.sub(r"\s+", " ", value).strip()


def _safe_json(value: Any, max_chars: int = 1600) -> str:
    text = json.dumps(value, ensure_ascii=True, default=str)
    return text if len(text) <= max_chars else text[:max_chars] + "..."


def _item_lines(title: str, items: List[str]) -> str:
    if not items:
        return f"\n## {title}\nNo records returned.\n"
    return f"\n## {title}\n" + "\n".join(items) + "\n"


def _document(connector_name: str, sections: List[Tuple[str, List[str]]], meta: Dict[str, Any] = None) -> str:
    text = [
        f"# {connector_name} connector sync",
        f"Synced at: {_now()}",
    ]
    for key, value in (meta or {}).items():
        if value not in (None, ""):
            text.append(f"{key}: {value}")
    for title, items in sections:
        text.append(_item_lines(title, items))
    return "\n".join(text)


def _auth_headers(token: str = "", bearer: bool = True, extra: Dict[str, str] = None) -> Dict[str, str]:
    headers = {"Accept": "application/json", **(extra or {})}
    if token:
        headers["Authorization"] = f"Bearer {token}" if bearer else token
    return headers


async def _get_json(client: httpx.AsyncClient, url: str, **kwargs) -> Any:
    response = await client.get(url, **kwargs)
    response.raise_for_status()
    return response.json()


async def _post_json(client: httpx.AsyncClient, url: str, **kwargs) -> Any:
    response = await client.post(url, **kwargs)
    response.raise_for_status()
    return response.json()


async def _sync_jira(client: httpx.AsyncClient, credentials: Dict[str, Any]) -> Tuple[str, Dict[str, Any]]:
    jql = credentials.get("jql") or "ORDER BY updated DESC"
    fields = "summary,status,assignee,reporter,priority,created,updated,issuetype,labels,description"
    if credentials.get("access_token") and credentials.get("cloud_id"):
        base = f"https://api.atlassian.com/ex/jira/{credentials['cloud_id']}"
        headers = _auth_headers(credentials["access_token"])
        auth = None
    else:
        _require(credentials, "site_url", "email", "api_token")
        base = _clean_url(credentials["site_url"])
        headers = {"Accept": "application/json"}
        auth = httpx.BasicAuth(credentials["email"], credentials["api_token"])

    response = await client.get(
        f"{base}/rest/api/3/search",
        params={"jql": jql, "maxResults": _limit(), "fields": fields},
        headers=headers,
        auth=auth,
    )
    if response.status_code >= 400:
        response = await client.post(
            f"{base}/rest/api/3/search",
            json={"jql": jql, "maxResults": _limit(), "fields": fields.split(",")},
            headers={**headers, "Content-Type": "application/json"},
            auth=auth,
        )
    if response.status_code >= 400:
        response = await client.get(
            f"{base}/rest/api/3/search/jql",
            params={"jql": jql, "maxResults": _limit(), "fields": fields},
            headers=headers,
            auth=auth,
        )
    response.raise_for_status()
    data = response.json()
    issues = []
    for issue in data.get("issues", []):
        f = issue.get("fields", {})
        assignee = (f.get("assignee") or {}).get("displayName") or "Unassigned"
        reporter = (f.get("reporter") or {}).get("displayName") or "Unknown"
        status = (f.get("status") or {}).get("name") or "Unknown"
        priority = (f.get("priority") or {}).get("name") or "No priority"
        issue_type = (f.get("issuetype") or {}).get("name") or "Issue"
        description = _safe_json(f.get("description"), 700) if f.get("description") else ""
        issues.append(
            f"- {issue.get('key')} [{status}] {f.get('summary', '')} | type={issue_type} | "
            f"priority={priority} | assignee={assignee} | reporter={reporter} | "
            f"created={f.get('created', '')} | updated={f.get('updated', '')} | labels={', '.join(f.get('labels') or [])} | {description}"
        )
    return _document("Jira", [("Issues", issues)], {"JQL": jql}), {"records": len(issues)}


async def _sync_confluence(client: httpx.AsyncClient, credentials: Dict[str, Any]) -> Tuple[str, Dict[str, Any]]:
    cql = credentials.get("cql") or 'type = "page" ORDER BY lastmodified DESC'
    if credentials.get("access_token") and credentials.get("cloud_id"):
        base = f"https://api.atlassian.com/ex/confluence/{credentials['cloud_id']}"
        headers = _auth_headers(credentials["access_token"])
        auth = None
    else:
        _require(credentials, "site_url", "email", "api_token")
        base = _clean_url(credentials["site_url"])
        headers = {"Accept": "application/json"}
        auth = httpx.BasicAuth(credentials["email"], credentials["api_token"])

    response = await client.get(
        f"{base}/wiki/rest/api/content/search",
        params={"cql": cql, "limit": _limit(), "expand": "body.storage,space,version"},
        headers=headers,
        auth=auth,
    )
    if response.status_code >= 400:
        response = await client.get(
            f"{base}/wiki/rest/api/search",
            params={"cql": cql, "limit": _limit()},
            headers=headers,
            auth=auth,
        )
    response.raise_for_status()
    data = response.json()
    pages = []
    for page in data.get("results", []):
        content = page.get("content") or page
        body = _strip_html(((content.get("body") or {}).get("storage") or {}).get("value", ""))
        version = content.get("version") or {}
        space = content.get("space") or {}
        pages.append(
            f"- {content.get('title', 'Untitled')} | id={content.get('id', '')} | space={space.get('name', '')} | "
            f"version={version.get('number', '')} | updated={version.get('when', '')}\n  {body[:1200]}"
        )
    return _document("Confluence", [("Pages", pages)], {"CQL": cql}), {"records": len(pages)}


async def _sync_github_source_snapshot(
    client: httpx.AsyncClient,
    base: str,
    headers: Dict[str, str],
    ref: str,
    code_paths: List[str],
) -> Tuple[List[Tuple[str, List[str]]], Dict[str, Any]]:
    file_limit = min(MAX_SOURCE_FILES, max(20, _limit() * 2))
    try:
        tree = await _get_json(
            client,
            f"{base}/git/trees/{quote(ref, safe='')}",
            headers=headers,
            params={"recursive": "1"},
        )
    except httpx.HTTPStatusError as exc:
        status = exc.response.status_code
        if status in (401, 403, 404):
            raise ValueError(
                "GitHub source code access failed. Make sure the token has Contents: Read-only "
                "permission for this repository, or leave the token blank for a public repository."
            ) from exc
        raise

    files = [
        item for item in tree.get("tree", [])
        if _source_file_allowed(item, code_paths)
    ]
    files = sorted(files, key=lambda item: str(item.get("path") or ""))[:file_limit]
    file_lines = [
        f"- {item.get('path')} | size={item.get('size', 0)} bytes | sha={str(item.get('sha', ''))[:12]}"
        for item in files
    ]
    if not file_lines:
        requested = ", ".join(code_paths) if code_paths else "repository root"
        return [("Source Files Selected", [f"No eligible source files found under {requested}."])], {
            "code_files": 0,
            "tree_truncated": bool(tree.get("truncated")),
        }

    extracts = []
    skipped = []
    total_chars = 0
    for item in files:
        if total_chars >= MAX_SOURCE_TOTAL_CHARS:
            skipped.append("- Stopped reading files after reaching the connector source snapshot size limit.")
            break
        path = str(item.get("path") or "")
        try:
            blob = await _get_json(client, f"{base}/git/blobs/{quote(str(item.get('sha')), safe='')}", headers=headers)
        except httpx.HTTPStatusError as exc:
            skipped.append(f"- {path} skipped: GitHub returned HTTP {exc.response.status_code}")
            continue

        content = str(blob.get("content") or "")
        if blob.get("encoding") == "base64":
            raw = base64.b64decode(content.encode("ascii"), validate=False)
            text = raw.decode("utf-8", errors="replace")
        else:
            text = content
        if "\x00" in text[:2000]:
            skipped.append(f"- {path} skipped: binary-looking content")
            continue
        if len(text) > MAX_SOURCE_FILE_CHARS:
            text = text[:MAX_SOURCE_FILE_CHARS] + "\n... file truncated by Base connector ..."
        remaining = MAX_SOURCE_TOTAL_CHARS - total_chars
        if len(text) > remaining:
            text = text[:remaining] + "\n... source snapshot truncated by Base connector ..."
        total_chars += len(text)
        language = _language_hint(path)
        extracts.append(
            f"### {path}\n"
            f"size={item.get('size', 0)} bytes | sha={str(item.get('sha', ''))[:12]}\n"
            f"```{language}\n{text}\n```"
        )

    sections = [("Source Files Selected", file_lines), ("Source File Extracts", extracts or ["No source file content could be decoded."])]
    if skipped:
        sections.append(("Source Files Skipped", skipped))
    return sections, {
        "code_files": len(extracts),
        "tree_truncated": bool(tree.get("truncated")),
        "code_chars": total_chars,
    }


async def _sync_github(client: httpx.AsyncClient, credentials: Dict[str, Any]) -> Tuple[str, Dict[str, Any]]:
    _require(credentials, "owner", "repo")
    owner = credentials["owner"]
    repo = credentials["repo"]
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    if credentials.get("token"):
        headers["Authorization"] = f"Bearer {credentials['token']}"
    base = f"https://api.github.com/repos/{quote(owner)}/{quote(repo)}"
    repo_info = await _get_json(client, base, headers=headers)
    ref = credentials.get("ref") or repo_info.get("default_branch") or "main"
    pulls = await _get_json(client, f"{base}/pulls", headers=headers, params={"state": "all", "per_page": _limit()})
    commits = await _get_json(client, f"{base}/commits", headers=headers, params={"per_page": min(_limit(), 100)})
    branches = await _get_json(client, f"{base}/branches", headers=headers, params={"per_page": min(_limit(), 100)})
    releases = await _get_json(client, f"{base}/releases", headers=headers, params={"per_page": min(_limit(), 100)})
    repo_lines = [
        f"- {repo_info.get('full_name')} | default_branch={repo_info.get('default_branch')} | "
        f"private={repo_info.get('private')} | language={repo_info.get('language')} | "
        f"pushed={repo_info.get('pushed_at')} | updated={repo_info.get('updated_at')}",
    ]
    pr_lines = [
        f"- PR #{item.get('number')} [{item.get('state')}] {item.get('title')} | by={item.get('user', {}).get('login')} | "
        f"created={item.get('created_at')} | updated={item.get('updated_at')} | merged={item.get('merged_at')} | url={item.get('html_url')}"
        for item in pulls
    ]
    commit_lines = [
        f"- {item.get('sha', '')[:12]} {((item.get('commit') or {}).get('message') or '').splitlines()[0]} | "
        f"author={((item.get('commit') or {}).get('author') or {}).get('name')} | date={((item.get('commit') or {}).get('author') or {}).get('date')}"
        for item in commits
    ]
    branch_lines = [f"- {item.get('name')} | sha={(item.get('commit') or {}).get('sha', '')[:12]}" for item in branches]
    release_lines = [
        f"- {item.get('tag_name')} {item.get('name') or ''} | draft={item.get('draft')} | prerelease={item.get('prerelease')} | "
        f"published={item.get('published_at')} | {item.get('body') or ''}"
        for item in releases
    ]
    sections = [
        ("Repository Overview", repo_lines),
        ("Pull Requests", pr_lines),
        ("Commits", commit_lines),
        ("Branches", branch_lines),
        ("Releases", release_lines),
    ]
    code_meta = {"code_files": 0, "tree_truncated": False}
    code_paths = _split_list(credentials.get("code_paths"))
    if _truthy(credentials.get("include_code"), default=True):
        source_sections, code_meta = await _sync_github_source_snapshot(client, base, headers, ref, code_paths)
        sections.extend(source_sections)
    return _document(
        "GitHub",
        sections,
        {
            "Repository": f"{owner}/{repo}",
            "Default branch": repo_info.get("default_branch"),
            "Code ref": ref,
            "Code paths": ", ".join(code_paths) if code_paths else "eligible files across repository",
            "Source tree truncated by GitHub": code_meta.get("tree_truncated"),
        },
    ), {"records": len(repo_lines) + len(pr_lines) + len(commit_lines) + len(branch_lines) + len(release_lines) + int(code_meta.get("code_files") or 0)}


async def _sync_gitlab(client: httpx.AsyncClient, credentials: Dict[str, Any]) -> Tuple[str, Dict[str, Any]]:
    _require(credentials, "project_id")
    base_url = _clean_url(credentials.get("base_url") or "https://gitlab.com")
    project_id = quote(str(credentials["project_id"]), safe="")
    headers = {"Accept": "application/json"}
    if credentials.get("token"):
        headers["PRIVATE-TOKEN"] = credentials["token"]
    base = f"{base_url}/api/v4/projects/{project_id}"
    merge_requests = await _get_json(client, f"{base}/merge_requests", headers=headers, params={"state": "all", "per_page": _limit()})
    commits = await _get_json(client, f"{base}/repository/commits", headers=headers, params={"per_page": min(_limit(), 100)})
    branches = await _get_json(client, f"{base}/repository/branches", headers=headers, params={"per_page": min(_limit(), 100)})
    releases = await _get_json(client, f"{base}/releases", headers=headers, params={"per_page": min(_limit(), 100)})
    mr_lines = [
        f"- MR !{item.get('iid')} [{item.get('state')}] {item.get('title')} | author={(item.get('author') or {}).get('username')} | "
        f"created={item.get('created_at')} | updated={item.get('updated_at')} | merged={item.get('merged_at')}"
        for item in merge_requests
    ]
    commit_lines = [f"- {item.get('short_id')} {item.get('title')} | author={item.get('author_name')} | date={item.get('created_at')}" for item in commits]
    branch_lines = [f"- {item.get('name')} | merged={item.get('merged')} | default={item.get('default')}" for item in branches]
    release_lines = [f"- {item.get('tag_name')} {item.get('name') or ''} | released={item.get('released_at')} | {item.get('description') or ''}" for item in releases]
    return _document("GitLab", [("Merge Requests", mr_lines), ("Commits", commit_lines), ("Branches", branch_lines), ("Releases", release_lines)]), {"records": len(mr_lines) + len(commit_lines)}


async def _sync_bitbucket(client: httpx.AsyncClient, credentials: Dict[str, Any]) -> Tuple[str, Dict[str, Any]]:
    _require(credentials, "workspace", "repo_slug")
    headers = {"Accept": "application/json"}
    auth = None
    if credentials.get("access_token"):
        headers["Authorization"] = f"Bearer {credentials['access_token']}"
    elif credentials.get("username") and credentials.get("app_password"):
        auth = httpx.BasicAuth(credentials["username"], credentials["app_password"])
    base = f"https://api.bitbucket.org/2.0/repositories/{quote(credentials['workspace'])}/{quote(credentials['repo_slug'])}"
    pulls = await _get_json(client, f"{base}/pullrequests", headers=headers, auth=auth, params={"state": "OPEN", "pagelen": _limit()})
    commits = await _get_json(client, f"{base}/commits", headers=headers, auth=auth, params={"pagelen": _limit()})
    branches = await _get_json(client, f"{base}/refs/branches", headers=headers, auth=auth, params={"pagelen": _limit()})
    pr_lines = [
        f"- PR #{item.get('id')} [{item.get('state')}] {item.get('title')} | author={((item.get('author') or {}).get('display_name') or '')} | "
        f"created={item.get('created_on')} | updated={item.get('updated_on')}"
        for item in pulls.get("values", [])
    ]
    commit_lines = [f"- {item.get('hash', '')[:12]} {item.get('message', '').splitlines()[0]} | date={item.get('date')}" for item in commits.get("values", [])]
    branch_lines = [f"- {item.get('name')} | target={(item.get('target') or {}).get('hash', '')[:12]}" for item in branches.get("values", [])]
    return _document("Bitbucket", [("Pull Requests", pr_lines), ("Commits", commit_lines), ("Branches", branch_lines)]), {"records": len(pr_lines) + len(commit_lines)}


async def _sync_linear(client: httpx.AsyncClient, credentials: Dict[str, Any]) -> Tuple[str, Dict[str, Any]]:
    _require(credentials, "api_key")
    query = """
    query ConnectorIssues($first: Int!) {
      issues(first: $first, orderBy: updatedAt) {
        nodes {
          identifier
          title
          priority
          estimate
          createdAt
          updatedAt
          url
          state { name }
          assignee { name }
          team { key name }
        }
      }
    }
    """
    data = await _post_json(
        client,
        "https://api.linear.app/graphql",
        headers={"Authorization": credentials["api_key"], "Content-Type": "application/json"},
        json={"query": query, "variables": {"first": _limit()}},
    )
    issues = ((data.get("data") or {}).get("issues") or {}).get("nodes", [])
    lines = [
        f"- {item.get('identifier')} [{(item.get('state') or {}).get('name')}] {item.get('title')} | "
        f"team={(item.get('team') or {}).get('key')} | assignee={(item.get('assignee') or {}).get('name') or 'Unassigned'} | "
        f"priority={item.get('priority')} | updated={item.get('updatedAt')} | {item.get('url')}"
        for item in issues
    ]
    return _document("Linear", [("Issues", lines)]), {"records": len(lines)}


async def _sync_azure_boards(client: httpx.AsyncClient, credentials: Dict[str, Any]) -> Tuple[str, Dict[str, Any]]:
    _require(credentials, "organization", "project", "pat")
    wiql = credentials.get("wiql") or "SELECT [System.Id] FROM WorkItems ORDER BY [System.ChangedDate] DESC"
    auth = httpx.BasicAuth("", credentials["pat"])
    base = f"https://dev.azure.com/{quote(credentials['organization'])}/{quote(credentials['project'])}/_apis"
    wiql_data = await _post_json(
        client,
        f"{base}/wit/wiql",
        params={"api-version": "7.1"},
        auth=auth,
        json={"query": wiql},
    )
    ids = [item["id"] for item in (wiql_data.get("workItems") or [])[:_limit()]]
    lines = []
    if ids:
        batch = await _post_json(
            client,
            f"{base}/wit/workitemsbatch",
            params={"api-version": "7.1"},
            auth=auth,
            json={"ids": ids, "fields": ["System.Id", "System.Title", "System.State", "System.AssignedTo", "System.ChangedDate", "System.WorkItemType"]},
        )
        for item in batch.get("value", []):
            f = item.get("fields", {})
            assignee = f.get("System.AssignedTo")
            if isinstance(assignee, dict):
                assignee = assignee.get("displayName")
            lines.append(
                f"- {f.get('System.Id')} [{f.get('System.State')}] {f.get('System.Title')} | "
                f"type={f.get('System.WorkItemType')} | assignee={assignee or 'Unassigned'} | changed={f.get('System.ChangedDate')}"
            )
    return _document("Azure Boards", [("Work Items", lines)], {"WIQL": wiql}), {"records": len(lines)}


async def _sync_slack(client: httpx.AsyncClient, credentials: Dict[str, Any]) -> Tuple[str, Dict[str, Any]]:
    _require(credentials, "bot_token", "channel_id")
    data = await _get_json(
        client,
        "https://slack.com/api/conversations.history",
        headers=_auth_headers(credentials["bot_token"]),
        params={"channel": credentials["channel_id"], "limit": min(_limit(), 200)},
    )
    if not data.get("ok"):
        raise ValueError(data.get("error") or "Slack API returned an error.")
    messages = [
        f"- {item.get('ts')} user={item.get('user') or item.get('bot_id') or 'unknown'} | {_strip_html(item.get('text', ''))}"
        for item in data.get("messages", [])
    ]
    return _document("Slack", [("Messages", messages)], {"Channel": credentials["channel_id"]}), {"records": len(messages)}


async def _sync_teams(client: httpx.AsyncClient, credentials: Dict[str, Any]) -> Tuple[str, Dict[str, Any]]:
    _require(credentials, "access_token")
    headers = _auth_headers(credentials["access_token"])
    sections: List[Tuple[str, List[str]]] = []
    if credentials.get("team_id") and credentials.get("channel_id"):
        try:
            messages = await _get_json(
                client,
                f"https://graph.microsoft.com/v1.0/teams/{credentials['team_id']}/channels/{credentials['channel_id']}/messages",
                headers=headers,
                params={"$top": min(_limit(), 50)},
            )
            lines = [
                f"- {item.get('createdDateTime')} from={((item.get('from') or {}).get('user') or {}).get('displayName') or 'unknown'} | "
                f"{_strip_html((item.get('body') or {}).get('content', ''))}"
                for item in messages.get("value", [])
            ]
        except Exception as exc:
            lines = [f"- Channel messages unavailable with current permissions: {exc}"]
        sections.append(("Channel Messages", lines))
    try:
        teams = await _get_json(client, "https://graph.microsoft.com/v1.0/me/joinedTeams", headers=headers)
        team_lines = [f"- {item.get('displayName')} | id={item.get('id')} | {item.get('description') or ''}" for item in teams.get("value", [])[:_limit()]]
    except Exception as exc:
        team_lines = [f"- Joined teams unavailable with current permissions: {exc}"]
    sections.insert(0, ("Joined Teams", team_lines))
    try:
        chats = await _get_json(client, "https://graph.microsoft.com/v1.0/me/chats", headers=headers, params={"$top": min(_limit(), 50)})
        chat_lines = [
            f"- {item.get('topic') or item.get('chatType')} | id={item.get('id')} | type={item.get('chatType')} | updated={item.get('lastUpdatedDateTime')}"
            for item in chats.get("value", [])
        ]
    except Exception as exc:
        chat_lines = [f"- Chat list unavailable with current permissions: {exc}"]
    sections.append(("Chats", chat_lines))
    if credentials.get("chat_id"):
        try:
            chat_messages = await _get_json(
                client,
                f"https://graph.microsoft.com/v1.0/chats/{credentials['chat_id']}/messages",
                headers=headers,
                params={"$top": min(_limit(), 50)},
            )
            lines = [
                f"- {item.get('createdDateTime')} from={((item.get('from') or {}).get('user') or {}).get('displayName') or 'unknown'} | "
                f"{_strip_html((item.get('body') or {}).get('content', ''))}"
                for item in chat_messages.get("value", [])
            ]
        except Exception as exc:
            lines = [f"- Chat messages unavailable with current permissions: {exc}"]
        sections.append(("Chat Messages", lines))
    return _document("Microsoft Teams", sections), {"records": sum(len(items) for _, items in sections)}


async def _sync_email(client: httpx.AsyncClient, credentials: Dict[str, Any]) -> Tuple[str, Dict[str, Any]]:
    _require(credentials, "access_token")
    params = {
        "$top": min(_limit(), 50),
        "$select": "subject,from,receivedDateTime,bodyPreview,conversationId,webLink",
        "$orderby": "receivedDateTime desc",
    }
    if credentials.get("search"):
        params["$search"] = f'"{credentials["search"]}"'
    data = await _get_json(client, "https://graph.microsoft.com/v1.0/me/messages", headers=_auth_headers(credentials["access_token"]), params=params)
    lines = []
    for item in data.get("value", []):
        sender = (((item.get("from") or {}).get("emailAddress") or {}).get("address") or "")
        lines.append(
            f"- {item.get('receivedDateTime')} | from={sender} | subject={item.get('subject')} | "
            f"conversation={item.get('conversationId')} | {item.get('bodyPreview') or ''} | {item.get('webLink') or ''}"
        )
    return _document("Email", [("Messages", lines)], {"Search": credentials.get("search", "")}), {"records": len(lines)}


async def _sync_notion(client: httpx.AsyncClient, credentials: Dict[str, Any]) -> Tuple[str, Dict[str, Any]]:
    _require(credentials, "integration_token")
    payload: Dict[str, Any] = {"page_size": min(_limit(), 100)}
    if credentials.get("query"):
        payload["query"] = credentials["query"]
    payload["filter"] = {"property": "object", "value": "page"}
    data = await _post_json(
        client,
        "https://api.notion.com/v1/search",
        headers={
            "Authorization": f"Bearer {credentials['integration_token']}",
            "Notion-Version": "2026-03-11",
            "Content-Type": "application/json",
        },
        json=payload,
    )
    pages = []
    for page in data.get("results", []):
        title = "Untitled"
        for prop in (page.get("properties") or {}).values():
            if prop.get("type") == "title" and prop.get("title"):
                title = "".join(part.get("plain_text", "") for part in prop["title"]) or title
                break
        pages.append(
            f"- {title} | id={page.get('id')} | created={page.get('created_time')} | edited={page.get('last_edited_time')} | {page.get('url')}"
        )
    return _document("Notion", [("Pages", pages)], {"Query": credentials.get("query", "")}), {"records": len(pages)}


async def _sync_google_drive(client: httpx.AsyncClient, credentials: Dict[str, Any]) -> Tuple[str, Dict[str, Any]]:
    _require(credentials, "access_token")
    query = credentials.get("query") or "trashed = false"
    data = await _get_json(
        client,
        "https://www.googleapis.com/drive/v3/files",
        headers=_auth_headers(credentials["access_token"]),
        params={
            "q": query,
            "pageSize": min(_limit(), 100),
            "fields": "files(id,name,mimeType,modifiedTime,webViewLink,size),nextPageToken",
        },
    )
    files = [
        f"- {item.get('name')} | mime={item.get('mimeType')} | modified={item.get('modifiedTime')} | size={item.get('size', '')} | {item.get('webViewLink', '')}"
        for item in data.get("files", [])
    ]
    return _document("Google Drive", [("Files", files)], {"Query": query}), {"records": len(files)}


async def _sync_sharepoint(client: httpx.AsyncClient, credentials: Dict[str, Any]) -> Tuple[str, Dict[str, Any]]:
    _require(credentials, "access_token")
    headers = _auth_headers(credentials["access_token"])
    if credentials.get("site_id") and credentials.get("drive_id"):
        url = f"https://graph.microsoft.com/v1.0/sites/{credentials['site_id']}/drives/{credentials['drive_id']}/root/children"
    elif credentials.get("site_id"):
        url = f"https://graph.microsoft.com/v1.0/sites/{credentials['site_id']}/drive/root/children"
    else:
        url = "https://graph.microsoft.com/v1.0/me/drive/root/children"
    data = await _get_json(client, url, headers=headers, params={"$top": min(_limit(), 200)})
    files = [
        f"- {item.get('name')} | type={'folder' if item.get('folder') else 'file'} | modified={item.get('lastModifiedDateTime')} | "
        f"size={item.get('size', '')} | {item.get('webUrl', '')}"
        for item in data.get("value", [])
    ]
    return _document("SharePoint", [("Drive Items", files)]), {"records": len(files)}


async def _sync_markdown_repo(client: httpx.AsyncClient, credentials: Dict[str, Any]) -> Tuple[str, Dict[str, Any]]:
    _require(credentials, "owner", "repo")
    path = credentials.get("path") or ""
    headers = {"Accept": "application/vnd.github+json"}
    if credentials.get("token"):
        headers["Authorization"] = f"Bearer {credentials['token']}"
    url = f"https://api.github.com/repos/{quote(credentials['owner'])}/{quote(credentials['repo'])}/contents/{quote(path)}"
    data = await _get_json(client, url, headers=headers)
    files = data if isinstance(data, list) else [data]
    md_files = [item for item in files if str(item.get("name", "")).lower().endswith((".md", ".txt"))][: min(_limit(), 20)]
    docs = []
    for item in md_files:
        raw_url = item.get("download_url")
        if not raw_url:
            continue
        response = await client.get(raw_url, headers=headers)
        response.raise_for_status()
        docs.append(f"\n## {item.get('path')}\n{response.text[:5000]}")
    file_lines = [f"- {item.get('path')} | size={item.get('size')} | {item.get('html_url')}" for item in files]
    text = _document("Markdown Repo", [("Files", file_lines)], {"Repository": f"{credentials['owner']}/{credentials['repo']}", "Path": path})
    if docs:
        text += "\n\n# Markdown file extracts\n" + "\n".join(docs)
    return text, {"records": len(file_lines)}


async def _sync_grafana(client: httpx.AsyncClient, credentials: Dict[str, Any]) -> Tuple[str, Dict[str, Any]]:
    _require(credentials, "base_url", "api_token")
    base = _clean_url(credentials["base_url"])
    headers = _auth_headers(credentials["api_token"])
    dashboards = await _get_json(client, f"{base}/api/search", headers=headers, params={"type": "dash-db", "limit": _limit()})
    dashboard_lines = [
        f"- {item.get('title')} | uid={item.get('uid')} | folder={item.get('folderTitle', '')} | url={item.get('url')}"
        for item in dashboards
    ]
    sections = [("Dashboards", dashboard_lines)]
    uid = credentials.get("dashboard_uid") or (dashboards[0].get("uid") if dashboards else "")
    if uid:
        detail = await _get_json(client, f"{base}/api/dashboards/uid/{quote(uid)}", headers=headers)
        dashboard = detail.get("dashboard") or {}
        panels = dashboard.get("panels") or []
        panel_lines = [
            f"- {panel.get('title') or panel.get('type')} | type={panel.get('type')} | targets={_safe_json(panel.get('targets', []), 800)}"
            for panel in panels[:_limit()]
        ]
        sections.append((f"Dashboard Panels ({uid})", panel_lines))
    return _document("Grafana", sections), {"records": sum(len(items) for _, items in sections)}


async def _sync_prometheus(client: httpx.AsyncClient, credentials: Dict[str, Any]) -> Tuple[str, Dict[str, Any]]:
    _require(credentials, "base_url")
    base = _clean_url(credentials["base_url"])
    headers = _auth_headers(credentials.get("bearer_token", ""))
    raw_queries = credentials.get("queries") or "up"
    queries = [item.strip() for item in re.split(r"[\n,]+", raw_queries) if item.strip()][:12]
    lines = []
    for query in queries:
        data = await _get_json(client, f"{base}/api/v1/query", headers=headers, params={"query": query})
        result = ((data.get("data") or {}).get("result") or [])[:10]
        lines.append(f"- Query `{query}` returned {len(result)} sample(s): {_safe_json(result, 1200)}")
    return _document("Prometheus", [("PromQL Results", lines)]), {"records": len(lines)}


async def _sync_datadog(client: httpx.AsyncClient, credentials: Dict[str, Any]) -> Tuple[str, Dict[str, Any]]:
    _require(credentials, "api_key", "app_key")
    site = credentials.get("site") or "datadoghq.com"
    base = f"https://api.{site}"
    headers = {
        "Accept": "application/json",
        "DD-API-KEY": credentials["api_key"],
        "DD-APPLICATION-KEY": credentials["app_key"],
    }
    monitors = await _get_json(client, f"{base}/api/v1/monitor", headers=headers, params={"page_size": _limit()})
    dashboards = await _get_json(client, f"{base}/api/v1/dashboard", headers=headers)
    monitor_lines = [
        f"- {item.get('name')} | type={item.get('type')} | overall_state={item.get('overall_state')} | query={item.get('query')}"
        for item in monitors[:_limit()]
    ]
    dash_lines = [
        f"- {item.get('title')} | id={item.get('id')} | modified={item.get('modified_at')}"
        for item in (dashboards.get("dashboards") or [])[:_limit()]
    ]
    return _document("Datadog", [("Monitors", monitor_lines), ("Dashboards", dash_lines)]), {"records": len(monitor_lines) + len(dash_lines)}


async def _sync_newrelic(client: httpx.AsyncClient, credentials: Dict[str, Any]) -> Tuple[str, Dict[str, Any]]:
    _require(credentials, "api_key", "account_id")
    nrql = credentials.get("nrql") or "SELECT count(*) FROM Transaction SINCE 1 day ago"
    query = """
    query BaseConnector($accountId: Int!, $nrql: Nrql!) {
      actor {
        account(id: $accountId) {
          nrql(query: $nrql) { results }
        }
      }
    }
    """
    data = await _post_json(
        client,
        "https://api.newrelic.com/graphql",
        headers={"API-Key": credentials["api_key"], "Content-Type": "application/json"},
        json={"query": query, "variables": {"accountId": int(credentials["account_id"]), "nrql": nrql}},
    )
    results = ((((data.get("data") or {}).get("actor") or {}).get("account") or {}).get("nrql") or {}).get("results") or []
    lines = [f"- NRQL `{nrql}` -> {_safe_json(results, 2000)}"]
    return _document("New Relic", [("NRQL Results", lines)]), {"records": len(results)}


async def _sync_pagerduty(client: httpx.AsyncClient, credentials: Dict[str, Any]) -> Tuple[str, Dict[str, Any]]:
    _require(credentials, "api_token")
    params = {"limit": _limit(), "total": "false", "sort_by": "created_at:desc"}
    if credentials.get("since"):
        params["since"] = credentials["since"]
    data = await _get_json(
        client,
        "https://api.pagerduty.com/incidents",
        headers={
            "Authorization": f"Token token={credentials['api_token']}",
            "Accept": "application/vnd.pagerduty+json;version=2",
        },
        params=params,
    )
    lines = [
        f"- {item.get('incident_number')} [{item.get('status')}] {item.get('title')} | urgency={item.get('urgency')} | "
        f"service={((item.get('service') or {}).get('summary') or '')} | created={item.get('created_at')} | updated={item.get('updated_at')} | {item.get('html_url')}"
        for item in data.get("incidents", [])
    ]
    return _document("PagerDuty", [("Incidents", lines)], {"Since": credentials.get("since", "")}), {"records": len(lines)}


async def _sync_opsgenie(client: httpx.AsyncClient, credentials: Dict[str, Any]) -> Tuple[str, Dict[str, Any]]:
    _require(credentials, "api_key")
    host = "api.eu.opsgenie.com" if str(credentials.get("region", "")).lower() == "eu" else "api.opsgenie.com"
    params = {"limit": _limit(), "sort": "createdAt", "order": "desc"}
    if credentials.get("query"):
        params["query"] = credentials["query"]
    data = await _get_json(
        client,
        f"https://{host}/v2/alerts",
        headers={"Authorization": f"GenieKey {credentials['api_key']}", "Accept": "application/json"},
        params=params,
    )
    lines = [
        f"- {item.get('tinyId')} [{item.get('status')}] {item.get('message')} | priority={item.get('priority')} | "
        f"created={item.get('createdAt')} | owner={item.get('owner')} | tags={', '.join(item.get('tags') or [])}"
        for item in data.get("data", [])
    ]
    return _document("Opsgenie", [("Alerts", lines)], {"Query": credentials.get("query", "")}), {"records": len(lines)}


async def _sync_statuspage(client: httpx.AsyncClient, credentials: Dict[str, Any]) -> Tuple[str, Dict[str, Any]]:
    _require(credentials, "api_key", "page_id")
    headers = {"Authorization": f"OAuth {credentials['api_key']}", "Accept": "application/json"}
    incidents = await _get_json(client, f"https://api.statuspage.io/v1/pages/{credentials['page_id']}/incidents", headers=headers, params={"limit": _limit()})
    components = await _get_json(client, f"https://api.statuspage.io/v1/pages/{credentials['page_id']}/components", headers=headers)
    incident_lines = [
        f"- [{item.get('status')}] {item.get('name')} | impact={item.get('impact')} | created={item.get('created_at')} | updated={item.get('updated_at')} | {item.get('shortlink') or ''}"
        for item in incidents[:_limit()]
    ]
    component_lines = [f"- {item.get('name')} [{item.get('status')}] group={item.get('group_id') or ''}" for item in components[:_limit()]]
    return _document("Statuspage", [("Incidents", incident_lines), ("Components", component_lines)]), {"records": len(incident_lines) + len(component_lines)}


async def _sync_zendesk(client: httpx.AsyncClient, credentials: Dict[str, Any]) -> Tuple[str, Dict[str, Any]]:
    _require(credentials, "subdomain", "email", "api_token")
    auth = httpx.BasicAuth(f"{credentials['email']}/token", credentials["api_token"])
    url = f"https://{credentials['subdomain']}.zendesk.com/api/v2/tickets.json"
    data = await _get_json(client, url, auth=auth, params={"per_page": min(_limit(), 100), "sort_by": "updated_at", "sort_order": "desc"})
    lines = [
        f"- Ticket #{item.get('id')} [{item.get('status')}] {item.get('subject')} | priority={item.get('priority')} | "
        f"requester={item.get('requester_id')} | created={item.get('created_at')} | updated={item.get('updated_at')}"
        for item in data.get("tickets", [])
    ]
    return _document("Zendesk", [("Tickets", lines)]), {"records": len(lines)}


async def _sync_intercom(client: httpx.AsyncClient, credentials: Dict[str, Any]) -> Tuple[str, Dict[str, Any]]:
    _require(credentials, "access_token")
    data = await _get_json(
        client,
        "https://api.intercom.io/conversations",
        headers={
            "Authorization": f"Bearer {credentials['access_token']}",
            "Accept": "application/json",
            "Intercom-Version": "2.11",
        },
        params={"per_page": min(_limit(), 100)},
    )
    lines = []
    for item in data.get("conversations", []):
        source = item.get("source") or {}
        lines.append(
            f"- Conversation {item.get('id')} [{item.get('state') or item.get('open')}] {source.get('subject') or ''} | "
            f"created={item.get('created_at')} | updated={item.get('updated_at')} | {source.get('body') or ''}"
        )
    return _document("Intercom", [("Conversations", lines)]), {"records": len(lines)}


async def _sync_freshdesk(client: httpx.AsyncClient, credentials: Dict[str, Any]) -> Tuple[str, Dict[str, Any]]:
    _require(credentials, "domain", "api_key")
    domain = _clean_url(credentials["domain"]).replace("https://", "").replace("http://", "")
    data = await _get_json(
        client,
        f"https://{domain}/api/v2/tickets",
        auth=httpx.BasicAuth(credentials["api_key"], "X"),
        params={"per_page": min(_limit(), 100), "order_by": "updated_at", "order_type": "desc"},
    )
    lines = [
        f"- Ticket #{item.get('id')} [{item.get('status')}] {item.get('subject')} | priority={item.get('priority')} | "
        f"requester={item.get('requester_id')} | created={item.get('created_at')} | updated={item.get('updated_at')}"
        for item in data
    ]
    return _document("Freshdesk", [("Tickets", lines)]), {"records": len(lines)}


async def _sync_posthog(client: httpx.AsyncClient, credentials: Dict[str, Any]) -> Tuple[str, Dict[str, Any]]:
    _require(credentials, "project_id", "personal_api_key")
    host = _clean_url(credentials.get("host") or "https://app.posthog.com")
    headers = _auth_headers(credentials["personal_api_key"])
    insights = await _get_json(client, f"{host}/api/projects/{quote(str(credentials['project_id']))}/insights/", headers=headers, params={"limit": min(_limit(), 100)})
    lines = [
        f"- Insight {item.get('id')} {item.get('name') or item.get('short_id') or ''} | created={item.get('created_at')} | updated={item.get('updated_at')} | type={item.get('filters_hash') or item.get('query') or ''}"
        for item in insights.get("results", [])
    ]
    return _document("PostHog", [("Insights", lines)]), {"records": len(lines)}


async def _sync_ga4(client: httpx.AsyncClient, credentials: Dict[str, Any]) -> Tuple[str, Dict[str, Any]]:
    _require(credentials, "property_id", "access_token")
    body = {
        "dateRanges": [{"startDate": "30daysAgo", "endDate": "today"}],
        "dimensions": [{"name": "sessionDefaultChannelGroup"}],
        "metrics": [{"name": "sessions"}, {"name": "conversions"}, {"name": "activeUsers"}],
        "limit": str(min(_limit(), 100)),
    }
    data = await _post_json(
        client,
        f"https://analyticsdata.googleapis.com/v1beta/properties/{credentials['property_id']}:runReport",
        headers={**_auth_headers(credentials["access_token"]), "Content-Type": "application/json"},
        json=body,
    )
    lines = []
    for row in data.get("rows", []):
        dims = ", ".join(item.get("value", "") for item in row.get("dimensionValues", []))
        metrics = ", ".join(item.get("value", "") for item in row.get("metricValues", []))
        lines.append(f"- {dims}: sessions, conversions, activeUsers = {metrics}")
    return _document("Google Analytics 4", [("Channel Metrics", lines)]), {"records": len(lines)}


async def _sync_mixpanel(client: httpx.AsyncClient, credentials: Dict[str, Any]) -> Tuple[str, Dict[str, Any]]:
    if credentials.get("export_url"):
        data = await _get_json(client, credentials["export_url"])
        lines = [f"- Export response: {_safe_json(data, 4000)}"]
        return _document("Mixpanel", [("Export", lines)]), {"records": 1}
    _require(credentials, "service_account_username", "service_account_secret")
    to_date = credentials.get("to_date") or datetime.utcnow().date().isoformat()
    from_date = credentials.get("from_date") or (datetime.utcnow().date() - timedelta(days=30)).isoformat()
    params = {"from_date": from_date, "to_date": to_date}
    if credentials.get("event"):
        params["event"] = json.dumps([credentials["event"]])
    response = await client.get(
        "https://data.mixpanel.com/api/2.0/export",
        params=params,
        auth=httpx.BasicAuth(credentials["service_account_username"], credentials["service_account_secret"]),
    )
    response.raise_for_status()
    rows = [line for line in response.text.splitlines() if line.strip()][: min(_limit(), 100)]
    lines = [f"- {row[:1200]}" for row in rows]
    return _document("Mixpanel", [("Events", lines)], {"From": from_date, "To": to_date}), {"records": len(lines)}


async def _sync_amplitude(client: httpx.AsyncClient, credentials: Dict[str, Any]) -> Tuple[str, Dict[str, Any]]:
    _require(credentials, "api_key", "secret_key")
    data = await _get_json(
        client,
        "https://amplitude.com/api/2/events/list",
        auth=httpx.BasicAuth(credentials["api_key"], credentials["secret_key"]),
    )
    events = data.get("data") or data.get("events") or []
    if isinstance(events, dict):
        events = events.get("events", [])
    lines = [f"- {item.get('event_type') or item.get('name') or _safe_json(item, 400)} | {_safe_json(item, 800)}" for item in events[:_limit()]]
    return _document("Amplitude", [("Events", lines)]), {"records": len(lines)}


async def _sync_powerbi(client: httpx.AsyncClient, credentials: Dict[str, Any]) -> Tuple[str, Dict[str, Any]]:
    _require(credentials, "access_token")
    base = "https://api.powerbi.com/v1.0/myorg"
    url = f"{base}/groups/{credentials['group_id']}/reports" if credentials.get("group_id") else f"{base}/reports"
    reports = await _get_json(client, url, headers=_auth_headers(credentials["access_token"]))
    lines = [f"- {item.get('name')} | id={item.get('id')} | webUrl={item.get('webUrl')}" for item in reports.get("value", [])]
    return _document("Power BI", [("Reports", lines)]), {"records": len(lines)}


async def _sync_generic_json(client: httpx.AsyncClient, credentials: Dict[str, Any], connector_name: str) -> Tuple[str, Dict[str, Any]]:
    _require(credentials, "endpoint_url")
    headers = _auth_headers(credentials.get("api_token", ""))
    data = await _get_json(client, credentials["endpoint_url"], headers=headers)
    if isinstance(data, list):
        rows = data[:_limit()]
    elif isinstance(data, dict):
        candidate = next((value for value in data.values() if isinstance(value, list)), [])
        rows = candidate[:_limit()] if candidate else [data]
    else:
        rows = [data]
    lines = [f"- {_safe_json(item, 1400)}" for item in rows]
    return _document(connector_name, [("Records", lines)], {"Endpoint": credentials["endpoint_url"]}), {"records": len(lines)}


async def _sync_cloudwatch(client: httpx.AsyncClient, credentials: Dict[str, Any]) -> Tuple[str, Dict[str, Any]]:
    import boto3

    region = credentials.get("region") or settings.aws_region
    namespace = credentials.get("namespace") or "AWS/ECS"
    cloudwatch = boto3.client("cloudwatch", region_name=region)
    response = cloudwatch.list_metrics(Namespace=namespace)
    metrics = response.get("Metrics", [])[:_limit()]
    lines = [
        f"- {item.get('MetricName')} | namespace={item.get('Namespace')} | dimensions={_safe_json(item.get('Dimensions', []), 500)}"
        for item in metrics
    ]
    return _document("CloudWatch", [("Metrics", lines)], {"Region": region, "Namespace": namespace}), {"records": len(lines)}


async def _sync_database(client: httpx.AsyncClient, credentials: Dict[str, Any]) -> Tuple[str, Dict[str, Any]]:
    _require(credentials, "database_url")
    import psycopg
    from psycopg.rows import dict_row

    lines = []
    with psycopg.connect(credentials["database_url"], row_factory=dict_row) as conn:
        with conn.cursor() as cur:
            cur.execute("SET statement_timeout = '5s';")
            cur.execute("SELECT now() AS checked_at, version() AS version;")
            lines.append(f"- Server: {_safe_json(cur.fetchone(), 1000)}")
            cur.execute("SELECT datname, pg_size_pretty(pg_database_size(datname)) AS size FROM pg_database ORDER BY pg_database_size(datname) DESC LIMIT 10;")
            lines.extend([f"- Database size: {row['datname']} = {row['size']}" for row in cur.fetchall()])
            cur.execute("SELECT state, count(*) AS sessions FROM pg_stat_activity GROUP BY state ORDER BY sessions DESC;")
            lines.extend([f"- Sessions: state={row['state']} count={row['sessions']}" for row in cur.fetchall()])
            cur.execute("SELECT relname, n_live_tup, n_dead_tup, last_vacuum, last_autovacuum FROM pg_stat_user_tables ORDER BY n_dead_tup DESC LIMIT 10;")
            lines.extend([f"- Table health: {_safe_json(row, 1000)}" for row in cur.fetchall()])
    return _document("Database Health", [("PostgreSQL Health Checks", lines)]), {"records": len(lines)}


SYNC_ADAPTERS: Dict[str, Callable[[httpx.AsyncClient, Dict[str, Any]], Awaitable[Tuple[str, Dict[str, Any]]]]] = {
    "jira": _sync_jira,
    "confluence": _sync_confluence,
    "github": _sync_github,
    "gitlab": _sync_gitlab,
    "bitbucket": _sync_bitbucket,
    "linear": _sync_linear,
    "azure_boards": _sync_azure_boards,
    "slack": _sync_slack,
    "teams": _sync_teams,
    "email": _sync_email,
    "notion": _sync_notion,
    "google_drive": _sync_google_drive,
    "sharepoint": _sync_sharepoint,
    "markdown_repo": _sync_markdown_repo,
    "grafana": _sync_grafana,
    "prometheus": _sync_prometheus,
    "datadog": _sync_datadog,
    "newrelic": _sync_newrelic,
    "cloudwatch": _sync_cloudwatch,
    "database": _sync_database,
    "pagerduty": _sync_pagerduty,
    "opsgenie": _sync_opsgenie,
    "statuspage": _sync_statuspage,
    "zendesk": _sync_zendesk,
    "intercom": _sync_intercom,
    "freshdesk": _sync_freshdesk,
    "posthog": _sync_posthog,
    "ga4": _sync_ga4,
    "mixpanel": _sync_mixpanel,
    "amplitude": _sync_amplitude,
    "powerbi": _sync_powerbi,
}


async def sync_connector(tenant_id: str, connector_id: str) -> Dict[str, Any]:
    if connector_id not in CATALOG_BY_ID:
        raise KeyError(f"Unknown connector: {connector_id}")
    definition = CATALOG_BY_ID[connector_id]
    if definition.get("upload_only"):
        raise ValueError("This connector is represented by uploaded files. Use Upload Source to add PDFs or exports.")

    connections = _read_connections(tenant_id)
    connection = connections.get(connector_id)
    if not connection or not connection.get("credentials"):
        raise ValueError("Connect this source before syncing.")

    credentials = connection["credentials"]
    adapter = SYNC_ADAPTERS.get(connector_id)
    connector_name = definition["name"]

    try:
        async with httpx.AsyncClient(timeout=settings.connector_timeout_seconds, follow_redirects=True) as client:
            if adapter:
                text, stats = await adapter(client, credentials)
            else:
                text, stats = await _sync_generic_json(client, credentials, connector_name)
        result = ingest_connector_text(
            tenant_id=tenant_id,
            connector_id=connector_id,
            connector_name=connector_name,
            filename=f"connector_{connector_id}_{datetime.utcnow().strftime('%Y%m%d_%H%M%S')}.md",
            text=text,
            metadata={"connector_auth_type": definition.get("auth_type", "")},
        )
        connections = _read_connections(tenant_id)
        current = connections.get(connector_id, connection)
        connections[connector_id] = {
            **current,
            "last_sync_at": _now(),
            "last_error": "",
            "last_document_id": result["document_id"],
            "last_filename": result["filename"],
            "sync_count": int(current.get("sync_count", 0)) + 1,
        }
        _write_connections(tenant_id, connections)
        return {
            "message": f"{connector_name} synced successfully.",
            "connector_id": connector_id,
            "connector_name": connector_name,
            "records_synced": int(stats.get("records", 0)),
            "document_id": result["document_id"],
            "filename": result["filename"],
            "chunks_created": result["chunks_created"],
        }
    except Exception as exc:
        connections = _read_connections(tenant_id)
        current = connections.get(connector_id, connection)
        current["last_error"] = str(exc)
        connections[connector_id] = current
        _write_connections(tenant_id, connections)
        write_audit_event(
            tenant_id,
            "connector.sync_failed",
            details={"connector_id": connector_id, "connector_name": connector_name, "error": str(exc)},
        )
        raise
