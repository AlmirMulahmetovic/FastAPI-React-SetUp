import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import create_database, database_exists, drop_database

from alembic.command import upgrade as alembic_upgrade
from alembic.config import Config as AlembicConfig
from config.app_config import AppConfig
from config.migration_config import MigrationConfig


@pytest.fixture
def db_engine():
    AppConfig.DATABASE_URL = f"{AppConfig.DATABASE_URL}_test"
    MigrationConfig.DATABASE_URL = AppConfig.DATABASE_URL
    engine = create_engine(AppConfig.DATABASE_URL)

    # create db
    create_database(engine.url)

    # execute all alembic migrations
    alembic_config = AlembicConfig("alembic.ini")
    alembic_upgrade(alembic_config, "head")
    try:
        yield engine.connect()
    finally:
        engine.dispose()
        if database_exists(AppConfig.DATABASE_URL):
            drop_database(AppConfig.DATABASE_URL)


@pytest.fixture
def session(db_engine):
    TestSession = sessionmaker(bind=db_engine)
    session = TestSession()
    try:
        yield session
    finally:
        session.close()
