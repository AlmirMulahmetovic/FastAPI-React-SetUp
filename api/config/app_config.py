from pydantic import BaseSettings, PostgresDsn

from config.enums import BestBetEnvironment


class AppSettings(BaseSettings):
    ENVIRONMENT: BestBetEnvironment = BestBetEnvironment.dev
    DATABASE_URL: PostgresDsn = "postgresql+psycopg2://postgres:not-secret@localhost:5440/bestbet"


AppConfig = AppSettings()
