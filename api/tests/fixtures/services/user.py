from unittest.mock import AsyncMock, MagicMock

import pytest


@pytest.fixture
def user_service_mock():
    return MagicMock(create_user=AsyncMock(), find_user_by_email=AsyncMock())


def user_service_override():
    return MagicMock()
