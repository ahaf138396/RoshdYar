from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache
from pathlib import Path
from typing import List, Optional, Literal

class BasicSettings(BaseModel):
    app_name:str
    app_env: Literal["development", "testing", "production"] = "development"
    api_prefix: str = "/api/v1"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

@lru_cache()
def get_basic() -> BasicSettings:
    return BasicSettings() # type: ignore