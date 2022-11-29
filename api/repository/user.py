from typing import Optional

import bcrypt
from fastapi import Depends
from sqlalchemy.orm import Session

from models.user import User
from schemas.user import CreateUserSchema
from services.database import DatabaseService


class UserRepository:
    def __init__(self, session: Session = Depends(DatabaseService.get_db_session)):
        self.session = session

    @staticmethod
    def _encrypt_password(password: str) -> str:
        return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

    async def save_user(self, user_data: CreateUserSchema) -> User:
        user_data.password = UserRepository._encrypt_password(user_data.password)
        user: User = User(**user_data.dict())
        self.session.add(user)
        self.session.commit()
        return user

    async def find_user_by_email(self, email: str) -> Optional[User]:
        return self.session.query(User).filter(User.email == email).one_or_none()
