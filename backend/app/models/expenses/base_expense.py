from sqlalchemy import Column, Integer, String, Float, ForeignKey

from app.database import Base

class BaseExpense(Base):
    __abstract__ = True
    id = Column(Integer, primary_key=True)
    name = Column(String)
    amount = Column(Float)
    category_id = Column(Integer, ForeignKey("categories.id"))
    user_id = Column(Integer, ForeignKey("users.id"))