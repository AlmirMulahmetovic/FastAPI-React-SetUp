from pydantic import BaseModel

from utils.string import to_camel_case


class BaseSchemaModel(BaseModel):
    class Config:
        orm = True
        alias_generator = to_camel_case
