import re
from datetime import datetime

from psycopg2 import tz
from sqlalchemy import BigInteger, Column, DateTime, text
from sqlalchemy.ext.declarative import as_declarative
from sqlalchemy.orm import declared_attr


def tz_utc_now():
    return datetime.now(tz=tz.FixedOffsetTimezone(offset=0))


def camel_to_snake_case(str):
    return re.sub(r"(?<!^)(?=[A-Z])", "_", str).lower()


@as_declarative()
class BaseModel:

    __name__: str

    @declared_attr
    def __tablename__(cls):
        return camel_to_snake_case(cls.__name__)

    id = Column(BigInteger, primary_key=True)
    created_at = Column(DateTime, nullable=False, server_default=text("statement_timestamp()"))
    updated_at = Column(
        DateTime,
        nullable=False,
        server_default=text("statement_timestamp()"),
        onupdate=tz_utc_now,
    )
