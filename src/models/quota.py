from sqlalchemy import Column, Integer, DateTime
from .base import Base


class Quota(Base):
    __tablename__ = "api_quota"

    id = Column(Integer, primary_key=True, index=True)
    date_created = Column(DateTime)
    date_updated = Column(DateTime)
    current_count = Column(Integer)
    max_count = Column(Integer)

    class Config:
        arbitrary_types_allowed = True
