from sqlalchemy.orm import Session

from app.models import Income

def create_income_repository(db: Session, name: str, amount: float) -> Income:
    new_income = Income(
        name=name,
        amount=amount,
    )

    db.add(new_income)
    db.commit()
    db.refresh(new_income)
    return new_income

def get_income_repository(db: Session):
    return db.query(Income).all()