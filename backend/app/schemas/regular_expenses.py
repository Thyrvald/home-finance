from typing import Optional
from pydantic import BaseModel
from datetime import date

from app.schemas import CategoryOut


class RegularExpenseIn(BaseModel):
    name: str
    amount: float
    due_date: date
    category_id: int
    is_paid: Optional[bool] = False


class RegularExpenseInternal(RegularExpenseIn):
    id: int


class RegularExpenseCreate(BaseModel):
    name: str
    amount: float
    due_date: date
    category_id: int
    is_paid: Optional[bool] = False

class RegularExpenseOut(RegularExpenseCreate):
    id: int
    category_name: str

    model_config = {"from_attributes": True}
