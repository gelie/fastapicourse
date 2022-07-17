from typing import Optional
from pydantic import BaseModel
from datetime import date, datetime


class JobBase(BaseModel):
    title: Optional[str] = None
    company: Optional[str] = None
    company_url: Optional[str] = None
    description: Optional[str] = None
    location: Optional[str] = "Remote"
    date_posted: Optional[date] = datetime.now().date()


class JobCreate(JobBase):
    title: str
    company: str
    location: str
    description: str


class JobShow(JobBase):
    title: str
    company: str
    company_url: Optional[str] = None
    location: str
    date_posted: date
    description: Optional[str]

    class Config:
        orm_mode = True
