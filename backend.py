from fastapi import FastAPI, Request, Form, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from sqlalchemy import create_engine, String, Text, select
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
    sessionmaker,
    Session
)

# ==========================================
# DATABASE SETUP
# ==========================================

engine = create_engine(
    "sqlite:///blog.db",
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

class Base(DeclarativeBase):
    pass


class Blog(Base):
    __tablename__ = "blogs"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(200))
    author: Mapped[str] = mapped_column(String(100))
    content: Mapped[str] = mapped_column(Text)


Base.metadata.create_all(bind=engine)

# ==========================================
# FASTAPI
# ==========================================

app = FastAPI()

# NEW
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="frontend")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ==========================================
# HOME
# ==========================================

@app.get("/", response_class=HTMLResponse)
def home_page(
    request: Request,
    db: Session = Depends(get_db)
):
    blogs = db.scalars(select(Blog)).all()

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "blogs": blogs
        }
    )

# ==========================================
# CREATE PAGE
# ==========================================

@app.get("/create", response_class=HTMLResponse)
def create_page(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="create_blog.html",
        context={}
    )

# ==========================================
# CREATE BLOG
# ==========================================

@app.post("/create")
def create_blog(
    title: str = Form(...),
    author: str = Form(...),
    content: str = Form(...),
    db: Session = Depends(get_db)
):

    blog = Blog(
        title=title,
        author=author,
        content=content
    )

    db.add(blog)
    db.commit()

    return RedirectResponse(
        url="/",
        status_code=303
    )

# ==========================================
# VIEW BLOG
# ==========================================

@app.get("/blog/{blog_id}", response_class=HTMLResponse)
def view_blog(
    request: Request,
    blog_id: int,
    db: Session = Depends(get_db)
):

    blog = db.get(Blog, blog_id)

    if not blog:
        return HTMLResponse(
            "<h1>Blog Not Found</h1>",
            status_code=404
        )

    return templates.TemplateResponse(
        request=request,
        name="view_blog.html",
        context={
            "blog": blog
        }
    )

# ==========================================
# EDIT PAGE
# ==========================================

@app.get("/edit/{blog_id}", response_class=HTMLResponse)
def edit_page(
    request: Request,
    blog_id: int,
    db: Session = Depends(get_db)
):

    blog = db.get(Blog, blog_id)

    if not blog:
        return HTMLResponse(
            "<h1>Blog Not Found</h1>",
            status_code=404
        )

    return templates.TemplateResponse(
        request=request,
        name="edit_blog.html",
        context={
            "blog": blog
        }
    )

# ==========================================
# UPDATE BLOG
# ==========================================

@app.post("/edit/{blog_id}")
def update_blog(
    blog_id: int,
    title: str = Form(...),
    author: str = Form(...),
    content: str = Form(...),
    db: Session = Depends(get_db)
):

    blog = db.get(Blog, blog_id)

    if blog:
        blog.title = title
        blog.author = author
        blog.content = content
        db.commit()

    return RedirectResponse(
        url="/",
        status_code=303
    )

# ==========================================
# DELETE PAGE
# ==========================================

@app.get("/delete/{blog_id}", response_class=HTMLResponse)
def delete_page(
    request: Request,
    blog_id: int,
    db: Session = Depends(get_db)
):

    blog = db.get(Blog, blog_id)

    if not blog:
        return HTMLResponse(
            "<h1>Blog Not Found</h1>",
            status_code=404
        )

    return templates.TemplateResponse(
        request=request,
        name="delete_blog.html",
        context={
            "blog": blog
        }
    )

# ==========================================
# DELETE BLOG
# ==========================================

@app.post("/delete/{blog_id}")
def delete_blog(
    blog_id: int,
    db: Session = Depends(get_db)
):

    blog = db.get(Blog, blog_id)

    if blog:
        db.delete(blog)
        db.commit()

    return RedirectResponse(
        url="/",
        status_code=303
    )

# ==========================================
# TEST
# ==========================================

@app.get("/test")
def test():
    return {
        "status": "success",
        "message": "Blog CRUD is working"
    }