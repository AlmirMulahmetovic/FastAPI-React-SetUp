from unittest.mock import MagicMock, patch

import pytest

from config.app_config import AppConfig
from services.authentication import (
    ALGORITHM,
    AuthenticationService,
    DecodeError,
    InvalidTokenError,
    NotAuthorizedException,
    UserNotFoundError,
)


class TestAuthenticationService:
    @patch("services.authentication.datetime")
    @patch("services.authentication.timedelta")
    @patch("services.authentication.encode")
    def test_generate_token(self, encode_mock, timedelta_mock, datetime_mock, user_service_mock):
        datetime_mock.utcnow.return_value = "current_time"
        timedelta_mock.return_value = "timedelta"
        assert AuthenticationService.generate_token(email := "default@gmail.com") == (
            encode_mock.return_value,
            datetime_mock.utcnow.return_value + timedelta_mock.return_value,
        )
        encode_mock.assert_called_once_with(
            {
                "email": email,
                "exp": datetime_mock.utcnow.return_value + timedelta_mock.return_value,
            },
            AppConfig.JWT_BASE,
            algorithm=ALGORITHM,
        )

    @patch("services.authentication.bcrypt")
    def test_check_user_password(self, bcrypt_mock, user_service_mock):
        AuthenticationService(user_service_mock).check_user_password(
            user_mock := MagicMock(), password_mock := MagicMock()
        )
        user_mock.password.encode.assert_called_once_with("utf-8")
        password_mock.encode.assert_called_once_with("utf-8")
        bcrypt_mock.checkpw.assert_called_once_with(
            password_mock.encode.return_value, user_mock.password.encode.return_value
        )

    @pytest.mark.asyncio
    @patch("services.authentication.decode")
    async def test_get_user_from_token(self, decode_mock, user_service_mock):

        decode_mock.return_value = {"email": "default@gmail.com"}
        assert (
            await AuthenticationService(user_service_mock).get_user_from_token(
                access_token_mock := MagicMock()
            )
            == user_service_mock.find_user_by_email.return_value
        )

        access_token_mock.removeprefix.assert_called_once_with("Bearer ")
        decode_mock.assert_called_with(
            access_token_mock.removeprefix.return_value, AppConfig.JWT_BASE, algorithms=[ALGORITHM]
        )
        user_service_mock.find_user_by_email.assert_called_once_with("default@gmail.com")

    @pytest.mark.asyncio
    async def test_get_user_from_token_no_access_token(self, user_service_mock):
        with pytest.raises(NotAuthorizedException):
            await AuthenticationService(user_service_mock).get_user_from_token(None)

    @pytest.mark.asyncio
    @pytest.mark.parametrize("decode_error", [DecodeError, InvalidTokenError])
    @patch("services.authentication.decode")
    async def test_get_user_from_token_handles_decode_errors(
        self, decode_mock, decode_error, user_service_mock
    ):
        decode_mock.side_effect = decode_error
        with pytest.raises(NotAuthorizedException):
            await AuthenticationService(user_service_mock).get_user_from_token(MagicMock())

    @pytest.mark.asyncio
    @patch("services.authentication.decode")
    async def test_get_user_from_token_handles_user_not_found(self, decode_mock, user_service_mock):
        decode_mock.return_value = {"email": "default@gmail.com"}
        user_service_mock.find_user_by_email.side_effect = UserNotFoundError(
            email="default@gmail.com"
        )
        with pytest.raises(NotAuthorizedException):
            await AuthenticationService(user_service_mock).get_user_from_token(MagicMock())
