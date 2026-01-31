from typing import Any
#from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import DeclarativeBase, declared_attr

#@as_declarative
class Base(DeclarativeBase):
    id : Any
    __name__ : str

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()
#this base class will serve as templates for our upcoming modules


