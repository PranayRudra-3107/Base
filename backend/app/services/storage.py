import json
import os
import re
from typing import Dict, List

from app.core.config import get_settings

settings = get_settings()


def _safe_tenant(tenant_id: str) -> str:
    return re.sub(r"[^a-zA-Z0-9_-]", "_", tenant_id or "default")


def _tenant_dir(tenant_id: str) -> str:
    path = os.path.join(settings.data_dir, _safe_tenant(tenant_id))
    os.makedirs(path, exist_ok=True)
    return path


def tenant_document_dir(tenant_id: str) -> str:
    path = os.path.join(settings.document_storage_dir, _safe_tenant(tenant_id))
    os.makedirs(path, exist_ok=True)
    return path


def save_raw_document(tenant_id: str, document_id: str, filename: str, file_bytes: bytes) -> str:
    safe_name = re.sub(r"[^a-zA-Z0-9_.-]", "_", filename)
    path = os.path.join(tenant_document_dir(tenant_id), f"{document_id}_{safe_name}")
    with open(path, "wb") as f:
        f.write(file_bytes)
    return path


def _json_path(tenant_id: str, name: str) -> str:
    return os.path.join(_tenant_dir(tenant_id), f"{name}.json")


def read_json(tenant_id: str, name: str, default):
    path = _json_path(tenant_id, name)
    if not os.path.exists(path):
        return default
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def write_json(tenant_id: str, name: str, data) -> None:
    with open(_json_path(tenant_id, name), "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def upsert_document_analysis(tenant_id: str, analysis: Dict) -> None:
    analyses = read_json(tenant_id, "analyses", [])
    analyses = [item for item in analyses if item.get("document_id") != analysis.get("document_id")]
    analyses.append(analysis)
    write_json(tenant_id, "analyses", analyses)


def list_document_analyses(tenant_id: str) -> List[Dict]:
    return read_json(tenant_id, "analyses", [])


def delete_document_analysis(tenant_id: str, document_id: str) -> bool:
    analyses = read_json(tenant_id, "analyses", [])
    kept = [item for item in analyses if item.get("document_id") != document_id]
    write_json(tenant_id, "analyses", kept)
    return len(kept) != len(analyses)
