from pydantic import BaseModel

class Event(BaseModel):
    id: int
    title: str
    date: str   # Format: YYYY-MM-DD
    time: str   # Format: HH:MM
    description: str