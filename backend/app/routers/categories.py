from fastapi import APIRouter
from app.schemas import CategoryIn, CategoryOut

router = APIRouter()

categories = []
category_id_counter = 0

@router.post("/category", response_model=CategoryOut)
def add_category(category: CategoryIn):
    global category_id_counter
    new_category = {"id": category_id_counter, "name": category.name}
    categories.append(new_category)
    category_id_counter += 1
    return {"message":"Category added successfully"}

@router.get("/category", response_model=list[CategoryOut])
def get_category():
    return categories