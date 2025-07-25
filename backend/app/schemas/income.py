from pydantic import BaseModel
from typing import Optional

class IncomeIn(BaseModel):
    name: str
    amount: float

class IncomeOut(IncomeIn):
    id: int