from sqlalchemy.orm import Session

from datetime import date

from app.models import RegularExpense


def create_regular_expense(db: Session, name: str, amount: float, due_date: date, is_paid: bool, category_id: int):
    regular_expense = RegularExpense(
        name=name,
        amount=amount,
        due_date=due_date,
        is_paid=is_paid,
        category_id=category_id,
    )

    db.add(regular_expense)
    db.commit()
    db.refresh(regular_expense)
    return regular_expense