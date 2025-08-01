from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas import IncomeCreate, IncomeOut
from app.services import income_service

router = APIRouter()

@router.post("/", response_model=IncomeOut)
def add_income(income: IncomeCreate, db: Session = Depends(get_db)):
    return income_service.create_income(db, income)

@router.get("/", response_model=list[IncomeOut])
def get_income(db: Session = Depends(get_db)):
    return income_service.get_income(db)