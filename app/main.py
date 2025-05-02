from fastapi import FastAPI
from .routes import camera, dashboard

app = FastAPI()

app.include_router(camera.router, prefix="/camera")
app.include_router(dashboard.router, prefix="/dashboard")

@app.get("/")
def read_root():
    return {"message": "Horus API is running"}
