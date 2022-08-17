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
from routes.api.version1.route_login import get_current_user_from_token
from db.models.users import User

router = APIRouter(prefix="/api/v1/jobs", tags=["jobs"])


@router.post("/", response_model=JobShow)
def create_job(
    job: JobCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user_from_token),
):
    owner_id = current_user.id
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
def delete_job_by_id(
    id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user_from_token),
):
    job = get_job_by_id(id=id, db=db)
    if not job:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Job with id {id} not found"
        )
    if job.owner_id == current_user.id or current_user.is_superuser:
        delete_job(id=id, db=db, owner_id=current_user.id)
        return {"detail": "Successfully deleted"}
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail=f"Insufficient permissions to delete job {id}",
    )


@router.put("/{id:int}")
def update_job_by_id(
    id: int,
    job: JobCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user_from_token),
):
    job = get_job_by_id(id=id, db=db)
    if not job:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Job with id {id} not found"
        )
    if job.owner_id == current_user.id or current_user.is_superuser:
        update_job(id=id, job=job, db=db, owner_id=current_user.id)
        return {"detail": "Successfully updated data"}
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail=f"Insufficient permissions to update job {id}",
    )
