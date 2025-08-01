from sqlalchemy.orm import Session

from app.repositories.expenses import one_time_expense_repository
from app.schemas import OneTimeExpenseCreate
from app.utils.database_helpers import validate_category_existence


def create_one_time_expense(db: Session, one_time_expense_in: OneTimeExpenseCreate):
    # Check if category exists
    validate_category_existence(db, one_time_expense_in.category_id)

    return one_time_expense_repository.create_one_time_expense(
        db,
        one_time_expense_in.name,
        one_time_expense_in.amount,
        one_time_expense_in.date,
        one_time_expense_in.category_id,
    )

def get_one_time_expenses(db: Session):
    return one_time_expense_repository.get_one_time_expenses(db)