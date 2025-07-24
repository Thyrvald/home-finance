from typing import Optional

from pydantic import BaseModel
from datetime import date

from app.schemas import CategoryOut


class OneTimeExpenseIn(BaseModel):
    name: str
    amount: float
    date: date
    category_id: int

class OneTimeExpenseOut(OneTimeExpenseIn):
    id: int
    Category: Optional[CategoryOut] = None