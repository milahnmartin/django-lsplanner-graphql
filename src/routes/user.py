from fastapi import APIRouter
from src.models.user import UserOut

from src.controllers.user import create_user, get_user, update_user, delete_user

router = APIRouter()

router.post("/users/", response_model=UserOut)(create_user)
router.get("/users/{user_id}", response_model=UserOut)(get_user)
router.put("/users/{user_id}", response_model=UserOut)(update_user)
router.delete("/users/{user_id}")(delete_user)
