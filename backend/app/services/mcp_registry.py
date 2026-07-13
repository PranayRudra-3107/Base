import base64
import hashlib
import json
import secrets
from datetime import datetime, timezone
from typing import Any, Dict, List
from urllib.parse import urlencode

import httpx

from app.core.config import get_settings
from app.services.storage import read_json, write_json

settings = get_settings()
REGISTRY_KEY = "mcp_registry"
OAUTH_STATE_KEY = "mcp_oauth_states"

PROVIDERS: Dict[str, Dict[str, Any]] = {
    "github": {
        "name": "github",
        "display_name": "GitHub MCP",
        "description": "Official GitHub server for repositories, code, commits, issues, pull requests, and Actions.",
        "url": "https://api.githubcopilot.com/mcp/x/all/readonly",
        "vendor": "GitHub",
        "authentication_options": ["bearer", "oauth"],
        "oauth_authorization_url": "https://github.com/login/oauth/authorize",
        "oauth_token_url": "https://github.com/login/oauth/access_token",
        "oauth_scopes": "repo read:org",
        "read_only": True,
    },
    "atlassian": {
        "name": "atlassian",
        "display_name": "Atlassian Rovo MCP",
        "description": "Official Atlassian server for Jira, Confluence, and Compass.",
        "url": "https://mcp.atlassian.com/v1/mcp",
        "vendor": "Atlassian",
        "authentication_options": ["bearer", "oauth"],
        "oauth_authorization_url": "https://auth.atlassian.com/authorize",
        "oauth_token_url": "https://auth.atlassian.com/oauth/token",
        "oauth_scopes": settings.atlassian_connector_scopes,
        "oauth_audience": "api.atlassian.com",
        "read_only": False,
    },
}


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _connections(project_id: str) -> Dict[str, Dict[str, Any]]:
    value = read_json(project_id, REGISTRY_KEY, {})
    return value if isinstance(value, dict) else {}


def _public(connection: Dict[str, Any]) -> Dict[str, Any]:
    return {key: value for key, value in connection.items() if key not in {"access_token", "refresh_token"}}


def provider_catalog(project_id: str = "") -> List[Dict[str, Any]]:
    connections = _connections(project_id) if project_id else {}
    return [
        {
            **{key: value for key, value in provider.items() if not key.startswith("oauth_")},
            "registered": name in connections,
            "oauth_available": oauth_available(name),
        }
        for name, provider in PROVIDERS.items()
    ]


def oauth_available(provider: str) -> bool:
    if provider == "github":
        return bool(settings.github_oauth_client_id)
    if provider == "atlassian":
        return bool(settings.atlassian_client_id)
    return False


def list_registered(project_id: str) -> List[Dict[str, Any]]:
    return [_public(value) for value in _connections(project_id).values()]


def register_provider(project_id: str, provider: str, auth_type: str, token: str = "") -> Dict[str, Any]:
    definition = PROVIDERS.get(provider)
    if not definition:
        raise KeyError(provider)
    if auth_type not in definition["authentication_options"]:
        raise ValueError(f"Unsupported authentication type for {provider}.")
    if auth_type == "bearer" and not token.strip():
        raise ValueError("A provider access token is required.")
    if auth_type == "oauth" and not oauth_available(provider):
        raise ValueError(f"{definition['display_name']} OAuth is not configured on the backend.")

    connections = _connections(project_id)
    existing = connections.get(provider, {})
    connections[provider] = {
        "name": provider,
        "provider": provider,
        "display_name": definition["display_name"],
        "description": definition["description"],
        "vendor": definition["vendor"],
        "url": definition["url"],
        "authentication": auth_type,
        "credential_available": bool(token.strip()) if auth_type == "bearer" else bool(existing.get("access_token")),
        "access_token": token.strip() or existing.get("access_token", ""),
        "refresh_token": existing.get("refresh_token", ""),
        "read_only": definition["read_only"],
        "project_ids": [project_id],
        "registered_at": existing.get("registered_at") or _now(),
        "connected_at": existing.get("connected_at", ""),
        "last_checked_at": existing.get("last_checked_at", ""),
        "last_error": "",
        "managed_by": "project-registry",
    }
    write_json(project_id, REGISTRY_KEY, connections)
    return _public(connections[provider])


