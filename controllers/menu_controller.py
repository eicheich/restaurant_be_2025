from sqlalchemy.orm import Session
from models import MenuCategory, MenuItem
from fastapi import HTTPException

# Category Operations
def get_all_categories(db: Session):
    return db.query(MenuCategory).all()

def get_category_by_id(db: Session, category_id: int):
    category = db.query(MenuCategory).filter(MenuCategory.id == category_id).first()
    if category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return category

def create_category(db: Session, category: MenuCategory):
    db.add(category)
    db.commit()
    db.refresh(category)
    return category

def update_category(db: Session, category_id: int, category_data: dict):
    category = get_category_by_id(db, category_id)

    for key, value in category_data.items():
        setattr(category, key, value)

    db.commit()
    db.refresh(category)
    return category

def delete_category(db: Session, category_id: int):
    category = get_category_by_id(db, category_id)

    db.delete(category)
    db.commit()
    return {"message": f"Category with id {category_id} deleted successfully"}

# Menu Item Operations
def get_all_menu_items(db: Session):
    return db.query(MenuItem).all()

def get_menu_items_by_category(db: Session, category_id: int):
    return db.query(MenuItem).filter(MenuItem.category_id == category_id).all()

def get_menu_item_by_id(db: Session, item_id: int):
    menu_item = db.query(MenuItem).filter(MenuItem.id == item_id).first()
    if menu_item is None:
        raise HTTPException(status_code=404, detail="Menu item not found")
    return menu_item

def create_menu_item(db: Session, menu_item: MenuItem):
    db.add(menu_item)
    db.commit()
    db.refresh(menu_item)
    return menu_item

def update_menu_item(db: Session, item_id: int, item_data: dict):
    menu_item = get_menu_item_by_id(db, item_id)

    for key, value in item_data.items():
        setattr(menu_item, key, value)

    db.commit()
    db.refresh(menu_item)
    return menu_item

def delete_menu_item(db: Session, item_id: int):
    menu_item = get_menu_item_by_id(db, item_id)

    db.delete(menu_item)
    db.commit()
    return {"message": f"Menu item with id {item_id} deleted successfully"}
