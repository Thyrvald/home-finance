from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session
from sqlalchemy.orm import joinedload

from app.database import get_db
from app.utils.database_helpers import validate_category_existence
from app.models import OneTimeExpense
from app.schemas import OneTimeExpenseCreate, OneTimeExpenseOut

router = APIRouter()

@router.post("/")
def add_one_time_expense(one_time_expense: OneTimeExpenseCreate, db: Session = Depends(get_db)):

    # Check if category exists
    validate_category_existence(db, one_time_expense.category_id)

    new_expense = OneTimeExpense(
        name=one_time_expense.name,
        amount=one_time_expense.amount,
        date=one_time_expense.date,
        category_id=one_time_expense.category_id
    )
    db.add(new_expense)
    db.commit()
    db.refresh(new_expense)

    return new_expense

@router.get("/", response_model=list[OneTimeExpenseOut])
def get_one_time_expenses(db: Session = Depends(get_db)):
    return db.query(OneTimeExpense).options(joinedload(OneTimeExpense.category)).all()