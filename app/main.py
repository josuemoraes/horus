import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routes import camera, dashboard

app = FastAPI()

static_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "static"))
app.mount("/static", StaticFiles(directory=static_dir), name="static")

app.include_router(camera.router, prefix="/camera")
app.include_router(dashboard.router, prefix="/dashboard")
