import json
import os
import re
from contextlib import asynccontextmanager
from typing import Any, AsyncIterator, Dict, List
from urllib.parse import urlparse

import httpx
from mcp import ClientSession
from mcp.client.streamable_http import streamable_http_client
from pydantic import AnyUrl

from app.core.config import get_settings

settings = get_settings()


def _configured_servers() -> List[Dict[str, Any]]:
    raw = (settings.mcp_external_servers_json or "[]").strip() or "[]"
    try:
        servers = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise ValueError("MCP_EXTERNAL_SERVERS_JSON must contain a valid JSON array.") from exc
    if not isinstance(servers, list):
        raise ValueError("MCP_EXTERNAL_SERVERS_JSON must contain a JSON array.")

    normalized = []
    names = set()
    for item in servers:
        if not isinstance(item, dict):
            raise ValueError("Each external MCP server configuration must be an object.")
        name = str(item.get("name", "")).strip()
        url = str(item.get("url", "")).strip()
        if not re.fullmatch(r"[a-zA-Z0-9_-]{1,80}", name):
            raise ValueError("External MCP server names may contain letters, numbers, underscores, and hyphens.")
        if name in names:
            raise ValueError(f"Duplicate external MCP server name: {name}")
        parsed = urlparse(url)
        if parsed.scheme not in {"http", "https"} or not parsed.netloc:
            raise ValueError(f"External MCP server '{name}' must use an absolute HTTP(S) URL.")
        project_ids = item.get("project_ids", [])
        if not isinstance(project_ids, list):
            raise ValueError(f"External MCP server '{name}' project_ids must be a JSON array.")
        names.add(name)
        normalized.append({
            "name": name,
            "url": url,
            "description": str(item.get("description", "")).strip(),
            "bearer_token_env": str(item.get("bearer_token_env", "")).strip(),
            "api_key_env": str(item.get("api_key_env", "")).strip(),
            "api_key_header": str(item.get("api_key_header", "X-API-Key")).strip() or "X-API-Key",
            "project_ids": [str(value).strip() for value in project_ids if str(value).strip()],
        })
    return normalized


def _public_server(server: Dict[str, Any]) -> Dict[str, Any]:
    bearer_env = server.get("bearer_token_env", "")
    api_key_env = server.get("api_key_env", "")
    return {
        "name": server["name"],
        "url": server["url"],
        "description": server.get("description", ""),
        "project_ids": server.get("project_ids", []),
        "authentication": (
            "bearer"
            if bearer_env
            else "api_key"
            if api_key_env
            else "none"
        ),
        "credential_available": bool(
            (bearer_env and os.getenv(bearer_env))
            or (api_key_env and os.getenv(api_key_env))
            or (not bearer_env and not api_key_env)
        ),
    }


def list_external_servers(project_id: str = "") -> List[Dict[str, Any]]:
    servers = _configured_servers()
    if project_id:
        servers = [
            item
            for item in servers
            if not item.get("project_ids") or project_id in item.get("project_ids", [])
        ]
    return [_public_server(item) for item in servers]


def get_external_server(name: str, project_id: str = "") -> Dict[str, Any]:
    server = next((item for item in _configured_servers() if item["name"] == name), None)
    if not server:
        raise KeyError(name)
    allowed_projects = server.get("project_ids", [])
    if project_id and allowed_projects and project_id not in allowed_projects:
        raise PermissionError(f"External MCP server '{name}' is not enabled for project '{project_id}'.")
    return server


def _request_headers(server: Dict[str, Any]) -> Dict[str, str]:
    headers = {}
    bearer_env = server.get("bearer_token_env")
    if bearer_env:
        token = os.getenv(bearer_env, "").strip()
        if not token:
            raise ValueError(f"Environment variable '{bearer_env}' is required for MCP server '{server['name']}'.")
        headers["Authorization"] = f"Bearer {token}"

    api_key_env = server.get("api_key_env")
    if api_key_env:
        api_key = os.getenv(api_key_env, "").strip()
        if not api_key:
            raise ValueError(f"Environment variable '{api_key_env}' is required for MCP server '{server['name']}'.")
        headers[server.get("api_key_header", "X-API-Key")] = api_key
    return headers


