from sqlalchemy import Column, Date, Boolean

from .base_expense import BaseExpense

class RegularExpense(BaseExpense):
    __tablename__ = "regular_expenses"

    due_date = Column(Date)
    is_paid = Column(Boolean)