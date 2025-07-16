from fastapi import APIRouter
from app.schemas import Income, Category, OneTimeExpense, RegularExpense

router = APIRouter()


income = []
categories = []
one_time_expenses = []
regular_expenses = []
@router.get("/ping")
def ping():
    return {"message":"pong"}

@router.post("/income")
def add_income(inc: Income):
    income.append(inc)
    return {"message":"Income added successfully"}

@router.get("/income")
def get_income():
    return {"income": income}

@router.post("/category")
def add_category(category: Category):
    categories.append(category)
    return {"message":"Category added successfully"}

@router.get("/category")
def get_category():
    return categories

@router.post("/one-time-expenses")
def add_one_time_expense(ote: OneTimeExpense):
    one_time_expenses.append(ote)
    return {"message":"Expense added successfully"}

@router.get("/one-time-expenses")
def get_one_time_expenses():
    return one_time_expenses

@router.post("/regular-expenses")
def add_regular_expense(regular_expense: RegularExpense):
    regular_expenses.append(regular_expense)
    return {"message":"Expense added successfully"}

@router.get("/regular-expenses")
def get_regular_expenses():
    return regular_expenses

@router.get("/balance")
def get_balance():
    income_total = sum(inc.amount for inc in income)
    expenses = sum(ote.amount for ote in one_time_expenses) + sum(regular_expense.amount for regular_expense in regular_expenses)
    return {"Balance": income_total - expenses}