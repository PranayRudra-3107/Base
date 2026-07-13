# MCP Registry Interview Demo

This demo shows Base acting in both MCP directions:

1. **MCP server:** GenAI clients connect to Base and call project intelligence tools.
2. **MCP client and registry:** Base discovers an allowlisted enterprise MCP server, calls tools, reads resources, and imports returned data into project RAG.

The included `Acme Enterprise Systems` server is intentionally open source and deterministic. It models Jira tickets, Confluence runbooks, PagerDuty incidents, and a controlled handoff-note write API without requiring third-party accounts.

## Architecture

```text
Interviewer / GenAI client
          |
          | Streamable HTTP MCP
          v
Base MCP server (/mcp)
          |
          +--> Base tools: search, dashboard, graph, RAG, multi-agent review

Base MCP registry (/api/mcp/registry)
          |
          | allowlisted Streamable HTTP MCP
          v
Acme Enterprise Systems (:8100/mcp)
          |
          +--> Jira-like records
          +--> Confluence-like runbooks
          +--> PagerDuty-like incidents
          +--> Controlled handoff-note writes
```

The registry is configuration-backed rather than accepting arbitrary URLs at runtime. This prevents server-side request forgery, keeps credentials in environment variables or Secrets Manager, and supports per-project server allowlists.

## Start The Demo

From the repository root:

```bash
docker compose -f docker-compose.mcp-demo.yml up --build -d
```

Run the automated proof:

```bash
python3 scripts/mcp_interview_smoke.py
```

The script creates a disposable Base project, then demonstrates:

1. Registry lookup.
2. MCP capability negotiation.
3. Reading `BASE-431` through a tool.
4. Writing a generated `HANDOFF-*` note through a controlled tool.
5. Reading `acme://runbooks/checkout`.
6. Importing enterprise search results into Base RAG.
7. Verifying the indexed source and deleting the disposable project.

For the visual registry, serve the frontend and point it to the demo backend:

```bash
cd frontend
python3 -m http.server 3000
```

Open:

```text
http://localhost:3000/?api=http://localhost:8010#/projects
```

Create a project, open **Connectors**, and use **Discover** in the MCP Registry section. The UI will show the server, authentication posture, tool count, and resource count.

Stop and remove the disposable stack:

```bash
docker compose -f docker-compose.mcp-demo.yml down --volumes
```

## Manual API Walkthrough

Set a project identifier from the Base project list:

```bash
export PROJECT_ID="your-project-id"
```

Inspect the registry:

```bash
curl http://localhost:8010/api/mcp/registry \
  -H "x-tenant-id: $PROJECT_ID" | jq
```

Discover capabilities:

```bash
curl http://localhost:8010/api/mcp/servers/acme_enterprise/capabilities \
  -H "x-tenant-id: $PROJECT_ID" | jq
```

Read enterprise data:

```bash
curl -X POST http://localhost:8010/api/mcp/servers/acme_enterprise/tools/get_record \
  -H "Content-Type: application/json" \
  -H "x-tenant-id: $PROJECT_ID" \
  -d '{"arguments":{"record_id":"BASE-431"}}' | jq
```

Write a handoff note:

```bash
curl -X POST http://localhost:8010/api/mcp/servers/acme_enterprise/tools/create_handoff_note \
  -H "Content-Type: application/json" \
  -H "x-tenant-id: $PROJECT_ID" \
  -d '{"arguments":{"project":"Base","owner":"Demo","summary":"Validate checkout rollback readiness."}}' | jq
```

Import enterprise data into Base:

```bash
curl -X POST http://localhost:8010/api/mcp/servers/acme_enterprise/import \
  -H "Content-Type: application/json" \
  -H "x-tenant-id: $PROJECT_ID" \
  -d '{"source_type":"tool","tool_name":"search_enterprise","arguments":{"query":"checkout"},"filename":"acme_checkout_context.md"}' | jq
```

## Interview Explanation

Use this concise narrative:

> I implemented Base as both an MCP server and an MCP client. Its registry is an allowlisted catalog of enterprise MCP endpoints with project-level access rules and environment-backed credentials. Base negotiates capabilities, calls tools or reads resources, normalizes the MCP response, and can ingest it through the same analysis, chunking, vector, keyword, knowledge-graph, and audit pipeline used by native connectors.

Then emphasize the engineering decisions:

- Streamable HTTP and the official MCP Python SDK.
- Capability discovery rather than hardcoded tool assumptions.
- Configuration-backed registry to prevent arbitrary outbound requests.
- Project allowlists and secret indirection.
- Read and controlled-write tool demonstrations.
- Normalized ingestion into RAG with auditability and source provenance.
