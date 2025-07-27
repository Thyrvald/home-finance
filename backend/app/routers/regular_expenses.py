from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Category, RegularExpense
from app.schemas import RegularExpenseIn, RegularExpenseCreate, RegularExpenseOut
from app.schemas.regular_expenses import RegularExpenseInternal

router = APIRouter()

# @router.post("/")
# def add_regular_expense(regular_expense: RegularExpenseIn):
#     global regular_expenses_id_counter
#
#     # sCheck if category exists
#     # category = next((cat for cat in categories if cat.id == regular_expense.category_id), None)
#     # if not category:
#     #     raise HTTPException(status_code=400, detail="Invalid category")
#
#     new_expense = RegularExpenseInternal(
#         id=regular_expenses_id_counter,
#         name=regular_expense.name,
#         amount=regular_expense.amount,
#         due_date=regular_expense.date,
#         category_id=regular_expense.category_id
#     )
#
#     regular_expenses.append(new_expense)
#     regular_expenses_id_counter += 1
#     return new_expense

@router.post("/", response_model=RegularExpenseCreate)
def add_regular_expense(regular_expense: RegularExpenseCreate, db: Session = Depends(get_db)):
    # Check if category exists
    existing = db.query(Category).filter(Category.id == regular_expense.category_id).first()
    if not existing:
        raise HTTPException(status_code=400, detail="No such category")

    new_expense = RegularExpense(
        name=regular_expense.name,
        amount=regular_expense.amount,
        due_date=regular_expense.due_date,
        category_id=regular_expense.category_id,
    )
    db.add(new_expense)
    db.commit()
    db.refresh(new_expense)

    return new_expense


@router.get("/", response_model=list[RegularExpenseOut])
def get_regular_expenses(db:Session = Depends(get_db)):
    regular_expenses = db.query(RegularExpense).all()
    results = []
    for expense in regular_expenses:
        results.append(RegularExpenseOut(
            id=expense.id,
            name=expense.name,
            amount=expense.amount,
            due_date=expense.due_date,
            category_id=expense.category_id,
            category_name=expense.category.name,
        ))
    return results
