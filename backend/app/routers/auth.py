from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from sqlalchemy.orm import Session
from sqlalchemy import or_

from app.database import get_db
from app.models import User
from app.utils.security import verify_password, create_access_token
from app.config.messages import *
from app.schemas import Token

router = APIRouter()

@router.post("/login", response_model=Token)
def login(user_in: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(or_(User.email == user_in.username, User.name == user_in.username)).first()
    if not user or not verify_password(user_in.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail=MSG_INVALID_CREDENTIALS)
    access_token = create_access_token(data={"sub": str(user.id)})
    return {"token": access_token, "token_type": "bearer"}