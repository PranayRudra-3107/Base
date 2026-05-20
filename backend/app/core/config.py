from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    openai_api_key: str = ""
    anthropic_api_key: str = ""
    chroma_persist_dir: str = "./chroma_db"
    data_dir: str = "./data"
    document_storage_dir: str = "./data/documents"
    audit_log_path: str = "./data/audit_log.jsonl"
    embedding_model: str = "text-embedding-3-small"
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
