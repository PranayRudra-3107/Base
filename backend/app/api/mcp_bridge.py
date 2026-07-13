import re
from typing import Any, Dict, Literal, Optional

from fastapi import APIRouter, Header, HTTPException
from pydantic import BaseModel, Field

from app.core.config import get_settings, parse_csv_setting
from app.services.audit_log import write_audit_event
from app.services.connector_ingestion import ingest_connector_text
from app.services.mcp_client import (
    call_external_tool,
    discover_external_server,
    external_result_text,
    list_external_servers,
    read_external_resource,
)
from app.services.projects import get_project

router = APIRouter()
settings = get_settings()


class MCPToolCallRequest(BaseModel):
    arguments: Dict[str, Any] = Field(default_factory=dict)


class MCPResourceReadRequest(BaseModel):
    uri: str = Field(max_length=2000)


class MCPImportRequest(BaseModel):
    source_type: Literal["tool", "resource"]
    tool_name: Optional[str] = Field(default=None, max_length=200)
    arguments: Dict[str, Any] = Field(default_factory=dict)
    resource_uri: Optional[str] = Field(default=None, max_length=2000)
    filename: Optional[str] = Field(default=None, max_length=180)


def _ensure_project(project_id: str) -> None:
    try:
        get_project(project_id)
    except KeyError as exc:
        raise HTTPException(status_code=404, detail="Project not found.") from exc


def _mcp_error(exc: Exception) -> HTTPException:
    if isinstance(exc, KeyError):
        return HTTPException(status_code=404, detail="External MCP server not found.")
    if isinstance(exc, PermissionError):
        return HTTPException(status_code=403, detail=str(exc))
    if isinstance(exc, ValueError):
        return HTTPException(status_code=400, detail=str(exc))
    return HTTPException(status_code=502, detail=f"External MCP request failed: {exc}")


def _import_filename(server_name: str, request: MCPImportRequest) -> str:
    if request.filename and request.filename.strip():
        candidate = request.filename.strip()
    else:
        subject = request.tool_name if request.source_type == "tool" else request.resource_uri
        safe_subject = re.sub(r"[^a-zA-Z0-9_.-]", "_", subject or request.source_type).strip("_.")
        candidate = f"mcp_{server_name}_{safe_subject[:80] or request.source_type}.md"
    safe_filename = re.sub(r"[^a-zA-Z0-9_.-]", "_", candidate).strip("_.")[:160] or "mcp_import.md"
    if not safe_filename.lower().endswith((".md", ".txt", ".csv")):
        safe_filename = f"{safe_filename}.md"
    return safe_filename


@router.get("/status")
async def mcp_status():
    """Describe the inbound Base MCP endpoint and configured outbound MCP servers without exposing secrets."""
    mcp_key_configured = bool(settings.mcp_api_key.strip())
    mcp_available = settings.environment.strip().lower() != "production" or mcp_key_configured
    return {
        "inbound": {
            "transport": "streamable-http",
            "endpoint": "/mcp",
            "available": mcp_available,
            "authentication_required": mcp_key_configured,
            "exposed_project_ids": parse_csv_setting(settings.mcp_exposed_project_ids),
        },
        "external_servers": list_external_servers(),
    }


@router.get("/servers")
async def external_servers(x_tenant_id: str = Header(default="default")):
    """List external MCP servers configured for the selected project."""
    return list_external_servers(x_tenant_id)


@router.get("/servers/{server_name}/capabilities")
async def external_server_capabilities(
    server_name: str,
    x_tenant_id: str = Header(default="default"),
):
    """Initialize an external MCP connection and discover its tools, resources, templates, and prompts."""
    _ensure_project(x_tenant_id)
    try:
        result = await discover_external_server(server_name, x_tenant_id)
        write_audit_event(
            x_tenant_id,
            "mcp.external.discovered",
            details={"server": server_name},
        )
        return result
    except Exception as exc:
        raise _mcp_error(exc) from exc


@router.post("/servers/{server_name}/tools/{tool_name}")
async def external_tool_call(
    server_name: str,
    tool_name: str,
    request: MCPToolCallRequest,
    x_tenant_id: str = Header(default="default"),
):
    """Call one tool on a configured external MCP server."""
    _ensure_project(x_tenant_id)
    try:
        result = await call_external_tool(
            server_name,
            tool_name,
            request.arguments,
            project_id=x_tenant_id,
        )
        write_audit_event(
            x_tenant_id,
            "mcp.external.tool_called",
            details={"server": server_name, "tool": tool_name, "is_error": result.get("is_error", False)},
        )
        return result
    except Exception as exc:
        raise _mcp_error(exc) from exc


@router.post("/servers/{server_name}/resources/read")
async def external_resource_read(
    server_name: str,
    request: MCPResourceReadRequest,
    x_tenant_id: str = Header(default="default"),
):
    """Read one URI from a configured external MCP server."""
    _ensure_project(x_tenant_id)
    if not request.uri.strip():
        raise HTTPException(status_code=400, detail="uri is required.")
    try:
        result = await read_external_resource(server_name, request.uri.strip(), x_tenant_id)
        write_audit_event(
            x_tenant_id,
            "mcp.external.resource_read",
            details={"server": server_name, "uri": request.uri[:500]},
        )
        return result
    except Exception as exc:
        raise _mcp_error(exc) from exc


@router.post("/servers/{server_name}/import")
async def import_external_mcp_data(
    server_name: str,
    request: MCPImportRequest,
    x_tenant_id: str = Header(default="default"),
):
    """Read an external MCP resource or tool result and index it into the selected Base project."""
    _ensure_project(x_tenant_id)
    try:
        if request.source_type == "tool":
            tool_name = (request.tool_name or "").strip()
            if not tool_name:
                raise ValueError("tool_name is required when source_type is 'tool'.")
            external_result = await call_external_tool(
                server_name,
                tool_name,
                request.arguments,
                project_id=x_tenant_id,
            )
            if external_result.get("is_error"):
                raise ValueError("The external MCP tool returned an error result and was not imported.")
            source_reference = tool_name
        else:
            resource_uri = (request.resource_uri or "").strip()
            if not resource_uri:
                raise ValueError("resource_uri is required when source_type is 'resource'.")
            external_result = await read_external_resource(server_name, resource_uri, x_tenant_id)
            source_reference = resource_uri

        text = external_result_text(external_result)
        ingestion = ingest_connector_text(
            tenant_id=x_tenant_id,
            connector_id=f"mcp_{server_name}",
            connector_name=f"MCP: {server_name}",
            filename=_import_filename(server_name, request),
            text=text,
            metadata={
                "mcp_server": server_name,
                "mcp_source_type": request.source_type,
                "mcp_source_reference": source_reference,
            },
        )
        write_audit_event(
            x_tenant_id,
            "mcp.external.imported",
            details={
                "server": server_name,
                "source_type": request.source_type,
                "source_reference": source_reference,
                "document_id": ingestion["document_id"],
                "chunks_created": ingestion["chunks_created"],
            },
        )
        return {
            "message": "External MCP data imported into the project knowledge base.",
            "server": server_name,
            "source_type": request.source_type,
            **ingestion,
        }
    except Exception as exc:
        raise _mcp_error(exc) from exc
