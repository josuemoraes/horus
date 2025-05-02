import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pathlib import Path

from .routes import camera, dashboard

app = FastAPI()

# Caminho absoluto da pasta 'static' dentro de 'app'
static_dir = str(Path(__file__).parent / "static")

# Monta a rota para arquivos estáticos
app.mount("/static", StaticFiles(directory=static_dir), name="static")

# Rotas da API
app.include_router(camera.router, prefix="/camera")
app.include_router(dashboard.router, prefix="/dashboard")

# Rota opcional para teste (ver se o path está correto)
@app.get("/test-path")
def show_static_path():
    return {"static_dir": static_dir}
