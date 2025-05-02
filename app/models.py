from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from .database import Base

class Detection(Base):
    __tablename__ = "detections"

    id = Column(Integer, primary_key=True, index=True)
    camera_id = Column(String, index=True)
    face_id = Column(String, index=True)
    duration = Column(Integer)
    timestamp = Column(DateTime, default=datetime.utcnow)
