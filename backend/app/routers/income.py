from fastapi import APIRouter
from app.schemas import Income

router = APIRouter()

income = []

@router.post("/income")
def add_income(inc: Income):
    income.append(inc)
    return {"message":"Income added successfully"}

@router.get("/income")
def get_income():
    return income