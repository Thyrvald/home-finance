from pydantic import BaseModel


class Income(BaseModel):
    id: float
    name: str
    amount: float