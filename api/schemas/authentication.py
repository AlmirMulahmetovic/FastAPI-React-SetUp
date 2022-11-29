from datetime import datetime

from pydantic import BaseModel, EmailStr


class SignUpReturnSchema(BaseModel):
    tokenExpiresAt: datetime


class LoginInputSchema(BaseModel):
    email: EmailStr
    password: str
