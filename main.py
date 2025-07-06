from fastapi import FastAPI, Request, HTTPException, Depends
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from database import SessionLocal, engine
from models import Event, EventDB
import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Dependency for DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Intro page
@app.get("/", response_class=HTMLResponse)
def intro(request: Request):
    return templates.TemplateResponse("intro.html", {"request": request})

# Main app page
@app.get("/home", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Add event to DB
@app.post("/events")
def add_event(event: Event, db: Session = Depends(get_db)):
    db_event = EventDB(**event.dict())
    db.add(db_event)
    db.commit()
    return {"message": "Event added"}

# Get all events
@app.get("/events")
def get_events(db: Session = Depends(get_db)):
    return db.query(EventDB).all()

# Delete event
@app.delete("/events/{event_id}")
def delete_event(event_id: int, db: Session = Depends(get_db)):
    event = db.query(EventDB).filter(EventDB.id == event_id).first()
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    db.delete(event)
    db.commit()
    return {"message": "Event deleted"}
