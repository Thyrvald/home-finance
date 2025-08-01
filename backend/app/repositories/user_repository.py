from sqlalchemy.orm import Session
from app.models import User
from app.utils.security import hash_password



def get_user_by_name_or_email(db: Session, name_or_email: str) -> User | None:
    return db.query(User).filter((User.email == name_or_email) | (User.name == name_or_email)).first()

def create_user(db: Session, name: str, email: str, hashed_password: str) -> User:
    new_user = User(
        name=name,
        email=email,
        hashed_password=hash_password(hashed_password),
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_all_users(db: Session):
    return db.query(User).all()

