from fastapi import APIRouter
from models.quota import QuotaOut
from src.controllers.quota import create_quota, get_quota, update_quota, delete_quota

router = APIRouter()

router.post("/quotas/", response_model=QuotaOut)(create_quota)
router.get("/quotas/{quota_id}", response_model=QuotaOut)(get_quota)
router.put("/quotas/{quota_id}", response_model=QuotaOut)(update_quota)
router.delete("/quotas/{quota_id}")(delete_quota)
