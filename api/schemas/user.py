from pydantic import EmailStr

from schemas.base import BaseSchemaModel


class CreateUserSchema(BaseSchemaModel):
    email: EmailStr
    first_name: str
    last_name: str
    password: str


class UserReturnSchema(BaseSchemaModel):
    email: EmailStr
