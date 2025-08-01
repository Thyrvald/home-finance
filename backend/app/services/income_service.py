from sqlalchemy.orm import Session

from app.schemas import IncomeCreate
from app.repositories import income_repository

def create_income(db: Session, income_in: IncomeCreate):
    return income_repository.create_income_repository(
        db,
        income_in.name,
        income_in.amount,
    )

def get_income(db: Session):
    return income_repository.get_income_repository(db)