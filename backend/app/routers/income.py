from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.income import Income
from app.schemas import IncomeCreate, IncomeOut

router = APIRouter()

@router.post("/", response_model=IncomeOut)
def add_income(income: IncomeCreate, db: Session = Depends(get_db)):
    new_income = Income(
        name=income.name,
        amount=income.amount,
    )
    db.add(new_income)
    db.commit()
    db.refresh(new_income)
    return new_income

@router.get("/", response_model=list[IncomeOut])
def get_income(db: Session = Depends(get_db)):
    return db.query(Income).all()