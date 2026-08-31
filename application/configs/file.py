from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache
from pathlib import Path
from typing import List, Optional, Literal

class FileSettings(BaseSettings):
    file_storage_path: Path = Field(
        default=Path("/var/app/uploads"),
        validation_alias="FILE_STORAGE_PATH"
    )

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

@lru_cache()
def get_file() -> FileSettings:
    return FileSettings() # type: ignore