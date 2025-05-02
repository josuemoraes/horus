import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from .routes import camera, dashboard

app = FastAPI()

# Caminho absoluto para a pasta 'static' dentro da pasta 'app'
current_dir = os.path.dirname(os.path.abspath(__file__))
static_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "static")

# Montar os arquivos estáticos
app.mount("/static", StaticFiles(directory=static_dir), name="static")

# Rotas principais
app.include_router(camera.router, prefix="/camera")
app.include_router(dashboard.router, prefix="/dashboard")

# (Opcional) Rota para testar o caminho dos arquivos estáticos
@app.get("/test-path")
def show_static_path():
    return {"static_dir": static_dir}
