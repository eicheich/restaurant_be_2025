from sqlalchemy.orm import Session
from models import MenuCategory, MenuItem, Article

def get_all_categories(db: Session):
    return db.query(MenuCategory).all()

def get_all_menu_items(db: Session):
    return db.query(MenuItem).all()

def get_all_articles(db: Session):
    return db.query(Article).all()

def create_category(db: Session, category: MenuCategory):
    db.add(category)
    db.commit()
    db.refresh(category)
    return category

def create_menu_item(db: Session, menu_item: MenuItem):
    db.add(menu_item)
    db.commit()
    db.refresh(menu_item)
    return menu_item

def create_article(db: Session, article: Article):
    db.add(article)
    db.commit()
    db.refresh(article)
    return article
