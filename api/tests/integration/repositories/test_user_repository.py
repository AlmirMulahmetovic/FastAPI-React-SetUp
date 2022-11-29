import pytest
from sqlalchemy.exc import IntegrityError

from repository.user import UserRepository


class TestUserRepository:
    @pytest.mark.parametrize(
        "user_email, expected_output",
        [
            ("default@gmail.com", pytest.lazy_fixture("db_default_user")),
            ("nonExistent@gmail.com", None),
        ],
    )
    @pytest.mark.asyncio
    async def test_find_user_by_email(self, session, user_email, expected_output):
        assert await UserRepository(session).find_user_by_email(user_email) == expected_output

    @pytest.mark.asyncio
    async def test_save_user(self, session, default_user_schema):
        return_value = await UserRepository(session).save_user(default_user_schema)
        assert return_value.email == default_user_schema.email
        assert return_value.password == default_user_schema.password
        assert return_value.first_name == default_user_schema.first_name
        assert return_value.last_name == default_user_schema.last_name

    @pytest.mark.asyncio
    async def test_save_user__user_already_exists(
        self, session, db_default_user, default_user_schema
    ):
        with pytest.raises(
            IntegrityError, match='duplicate key value violates unique constraint "ix_user_email"'
        ):
            await UserRepository(session).save_user(default_user_schema)

    # async def save_user(self, user_data: CreateUserSchema) -> User:
    #     user_data.password = UserRepository._encrypt_password(user_data.password)
    #     user: User = User(**user_data.dict())
    #     self.session.add(user)
    #     self.session.commit()
    #     return user
