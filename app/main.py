from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import os

from .routes import camera, dashboard

app = FastAPI()

# Rotas da API
app.include_router(camera.router, prefix="/camera")
app.include_router(dashboard.router, prefix="/dashboard")

# Servir arquivos estáticos
app.mount("/static", StaticFiles(directory="app/static"), name="static")

@app.get("/")
def read_root():
    return {"message": "Horus API is running"}
