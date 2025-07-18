from typing import Optional
from pydantic import BaseModel
from datetime import date

class Income(BaseModel):
    name: str
    amount: float

class Category(BaseModel):
    name: str

class RegularExpense(BaseModel):
    name: str
    amount: float
    due_date: date
    Category: Category
    is_paid: Optional[bool] = False

class OneTimeExpense(BaseModel):
    name: str
    amount: float
    date: date
    Category: Category