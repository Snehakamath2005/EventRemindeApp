from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from database import Base

# Pydantic model for request/response
class Event(BaseModel):
    id: int
    title: str
    date: str
    time: str
    description: str = None

# SQLAlchemy model for DB table
class EventDB(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    date = Column(String, nullable=False)
    time = Column(String, nullable=False)
    description = Column(String)
