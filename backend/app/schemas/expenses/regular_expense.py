from typing import Optional

from datetime import date

from .base_expense import BaseExpense, BaseExpenseOut

class RegularExpenseCreate(BaseExpense):
    due_date: date
    is_paid: Optional[bool] = False

class RegularExpenseOut(RegularExpenseCreate, BaseExpenseOut):
    pass
