from fastapi import FastAPI
from typing import List
from fastapi.middleware.cors import CORSMiddleware

from app.models import *

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Na początek * — w produkcji wpisz konkretną domenę
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

income = []
categories = []
one_time_expenses = []
regular_expenses = []
@app.get("/ping")
def ping():
    return {"message":"pong"}

@app.post("/income")
def add_income(inc: Income):
    income.append(inc)
    return {"message":"Income added successfully"}

@app.get("/income")
def get_income():
    return {"income": income}

@app.post("/category")
def add_category(category: Category):
    categories.append(category)
    return {"message":"Category added successfully"}

@app.get("/category")
def get_category():
    return categories

@app.post("/one-time-expenses")
def add_one_time_expense(ote: OneTimeExpense):
    one_time_expenses.append(ote)
    return {"message":"Expense added successfully"}

@app.get("/one-time-expenses")
def get_one_time_expenses():
    return one_time_expenses

@app.post("/regular-expenses")
def add_regular_expense(regular_expense: RegularExpense):
    regular_expenses.append(regular_expense)
    return {"message":"Expense added successfully"}

@app.get("/regular-expenses")
def get_regular_expenses():
    return regular_expenses

@app.get("/balance")
def get_balance():
    income_total = sum(inc.amount for inc in income)
    expenses = sum(ote.amount for ote in one_time_expenses) + sum(regular_expense.amount for regular_expense in regular_expenses)
    return {"Balance": income_total - expenses}
    



# def main():
#     print("Hello World")
#     app("czemu")
#     print(fibonacci(1))
#     print(fibonacci(10))
#
# if __name__ == "__main__":
#     main()