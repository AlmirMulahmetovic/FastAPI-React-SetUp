from unittest.mock import AsyncMock, MagicMock

import pytest

from app import app
from controllers.authentication import AuthenticationController


@pytest.fixture
def authentication_controller_mock(token_expiration_date):
    controller_mock = MagicMock(
        sign_up=AsyncMock(return_value={"tokenExpiresAt": token_expiration_date}),
        login=AsyncMock(return_value={"tokenExpiresAt": token_expiration_date}),
    )
    app.dependency_overrides[AuthenticationController] = lambda: controller_mock
    yield controller_mock
    del app.dependency_overrides[AuthenticationController]
