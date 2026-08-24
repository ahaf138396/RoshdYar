from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache
from pathlib import Path
from typing import List, Optional, Literal

class DatabaseSettings(BaseModel):
    database_url: str = Field(validation_alias="DATABASE_URL")

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

@lru_cache()
def get_db() -> DatabaseSettings:
    return DatabaseSettings() # type: ignore