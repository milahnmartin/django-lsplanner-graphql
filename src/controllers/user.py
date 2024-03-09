from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from src.schemas.user import UserCreate, UserUpdate
from src.models.user import User
from src.config import get_db


def create_user(user_data: UserCreate, db: Session = Depends(get_db)):
    user = User(**user_data.model_dump())
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


def update_user(user_id: int, user_data: UserUpdate, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    for var, value in vars(user_data).items():
        setattr(user, var, value) if value else None
    db.commit()
    db.refresh(user)
    return user


def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(user)
    db.commit()
