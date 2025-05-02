from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import Detection

router = APIRouter()

@router.post("/detect")
async def detect(request: Request, db: Session = Depends(get_db)):
    data = await request.json()

    detection = Detection(
        camera_id=data.get("camera_id", "desconhecida"),
        face_id=data.get("face_id", "anonimo"),
        duration=data.get("duration", 0)
    )

    db.add(detection)
    db.commit()
    db.refresh(detection)

    return {
        "message": "Detecção salva com sucesso",
        "id": detection.id,
        "timestamp": str(detection.timestamp)
    }
