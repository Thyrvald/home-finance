from datetime import date

from sqlalchemy.orm import Session, joinedload

from app.models import OneTimeExpense


def create_one_time_expense(db: Session, name: str, amount: float, payment_date: date, category_id: int):
    new_expense = OneTimeExpense(
        name=name,
        amount=amount,
        date=payment_date,
        category_id=category_id,
    )

    db.add(new_expense)
    db.commit()
    db.refresh(new_expense)
    return new_expense

def get_one_time_expenses(db: Session):
    return db.query(OneTimeExpense).options(joinedload(OneTimeExpense.category)).all()