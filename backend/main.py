from fastapi import FastAPI
from core.config import settings
from db.session import engine
from db.base import Base
from routes.base import api_router
from fastapi.staticfiles import StaticFiles


def create_tables():
    Base.metadata.create_all(bind=engine)


def include_router(app):
    app.include_router(api_router)


def static_files(app):
    app.mount("/static", StaticFiles(directory="static"), name="static")


def start_application():
    app = FastAPI(
        title=settings.PROJECT_TITLE,
        version=settings.PROJECT_VERSION,
        docs_url="/documentation",
        redoc_url=None,
    )
    create_tables()
    include_router(app)
    static_files(app)
    return app


app = start_application()
