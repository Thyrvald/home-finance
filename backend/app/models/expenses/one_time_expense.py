from sqlalchemy import Column, Date
from sqlalchemy.orm import relationship, declared_attr

from .base_expense import BaseExpense

class OneTimeExpense(BaseExpense):
    __tablename__ = "one_time_expenses"

    date = Column(Date)

    @declared_attr
    def category(cls):
        return relationship("Category", back_populates=cls.__tablename__)