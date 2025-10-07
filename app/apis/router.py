from fastapi import APIRouter

from app.apis.api.auth.sign_up import router as register

router  = APIRouter(tags=["api"])

router.include_router(register)