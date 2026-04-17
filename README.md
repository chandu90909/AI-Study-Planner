# 🚀 AI Study Planner with Google Calendar Integration

## 📌 Overview

AI Study Planner is a web-based application that generates a personalized study plan based on the course and duration provided by the user.
It automatically schedules tasks into Google Calendar and sends event invitations via email.

---

## ✨ Features

* 📘 Generate structured study plans
* 📅 Automatic Google Calendar integration
* 📩 Email invitation support for events
* 🌐 Clean and responsive web interface
* ⚡ Fully automated workflow (no manual scheduling)

---

## 🛠️ Tech Stack

* **Frontend:** HTML, CSS
* **Backend:** Flask (Python)
* **API:** Google Calendar API
* **Authentication:** OAuth 2.0

---

## 📂 Project Structure

```
Task_Planner_Web/
│── app.py
│── ai_planner.py
│── templates/
│     └── index.html
│── .gitignore
│── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```
git clone https://github.com/chandu90909/AI-Study-Planner.git
cd AI-Study-Planner
```

---

### 2. Install dependencies

```
pip install flask google-api-python-client google-auth google-auth-oauthlib
```

---

### 3. Google API Setup

1. Go to Google Cloud Console
2. Create a project
3. Enable **Google Calendar API**
4. Create OAuth credentials (Desktop App)
5. Download `credentials.json`
6. Place it in the project folder

---

### 4. Run the application

```
python app.py
```

---

### 5. Open in browser

```
http://127.0.0.1:5000
```

---

## 📸 Output

* Users enter course, duration, and email
* Study plan is generated
* Events are added to Google Calendar
* Email invitations are sent

---

## 🚀 Future Enhancements

* ⏰ Custom time slots selection
* 🔔 Reminder notifications
* 🌙 Dark mode UI
* 🌐 Deployment (public web app)
* 🧠 Real AI-based planning using LLM

---

## 👨‍💻 Author

**Chalapathi Kommuru**

---

## ⭐ If you like this project

Give it a star on GitHub ⭐
