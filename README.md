📅 Event Reminder App
A simple Event Reminder web application built with FastAPI, HTML/CSS, and JavaScript. This app lets you:

✅ Add events with title, date, time, and description
✅ View upcoming events
✅ Delete events
✅ Countdown to the next upcoming event
✅ Basic search and mark events as completed

🚀 Features
Add, view, and delete events
Countdown timer for next event
Mark events as completed (visual strike-through)
Search/filter events by title
Responsive UI with background image
Intro/Landing page before event management

🛠️ Tech Stack
Backend: FastAPI
Frontend: HTML, CSS, JavaScript
Templating: Jinja2
Static files: Managed via FastAPI

⚙️ Setup Instructions
1. Clone the Repository
git clone "url"
cd EventRemindeApp

2. Install Dependencies
Make sure you have Python 3.11 or newer:
pip install -r requirements.txt

3. Run the Application
uvicorn main:app --reload
Visit the app at:
http://127.0.0.1:8000

📂 Project Structure
EventRemindeApp/
├── main.py              # FastAPI main server file
├── events.py            # Event logic functions
├── models.py            # Event model definition
├── templates/
│   ├── index.html       # Main frontend page
│   └── intro.html       # Optional landing page
├── static/
│   ├── style.css        # CSS styles
│   ├── background.jpg   # Background image
├── requirements.txt     # Project dependencies
└── README.md            # This file


💡 Future Enhancements
Email reminders with SMTP
Edit/Update events
Add categories for events
Mobile-friendly improvements