from fastapi import FastAPI
from typing import List
from fastapi.middleware.cors import CORSMiddleware

from app.schemas import *

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Na początek * — w produkcji wpisz konkretną domenę
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)