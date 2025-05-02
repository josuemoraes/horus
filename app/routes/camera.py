from fastapi import APIRouter, Request
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import Detection
from datetime import datetime

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/detect")
async def receive_detection(request: Request):
    data = await request.json()

    db: Session = next(get_db())

    detection = Detection(
        camera_id=data.get("camera_id", "unknown"),
        face_id=data.get("face_id", "anon"),
        timestamp=datetime.utcnow(),
        duration=data.get("duration", 0)
    )
    db.add(detection)
    db.commit()
    db.refresh(detection)

    return {"status": "saved", "id": detection.id}
