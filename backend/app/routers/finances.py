from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Income, OneTimeExpense, RegularExpense
router = APIRouter()

@router.get("/ping")
def ping():
    return {"message":"pong"}

@router.get("/")
def get_balance(db: Session = Depends(get_db)):
    income_total = sum(inc.amount for inc in db.query(Income).all())

    expenses = sum(ote.amount for ote in db.query(OneTimeExpense).all()) + sum(regular_expense.amount for regular_expense in db.query(RegularExpense).all())
    return [{"amount": income_total - expenses}]