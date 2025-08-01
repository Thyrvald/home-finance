from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas import OneTimeExpenseCreate, OneTimeExpenseOut
from app.services.expenses import one_time_expense_service
from app.services.expenses.one_time_expense_service import create_one_time_expense

router = APIRouter()

@router.post("/")
def add_one_time_expense(one_time_expense: OneTimeExpenseCreate, db: Session = Depends(get_db)):
    return create_one_time_expense(db, one_time_expense)

@router.get("/", response_model=list[OneTimeExpenseOut])
def get_one_time_expenses(db: Session = Depends(get_db)):
    return one_time_expense_service.get_one_time_expenses(db)