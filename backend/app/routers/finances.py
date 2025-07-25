from fastapi import APIRouter
from app.routers import income, one_time_expenses, regular_expenses
router = APIRouter()

@router.get("/ping")
def ping():
    return {"message":"pong"}

@router.get("/")
def get_balance():
    income_total = sum(inc.amount for inc in income.income)
    expenses = sum(ote.amount for ote in one_time_expenses.one_time_expenses) + sum(regular_expense.amount for regular_expense in regular_expenses.regular_expenses)
    return [{"amount": income_total - expenses}]