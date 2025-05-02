import os
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI
from .routes import camera, dashboard

app = FastAPI()

# ⬇️ Caminho absoluto corrigido
static_dir = os.path.join(os.path.dirname(__file__), "static")
app.mount("/static", StaticFiles(directory=static_dir), name="static")

app.include_router(camera.router, prefix="/camera")
app.include_router(dashboard.router, prefix="/dashboard")
