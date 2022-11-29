import pytest

from schemas.authentication import LoginInputSchema
from schemas.user import CreateUserSchema


@pytest.fixture
def default_user_schema():
    return CreateUserSchema(
        email="default@gmail.com",
        firstName="Almir",
        lastName="Mulahmetovic",
        password="defaultpass",
    )


@pytest.fixture
def default_sign_up_data():
    return {
        "email": "default@gmail.com",
        "firstName": "Almir",
        "lastName": "Mulahmetovic",
        "password": "defaultpass",
    }


@pytest.fixture
def default_login_data():
    return {"email": "default@gmail.com", "password": "defaultpass"}


@pytest.fixture
def default_login_schema():
    return LoginInputSchema(email="default@gmail.com", password="defaultpass")
