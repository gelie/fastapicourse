from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.jobs import JobCreate, JobShow
from db.session import get_db
from db.repository.jobs import create_new_job

router = APIRouter()


@router.post("/", response_model=JobShow)
def create_job(job: JobCreate, db: Session = Depends(get_db)):
    owner_id = 1
    job = create_new_job(job, db, owner_id)
    return job
