from sqlalchemy import Column, Unicode


class EnumMixin:
    id = None
    name = Column(Unicode(length=100), primary_key=True, index=True)
    description = Column(Unicode(length=500), nullable=False)
