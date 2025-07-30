from sqlalchemy import Column, Integer, String, Float, ForeignKey

from app.database import Base

class Income(Base):
    __tablename__ = "income"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    amount = Column(Float)
    user_id = Column(Integer, ForeignKey("users.id"))