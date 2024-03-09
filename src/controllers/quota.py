from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from src.schemas.quota import QuotaCreate, QuotaUpdate
from src.models.quota import Quota
from src.config import get_db


def create_quota(quota_data: QuotaCreate, db: Session = Depends(get_db)):
    quota = Quota(**quota_data.model_dump())
    db.add(quota)
    db.commit()
    db.refresh(quota)
    return quota


def get_quota(quota_id: int, db: Session = Depends(get_db)):
    quota = db.query(Quota).filter(Quota.id == quota_id).first()
    if quota is None:
        raise HTTPException(status_code=404, detail="Quota not found")
    return quota


def update_quota(quota_id: int, quota_data: QuotaUpdate, db: Session = Depends(get_db)):
    quota = db.query(Quota).filter(Quota.id == quota_id).first()
    if quota is None:
        raise HTTPException(status_code=404, detail="Quota not found")
    for var, value in vars(quota_data).items():
        setattr(quota, var, value) if value else None
    db.commit()
    db.refresh(quota)
    return quota


def delete_quota(quota_id: int, db: Session = Depends(get_db)):
    quota = db.query(Quota).filter(Quota.id == quota_id).first()
    if quota is None:
        raise HTTPException(status_code=404, detail="Quota not found")
    db.delete(quota)
    db.commit()
