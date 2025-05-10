from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from controllers.menu_controller import (
    get_all_categories, create_category, get_category_by_id, update_category, delete_category,
    get_all_menu_items, create_menu_item, get_menu_item_by_id, get_menu_items_by_category,
    update_menu_item, delete_menu_item
)
from models import MenuCategory as MenuCategoryModel, MenuItem as MenuItemModel
from schemas.menu import Category, CategoryCreate, CategoryUpdate, MenuItem, MenuItemCreate, MenuItemUpdate
from routes import get_db
from typing import List, Optional

menu_router = APIRouter(
    prefix="/menu",
    tags=["menu"],
)

# Category routes
@menu_router.get("/categories", response_model=List[Category])
def read_categories(db: Session = Depends(get_db)):
    return get_all_categories(db)

@menu_router.get("/categories/{category_id}", response_model=Category)
def read_category(category_id: int, db: Session = Depends(get_db)):
    return get_category_by_id(db, category_id)

@menu_router.post("/categories", response_model=Category, status_code=201)
def add_category(category: CategoryCreate, db: Session = Depends(get_db)):
    db_category = MenuCategoryModel(name=category.name)
    return create_category(db, db_category)

@menu_router.put("/categories/{category_id}", response_model=Category)
def update_category_endpoint(category_id: int, category_data: CategoryUpdate, db: Session = Depends(get_db)):
    return update_category(db, category_id, category_data.dict(exclude_unset=True))

@menu_router.delete("/categories/{category_id}")
def delete_category_endpoint(category_id: int, db: Session = Depends(get_db)):
    return delete_category(db, category_id)

# Menu item routes
@menu_router.get("/items", response_model=List[MenuItem])
def read_menu_items(category_id: Optional[int] = None, db: Session = Depends(get_db)):
    if category_id:
        return get_menu_items_by_category(db, category_id)
    return get_all_menu_items(db)

@menu_router.get("/items/{item_id}", response_model=MenuItem)
def read_menu_item(item_id: int, db: Session = Depends(get_db)):
    return get_menu_item_by_id(db, item_id)

@menu_router.post("/items", response_model=MenuItem, status_code=201)
def add_menu_item(item: MenuItemCreate, db: Session = Depends(get_db)):
    db_menu_item = MenuItemModel(
        category_id=item.category_id,
        image=item.image,
        title=item.title,
        description=item.description,
        rate=item.rate,
        total_review=item.total_review,
        price=item.price
    )
    return create_menu_item(db, db_menu_item)

@menu_router.put("/items/{item_id}", response_model=MenuItem)
def update_menu_item_endpoint(item_id: int, item_data: MenuItemUpdate, db: Session = Depends(get_db)):
    return update_menu_item(db, item_id, item_data.dict(exclude_unset=True))

@menu_router.delete("/items/{item_id}")
def delete_menu_item_endpoint(item_id: int, db: Session = Depends(get_db)):
    return delete_menu_item(db, item_id)
