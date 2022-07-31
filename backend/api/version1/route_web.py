from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from schemas.users import UserCreate, UserShow
from db.session import get_db
from db.repository.jobs import retrieve_jobs


router = APIRouter()

templates = Jinja2Templates(directory="templates")


@router.get("/", include_in_schema=False, response_class=HTMLResponse)
def home(request: Request, db: Session = Depends(get_db)):
    jobs = retrieve_jobs(db=db)
    context = dict(request=request, jobs=jobs)
    return templates.TemplateResponse("index.html", context=context)
