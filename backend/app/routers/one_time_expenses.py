from fastapi import APIRouter
from app.schemas import OneTimeExpense

router = APIRouter()

one_time_expenses = []

@router.post("/one-time-expenses")
def add_one_time_expense(ote: OneTimeExpense):
    one_time_expenses.append(ote)
    return {"message":"Expense added successfully"}

@router.get("/one-time-expenses")
def get_one_time_expenses():
    return one_time_expenses