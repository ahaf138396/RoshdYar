from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache
from pathlib import Path
from typing import List, Optional, Literal

class BasicSettings(BaseSettings):
    app_name:str | None = None
    env: Literal["development", "testing", "production"] | None = "development"
    api_prefix: str | None = "/api/v1"
    app_host: str | None = "127.0.0.1"
    app_port: int | None = 8000
    app_description: str | None = None

    model_config = SettingsConfigDict(
        extra="ignore",
    )

@lru_cache()
def get_basic() -> BasicSettings:
    return BasicSettings() # type: ignore