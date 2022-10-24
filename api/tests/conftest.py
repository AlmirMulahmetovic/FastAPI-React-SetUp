from glob import glob
from unittest.mock import MagicMock

import pytest
from fastapi.testclient import TestClient

from app import app, get_db_session

pytest_plugins = [
    fixture.replace("/", ".").replace("\\", ".").replace(".py", "")
    for fixture in glob("tests/fixtures/**/*.py", recursive=True)
    if "__" not in fixture
]

db = MagicMock()


@pytest.fixture
def db_mock():
    return db


def override_get_db_session():
    return db


app.dependency_overrides[get_db_session] = override_get_db_session


@pytest.fixture
def client():
    yield TestClient(app)
