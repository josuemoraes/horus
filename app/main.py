import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from .routes import camera, dashboard

app = FastAPI()

# 🗂 Caminho correto para pasta static dentro de app/
base_dir = os.path.dirname(os.path.abspath(__file__))
static_dir = os.path.join(base_dir, "static")

# 📂 Serve arquivos estáticos na rota /static/
app.mount("/static", StaticFiles(directory=static_dir), name="static")

# 🔁 Rotas da aplicação
app.include_router(camera.router, prefix="/camera")
app.include_router(dashboard.router, prefix="/dashboard")
