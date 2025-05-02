from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()

class Detection(Base):
    __tablename__ = "detections"
    id = Column(Integer, primary_key=True, index=True)
    camera_id = Column(String)
    face_id = Column(String)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
    duration = Column(Integer)
