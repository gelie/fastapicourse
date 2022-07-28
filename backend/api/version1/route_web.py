from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from schemas.users import UserCreate, UserShow
from db.session import get_db


router = APIRouter()

templates = Jinja2Templates(directory="templates")


@router.get("/", include_in_schema=False, response_class=HTMLResponse)
def home(request: Request):
    context = dict(request=request)
    return templates.TemplateResponse("index.html", context=context)
