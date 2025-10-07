# **Mentorship-matching-API-Capstone-project**
## 📌 Overview of the project

The **Mentorship Matching API** is a Django REST Framework (DRF)-based backend application designed to connect **mentors** and **mentees** based on shared skills and learning interests.  
It enables mentees to search for mentors by skill, send mentorship requests, and allows mentors to accept or decline those requests — creating a simple and efficient mentorship-matching system.

This project is built as part of the **ALX Backend Engineering Capstone Project**.


## 🎯 Project Objectives
- Implement a RESTful API using Django and Django REST Framework (DRF)
- Manage user roles (Mentor and Mentee)
- Enable skill-based mentor search
- Handle mentorship requests between users
- Secure all endpoints using Token Authentication
- Demonstrate understanding of database relationships and API development best practices

---

## 🧩 Entity Relationship Diagram (ERD)
**Relationships Overview:**
- One `User` can be both a mentor and a mentee.
- A `User` can have many `Skills` (Many-to-Many relationship through `ProfileSkill`).
- A `MentorshipRequest` connects one mentee to one mentor for a specific skill.


---

## 🚀 Features
### 👤 User Management
- Register and authenticate users
- Assign roles (mentor/mentee)
- Update user profiles

### 🧠 Skills Management
- Create and list available skills
- Associate users with skills and proficiency levels

### 🤝 Mentorship Requests
- Mentees can send mentorship requests to mentors
- Mentors can accept or decline requests
- View active mentorships and request history

### 🔍 Search Functionality
- Filter mentors by skill (`/api/mentors/?skill=Python`)

---

## ⚙️ Technologies Used
- **Python 3**
- **Django 5+**
- **Django REST Framework**
- **SQLite3** (default database)
- **Token Authentication (DRF)**

---

## 🛠️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Pochere/Mentorship-matching-API-Capstone-project.git
cd Mentorship-matching-API-Capstone-project


