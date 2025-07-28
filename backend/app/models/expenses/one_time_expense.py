from sqlalchemy import Column, Date

from .base_expense import BaseExpense

class OneTimeExpense(BaseExpense):
    __tablename__ = "one_time_expenses"

    date = Column(Date)