from typing import List

from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.database import get_db
from app.models import User
from app.schemas import UserCreate, UserOut
from app.services import user_service
router = APIRouter()

@router.post("/", response_model=UserOut)
def add_user(user: UserCreate, db: Session = Depends(get_db)):
    return user_service.create_user(db, user)

@router.get("/", response_model=List[UserOut])
def get_users(db: Session = Depends(get_db)):
    return user_service.get_all_users(db)