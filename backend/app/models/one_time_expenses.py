from sqlalchemy import Column, Integer, String, Float, ForeignKey, Date
from sqlalchemy.orm import relationship
from app.database import Base


class OneTimeExpense(Base):
    __tablename__ = "one_time_expenses"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    amount = Column(Float)
    date = Column(Date)
    category_id = Column(Integer, ForeignKey("categories.id"))

    category = relationship("Category", backref="one_time_expenses")