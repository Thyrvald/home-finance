from fastapi import APIRouter
from app.schemas import IncomeIn, IncomeOut

router = APIRouter()

income: list[IncomeOut] = []
income_id_counter = 0

@router.post("/")
def add_income(inc: IncomeIn):
    global income_id_counter

    new_income = IncomeOut(
        id=income_id_counter,
        name=inc.name,
        amount=inc.amount,
    )

    income.append(new_income)
    income_id_counter += 1
    return income

@router.get("/")
def get_income():
    return income