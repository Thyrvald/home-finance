from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.models import Category
from app.config.messages import MSG_CATEGORY_NOT_FOUND, MSG_CATEGORY_ALREADY_EXISTS
from app.schemas import CategoryCreate


def validate_category_existence(db: Session, expense_category_id: int):
    existing = db.query(Category).filter(Category.id == expense_category_id).first()
    if not existing:
        raise HTTPException(status_code=400, detail=MSG_CATEGORY_NOT_FOUND)

def check_if_category_already_exists(db: Session, category: CategoryCreate):
    existing = db.query(Category).filter(Category.name == category.name).first()
    if existing:
        raise HTTPException(status_code=400, detail=MSG_CATEGORY_ALREADY_EXISTS)