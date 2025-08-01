from sqlalchemy.orm import Session
from app.repositories import user_repository
from app.schemas import UserCreate

def create_user(db: Session, user_in: UserCreate):
    return user_repository.create_user(
        db,
        name=user_in.name,
        email=user_in.email,
        hashed_password=user_in.password,
    )

def get_all_users(db: Session):
    return user_repository.get_all_users(db)