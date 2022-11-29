from fastapi import Depends, HTTPException, Response, status

from schemas.user import CreateUserSchema
from services.authentication import AuthenticationService
from services.user import UserService


class AuthenticationController:
    def __init__(
        self,
        authentication_service: AuthenticationService = Depends(AuthenticationService),
        user_service: UserService = Depends(UserService),
    ):
        self.authentication_service: AuthenticationService = authentication_service
        self.user_service: UserService = user_service

    async def sign_up(self, response: Response, user_data: CreateUserSchema) -> dict:
        user = await self.user_service.create_user(user_data)
        token, expiration_date = self.authentication_service.generate_token(user.email)
        response.set_cookie(
            "access_token",
            value=f"Bearer {token}",
            httponly=True,
            samesite="strict",
            expires=expiration_date.strftime("%a, %d %b %Y %H:%M:%S GMT"),
        )
        return {"tokenExpiresAt": expiration_date}

    async def login(self, response: Response, user_data: CreateUserSchema) -> dict:
        user = await self.user_service.find_user_by_email(user_data.email)

        if not self.authentication_service.check_user_password(user, user_data.password):
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid password!")

        token, expiration_date = self.authentication_service.generate_token(user.email)
        response.set_cookie(
            "access_token",
            value=f"Bearer {token}",
            httponly=True,
            samesite="strict",
            expires=expiration_date.strftime("%a, %d %b %Y %H:%M:%S GMT"),
        )
        return {"tokenExpiresAt": expiration_date}

    def logout(self, response: Response) -> None:
        response.delete_cookie("access_token")
