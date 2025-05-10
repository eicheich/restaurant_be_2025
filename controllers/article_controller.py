from sqlalchemy.orm import Session
from models import Article
from fastapi import HTTPException

def get_all_articles(db: Session):
    return db.query(Article).all()

def get_article_by_id(db: Session, article_id: int):
    article = db.query(Article).filter(Article.id == article_id).first()
    if article is None:
        raise HTTPException(status_code=404, detail="Article not found")
    return article

def create_article(db: Session, article: Article):
    db.add(article)
    db.commit()
    db.refresh(article)
    return article

def update_article(db: Session, article_id: int, article_data: dict):
    article = get_article_by_id(db, article_id)

    for key, value in article_data.items():
        setattr(article, key, value)

    db.commit()
    db.refresh(article)
    return article

def delete_article(db: Session, article_id: int):
    article = get_article_by_id(db, article_id)

    db.delete(article)
    db.commit()
    return {"message": f"Article with id {article_id} deleted successfully"}
