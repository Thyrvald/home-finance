from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.database import get_db
from app.services import category_service
from app.schemas import CategoryCreate, CategoryOut
from app.utils.database_helpers import check_if_category_already_exists

router = APIRouter()

@router.post("/", response_model=CategoryOut)
def add_category(category: CategoryCreate, db: Session = Depends(get_db)):
    check_if_category_already_exists(db, category)
    return category_service.create_category(db, category)

@router.get("/", response_model=list[CategoryOut])
def get_category(db: Session = Depends(get_db)):
    return category_service.get_all_categories(db)