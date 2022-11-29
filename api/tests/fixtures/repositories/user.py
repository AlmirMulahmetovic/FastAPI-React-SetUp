from unittest.mock import AsyncMock, MagicMock

import pytest


@pytest.fixture
def user_repository_mock():
    return MagicMock(find_user_by_email=AsyncMock(), save_user=AsyncMock())


def user_repository_override():
    return MagicMock()
