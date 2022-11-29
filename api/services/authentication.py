from datetime import datetime, timedelta
from typing import Any

import bcrypt
from fastapi import Depends, HTTPException, status
from jwt import DecodeError, InvalidTokenError, decode, encode

from config.app_config import AppConfig
from models.user import User
from services.user import UserNotFoundError, UserService

ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 1


class NotAuthorizedException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorised to perform action."
        )


class InvalidPasswordException(Exception):
    pass


class AuthenticationService:
    def __init__(self, user_service: UserService = Depends(UserService)):
        self.user_service: UserService = user_service
        print(self.user_service)

    @staticmethod
    def generate_token(email: str) -> tuple[Any, datetime]:
        payload = {
            "email": email,
            "exp": (
                token_expires_at := datetime.utcnow()
                + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
            ),
        }
        return encode(payload, AppConfig.JWT_BASE, algorithm=ALGORITHM), token_expires_at

    async def get_user_from_token(self, access_token: str) -> str:
        if access_token is None:
            raise NotAuthorizedException()

        try:
            token = decode(
                access_token.removeprefix("Bearer "), AppConfig.JWT_BASE, algorithms=[ALGORITHM]
            )
        except (DecodeError, InvalidTokenError):
            raise NotAuthorizedException()

        try:
            return await self.user_service.find_user_by_email(token["email"])
        except UserNotFoundError:
            raise NotAuthorizedException()

    @staticmethod
    def check_user_password(user: User, password: str):
        return bcrypt.checkpw(password.encode("utf-8"), user.password.encode("utf-8"))
