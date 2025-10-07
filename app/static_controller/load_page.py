from fastapi import APIRouter, HTTPException

router = APIRouter(tags=["load_page"])

@router.get("/{path:path}")
async def load_page(path: str):
	if(path.startswith("api")):
		raise HTTPException(status_code=404)

	if(path == "" or path == "home" or path == "home/"):
		return {"path":"home!!!"}
	return {"path":path}