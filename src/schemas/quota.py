from pydantic import BaseModel
from datetime import datetime


class QuotaBase(BaseModel):
    current_count: int
    max_count: int


class QuotaCreate(QuotaBase):
    pass


class QuotaUpdate(QuotaBase):
    pass


class Quota(QuotaBase):
    id: int
    date_created: datetime
    date_updated: datetime

    class Config:
        orm_mode = True
