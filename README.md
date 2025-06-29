📄 Smart Task Tracker – Backend (Django + DRF)
markdown
Copy
Edit
# 🛠️ Smart Task Tracker – Backend (Django + DRF)

This is the **Django REST Framework backend** for Smart Task Tracker – a full-stack task management system with JWT authentication, project-task nesting, role-based access, and activity logging.

---

## 🚀 Features

- 🔐 JWT Authentication (SimpleJWT)
- 👥 Roles: Admin & Contributor
- 📁 Projects: Create, view, and manage projects
- ✅ Tasks: Assign, update status, track deadlines
- 📜 Activity Log: Tracks last changes to each task
- 🗂️ SQLite by default (can be switched to PostgreSQL)
- 🌐 CORS-enabled for frontend access

---

## 🛠 Tech Stack

- Django
- Django REST Framework
- SimpleJWT
- Gunicorn (for production)
- CORS Headers
- SQLite / PostgreSQL

---

## 🔧 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/YOUR_USERNAME/smart-task-backend.git
cd smart-task-backend
2. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
3. Apply migrations and run
bash
Copy
Edit
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
🔐 API Authentication
Use SimpleJWT:

bash
Copy
Edit
POST /api/token/
{
  "username": "your_user",
  "password": "your_pass"
}
Use the access token in Authorization: Bearer <token> header.

🔗 API Endpoints
Resource	Endpoint
Login Token	/api/token/
Projects	/api/projects/
Tasks	/api/tasks/
Activity Log	/api/logs/
Users	/api/users/ (admin only)

🏁 Deployment Ready (Render)
Includes:

Procfile

requirements.txt

runtime.txt

📜 License
Built for educational/demo purposes only.

csharp
Copy
Edit
