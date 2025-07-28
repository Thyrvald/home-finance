from sqlalchemy.orm import Session

from app.models import Income, OneTimeExpense, RegularExpense

def calculate_balance(db: Session):
    income_total = sum(income.amount for income in db.query(Income).all())
    expense_total = sum(expense.amount for expense in db.query(OneTimeExpense).all()) + sum(expense.amount for expense in db.query(RegularExpense).all())
    return income_total - expense_total