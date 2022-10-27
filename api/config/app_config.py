from pydantic import BaseSettings, PostgresDsn

from config.enums import BestBetEnvironment


class AppSettings(BaseSettings):
    ENVIRONMENT: BestBetEnvironment = BestBetEnvironment.dev
    DATABASE_URL: PostgresDsn = "postgresql+psycopg2://postgres:not-secret@localhost:5440/bestbet"
    CORS_ALLOWED_ORIGINS = ["http://localhost:3000"]
    CORS_ALLOWED_METHODS = ["*"]
    CORS_ALLOWED_HEADERS = ["*"]


AppConfig = AppSettings()
