# Django Authentication System

<p align="center">
<img src="https://img.shields.io/badge/Python-3.12-blue">
<img src="https://img.shields.io/badge/Django-5.0-green">
<img src="https://img.shields.io/badge/License-MIT-yellow">
<img src="https://img.shields.io/badge/Project-Active-success">
</p>

---

## 📌 Project Description

A complete authentication system built with Django.  
This project includes user registration, login, logout and profile management.

The project demonstrates a clean Django project structure with reusable templates and modern UI using Tailwind CSS.

---

## ✨ Features

- User Registration
- Secure Login System
- Logout System
- Profile Page
- Profile Image Upload
- Custom User Model
- Django Messages Framework
- Tailwind CSS UI
- Responsive Navbar

---

## 📸 Project Preview

![Project Preview](media/Full_page.jpeg)

---

## 🛠 Technologies Used

- Python
- Django
- Tailwind CSS
- HTML
- SQLite
- Git
- GitHub

---

## 📁 Project Structure

```
Class-48
│
├── accounts
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── tests.py
│   ├── migrations
│   └── __pycache__
│
├── auth_project
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── templates
│   ├── accounts
│   │   ├── index.html
│   │   ├── login.html
│   │   ├── register.html
│   │   └── profile_page.html
│   │
│   └── includes
│       ├── header.html
│       └── footer.html
│
├── static
│
├── media
│   ├── profile
│   └── Full_page.jpeg
│
├── manage.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙ Installation

Clone Repository

```
git clone https://github.com/officialontar/Class-48.git
```

Go to Project Folder

```
cd Class-48
```

Create Virtual Environment

```
python -m venv .venv
```

Activate Environment

```
.venv\Scripts\activate
```

Install Dependencies

```
pip install -r requirements.txt
```

Run Migrations

```
python manage.py migrate
```

Run Server

```
python manage.py runserver
```

---

## 👨‍💻 Author

Sakib Khan  

GitHub  
https://github.com/officialontar

---

## ⭐ Project Status

This is a learning project for building Django authentication systems.