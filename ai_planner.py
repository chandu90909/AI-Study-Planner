from datetime import datetime, timedelta
import os.path

from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# 🔐 Scope
SCOPES = ['https://www.googleapis.com/auth/calendar']


# 🟢 Authenticate with Google
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


# 🧠 Generate Study Plan
def generate_plan(course, days):
    topics = {
        "dsa": [
            "Arrays", "Searching", "Sorting", "Strings",
            "Recursion", "Linked List", "Stack", "Queue",
            "Trees", "Graphs", "Dynamic Programming"
        ],
        "python": [
            "Basics", "Loops", "Functions", "Lists",
            "Dictionaries", "OOP", "File Handling",
            "Modules", "Projects"
        ],
        "web": [
            "HTML", "CSS", "Flexbox", "JavaScript",
            "DOM", "Events", "Responsive Design", "Projects"
        ]
    }

    selected = topics.get(course.lower(), ["Basics", "Practice"])

    tasks = []
    for i in range(days):
        topic = selected[i % len(selected)]
        tasks.append(f"Day {i+1}: Learn {topic}")

    return tasks


# 📅 Add events to Google Calendar
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
            'attendees': [
                {'email': email}
            ],
        }

        service.events().insert(
            calendarId='primary',
            body=event,
            sendUpdates='all'
        ).execute()

        print(f"✅ Added: {task}")

    print("\n🎉 All tasks added to Google Calendar!")


# ▶️ MAIN PROGRAM
if __name__ == "__main__":
    course = input("Enter course name: ")
    weeks = int(input("Enter duration (weeks): "))
    email = input("Enter email to invite: ")

    days = weeks * 7

    service = authenticate()
    tasks = generate_plan(course, days)
    add_to_calendar(service, tasks, email)