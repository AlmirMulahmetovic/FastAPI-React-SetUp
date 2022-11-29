from unittest.mock import MagicMock

import pytest
from fastapi import HTTPException

from controllers.authentication import AuthenticationController


class TestAuthentcationController:
    @pytest.mark.asyncio
    async def test_sign_up(
        self, authentication_service_mock, user_service_mock, token, token_expiration_date
    ):
        assert await AuthenticationController(
            authentication_service_mock, user_service_mock
        ).sign_up(response_mock := MagicMock(), user_data_mock := MagicMock()) == {
            "tokenExpiresAt": token_expiration_date
        }
        user_service_mock.create_user.assert_called_with(user_data_mock)
        authentication_service_mock.generate_token.assert_called_with(
            user_service_mock.create_user.return_value.email
        )
        response_mock.set_cookie.assert_called_with(
            "access_token",
            value=f"Bearer {token}",
            httponly=True,
            samesite="strict",
            expires=token_expiration_date.strftime("%a, %d %b %Y %H:%M:%S GMT"),
        )

    @pytest.mark.asyncio
    async def test_login(
        self, authentication_service_mock, user_service_mock, token, token_expiration_date
    ):
        assert await AuthenticationController(authentication_service_mock, user_service_mock).login(
            response_mock := MagicMock(), user_data_mock := MagicMock()
        ) == {"tokenExpiresAt": token_expiration_date}
        user_service_mock.find_user_by_email.assert_called_with(user_data_mock.email)
        authentication_service_mock.check_user_password.assert_called_with(
            user_service_mock.find_user_by_email.return_value, user_data_mock.password
        )
        authentication_service_mock.generate_token.assert_called_with(
            user_service_mock.find_user_by_email.return_value.email
        )
        response_mock.set_cookie.assert_called_with(
            "access_token",
            value=f"Bearer {token}",
            httponly=True,
            samesite="strict",
            expires=token_expiration_date.strftime("%a, %d %b %Y %H:%M:%S GMT"),
        )

    @pytest.mark.asyncio
    async def test_login_invalid_password(self, authentication_service_mock, user_service_mock):
        authentication_service_mock.check_user_password.return_value = False
        with pytest.raises(HTTPException):
            await AuthenticationController(authentication_service_mock, user_service_mock).login(
                MagicMock(), MagicMock()
            )

    def test_logout(self, authentication_service_mock, user_service_mock):
        AuthenticationController(authentication_service_mock, user_service_mock).logout(
            response_mock := MagicMock()
        )
        response_mock.delete_cookie.assert_called_with("access_token")
