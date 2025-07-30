from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    user_id = Column(Integer, ForeignKey("users.id"))

    one_time_expenses = relationship("OneTimeExpense", back_populates="category")
    regular_expenses = relationship("RegularExpense", back_populates="category")