from sqlalchemy.orm import Session, joinedload

from app.models import RegularExpense
from app.repositories.expenses import regular_expense_repository
from app.schemas import RegularExpenseCreate
from app.utils.database_helpers import validate_category_existence


def create_regular_expense(db: Session, regular_expense_in: RegularExpenseCreate) -> RegularExpense:
    # Check if category exists
    validate_category_existence(db, regular_expense_in.category_id)

    return regular_expense_repository.create_regular_expense(
        db,
        name=regular_expense_in.name,
        amount=regular_expense_in.amount,
        due_date=regular_expense_in.due_date,
        is_paid=regular_expense_in.is_paid,
        category_id=regular_expense_in.category_id,
    )

def get_regular_expenses(db: Session):
    return db.query(RegularExpense).options(joinedload(RegularExpense.category)).all()