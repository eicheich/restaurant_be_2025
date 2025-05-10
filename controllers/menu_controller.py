from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from models import MenuCategory, MenuItem
from exceptions import DatabaseError, ResourceNotFoundError, DuplicateResourceError, ValidationError

# Category Operations
def get_all_categories(db: Session):
    try:
        return db.query(MenuCategory).all()
    except SQLAlchemyError as e:
        raise DatabaseError(str(e))

def get_category_by_id(db: Session, category_id: int):
    try:
        category = db.query(MenuCategory).filter(MenuCategory.id == category_id).first()
        if category is None:
            raise ResourceNotFoundError("Category", category_id)
        return category
    except SQLAlchemyError as e:
        raise DatabaseError(str(e))

def create_category(db: Session, category: MenuCategory):
    try:
        db.add(category)
        db.commit()
        db.refresh(category)
        return category
    except IntegrityError as e:
        db.rollback()
        if "Duplicate entry" in str(e):
            raise DuplicateResourceError("Category", "name", category.name)
        raise DatabaseError(str(e))
    except SQLAlchemyError as e:
        db.rollback()
        raise DatabaseError(str(e))

def update_category(db: Session, category_id: int, category_data: dict):
    try:
        category = get_category_by_id(db, category_id)

        for key, value in category_data.items():
            if not hasattr(category, key):
                raise ValidationError(f"Invalid field: {key}")
            setattr(category, key, value)

        db.commit()
        db.refresh(category)
        return category
    except IntegrityError as e:
        db.rollback()
        if "Duplicate entry" in str(e):
            raise DuplicateResourceError("Category", "name", category_data.get("name"))
        raise DatabaseError(str(e))
    except SQLAlchemyError as e:
        db.rollback()
        raise DatabaseError(str(e))

def delete_category(db: Session, category_id: int):
    try:
        category = get_category_by_id(db, category_id)
        db.delete(category)
        db.commit()
        return {"message": f"Category with id {category_id} deleted successfully"}
    except SQLAlchemyError as e:
        db.rollback()
        raise DatabaseError(str(e))

# Menu Item Operations
def get_all_menu_items(db: Session):
    try:
        return db.query(MenuItem).all()
    except SQLAlchemyError as e:
        raise DatabaseError(str(e))

def get_menu_items_by_category(db: Session, category_id: int):
    try:
        # First check if category exists
        get_category_by_id(db, category_id)
        return db.query(MenuItem).filter(MenuItem.category_id == category_id).all()
    except SQLAlchemyError as e:
        raise DatabaseError(str(e))

def get_menu_item_by_id(db: Session, item_id: int):
    try:
        menu_item = db.query(MenuItem).filter(MenuItem.id == item_id).first()
        if menu_item is None:
            raise ResourceNotFoundError("Menu item", item_id)
        return menu_item
    except SQLAlchemyError as e:
        raise DatabaseError(str(e))

def create_menu_item(db: Session, menu_item: MenuItem):
    try:
        # First check if category exists
        get_category_by_id(db, menu_item.category_id)

        db.add(menu_item)
        db.commit()
        db.refresh(menu_item)
        return menu_item
    except SQLAlchemyError as e:
        db.rollback()
        raise DatabaseError(str(e))

def update_menu_item(db: Session, item_id: int, item_data: dict):
    try:
        menu_item = get_menu_item_by_id(db, item_id)

        # If category_id is being updated, verify the new category exists
        if "category_id" in item_data:
            get_category_by_id(db, item_data["category_id"])

        for key, value in item_data.items():
            if not hasattr(menu_item, key):
                raise ValidationError(f"Invalid field: {key}")
            setattr(menu_item, key, value)

        db.commit()
        db.refresh(menu_item)
        return menu_item
    except SQLAlchemyError as e:
        db.rollback()
        raise DatabaseError(str(e))

def delete_menu_item(db: Session, item_id: int):
    try:
        menu_item = get_menu_item_by_id(db, item_id)
        db.delete(menu_item)
        db.commit()
        return {"message": f"Menu item with id {item_id} deleted successfully"}
    except SQLAlchemyError as e:
        db.rollback()
        raise DatabaseError(str(e))
