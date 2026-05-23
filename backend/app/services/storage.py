import json
import os
import re
from typing import Dict, List
from urllib.parse import quote, urlparse

from app.core.config import get_settings
from app.services.database import postgres_enabled, read_json_record, write_json_record

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


def _s3_client():
    import boto3

    return boto3.client("s3", region_name=settings.aws_region)


def _s3_key(tenant_id: str, document_id: str, filename: str) -> str:
    safe_name = re.sub(r"[^a-zA-Z0-9_.-]", "_", filename)
    prefix = settings.s3_prefix.strip("/")
    key = f"documents/{_safe_tenant(tenant_id)}/{document_id}_{safe_name}"
    return f"{prefix}/{key}" if prefix else key


def save_raw_document(tenant_id: str, document_id: str, filename: str, file_bytes: bytes) -> str:
    if settings.document_storage_backend.lower() == "s3":
        if not settings.s3_bucket:
            raise RuntimeError("S3_BUCKET is required when DOCUMENT_STORAGE_BACKEND=s3.")
        key = _s3_key(tenant_id, document_id, filename)
        _s3_client().put_object(
            Bucket=settings.s3_bucket,
            Key=key,
            Body=file_bytes,
            ContentType="application/octet-stream",
            Metadata={
                "tenant_id": quote(_safe_tenant(tenant_id), safe=""),
                "document_id": document_id,
                "filename": quote(filename, safe=""),
            },
        )
        return f"s3://{settings.s3_bucket}/{key}"

    safe_name = re.sub(r"[^a-zA-Z0-9_.-]", "_", filename)
    path = os.path.join(tenant_document_dir(tenant_id), f"{document_id}_{safe_name}")
    with open(path, "wb") as f:
        f.write(file_bytes)
    return path


def read_raw_document(storage_path: str) -> bytes:
    if not storage_path:
        raise FileNotFoundError("No storage path recorded for document.")
    if storage_path.startswith("s3://"):
        parsed = urlparse(storage_path)
        response = _s3_client().get_object(Bucket=parsed.netloc, Key=parsed.path.lstrip("/"))
        return response["Body"].read()
    with open(storage_path, "rb") as f:
        return f.read()


def delete_raw_document(storage_path: str) -> bool:
    if not storage_path:
        return False
    if storage_path.startswith("s3://"):
        parsed = urlparse(storage_path)
        _s3_client().delete_object(Bucket=parsed.netloc, Key=parsed.path.lstrip("/"))
        return True
    if os.path.exists(storage_path):
        os.remove(storage_path)
        return True
    return False


def _json_path(tenant_id: str, name: str) -> str:
    return os.path.join(_tenant_dir(tenant_id), f"{name}.json")


def read_json(tenant_id: str, name: str, default):
    if postgres_enabled():
        return read_json_record(_safe_tenant(tenant_id), name, default)

    path = _json_path(tenant_id, name)
    if not os.path.exists(path):
        return default
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def write_json(tenant_id: str, name: str, data) -> None:
    if postgres_enabled():
        write_json_record(_safe_tenant(tenant_id), name, data)
        return

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
