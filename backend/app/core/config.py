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
    web_search_enabled: bool = True
    web_search_model: str = "gpt-4o-mini"
    web_search_tool: str = "web_search"
    web_search_context_size: str = "medium"
    web_search_min_relevance: float = 0.2
    chunk_size: int = 500
    chunk_overlap: int = 50
    retrieval_k: int = 5

    class Config:
        env_file = ".env"


@lru_cache()
def get_settings():
    return Settings()


def parse_csv_setting(value: str) -> list[str]:
    return [item.strip() for item in (value or "").split(",") if item.strip()]
