from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


from fastapi import FastAPI, Request, Response
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config.app_config import AppConfig

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


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response


def get_db_session(request: Request):
    return request.state.db


@app.get("/")
def get_root():
    return "Hello world!"
