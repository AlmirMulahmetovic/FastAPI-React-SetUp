from fastapi import Cookie, Depends, Request

from services.authentication import AuthenticationService


async def authentication_middlware(
    request=Request,
    access_token: str = Cookie(default=None),
    authentication_service: AuthenticationService = Depends(AuthenticationService),
):
    user = await authentication_service.get_user_from_token(access_token)
    request.user = user
