from datetime import date

from .base_expense import BaseExpense, BaseExpenseOut

class OneTimeExpenseCreate(BaseExpense):
    date: date

class OneTimeExpenseOut(OneTimeExpenseCreate, BaseExpenseOut):
    pass