from sqlalchemy import Column, Unicode

from models.base.base_model import BaseModel


class User(BaseModel):
    email = Column(Unicode(100), unique=True, nullable=False, index=True)
    first_name = Column(Unicode(100), nullable=False)
    last_name = Column(Unicode(100), nullable=False)
    password = Column(Unicode, nullable=False)