@asynccontextmanager
async def external_mcp_session(server: Dict[str, Any]) -> AsyncIterator[tuple[ClientSession, Any]]:
    timeout = httpx.Timeout(settings.mcp_request_timeout_seconds)
    async with httpx.AsyncClient(
        headers=_request_headers(server),
        timeout=timeout,
        follow_redirects=True,
    ) as http_client:
        async with streamable_http_client(server["url"], http_client=http_client) as (read, write, _):
            async with ClientSession(read, write) as session:
                initialize = await session.initialize()
                yield session, initialize


def _dump_model(value: Any) -> Any:
    if hasattr(value, "model_dump"):
        return value.model_dump(mode="json", by_alias=True, exclude_none=True)
    if isinstance(value, list):
        return [_dump_model(item) for item in value]
    if isinstance(value, dict):
        return {key: _dump_model(item) for key, item in value.items()}
    return value


def _extract_text(contents: List[Any]) -> str:
    parts = []
    for item in contents or []:
        text = getattr(item, "text", None)
        if text:
            parts.append(str(text))
            continue
        resource = getattr(item, "resource", None)
        resource_text = getattr(resource, "text", None) if resource is not None else None
        if resource_text:
            parts.append(str(resource_text))
    return "\n\n".join(part.strip() for part in parts if part.strip())


async def discover_external_server(name: str, project_id: str = "") -> Dict[str, Any]:
    server = get_external_server(name, project_id)
    async with external_mcp_session(server) as (session, initialize):
        capabilities = getattr(initialize, "capabilities", None)
        tools = await session.list_tools() if getattr(capabilities, "tools", None) is not None else None
        resources = await session.list_resources() if getattr(capabilities, "resources", None) is not None else None
        templates = await session.list_resource_templates() if getattr(capabilities, "resources", None) is not None else None
        prompts = await session.list_prompts() if getattr(capabilities, "prompts", None) is not None else None
        return {
            "server": _public_server(server),
            "server_info": _dump_model(getattr(initialize, "serverInfo", None)),
            "capabilities": _dump_model(capabilities),
            "tools": _dump_model(getattr(tools, "tools", [])),
            "resources": _dump_model(getattr(resources, "resources", [])),
            "resource_templates": _dump_model(getattr(templates, "resourceTemplates", [])),
            "prompts": _dump_model(getattr(prompts, "prompts", [])),
        }


async def call_external_tool(
    name: str,
    tool_name: str,
    arguments: Dict[str, Any],
    project_id: str = "",
) -> Dict[str, Any]:
    server = get_external_server(name, project_id)
    async with external_mcp_session(server) as (session, _):
        result = await session.call_tool(tool_name, arguments=arguments or {})
    text = _extract_text(getattr(result, "content", []))
    structured = getattr(result, "structuredContent", None)
    return {
        "server": _public_server(server),
        "tool": tool_name,
        "is_error": bool(getattr(result, "isError", False)),
        "text": text,
        "structured_content": _dump_model(structured),
        "content": _dump_model(getattr(result, "content", [])),
    }


async def read_external_resource(name: str, uri: str, project_id: str = "") -> Dict[str, Any]:
    server = get_external_server(name, project_id)
    async with external_mcp_session(server) as (session, _):
        result = await session.read_resource(AnyUrl(uri))
    contents = getattr(result, "contents", [])
    return {
        "server": _public_server(server),
        "uri": uri,
        "text": _extract_text(contents),
        "contents": _dump_model(contents),
    }


def external_result_text(result: Dict[str, Any]) -> str:
    parts = []
    if result.get("text"):
        parts.append(result["text"])
    if result.get("structured_content") is not None:
        parts.append(json.dumps(result["structured_content"], indent=2, ensure_ascii=True, default=str))
    text = "\n\n".join(part.strip() for part in parts if part and part.strip())
    if not text:
        raise ValueError("The external MCP response did not contain importable text or structured content.")
    maximum = max(1000, int(settings.mcp_max_import_chars))
    if len(text) > maximum:
        text = f"{text[:maximum]}\n\n[Base truncated this MCP import at {maximum} characters.]"
    return text
