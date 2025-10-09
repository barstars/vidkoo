from fastapi import APIRouter

from app.apis.api.auth.sign_up import router as register

router  = APIRouter()

router.include_router(register, tags=["register"])