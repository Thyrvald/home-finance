from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session

from app.database import get_db
from app.models.category import Category
from app.schemas import CategoryCreate, CategoryOut

router = APIRouter()

@router.post("/", response_model=CategoryOut)
def add_category(category: CategoryCreate, db: Session = Depends(get_db)):
    # Check if category exists
    existing = db.query(Category).filter(Category.name == category.name).first()
    if existing:
        raise HTTPException(status_code=400, detail="Category already exists")

    new_category = Category(
        name=category.name
    )
    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return new_category

@router.get("/", response_model=list[CategoryOut])
def get_category(db: Session = Depends(get_db)):
    return db.query(Category).all()