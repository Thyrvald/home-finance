from fastapi import FastAPI
from typing import List
from fastapi.middleware.cors import CORSMiddleware

from app.schemas import *
from app.routers import finances, income, one_time_expenses, regular_expenses, categories
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Na początek * — w produkcji wpisz konkretną domenę
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(income.router, prefix="/income", tags=["Income"])
app.include_router(one_time_expenses.router, prefix="/one-time-expenses", tags=["OneTimeExpenses"])
app.include_router(regular_expenses.router, prefix="/regular-expenses", tags=["RegularExpenses"])

app.include_router(categories.router, prefix="/categories", tags=["Categories"])