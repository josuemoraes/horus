from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import os

from .routes import camera, dashboard

app = FastAPI()

# ⬇️ ESSA LINHA É ESSENCIAL
app.mount("/static", StaticFiles(directory="app/static"), name="static")

app.include_router(camera.router, prefix="/camera")
app.include_router(dashboard.router, prefix="/dashboard")

@app.get("/")
def read_root():
    return {"message": "Horus is running"}
