from fastapi import APIRouter
from app.schemas import CategoryIn, CategoryOut

router = APIRouter()

categories: list[CategoryOut] = []
category_id_counter = 0

@router.post("/", response_model=CategoryOut)
def add_category(category: CategoryIn):
    global category_id_counter
    new_category = CategoryOut(
        id = category_id_counter,
        name = category.name,
    )
    categories.append(new_category)
    category_id_counter += 1
    return new_category

@router.get("/", response_model=list[CategoryOut])
def get_category():
    return categories