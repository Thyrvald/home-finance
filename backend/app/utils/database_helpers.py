from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.models import Category
from app.config.messages import MSG_CATEGORY_NOT_FOUND


def validate_category_existence(db: Session, expense_category_id: int):
    existing = db.query(Category).filter(Category.id == expense_category_id).first()
    if not existing:
        raise HTTPException(status_code=400, detail=MSG_CATEGORY_NOT_FOUND)