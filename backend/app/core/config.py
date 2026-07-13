from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    openai_api_key: str = ""
    anthropic_api_key: str = ""
    environment: str = "local"
    cors_origins: str = "https://yourdomain.vercel.app,http://localhost:3000,http://127.0.0.1:3000"
    chroma_persist_dir: str = "./chroma_db"
    data_dir: str = "./data"
    document_storage_dir: str = "./data/documents"
    audit_log_path: str = "./data/audit_log.jsonl"
    metadata_backend: str = "local"
    document_storage_backend: str = "local"
    vector_backend: str = "chroma"
    database_url: str = ""
    s3_bucket: str = ""
    s3_prefix: str = "base"
    aws_region: str = "us-east-1"
    embedding_model: str = "text-embedding-3-small"
    embedding_dimensions: int = 1536
    llm_model: str = "gpt-4o"
    langfuse_public_key: str = ""
    langfuse_secret_key: str = ""
    langfuse_base_url: str = "https://cloud.langfuse.com"
    langfuse_tracing_environment: str = "local"
    web_search_enabled: bool = True
    web_search_model: str = "gpt-4o-mini"
    web_search_tool: str = "web_search"
    web_search_context_size: str = "medium"
    web_search_min_relevance: float = 0.2
    chunk_size: int = 500
    chunk_overlap: int = 50
    retrieval_k: int = 5
    public_app_url: str = ""
    connector_sync_limit: int = 50
    connector_timeout_seconds: float = 25
    mcp_api_key: str = ""
    mcp_exposed_project_ids: str = ""
    mcp_allowed_hosts: str = "127.0.0.1:*,localhost:*,[::1]:*"
    mcp_allowed_origins: str = "http://127.0.0.1:*,http://localhost:*,http://[::1]:*"
    mcp_external_servers_json: str = "[]"
    mcp_request_timeout_seconds: float = 30
    mcp_max_import_chars: int = 200000
    microsoft_client_id: str = ""
    microsoft_client_secret: str = ""
    microsoft_tenant_id: str = "organizations"
    microsoft_redirect_uri: str = ""
    microsoft_connector_scopes: str = "offline_access User.Read Mail.Read Team.ReadBasic.All Channel.ReadBasic.All ChannelMessage.Read.All Chat.Read Sites.Read.All Files.Read.All"
    atlassian_client_id: str = ""
    atlassian_client_secret: str = ""
    atlassian_redirect_uri: str = ""
    atlassian_connector_scopes: str = "read:jira-work read:jira-user read:confluence-content.all read:confluence-space.summary offline_access"

    class Config:
        env_file = ".env"


@lru_cache()
def get_settings():
    return Settings()


def parse_csv_setting(value: str) -> list[str]:
    return [item.strip() for item in (value or "").split(",") if item.strip()]
