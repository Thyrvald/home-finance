from pydantic import BaseModel
from datetime import date


class OneTimeExpenseIn(BaseModel):
    name: str
    amount: float
    date: date
    category_id: int

class OneTimeExpenseOut(OneTimeExpenseIn):
    id: int