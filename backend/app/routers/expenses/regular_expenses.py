from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.database import get_db
from app.services.expenses import regular_expense_service
from app.schemas import RegularExpenseCreate, RegularExpenseOut

router = APIRouter()

@router.post("/", response_model=RegularExpenseCreate)
def add_regular_expense(regular_expense: RegularExpenseCreate, db: Session = Depends(get_db)):
    return regular_expense_service.create_regular_expense(db, regular_expense_in=regular_expense)

@router.get("/", response_model=list[RegularExpenseOut])
def get_regular_expenses(db: Session = Depends(get_db)):
    return regular_expense_service.get_regular_expenses(db)
