from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.database import get_db
from app.services.finances import calculate_balance

router = APIRouter()

@router.get("/")
def get_balance(db: Session = Depends(get_db)):
    return [{"amount": calculate_balance(db)}]