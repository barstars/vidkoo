# 5432
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.apis.router import router as apiRouter
from app.static_controller.load_page import router as load_page


app = FastAPI()

app.include_router(apiRouter, prefix="/api", tags=["api"])

app.mount("/static", StaticFiles(directory="front"), name="static")
app.include_router(load_page)