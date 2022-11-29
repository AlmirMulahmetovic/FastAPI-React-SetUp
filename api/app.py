from fastapi import APIRouter, Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from starlette.middleware.base import BaseHTTPMiddleware

from config.app_config import AppConfig
from middleware.authentication_midleware import authentication_middlware
from routes.authentication import authentication_router
from services.database import DatabaseService

unprotected_router = APIRouter()
unprotected_router.include_router(authentication_router)

protected_router = APIRouter(dependencies=[Depends(authentication_middlware)])


@protected_router.get("/")
def get_root():
    return "Hello world!"


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=AppConfig.CORS_ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=AppConfig.CORS_ALLOWED_METHODS,
    allow_headers=AppConfig.CORS_ALLOWED_HEADERS,
)

engine = create_engine(url=AppConfig.DATABASE_URL)
SessionLocal = sessionmaker(autoflush=False, bind=engine)


app.add_middleware(BaseHTTPMiddleware, dispatch=DatabaseService.db_session_middleware)
app.include_router(unprotected_router)
app.include_router(protected_router)
