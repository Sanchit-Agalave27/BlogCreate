# 🚀 FastAPI Blog CRUD Application

A modern Blog Management System built with **FastAPI**, **SQLAlchemy**, **SQLite**, and **Jinja2 Templates**. This project demonstrates complete CRUD (Create, Read, Update, Delete) operations with a clean and responsive user interface.

## ✨ Features

* Create new blog posts
* View all blog posts
* Read individual blog articles
* Edit existing blogs
* Delete blogs
* SQLite database integration
* SQLAlchemy ORM
* Jinja2 template rendering
* Responsive modern UI
* Glassmorphism-inspired design

---

## 🛠️ Tech Stack

### Backend

* FastAPI
* SQLAlchemy
* SQLite
* Python

### Frontend

* HTML5
* CSS3
* Jinja2 Templates

---

## 📁 Project Structure

```text
BlogCreate/
│
├── backend.py
├── requirements.txt
├── blog.db
│
├── frontend/
│   ├── base.html
│   ├── index.html
│   ├── create_blog.html
│   ├── edit_blog.html
│   ├── view_blog.html
│   └── delete_blog.html
│
└── static/
    └── style.css
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/Sanchit-Agalave27/BlogCreate.git
cd BlogCreate
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

#### Windows

```bash
venv\Scripts\activate
```

#### macOS/Linux

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
uvicorn backend:app --reload
```

Open your browser and visit:

```text
http://127.0.0.1:8000
```

---

## 📌 Available Routes

| Route          | Method | Description         |
| -------------- | ------ | ------------------- |
| `/`            | GET    | View all blogs      |
| `/create`      | GET    | Create blog page    |
| `/create`      | POST   | Create a new blog   |
| `/blog/{id}`   | GET    | View a blog         |
| `/edit/{id}`   | GET    | Edit blog page      |
| `/edit/{id}`   | POST   | Update blog         |
| `/delete/{id}` | GET    | Delete confirmation |
| `/delete/{id}` | POST   | Delete blog         |
| `/test`        | GET    | API test route      |

---

## 🗄️ Database

The application uses SQLite as the database and SQLAlchemy as the ORM.

### Blog Model

```python
class Blog(Base):
    __tablename__ = "blogs"

    id: int
    title: str
    author: str
    content: str
```

---

## 🎯 Learning Objectives

This project demonstrates:

* FastAPI fundamentals
* CRUD operations
* SQLAlchemy ORM
* SQLite database integration
* Dependency Injection
* Jinja2 Templates
* Static file handling
* Responsive frontend development

---

## 📜 License

This project is open-source and available for educational and personal use.

---

## 👨‍💻 Author

**Sanchit Agalave**

GitHub: https://github.com/Sanchit-Agalave27
