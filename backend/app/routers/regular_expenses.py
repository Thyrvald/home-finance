from fastapi import APIRouter
from app.schemas import RegularExpense

router = APIRouter()

regular_expenses = []

@router.post("/")
def add_regular_expense(regular_expense: RegularExpense):
    regular_expenses.append(regular_expense)
    return {"message":"Expense added successfully"}

@router.get("/")
def get_regular_expenses():
    return regular_expenses