# 🚀 Blog Create - Modern FastAPI Blog Platform

A modern blogging platform built using **FastAPI**, **SQLAlchemy**, **SQLite**, and **Jinja2 Templates**. The application provides complete CRUD functionality with image uploads, search, pagination, and a responsive Black + Emerald themed UI.

---

## 🌐 Live Demo

**Deployed Application**

https://blogcreate-cv3k.onrender.com

---

## ✨ Features

### 📝 Blog Management

* Create blog posts
* Edit existing blogs
* Delete blogs
* View complete blog articles
* Responsive blog dashboard

### 🖼 Image Upload Support

* Upload images while creating blogs
* Display featured images on blog cards
* Image preview on blog detail page

### 🔍 Search Functionality

* Search blogs by title
* Dynamic filtering using query parameters

### 📄 Pagination

* Paginated blog listing
* Improved navigation for large collections

### 📅 Blog Metadata

* Author information
* Automatic creation date tracking

### 🎨 Modern User Interface

* Black + Emerald theme
* Glassmorphism-inspired cards
* Smooth hover animations
* Fully responsive design
* Mobile-friendly layout

---

## 🛠 Tech Stack

### Backend

* FastAPI
* SQLAlchemy
* SQLite
* Python

### Frontend

* HTML5
* CSS3
* Jinja2 Templates

### Additional Features

* Image Upload Handling
* Static File Serving
* Search Engine
* Pagination System

---

## 📁 Project Structure

```text
BlogCreate/
│
├── backend.py
├── requirements.txt
├── blog.db
│
├── uploads/
│
├── frontend/
│   ├── base.html
│   ├── index.html
│   ├── create_blog.html
│   ├── edit_blog.html
│   ├── view_blog.html
│   └── delete_blog.html
│
├── static/
│   └── style.css
│
└── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/Sanchit-Agalave27/BlogCreate.git
cd BlogCreate
```

### Create Virtual Environment

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### Linux / macOS

```bash
python -m venv venv
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 📦 Requirements

```txt
fastapi==0.116.1
uvicorn==0.35.0
jinja2==3.1.6
sqlalchemy==2.0.43
python-multipart==0.0.20
pillow==10.4.0
```

---

## ▶️ Run Locally

```bash
uvicorn backend:app --reload
```

Open:

```text
http://127.0.0.1:8000
```

---

## 📌 Available Routes

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
| /test        | GET    | API Health Check    |

---

## 🗄 Database Model

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

## 🚀 Deployment

This application is deployed on Render.

Live URL:

https://blogcreate-27uk.onrender.com

Deployment command:

```bash
uvicorn backend:app --host 0.0.0.0 --port $PORT
```

---

## 🎯 Learning Outcomes

This project demonstrates:

* FastAPI Development
* CRUD Operations
* SQLAlchemy ORM
* SQLite Integration
* Dependency Injection
* File Upload Handling
* Static File Serving
* Search Implementation
* Pagination Logic
* Jinja2 Template Rendering
* Responsive UI Design
* Cloud Deployment using Render

---

## 📸 Key Features Showcase

✅ Create Blogs

✅ Upload Images

✅ Search Blogs

✅ Pagination

✅ Edit & Delete Posts

✅ Responsive Design

✅ Dark Modern UI

✅ Render Deployment

---

## 👨‍💻 Author

**Sanchit Agalave**

GitHub:
https://github.com/Sanchit-Agalave27

Project Repository:
https://github.com/Sanchit-Agalave27/BlogCreate

Live Demo:
https://blogcreate-cv3k.onrender.com

---

⭐ If you found this project useful, consider starring the repository.
