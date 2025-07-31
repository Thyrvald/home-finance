from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import jwt

from app.config.security import *

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password:str) -> str:
    return password_context.hash(password)

def verify_password(plain_password:str, hashed_password:str) -> bool:
    return password_context.verify(plain_password, hashed_password)

def create_access_token(data: dict, expire_delta: timedelta | None = None) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + (expire_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)