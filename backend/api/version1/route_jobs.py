from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from schemas.jobs import JobCreate, JobShow
from db.session import get_db
from db.repository.jobs import (
    create_new_job,
    retrieve_job,
    retrieve_jobs,
    delete_job,
    update_job,
)

router = APIRouter()


@router.post("/", response_model=JobShow)
def create_job(job: JobCreate, db: Session = Depends(get_db)):
    owner_id = 1
    job = create_new_job(job, db, owner_id)
    return job


@router.get("/{id:int}", response_model=JobShow)
def get_job_by_id(id: int, db: Session = Depends(get_db)):
    job = retrieve_job(id, db)
    if not job:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Job with id {id} does not exist!!",
        )
    return job


@router.get("/", response_model=list[JobShow])
def get_all_jobs(db: Session = Depends(get_db)):
    jobs = retrieve_jobs(db)
    if not jobs:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"No jobs found!!"
        )
    return jobs


@router.delete("/{id:int}")
def delete_job_by_id(id: int, db: Session = Depends(get_db)):
    owner_id = 1
    message = delete_job(id=id, db=db, owner_id=owner_id)
    if not message:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Job with id {id} not found"
        )
    return {"detail": "Successfully deleted"}


@router.put("/{id:int}")
def update_job_by_id(id: int, job: JobCreate, db: Session = Depends(get_db)):
    owner_id = 1
    message = update_job(id, job, db, owner_id)
    if not message:
        raise HTTPException(
            status_code=404, detail=f"Job with id {id} does not exist!!"
        )
    return {"detail": "Successfully updated data"}
