from sqlalchemy.orm import Session

from app.repositories import category_repository
from app.schemas import CategoryCreate

def create_category(db: Session, category: CategoryCreate):
    return category_repository.create_category(db, category.name)

def get_all_categories(db: Session):
    return category_repository.get_all_categories(db)