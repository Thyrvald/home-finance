from fastapi import APIRouter, HTTPException
from app.schemas import OneTimeExpenseIn, OneTimeExpenseInternal, OneTimeExpenseOut, RegularExpenseOut
from app.routers.categories import categories

router = APIRouter()

one_time_expenses: list[OneTimeExpenseInternal] = []
one_time_expenses_id_counter = 0

@router.post("/")
def add_one_time_expense(one_time_expense: OneTimeExpenseIn):
    global one_time_expenses_id_counter

    # Check if category exists
    category = next((cat for cat in categories if cat.id == one_time_expense.category_id), None)
    if not category:
        raise HTTPException(status_code=400, detail="Invalid category")

    new_expense = OneTimeExpenseInternal(
        id = one_time_expenses_id_counter,
        name = one_time_expense.name,
        amount = one_time_expense.amount,
        date = one_time_expense.date,
        category_id = one_time_expense.category_id,
    )

    one_time_expenses.append(new_expense)
    one_time_expenses_id_counter += 1
    return new_expense

@router.get("/", response_model=list[OneTimeExpenseOut])
def get_one_time_expenses():
    results = []
    for expense in one_time_expenses:
        category = next ((cat for cat in categories if cat.id == expense.category_id), None)
        results.append(OneTimeExpenseOut(
            id = expense.id,
            name = expense.name,
            amount = expense.amount,
            date = expense.date,
            category_id = expense.category_id,
            category_name = category.name,
        ))
    return results