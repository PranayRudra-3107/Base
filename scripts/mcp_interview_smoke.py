#!/usr/bin/env python3
"""Run the Base MCP registry interview scenario against a local demo stack."""

import json
import os
import sys
import time
import urllib.error
import urllib.request


BASE_URL = os.getenv("BASE_DEMO_URL", "http://127.0.0.1:8010").rstrip("/")


def request(path, method="GET", payload=None, project_id=""):
    body = json.dumps(payload).encode() if payload is not None else None
    headers = {"Content-Type": "application/json"}
    if project_id:
        headers["x-tenant-id"] = project_id
    req = urllib.request.Request(f"{BASE_URL}{path}", data=body, headers=headers, method=method)
    with urllib.request.urlopen(req, timeout=45) as response:
        return json.loads(response.read().decode())


def wait_for_base():
    for _ in range(60):
        try:
            request("/health")
            return
        except (OSError, urllib.error.URLError):
            time.sleep(1)
    raise RuntimeError(f"Base did not become ready at {BASE_URL}")


def stage(label, value):
    print(f"\n[{label}]")
    print(json.dumps(value, indent=2, ensure_ascii=True))


def main():
    wait_for_base()
    project = request(
        "/api/projects/",
        method="POST",
        payload={"name": "MCP Interview Demo", "description": "Disposable registry and interoperability test"},
    )
    project_id = project["project_id"]
    stage("1. PROJECT", {"project_id": project_id, "name": project["name"]})

    try:
        registry = request("/api/mcp/registry", project_id=project_id)
        assert registry["server_count"] == 1
        stage("2. REGISTRY", registry)

        capabilities = request(
            "/api/mcp/servers/acme_enterprise/capabilities",
            project_id=project_id,
        )
        tool_names = [tool["name"] for tool in capabilities.get("tools", [])]
        assert {"search_enterprise", "get_record", "create_handoff_note"}.issubset(tool_names)
        stage(
            "3. DISCOVERY",
            {
                "server": capabilities.get("server_info"),
                "tools": tool_names,
                "resources": [item.get("uri") for item in capabilities.get("resources", [])],
                "resource_templates": [item.get("uriTemplate") for item in capabilities.get("resource_templates", [])],
            },
        )

        record = request(
            "/api/mcp/servers/acme_enterprise/tools/get_record",
            method="POST",
            payload={"arguments": {"record_id": "BASE-431"}},
            project_id=project_id,
        )
        assert "BASE-431" in record.get("text", "")
        stage("4. READ TOOL", {"tool": record["tool"], "text": record["text"]})

        note = request(
            "/api/mcp/servers/acme_enterprise/tools/create_handoff_note",
            method="POST",
            payload={
                "arguments": {
                    "project": "Base",
                    "owner": "Interview Demo",
                    "summary": "Investigate BASE-431 and validate the checkout rollback threshold.",
                }
            },
            project_id=project_id,
        )
        assert "HANDOFF-" in note.get("text", "")
        stage("5. WRITE TOOL", {"tool": note["tool"], "text": note["text"]})

        resource = request(
            "/api/mcp/servers/acme_enterprise/resources/read",
            method="POST",
            payload={"uri": "acme://runbooks/checkout"},
            project_id=project_id,
        )
        assert "Checkout Rollback Runbook" in resource.get("text", "")
        stage("6. RESOURCE", {"uri": resource["uri"], "text": resource["text"][:500]})

        imported = request(
            "/api/mcp/servers/acme_enterprise/import",
            method="POST",
            payload={
                "source_type": "tool",
                "tool_name": "search_enterprise",
                "arguments": {"query": "checkout", "source": "all", "limit": 10},
                "filename": "acme_checkout_context.md",
            },
            project_id=project_id,
        )
        assert imported.get("chunks_created", 0) > 0
        documents = request("/api/documents/", project_id=project_id)
        assert any(item.get("filename") == "acme_checkout_context.md" for item in documents)
        stage(
            "7. IMPORT TO RAG",
            {
                "document_id": imported["document_id"],
                "chunks_created": imported["chunks_created"],
                "indexed_sources": [item.get("filename") for item in documents],
            },
        )
        print("\nMCP interview demo passed end to end.")
    finally:
        request(f"/api/projects/{project_id}", method="DELETE")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"MCP interview demo failed: {exc}", file=sys.stderr)
        raise
