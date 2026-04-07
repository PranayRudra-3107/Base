from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    openai_api_key: str = ""
    anthropic_api_key: str = ""
    chroma_persist_dir: str = "./chroma_db"
    embedding_model: str = "text-embedding-3-small"
    llm_model: str = "gpt-4o"
    chunk_size: int = 500
    chunk_overlap: int = 50
    retrieval_k: int = 5

    class Config:
        env_file = ".env"


@lru_cache()
def get_settings():
    return Settings()
