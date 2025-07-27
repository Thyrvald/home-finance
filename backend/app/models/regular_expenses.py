from sqlalchemy import Column, Integer, String, Float, ForeignKey, Date, Boolean
from sqlalchemy.orm import relationship
from app.database import Base


class RegularExpense(Base):
    __tablename__ = "regular_expenses"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    amount = Column(Float)
    due_date = Column(Date)
    category_id = Column(Integer, ForeignKey("categories.id"))
    is_paid = Column(Boolean)

    category = relationship("Category", backref="regular_expenses")