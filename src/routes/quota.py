from fastapi import APIRouter
from src.schemas.quota import Quota
from src.controllers.quota import create_quota, get_quota, update_quota, delete_quota

router = APIRouter()

router.post("/quotas/", response_model=Quota)(create_quota)
router.get("/quotas/{quota_id}", response_model=Quota)(get_quota)
router.put("/quotas/{quota_id}", response_model=Quota)(update_quota)
router.delete("/quotas/{quota_id}")(delete_quota)
