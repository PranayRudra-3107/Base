from typing import Any, Dict

from fastapi import APIRouter, Header, HTTPException, Query
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

from app.services.connectors import (
    complete_oauth,
    disconnect_connector,
    list_connector_statuses,
    save_connector_credentials,
    start_oauth,
    sync_connector,
)

router = APIRouter()


class ConnectorCredentialsRequest(BaseModel):
    credentials: Dict[str, Any] = {}


@router.get("/")
def list_connectors(x_tenant_id: str = Header(default="default")):
    """Return every supported connector and the tenant's connection state."""
    return list_connector_statuses(x_tenant_id)


@router.post("/{connector_id}/credentials")
def connect_with_credentials(
    connector_id: str,
    payload: ConnectorCredentialsRequest,
    x_tenant_id: str = Header(default="default"),
):
    """Save connector credentials for a project workspace."""
    try:
        return save_connector_credentials(x_tenant_id, connector_id, payload.credentials)
    except KeyError as exc:
        raise HTTPException(status_code=404, detail=str(exc))
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc))


@router.post("/{connector_id}/authorize")
def authorize_connector(
    connector_id: str,
    x_tenant_id: str = Header(default="default"),
):
    """Start OAuth for connectors that support it."""
    try:
        return start_oauth(x_tenant_id, connector_id)
    except KeyError as exc:
        raise HTTPException(status_code=404, detail=str(exc))
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc))


@router.get("/oauth/{provider}/callback", response_class=HTMLResponse)
async def oauth_callback(
    provider: str,
    code: str = Query(default=""),
    state: str = Query(default=""),
    error: str = Query(default=""),
):
    """Complete OAuth and show a small browser result page."""
    if error:
        return HTMLResponse(
            f"<h1>Base connector sign-in failed</h1><p>{error}</p><p>You can close this tab and return to Base.</p>",
            status_code=400,
        )
    try:
        result = await complete_oauth(provider, code, state)
    except Exception as exc:
        return HTMLResponse(
            f"<h1>Base connector sign-in failed</h1><p>{str(exc)}</p><p>You can close this tab and try again.</p>",
            status_code=400,
        )

    return HTMLResponse(
        f"""
        <html>
          <body style="font-family: system-ui, sans-serif; padding: 32px;">
            <h1>Connected {result['connector_name']}</h1>
            <p>The connector was saved for project <code>{result['tenant_id']}</code>.</p>
            <p>You can close this tab and press Refresh in Base.</p>
            <script>
              if (window.opener) {{
                window.opener.postMessage({{type:'base.connector.connected', connectorId:'{result['connector_id']}'}}, '*');
              }}
            </script>
          </body>
        </html>
        """
    )


@router.post("/{connector_id}/sync")
async def sync_connector_endpoint(
    connector_id: str,
    x_tenant_id: str = Header(default="default"),
):
    """Fetch connector data and index it as a project source."""
    try:
        return await sync_connector(x_tenant_id, connector_id)
    except KeyError as exc:
        raise HTTPException(status_code=404, detail=str(exc))
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc))
    except Exception as exc:
        raise HTTPException(status_code=502, detail=f"Connector sync failed: {exc}")


@router.delete("/{connector_id}")
def disconnect_connector_endpoint(
    connector_id: str,
    x_tenant_id: str = Header(default="default"),
):
    """Remove stored connector credentials and state for a project."""
    try:
        disconnect_connector(x_tenant_id, connector_id)
        return {"message": "Connector disconnected.", "connector_id": connector_id}
    except KeyError as exc:
        raise HTTPException(status_code=404, detail=str(exc))
