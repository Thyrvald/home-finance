from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Category, OneTimeExpense

from app.schemas import OneTimeExpenseCreate, OneTimeExpenseOut

router = APIRouter()

@router.post("/")
def add_one_time_expense(one_time_expense: OneTimeExpenseCreate, db: Session = Depends(get_db)):

    # # Check if category exists
    existing = db.query(Category).filter(Category.id == one_time_expense.category_id).first()
    if not existing:
        raise HTTPException(status_code=400, detail="No such category")

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
    one_time_expenses = db.query(OneTimeExpense).all()
    results = []
    for expense in one_time_expenses:
        results.append(OneTimeExpenseOut(
            id = expense.id,
            name = expense.name,
            amount = expense.amount,
            date = expense.date,
            category_id = expense.category_id,
            category_name = db.query(Category).filter(Category.id == expense.category_id).first().name,
        ))
    return results