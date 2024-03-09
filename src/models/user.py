from sqlalchemy import Column, Integer, String, DateTime
from .base import Base
from pydantic import BaseModel


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password_hash = Column(String)
    date_created = Column(DateTime)


class UserOut(BaseModel):
    id: int
    username: str
    email: str
    date_created: DateTime

    class Config:
        orm_mode = True
