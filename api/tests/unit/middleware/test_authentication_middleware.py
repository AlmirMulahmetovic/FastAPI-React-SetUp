from unittest.mock import MagicMock

import pytest

from middleware.authentication_midleware import authentication_middlware


class TestAuthenticationMiddleware:
    @pytest.mark.asyncio
    async def test_authentication_middleware(self, authentication_service_mock):
        await authentication_middlware(
            request_mock := MagicMock(),
            access_token_mock := MagicMock(),
            authentication_service_mock,
        )

        authentication_service_mock.get_user_from_token.assert_called_once_with(access_token_mock)
        assert request_mock.user == authentication_service_mock.get_user_from_token.return_value
