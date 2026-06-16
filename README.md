# 🚀 BlogCreate - FastAPI Blog Platform

A modern full-stack blogging platform built with **FastAPI**, **SQLAlchemy**, **SQLite**, and **Jinja2**.

BlogSpace allows users to create, edit, search, and manage blog posts with image uploads, pagination, and a modern Black + Emerald user interface.

---

# ✨ Features

### 📝 Blog Management

* Create blog posts
* Edit existing blogs
* Delete blogs
* Read full blog articles
* View all blog posts

### 🖼 Media Support

* Upload images for blogs
* Automatic image display on blog cards
* Featured image support on blog pages

### 🔍 Search

* Search blogs by title
* Instant filtering through query parameters

### 📄 Pagination

* Paginated blog listing
* Improved browsing experience
* Faster page loading

### 📅 Post Metadata

* Automatic created date
* Author information

### 🎨 Modern UI

* Black + Emerald color theme
* Responsive design
* Glassmorphism-inspired cards
* Mobile-friendly layout
* Smooth hover animations

---

# 🛠 Tech Stack

## Backend

* FastAPI
* SQLAlchemy
* SQLite
* Python

## Frontend

* HTML5
* CSS3
* Jinja2 Templates

## Additional Features

* Static File Serving
* Image Upload Handling
* Pagination Logic
* Search Functionality

---

# 📁 Project Structure

```text
BlogCreate/
│
├── backend.py
├── requirements.txt
├── blog.db
│
├── uploads/
│   └── uploaded_images
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

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/Sanchit-Agalave27/BlogCreate.git
cd BlogCreate
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python -m venv venv
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 📦 Requirements

```txt
fastapi==0.116.1
uvicorn==0.35.0
jinja2==3.1.6
sqlalchemy==2.0.43
python-multipart==0.0.20
pillow==10.4.0
```

---

# ▶️ Run the Application

```bash
uvicorn backend:app --reload
```

Open:

```text
http://127.0.0.1:8000
```

---

# 📌 Available Routes

| Route        | Method | Description         |
| ------------ | ------ | ------------------- |
| /            | GET    | Home Page           |
| /create      | GET    | Create Blog Page    |
| /create      | POST   | Create Blog         |
| /blog/{id}   | GET    | View Blog           |
| /edit/{id}   | GET    | Edit Blog Page      |
| /edit/{id}   | POST   | Update Blog         |
| /delete/{id} | GET    | Delete Confirmation |
| /delete/{id} | POST   | Delete Blog         |
| /test        | GET    | API Test Route      |

---

# 🗄 Database Model

```python
class Blog(Base):
    __tablename__ = "blogs"

    id: int
    title: str
    author: str
    content: str
    image_path: str
    created_at: datetime
```

---

# 🔥 Highlights

* Image Upload Support
* Search Functionality
* Pagination System
* Responsive Design
* Dark Theme UI
* SQLite Database
* SQLAlchemy ORM
* FastAPI Backend
* Jinja2 Templating

---

# 🚀 Deployment

This project can be deployed on:

* Render
* Railway
* Fly.io
* VPS Servers
* Docker Containers

Example:

```bash
uvicorn backend:app --host 0.0.0.0 --port $PORT
```

---

# 🎯 Learning Outcomes

This project demonstrates:

* FastAPI Fundamentals
* CRUD Operations
* SQLAlchemy ORM
* SQLite Integration
* Dependency Injection
* File Upload Handling
* Static File Serving
* Search Implementation
* Pagination Implementation
* Template Rendering with Jinja2
* Responsive UI Design

---

# 👨‍💻 Author

Sanchit Agalave

GitHub:
https://github.com/Sanchit-Agalave27

---

⭐ If you found this project useful, consider starring the repository.

