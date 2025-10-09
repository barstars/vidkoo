import os

from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse

router = APIRouter(tags=["load_page"])

@router.get("/{path:path}")
async def load_page(path: str):
	if(path.startswith("api")):
		print("api")
		raise HTTPException(status_code=404)

	if(path == ""):
		path = "home"

	if(path[-1] == "/"):
		path = path[:len(path)-1]

	file_path = "front/"+path+"/index.html"

	if(not os.path.exists(file_path)):
		raise HTTPException(status_code=404)

	return FileResponse(file_path)