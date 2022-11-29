from fastapi import APIRouter, Body, Depends, Response, status

from controllers.authentication import AuthenticationController
from schemas.authentication import LoginInputSchema, SignUpReturnSchema
from schemas.user import CreateUserSchema

authentication_router = APIRouter()


@authentication_router.post(
    "/sign-up", status_code=status.HTTP_201_CREATED, response_model=SignUpReturnSchema
)
async def sign_up(
    response: Response,
    user_data: CreateUserSchema = Body(),
    authentication_controller=Depends(AuthenticationController),
):
    return await authentication_controller.sign_up(response, user_data)


@authentication_router.post(
    "/login", status_code=status.HTTP_200_OK, response_model=SignUpReturnSchema
)
async def login(
    response: Response,
    user_data: LoginInputSchema = Body(),
    authentication_controller=Depends(AuthenticationController),
):
    return await authentication_controller.login(response, user_data)


@authentication_router.post("/logout", status_code=status.HTTP_200_OK)
def logout(response: Response, authentication_controller=Depends(AuthenticationController)):
    authentication_controller.logout(response)
