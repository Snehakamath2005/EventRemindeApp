from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from models import Event
import events

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def intro(request: Request):
    return templates.TemplateResponse("intro.html", {"request": request})


@app.get("/home", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Add Event Route
@app.post("/events")
def add_new_event(event: Event):
    return events.add_event(event)

# View All Events Route
@app.get("/events")
def view_all_events():
    return events.get_all_events()

# Delete Event Route
@app.delete("/events/{event_id}")
def delete_event(event_id: int):
    if not any(e.id == event_id for e in events.get_all_events()):
        raise HTTPException(status_code=404, detail="Event not found")
    return events.remove_event(event_id)
