import os
from enum import Enum
from typing import Optional

from pydantic import BaseSettings

secrets_dir = os.environ.get("SECRETS_DIR", "/tmp")


class Settings(BaseSettings):
    # Database
    DATABASE_URL: str
    MODELS_ECHO_QUERIES: bool = False

    class Config:
        secrets_dir = secrets_dir
        env_file = ".env"
        case_sensitive = True


settings = Settings()
