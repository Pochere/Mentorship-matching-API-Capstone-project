# 🧩 **Mentorship Matching API (Capstone Project)**  

## 📌 Overview
The **Mentorship Matching API** is a Django REST Framework (DRF)-based backend system that connects **mentors** and **mentees** based on shared skills, interests, and learning goals.  
It enables mentees to discover mentors, schedule sessions, and build meaningful mentorship relationships — all through a secure, token-authenticated REST API.

This project was developed as part of the **ALX Backend Engineering Capstone Project**.

---

## 🎯 **Project Objectives**
- Develop a **RESTful API** using Django & Django REST Framework  
- Manage user roles (**Mentor** and **Mentee**)  
- Enable mentorship session creation and tracking  
- Implement **secure token-based authentication**  
- Demonstrate mastery of **database relationships** and **API design principles**

---

## 🧠 **Entity Relationship Overview**
- Each `User` can act as both a **Mentor** and a **Mentee**.  
- A `Mentor` can have multiple `MentorshipSessions`.  
- A `Mentee` can have multiple `MentorshipSessions`.  
- Each `MentorshipSession` connects one mentor to one mentee with a defined topic, date, and time.

---
## 🚀 **Key Features**
### 👥 User Management
- Register and authenticate users via token authentication  
- Create, update, and manage user profiles  
- Manage roles as **mentor** or **mentee**

### 🧑‍🏫 Mentorship Management
- Create and manage mentor and mentee profiles  
- Schedule mentorship sessions  
- Mark sessions as complete or pending  
- Admin panel for managing users and sessions

### 🔐 Authentication
- User registration and login using **Token Authentication**
- Protected API routes accessible only to authenticated users

---

## ⚙️ **Tech Stack**
- **Python 3.12+**
- **Django 5+**
- **Django REST Framework**
- **SQLite3** (default database)
- **DRF Token Authentication**

---

## 🛠️ **Setup Instructions**

### 1. Clone the Repository
```bash
git clone https://github.com/Pochere/Mentorship-matching-API-Capstone-project.git
cd Mentorship-matching-API-Capstone-project

### 2. Create and Activate a Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate        # On Windows
# OR
source venv/bin/activate     # On Mac/Linux

### 3. Install Dependencies
    bash
pip install -r requirements.txt

### 4. Apply Migrations
    bash
python manage.py makemigrations
python manage.py migrate

### 5. Create a Superuser
    bash
python manage.py createsuperuser

### 6. Run Development Server
    bash
python manage.py runserver

Access the app at 👉 http://127.0.0.1:8000/

### 7. Authentication Endpoints
    bash
POST   /api/auth/register/       -> Register a new user
POST   /api/auth/login/          -> Login user and receive authentication token

### 8. Core API Endpoints
    bash
GET / POST     api/mentors/             -> List or create mentors
GET / POST     api/mentees/             -> List or create mentees
GET / POST     api/sessions/            -> List or create mentorship sessions
PUT / PATCH / DELETE  /api/sessions/{id}/ -> Update or delete a session

### Example API Usage
**Register a User**
bash
curl -X POST http://127.0.0.1:8000/api/auth/register/ \
     -H "Content-Type: application/json" \
     -d '{"username":"pauline","password":"Test12345","email":"pauline@example.com"}'

**Login User**
bash
curl -X POST http://127.0.0.1:8000/api/auth/login/ \
     -H "Content-Type: application/json" \
     -d '{"username":"pauline","password":"Test12345"}'

**Create a Mentor Profile**
bash
curl -X POST http://127.0.0.1:8000/api/mentors/ \
     -H "Content-Type: application/json" \
     -H "Authorization: Token YOUR_TOKEN_HERE" \
     -d '{"user":1,"bio":"Experienced business strategist","expertise":"Business Management","availability":true}'

**Create a Mentorship Session**
bash
curl -X POST http://127.0.0.1:8000/api/sessions/ \
     -H "Content-Type: application/json" \
     -H "Authorization: Token YOUR_TOKEN_HERE" \
     -d '{"mentor":1,"mentee":1,"topic":"Business growth planning","date":"2025-10-16","time":"10:00:00","status":"scheduled"}'

***Admin Dashboard***
curl -X POST http://127.0.0.1:8000/api/sessions/ \
     -H "Content-Type: application/json" \
     -H "Authorization: Token YOUR_TOKEN_HERE" \
     -d '{"mentor":1,"mentee":1,"topic":"Business growth planning","date":"2025-10-16","time":"10:00:00","status":"scheduled"}'


# Deployment
     Used **pythonanywhere** to deploy my Mentorship matching API and the URL is as below:

    pochere.pythonanywhere.com and below are the API endpoints:

    Purpose	        Method	         URL
 🔐 Admin Dashboard 	—	     https://pochere.pythonanywhere.com/admin/

 🧭 API Root	       GET	     https://pochere.pythonanywhere.com/api/

👤 Register User	  POST	     https://pochere.pythonanywhere.com/api/auth/register/

🔑 Login User	      POST     	 https://pochere.pythonanywhere.com/api/auth/login/

🧑‍🏫 Mentors	        GET / POST	https://pochere.pythonanywhere.com/api/mentors/

👩‍🎓 Mentees	        GET / POST	https://pochere.pythonanywhere.com/api/mentees/

🗓️ Mentorship Sessions	GET / POST	https://pochere.pythonanywhere.com/api/sessions/

✏️ Update/Delete Session	PUT / PATCH / DELETE	https://pochere.pythonanywhere.com/api/sessions/{id}/

---

## 🔐 Authentication Note

When accessing the API endpoints (for example, [https://pochere.pythonanywhere.com/api/mentors/](https://pochere.pythonanywhere.com/api/mentors/)),  
you may see a message like this:

```json
{
    "detail": "Authentication credentials were not provided."
}
This means the API is working correctly but requires authentication.
Only registered and logged-in users with valid tokens can make requests such as POST, PUT, or DELETE.

If you only want to view or test the admin interface, you can log in through:

👉 https://pochere.pythonanywhere.com/admin/
