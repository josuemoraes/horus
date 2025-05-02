import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from .routes import camera, dashboard

app = FastAPI()

# Caminho absoluto correto para a pasta static dentro de app
current_dir = os.path.dirname(os.path.abspath(__file__))
static_dir = os.path.join(current_dir, "static")

app.mount("/static", StaticFiles(directory=static_dir), name="static")

app.include_router(camera.router, prefix="/camera")
app.include_router(dashboard.router, prefix="/dashboard")
