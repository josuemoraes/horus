from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import Detection

router = APIRouter()

@router.get("/")
def list_detections(db: Session = Depends(get_db)):
    detections = db.query(Detection).order_by(Detection.timestamp.desc()).limit(100).all()
    return [
        {
            "id": d.id,
            "camera_id": d.camera_id,
            "face_id": d.face_id,
            "duration": d.duration,
            "timestamp": d.timestamp.isoformat()
        }
        for d in detections
    ]
