from pydantic import BaseModel
from typing import Optional

class IncomeCreate(BaseModel):
    name: str
    amount: float

class IncomeOut(IncomeCreate):
    id: int

    model_config = {"from_attributes": True}