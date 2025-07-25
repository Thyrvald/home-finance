from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import finances, income, one_time_expenses, regular_expenses, categories
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],  # Na początek * — w produkcji wpisz konkretną domenę
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(income.router, prefix="/income", tags=["Income"])
app.include_router(one_time_expenses.router, prefix="/one-time-expenses", tags=["OneTimeExpenses"])
app.include_router(regular_expenses.router, prefix="/regular-expenses", tags=["RegularExpenses"])
app.include_router(categories.router, prefix="/category", tags=["Categories"])
app.include_router(finances.router, prefix="/balance", tags=["Balance"])