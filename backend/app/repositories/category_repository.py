from sqlalchemy.orm import Session

from app.models import Category

def create_category(db: Session, category_name: str) -> Category:
    new_category = Category(name=category_name)

    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return new_category

def get_all_categories(db: Session):
    return db.query(Category).all()