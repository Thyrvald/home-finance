from pydantic import BaseModel
from datetime import date


class OneTimeExpenseCreate(BaseModel):
    name: str
    amount: float
    date: date
    category_id: int

class OneTimeExpenseOut(OneTimeExpenseCreate):
    id: int
    category_name: str

    model_config = {"from_attributes": True}