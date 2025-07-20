from pydantic import BaseModel
from datetime import date


class OneTimeExpense(BaseModel):
    id: float
    name: str
    amount: float
    date: date
    # Category: Category