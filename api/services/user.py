from fastapi import Depends, HTTPException, status

from models.user import User
from repository.user import UserRepository
from schemas.user import CreateUserSchema


class UserNotFoundError(HTTPException):
    def __init__(self, email):
        super().__init__(
            status_code=status.HTTP_403_FORBIDDEN, detail=f"User with email {email} does not exist!"
        )


class UserAlreadyExistsError(HTTPException):
    def __init__(self, email):
        super().__init__(
            status_code=status.HTTP_403_FORBIDDEN, detail=f"User with email {email} already exists!"
        )


class UserService:
    def __init__(self, user_repository: UserRepository = Depends(UserRepository)):
        self.user_repository: UserRepository = user_repository

    async def create_user(self, user_data: CreateUserSchema) -> User:
        if (await self.user_repository.find_user_by_email(user_data.email)) is not None:
            raise UserAlreadyExistsError(user_data.email)

        return await self.user_repository.save_user(user_data)

    async def find_user_by_email(self, email: str) -> User:
        if (user := await self.user_repository.find_user_by_email(email)) is None:
            raise UserNotFoundError(email)

        return user


user_service = UserService()
