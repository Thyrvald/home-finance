from pydantic import BaseModel

from app.schemas import CategoryOut

class BaseExpense(BaseModel):
    name: str
    amount: float
    category_id: int

class BaseExpenseOut(BaseExpense):
    id: int
    category: CategoryOut

    model_config = {"from_attributes": True}