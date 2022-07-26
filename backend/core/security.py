from datetime import datetime, timedelta
from jose import jwt
from core.config import settings


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(
            minutes=int(settings.ACCESS_TOKEN_EXPIRY)
        )
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM
    )
    return encoded_jwt


def decode_token(
    token: str,
    secret: str = settings.SECRET_KEY,
    algorithm: list = [settings.ALGORITHM],
):
    decoded_token = jwt.decode(token, secret, algorithm)
    return decoded_token
