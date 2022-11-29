import pytest


@pytest.fixture
def db_default_user(session, default_user_model):
    session.add(default_user_model)
    session.commit()
    return default_user_model
