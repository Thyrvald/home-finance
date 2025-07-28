from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship, declared_attr

from app.database import Base

class BaseExpense(Base):
    __abstract__ = True
    id = Column(Integer, primary_key=True)
    name = Column(String)
    amount = Column(Float)
    category_id = Column(Integer, ForeignKey("categories.id"))

    @declared_attr
    def category(cls):
        return relationship("Category", back_populates=cls.__tablename__)