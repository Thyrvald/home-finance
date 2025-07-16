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
    date: date
    Category: Category

class OneTimeExpense(BaseModel):
    name: str
    amount: float
    date: date
    Category: Category