from unittest.mock import MagicMock

import pytest

from services.user import UserAlreadyExistsError, UserNotFoundError, UserService


class TestUserService:
    @pytest.mark.asyncio
    async def test_create_user(self, user_repository_mock):
        user_repository_mock.find_user_by_email.return_value = None
        return_value = await UserService(user_repository_mock).create_user(
            user_data_mock := MagicMock()
        )

        user_repository_mock.find_user_by_email.assert_called_once_with(user_data_mock.email)
        user_repository_mock.save_user.assert_called_once_with(user_data_mock)
        assert return_value == user_repository_mock.save_user.return_value

    @pytest.mark.asyncio
    async def test_create_user_user_already_exists(self, user_repository_mock):
        user_repository_mock.find_user_by_email.return_value = MagicMock()
        with pytest.raises(UserAlreadyExistsError):
            await UserService(user_repository_mock).create_user(user_data_mock := MagicMock())

        user_repository_mock.find_user_by_email.assert_called_once_with(user_data_mock.email)
        user_repository_mock.save_user.assert_not_called()

    @pytest.mark.asyncio
    async def test_find_user_by_email(self, user_repository_mock):
        user_repository_mock.find_user_by_email.return_value = MagicMock()
        return_value = await UserService(user_repository_mock).find_user_by_email(
            email_mock := MagicMock()
        )

        user_repository_mock.find_user_by_email.assert_called_once_with(email_mock)
        assert return_value == user_repository_mock.find_user_by_email.return_value

    @pytest.mark.asyncio
    async def test_find_user_by_email_user_not_found(self, user_repository_mock):
        user_repository_mock.find_user_by_email.return_value = None
        with pytest.raises(UserNotFoundError):
            await UserService(user_repository_mock).find_user_by_email(email_mock := MagicMock())

        user_repository_mock.find_user_by_email.assert_called_once_with(email_mock)
