from fastapi import Request, Response, status
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from config.app_config import AppConfig

engine = create_engine(url=AppConfig.DATABASE_URL)
SessionLocal = sessionmaker(autoflush=False, bind=engine)


class DatabaseService:
    @staticmethod
    async def db_session_middleware(request: Request, call_next) -> Response:
        response = Response(
            "Internal server error", status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
        try:
            request.state.db = SessionLocal()
            response = await call_next(request)
        finally:
            request.state.db.close()
        return response

    @staticmethod
    def get_db_session(request: Request) -> Session:
        return request.state.db
