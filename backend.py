from datetime import datetime
from pathlib import Path
import shutil
import math

from fastapi import (
    FastAPI,
    Request,
    Form,
    Depends,
    UploadFile,
    File
)

from fastapi.responses import (
    HTMLResponse,
    RedirectResponse
)

from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from sqlalchemy import (
    create_engine,
    String,
    Text,
    DateTime,
    select
)

from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
    sessionmaker,
    Session
)

# ==========================================
# DATABASE
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

    image_path: Mapped[str] = mapped_column(
        String(500),
        default=""
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )


Base.metadata.create_all(bind=engine)

# ==========================================
# APP
# ==========================================

app = FastAPI()

templates = Jinja2Templates(directory="frontend")

# CSS
app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)

# Uploaded Images
app.mount(
    "/uploads",
    StaticFiles(directory="uploads"),
    name="uploads"
)

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

# ==========================================
# DATABASE DEPENDENCY
# ==========================================


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
    search: str = "",
    page: int = 1,
    db: Session = Depends(get_db)
):

    stmt = select(Blog)

    if search:
        stmt = stmt.where(
            Blog.title.contains(search)
        )

    all_blogs = db.scalars(stmt).all()

    PER_PAGE = 6

    total = len(all_blogs)

    pages = max(
        1,
        math.ceil(total / PER_PAGE)
    )

    start = (page - 1) * PER_PAGE
    end = start + PER_PAGE

    blogs = all_blogs[start:end]

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "blogs": blogs,
            "search": search,
            "page": page,
            "pages": pages
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
    image: UploadFile = File(...),
    db: Session = Depends(get_db)
):

    filename = ""

    if image and image.filename:

        filename = (
            f"{datetime.now().timestamp()}_"
            f"{image.filename}"
        )

        file_path = UPLOAD_DIR / filename

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(
                image.file,
                buffer
            )

    blog = Blog(
        title=title,
        author=author,
        content=content,
        image_path=filename
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

@app.get(
    "/blog/{blog_id}",
    response_class=HTMLResponse
)
def view_blog(
    request: Request,
    blog_id: int,
    db: Session = Depends(get_db)
):

    blog = db.get(
        Blog,
        blog_id
    )

    if not blog:
        return HTMLResponse(
            content="<h1>Blog Not Found</h1>",
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

@app.get(
    "/edit/{blog_id}",
    response_class=HTMLResponse
)
def edit_page(
    request: Request,
    blog_id: int,
    db: Session = Depends(get_db)
):

    blog = db.get(
        Blog,
        blog_id
    )

    if not blog:
        return HTMLResponse(
            content="<h1>Blog Not Found</h1>",
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
    image: UploadFile | None = File(None),
    db: Session = Depends(get_db)
):

    blog = db.get(
        Blog,
        blog_id
    )

    if blog:

        blog.title = title
        blog.author = author
        blog.content = content

        if image and image.filename:

            filename = (
                f"{datetime.now().timestamp()}_"
                f"{image.filename}"
            )

            file_path = UPLOAD_DIR / filename

            with open(file_path, "wb") as buffer:
                shutil.copyfileobj(
                    image.file,
                    buffer
                )

            blog.image_path = filename

        db.commit()

    return RedirectResponse(
        url="/",
        status_code=303
    )


# ==========================================
# DELETE PAGE
# ==========================================

@app.get(
    "/delete/{blog_id}",
    response_class=HTMLResponse
)
def delete_page(
    request: Request,
    blog_id: int,
    db: Session = Depends(get_db)
):

    blog = db.get(
        Blog,
        blog_id
    )

    if not blog:
        return HTMLResponse(
            content="<h1>Blog Not Found</h1>",
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

    blog = db.get(
        Blog,
        blog_id
    )

    if blog:

        if blog.image_path:

            image_file = (
                UPLOAD_DIR /
                blog.image_path
            )

            if image_file.exists():
                image_file.unlink()

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