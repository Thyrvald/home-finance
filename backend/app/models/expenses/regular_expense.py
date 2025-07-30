from sqlalchemy import Column, Date, Boolean
from sqlalchemy.orm import relationship, declared_attr

from .base_expense import BaseExpense

class RegularExpense(BaseExpense):
    __tablename__ = "regular_expenses"

    due_date = Column(Date)
    is_paid = Column(Boolean)

    @declared_attr
    def category(cls):
        return relationship("Category", back_populates=cls.__tablename__)