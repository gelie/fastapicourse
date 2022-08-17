from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from schemas.users import UserCreate, UserShow
from db.session import get_db
from db.repository.jobs import retrieve_jobs, retrieve_job


router = APIRouter(prefix="", tags=["web", "ui"], include_in_schema=False)

templates = Jinja2Templates(directory="templates")


@router.get("/", response_class=HTMLResponse)
def home(request: Request):
    context = dict(request=request)
    return templates.TemplateResponse("index.html", context=context)


@router.get("/jobs", response_class=HTMLResponse)
def home(request: Request, db: Session = Depends(get_db)):
    jobs = retrieve_jobs(db=db)
    context = dict(request=request, jobs=jobs)
    return templates.TemplateResponse("jobs.html", context=context)


@router.get("/jobs/{id:int}", response_class=HTMLResponse)
def get_job_by_id(request: Request, id: int, db: Session = Depends(get_db)):
    job = retrieve_job(id, db)
    context = dict(request=request, job=job)
    return templates.TemplateResponse("components/modal.html", context)


@router.get("/docs", response_class=HTMLResponse)
def docs(request: Request):
    context = dict(request=request)
    return templates.TemplateResponse("components/docs.html", context)


@router.get("/about", response_class=HTMLResponse)
def about(request: Request):
    context = dict(request=request)
    return templates.TemplateResponse("about.html", context)
