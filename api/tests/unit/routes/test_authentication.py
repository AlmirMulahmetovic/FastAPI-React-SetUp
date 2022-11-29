import pytest


class TestAuthenticationRoutes:
    @pytest.mark.asyncio
    async def test_sign_up(
        self,
        async_client,
        authentication_controller_mock,
        default_sign_up_data,
        token_expiration_date,
    ):
        async with async_client:
            response = await async_client.request(
                method="POST", url="/sign-up", json=default_sign_up_data
            )

        authentication_controller_mock.sign_up.assert_called_once()
        assert response.status_code == 201
        assert response.json() == {
            "tokenExpiresAt": token_expiration_date.strftime("%Y-%m-%dT%H:%M:%S.%f")
        }

    @pytest.mark.asyncio
    async def test_login(
        self,
        async_client,
        authentication_controller_mock,
        default_login_data,
        token_expiration_date,
    ):
        async with async_client:
            response = await async_client.request(
                method="POST", url="/login", json=default_login_data
            )

        authentication_controller_mock.login.assert_called_once()
        assert response.status_code == 200
        assert response.json() == {
            "tokenExpiresAt": token_expiration_date.strftime("%Y-%m-%dT%H:%M:%S.%f")
        }

    def test_logout(self, client, authentication_controller_mock):
        client.post("/logout")
        authentication_controller_mock.logout.assert_called_once()
