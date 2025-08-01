from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import engine, Base
from app.routers import balance, income, categories
from app.routers.expenses import one_time_expenses, regular_expenses
from app.routers import users

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(income.router, prefix="/income", tags=["Income"])
app.include_router(one_time_expenses.router, prefix="/one-time-expenses", tags=["OneTimeExpenses"])
app.include_router(regular_expenses.router, prefix="/regular-expenses", tags=["RegularExpenses"])
app.include_router(categories.router, prefix="/category", tags=["Categories"])
app.include_router(balance.router, prefix="/balance", tags=["Balance"])
app.include_router(users.router, prefix="/user", tags=["Users"])