from pydantic import BaseModel
from typing import Optional

class Income(BaseModel):
    id: Optional[float] = 1
    name: str
    amount: float