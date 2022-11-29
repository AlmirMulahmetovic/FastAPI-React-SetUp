import pytest

from models.user import User


@pytest.fixture
def default_user_model(default_user_schema):
    return User(**default_user_schema.dict())
