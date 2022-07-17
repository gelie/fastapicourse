from sqlalchemy.orm import Session
from db.models.users import User
from schemas.users import UserCreate
from core.hashing import Hasher


def create_new_user(user: UserCreate, db: Session):
    print(type(db))
    user = User(
        username=user.username,
        email=user.email,
        hashed_password=Hasher.get_pwd_hash(user.password),
        is_active=True,
        is_superuser=False,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
