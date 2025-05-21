# 🎓 Campus Management System (Django)

A web-based Campus Management System for managing Students, Teachers, and Admins with roles, authentication, course enrollment, assignment submissions, results, REST APIs, and more.

---

## 🚀 Features

- 👤 User Roles: Student, Teacher, Admin
- 🔐 Authentication & Role-Based Access
- 📚 Course Management & Enrollment
- 📝 Assignment Upload & Grading
- 📊 Result Display
- 🔁 Custom Middleware & Signals
- 📩 Console Email Notifications
- ⚙️ Django Admin Customization
- 🌐 REST APIs with Token Authentication
- 🧪 Unit Tests for Models, Views, APIs

---

## 🏗️ Tech Stack

- Python 3.x
- Django
- Django REST Framework
  
- HTML/CSS/Bootstrap (Templates)

---

## 📦 Installation

```bash
git clone https://github.com/yourusername/campus-management-system.git
cd campus-management-system/campus_mgmt
python -m venv env
source env/bin/activate  # For Windows: env\Scripts\activate

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
