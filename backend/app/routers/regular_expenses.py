from fastapi import APIRouter, HTTPException
from app.schemas import RegularExpenseIn, RegularExpenseOut
from app.routers.categories import categories
from app.schemas.regular_expenses import RegularExpenseInternal

router = APIRouter()

regular_expenses: list[RegularExpenseInternal] = []
regular_expenses_id_counter = 0

@router.post("/")
def add_regular_expense(regular_expense: RegularExpenseIn):
    global regular_expenses_id_counter

    # sCheck if category exists
    category = next((cat for cat in categories if cat.id == regular_expense.category_id), None)
    if not category:
        raise HTTPException(status_code=400, detail="Invalid category")

    new_expense = RegularExpenseInternal(
        id=regular_expenses_id_counter,
        name=regular_expense.name,
        amount=regular_expense.amount,
        due_date=regular_expense.date,
        category_id=regular_expense.category_id
    )

    regular_expenses.append(new_expense)
    regular_expenses_id_counter += 1
    return new_expense

@router.get("/", response_model=list[RegularExpenseOut])
def get_regular_expenses():
    results = []
    for expense in regular_expenses:
        category = next ((cat for cat in categories if cat.id == expense.category_id), None)
        results.append(RegularExpenseOut(
            id=expense.id,
            name=expense.name,
            amount=expense.amount,
            due_date=expense.date,
            category_id=expense.category_id,
            category_name=category.name,
        ))
    return results

