from sqlalchemy.orm import Session
from schemas.jobs import JobCreate
from db.models.jobs import Job


def create_new_job(job: JobCreate, db: Session, owner_id: int):
    job = Job(**job.dict(), owner_id=owner_id)
    db.add(job)
    db.commit()
    db.refresh(job)
    return job


def retrieve_job(id: int, db: Session):
    job = db.query(Job).filter(Job.id == id).first()
    return job


def retrieve_jobs(db: Session):
    jobs = db.query(Job).filter(Job.is_active == True).all()
    return jobs


def delete_job(id: int, db: Session, owner_id: int):
    job = db.query(Job).filter(Job.id == id).first()
    if job is None:
        return 0
    db.delete(job)
    db.commit()
    return 1


def update_job(id: int, job: JobCreate, db: Session, owner_id: int):
    old_job = db.query(Job).filter(Job.id == id)
    if not old_job.first():
        return 0
    job.__dict__.update(owner_id=owner_id)
    old_job.update(job.__dict__)
    db.commit()
    return 1
