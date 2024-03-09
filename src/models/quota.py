from sqlalchemy import Column, Integer, DateTime
from .base import Base
from pydantic import BaseModel


class Quota(Base):
    __tablename__ = "api_quota"

    id = Column(Integer, primary_key=True, index=True)
    date_created = Column(DateTime)
    date_updated = Column(DateTime)
    current_count = Column(Integer)
    max_count = Column(Integer)


class QuotaOut(BaseModel):
    id: int
    date_created: DateTime
    date_updated: DateTime
    current_count: int
    max_count: int

    class Config:
        orm_mode = True
