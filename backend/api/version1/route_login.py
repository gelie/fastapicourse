from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from db.repository.login import get_user
from sqlalchemy.orm import Session
from db.session import get_db
from core.hashing import Hasher
from core.security import create_access_token, decode_token
from jose import JWTError

router = APIRouter()


@router.post("/token")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
):
    username = form_data.username
    password = form_data.password
    user = get_user(username=username, db=db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Username is not valid"
        )
    authenticate_user = Hasher.verify_pwd(password, user.hashed_password)
    if not authenticate_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Password is incorrect"
        )
    data = dict(sub=username)
    token = create_access_token(data=data)
    return dict(access_token=token, token_type="bearer")


oauth_scheme = OAuth2PasswordBearer("/login/token")


def get_current_user_from_token(
    token: str = Depends(oauth_scheme), db: Session = Depends(get_db)
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
    )

    try:
        payload = decode_token(token=token)
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = get_user(username, db)
    if user is None:
        raise credentials_exception
    return user
