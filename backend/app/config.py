import os
from functools import lru_cache
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    openai_api_key: str = Field(default="", env="OPENAI_API_KEY")
    serp_api_key: str = Field(default="", env="SERP_API_KEY")
    firecrawl_api_key: str = Field(default="", env="FIRECRAWL_API_KEY")
    openai_model: str = Field(default="gpt-4o-mini", env="OPENAI_MODEL")
    serp_base_url: str = Field(default="https://serpapi.com/search", env="SERP_BASE_URL")
    firecrawl_base_url: str = Field(default="https://api.firecrawl.dev/v1/crawl", env="FIRECRAWL_BASE_URL")
    app_name: str = Field(default="AI Business Presence Auditor")

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=False
    )


@lru_cache()
def get_settings() -> Settings:
    return Settings()

