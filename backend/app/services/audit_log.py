import json
import os
from datetime import datetime
from typing import Dict, List

from app.core.config import get_settings

settings = get_settings()


def write_audit_event(
    tenant_id: str,
    action: str,
    actor: str = "system",
    details: Dict = None,
) -> Dict:
    os.makedirs(os.path.dirname(settings.audit_log_path), exist_ok=True)
    event = {
        "timestamp": datetime.utcnow().isoformat(),
        "tenant_id": tenant_id,
        "actor": actor,
        "action": action,
        "details": details or {},
    }
    with open(settings.audit_log_path, "a", encoding="utf-8") as f:
        f.write(json.dumps(event) + "\n")
    return event


def read_audit_events(tenant_id: str, limit: int = 100) -> List[Dict]:
    if not os.path.exists(settings.audit_log_path):
        return []

    events = []
    with open(settings.audit_log_path, "r", encoding="utf-8") as f:
        for line in f:
            try:
                event = json.loads(line)
            except json.JSONDecodeError:
                continue
            if event.get("tenant_id") == tenant_id:
                events.append(event)

    return list(reversed(events[-limit:]))
