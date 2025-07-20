from typing import Optional
from pydantic import BaseModel
from datetime import date


class RegularExpense(BaseModel):
    id: float
    name: str
    amount: float
    due_date: date
    # Category: Category
    is_paid: Optional[bool] = False