# routes/user.py
from fastapi import APIRouter
from src.schemas.user import User
from src.controllers.user import create_user, get_user, update_user, delete_user

router = APIRouter()

router.post("/users/", response_model=User)(create_user)
router.get("/users/{user_id}", response_model=User)(get_user)
router.put("/users/{user_id}", response_model=User)(update_user)
router.delete("/users/{user_id}", response_model=User)(delete_user)
