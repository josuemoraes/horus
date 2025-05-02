from fastapi import APIRouter
from datetime import datetime

router = APIRouter()

@router.post("/detect")
def receive_detection(data: dict):
    # Aqui você vai inserir no banco real
    return {"status": "received", "data": data}
