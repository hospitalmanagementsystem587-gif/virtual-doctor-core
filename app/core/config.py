from typing import List
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = "Virtual Doctor Copilot"
    APP_ENV: str = "development"
    DEBUG: bool = True
    PORT: int = 8010
    HOST: str = "0.0.0.0"

    # Override in production with a JSON list of the exact embedding sites' origins.
    CORS_ORIGINS: List[str] = [
        "http://localhost:3000",
        "http://localhost:8000",
        "http://127.0.0.1:8000",
        "http://localhost:8010",
    ]

    LLM_PROVIDER: str = "gemini"  # "gemini" | "mock"
    GEMINI_API_KEY: str = ""
    GEMINI_MODEL: str = "gemini-2.5-flash"

    EMBEDDING_MODEL_NAME: str = "gemini-embedding-001"
    EMBEDDING_DIMENSIONS: int = 768

    HMS_API_URL: str = ""
    HMS_API_KEY: str = ""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )


settings = Settings()
