from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session
from sqlalchemy.orm import joinedload

from app.database import get_db
from app.utils.database_helpers import validate_category_existence
from app.models import RegularExpense
from app.schemas import RegularExpenseCreate, RegularExpenseOut

router = APIRouter()

@router.post("/", response_model=RegularExpenseCreate)
def add_regular_expense(regular_expense: RegularExpenseCreate, db: Session = Depends(get_db)):
    # Check if category exists
    validate_category_existence(db, regular_expense.category_id)

    new_expense = RegularExpense(
        name=regular_expense.name,
        amount=regular_expense.amount,
        due_date=regular_expense.due_date,
        category_id=regular_expense.category_id,
    )
    db.add(new_expense)
    db.commit()
    db.refresh(new_expense)

    return new_expense

@router.get("/", response_model=list[RegularExpenseOut])
def get_regular_expenses(db: Session = Depends(get_db)):
    return db.query(RegularExpense).options(joinedload(RegularExpense.category)).all()
