from models import Event

# In-memory list to store events
event_list = []

# Add Event
def add_event(event: Event):
    event_list.append(event)
    return event

# Get All Events
def get_all_events():
    return event_list

# Remove Event by ID
def remove_event(event_id: int):
    global event_list
    event_list = [event for event in event_list if event.id != event_id]
    return {"message": "Event removed successfully"}