from flask import Flask, render_template, request
from datetime import datetime, timedelta
import os.path

from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

app = Flask(__name__)

SCOPES = ['https://www.googleapis.com/auth/calendar']


# 🔐 Authenticate
def authenticate():
    creds = None

    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    if not creds or not creds.valid:
        flow = InstalledAppFlow.from_client_secrets_file(
            'credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)

        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    return build('calendar', 'v3', credentials=creds)


# 🧠 Generate plan
def generate_plan(course, days):
    topics = {
        "dsa": ["Arrays", "Sorting", "Trees", "Graphs"],
        "python": ["Basics", "Loops", "OOP", "Projects"]
    }

    selected = topics.get(course.lower(), ["Basics"])

    tasks = []
    for i in range(days):
        topic = selected[i % len(selected)]
        tasks.append(f"Day {i+1}: {topic}")

    return tasks


# 📅 Add to calendar
def add_to_calendar(service, tasks, email):
    start_date = datetime.now()

    for i, task in enumerate(tasks):
        event_date = start_date + timedelta(days=i)

        event = {
            'summary': task,
            'start': {
                'dateTime': (event_date + timedelta(hours=9)).isoformat(),
                'timeZone': 'Asia/Kolkata',
            },
            'end': {
                'dateTime': (event_date + timedelta(hours=10)).isoformat(),
                'timeZone': 'Asia/Kolkata',
            },
            'attendees': [{'email': email}],
        }

        service.events().insert(
            calendarId='primary',
            body=event,
            sendUpdates='all'
        ).execute()


# 🌐 Route
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        course = request.form["course"]
        weeks = int(request.form["weeks"])
        email = request.form["email"]

        days = weeks * 7

        service = authenticate()
        tasks = generate_plan(course, days)
        add_to_calendar(service, tasks, email)

        return render_template("index.html", message="✅ Plan added to calendar!")

    return render_template("index.html", message="")


# ▶️ Run
if __name__ == "__main__":
    app.run(debug=True)