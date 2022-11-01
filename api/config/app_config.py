from typing import Sequence

from pydantic import BaseSettings, PostgresDsn

from config.enums import BestBetEnvironment


class AppSettings(BaseSettings):
    ENVIRONMENT: BestBetEnvironment
    DATABASE_URL: PostgresDsn
    CORS_ALLOWED_ORIGINS: Sequence[str]
    CORS_ALLOWED_METHODS: Sequence[str] = ["*"]
    CORS_ALLOWED_HEADERS: Sequence[str] = ["*"]


AppConfig = AppSettings()
