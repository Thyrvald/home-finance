from fastapi import APIRouter
from app.schemas import Income

router = APIRouter()

income = []

@router.post("/")
def add_income(inc: Income):
    income.append(inc)
    return {"message":"Income added successfully"}

@router.get("/")
def get_income():
    return income