def unregister_provider(project_id: str, provider: str) -> None:
    connections = _connections(project_id)
    if provider not in connections:
        raise KeyError(provider)
    connections.pop(provider)
    write_json(project_id, REGISTRY_KEY, connections)


def registered_server(project_id: str, name: str) -> Dict[str, Any] | None:
    return _connections(project_id).get(name)


def mark_connection(project_id: str, name: str, error: str = "") -> None:
    connections = _connections(project_id)
    if name not in connections:
        return
    connections[name]["last_checked_at"] = _now()
    connections[name]["last_error"] = error[:500]
    if not error:
        connections[name]["connected_at"] = _now()
        connections[name]["credential_available"] = True
    write_json(project_id, REGISTRY_KEY, connections)


def _oauth_config(provider: str) -> tuple[str, str]:
    if provider == "github":
        return settings.github_oauth_client_id, settings.github_oauth_client_secret
    if provider == "atlassian":
        return settings.atlassian_client_id, settings.atlassian_client_secret
    return "", ""


def _redirect_uri(provider: str) -> str:
    configured = settings.github_oauth_redirect_uri if provider == "github" else settings.atlassian_mcp_redirect_uri
    base = (settings.public_app_url or "http://localhost:8000").rstrip("/")
    return configured or f"{base}/api/mcp/oauth/{provider}/callback"


def start_oauth(project_id: str, provider: str) -> Dict[str, str]:
    definition = PROVIDERS.get(provider)
    if not definition or not oauth_available(provider):
        raise ValueError(f"OAuth is not configured for {provider}.")
    client_id, _ = _oauth_config(provider)
    state = secrets.token_urlsafe(32)
    verifier = secrets.token_urlsafe(64)
    challenge = base64.urlsafe_b64encode(hashlib.sha256(verifier.encode()).digest()).decode().rstrip("=")
    states = read_json("_global", OAUTH_STATE_KEY, {})
    states[state] = {"project_id": project_id, "provider": provider, "verifier": verifier, "created_at": _now()}
    write_json("_global", OAUTH_STATE_KEY, states)
    params = {
        "client_id": client_id,
        "redirect_uri": _redirect_uri(provider),
        "response_type": "code",
        "scope": definition["oauth_scopes"],
        "state": state,
        "code_challenge": challenge,
        "code_challenge_method": "S256",
    }
    if definition.get("oauth_audience"):
        params["audience"] = definition["oauth_audience"]
        params["prompt"] = "consent"
    return {"authorization_url": f"{definition['oauth_authorization_url']}?{urlencode(params)}", "state": state}


async def complete_oauth(provider: str, code: str, state: str) -> Dict[str, Any]:
    states = read_json("_global", OAUTH_STATE_KEY, {})
    pending = states.pop(state, None)
    write_json("_global", OAUTH_STATE_KEY, states)
    if not pending or pending.get("provider") != provider:
        raise ValueError("OAuth state is invalid or expired.")
    definition = PROVIDERS[provider]
    client_id, client_secret = _oauth_config(provider)
    payload = {
        "grant_type": "authorization_code",
        "client_id": client_id,
        "client_secret": client_secret,
        "code": code,
        "redirect_uri": _redirect_uri(provider),
        "code_verifier": pending["verifier"],
    }
    async with httpx.AsyncClient(timeout=settings.mcp_request_timeout_seconds) as client:
        if provider == "atlassian":
            response = await client.post(definition["oauth_token_url"], json=payload)
        else:
            response = await client.post(definition["oauth_token_url"], data=payload, headers={"Accept": "application/json"})
        response.raise_for_status()
        credentials = response.json()
    token = credentials.get("access_token", "")
    connection = register_provider(pending["project_id"], provider, "oauth")
    connections = _connections(pending["project_id"])
    connections[provider]["access_token"] = token
    connections[provider]["refresh_token"] = credentials.get("refresh_token", "")
    connections[provider]["credential_available"] = bool(token)
    connections[provider]["connected_at"] = _now()
    write_json(pending["project_id"], REGISTRY_KEY, connections)
    return {"project_id": pending["project_id"], "provider": provider, "connection": connection}
