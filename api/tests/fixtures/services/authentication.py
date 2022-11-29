from datetime import datetime
from unittest.mock import AsyncMock, MagicMock

import pytest

TOKEN_EXPIRATION_DATE = datetime.now()


@pytest.fixture
def token():
    return "Bearer token"


@pytest.fixture
def token_expiration_date():
    return TOKEN_EXPIRATION_DATE


@pytest.fixture
def authentication_service_mock(token):
    return MagicMock(
        generate_token=MagicMock(return_value=(token, TOKEN_EXPIRATION_DATE)),
        check_user_password=MagicMock(return_value=True),
        get_user_from_token=AsyncMock(),
    )


def authentication_service_override():
    return MagicMock()
