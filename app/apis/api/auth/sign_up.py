from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter(prefix="/auth/sign_up",tags=["sign_up"])

@router.get("")
async def function():
	return JSONResponse(status_code=200, content={"message":"success"})