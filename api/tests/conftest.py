from glob import glob
from unittest.mock import MagicMock

import pytest
from fastapi.testclient import TestClient
from httpx import AsyncClient

from app import app
from services.database import DatabaseService

pytest_plugins = [
    fixture.replace("/", ".").replace("\\", ".").replace(".py", "")
    for fixture in glob("tests/fixtures/**/*.py", recursive=True)
    + glob("tests/integration/fixtures/**/*.py", recursive=True)
    if "__" not in fixture
]


@pytest.fixture
def session_mock():
    session = MagicMock()
    app.dependency_overrides[DatabaseService.get_db_session] = lambda: session
    yield session
    del app.dependency_overrides[DatabaseService.get_db_session]


@pytest.fixture
def client(session_mock):
    with TestClient(app) as client:
        yield client


@pytest.fixture
def async_client(session_mock):
    return AsyncClient(app=app, base_url="http://localhost")
