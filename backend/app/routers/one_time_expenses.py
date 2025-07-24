from fastapi import APIRouter, HTTPException
from app.schemas import OneTimeExpenseIn, OneTimeExpenseOut
from app.routers.categories import categories

router = APIRouter()

one_time_expenses = []
one_time_expenses_id_counter = 0

@router.post("/")
def add_one_time_expense(ote: OneTimeExpenseIn):
    global one_time_expenses_id_counter

    # sprawdzamy, czy kategoria istnieje
    category = next((cat for cat in categories if cat["id"] == ote.category_id), None)
    if not category:
        raise HTTPException(status_code=400, detail="Invalid category")

    new_expense = {
        "id": one_time_expenses_id_counter,
        "name": ote.name,
        "amount": ote.amount,
        "date": ote.date,
        "category_id": ote.category_id,
    }

    one_time_expenses.append(new_expense)
    one_time_expenses_id_counter += 1
    return new_expense

@router.get("/", response_model=list[OneTimeExpenseOut])
def get_one_time_expenses():
    results = []
    for expense in one_time_expenses:
        category = next ((cat for cat in categories if cat ["id"] == expense["category_id"]), None)
        results.append({
            **expense,
            "Category": category
        })
    return results