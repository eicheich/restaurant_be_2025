from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from models import Article
from exceptions import DatabaseError, ResourceNotFoundError, ValidationError

def get_all_articles(db: Session):
    try:
        return db.query(Article).all()
    except SQLAlchemyError as e:
        raise DatabaseError(str(e))

def get_article_by_id(db: Session, article_id: int):
    try:
        article = db.query(Article).filter(Article.id == article_id).first()
        if article is None:
            raise ResourceNotFoundError("Article", article_id)
        return article
    except SQLAlchemyError as e:
        raise DatabaseError(str(e))

def create_article(db: Session, article: Article):
    try:
        db.add(article)
        db.commit()
        db.refresh(article)
        return article
    except SQLAlchemyError as e:
        db.rollback()
        raise DatabaseError(str(e))

def update_article(db: Session, article_id: int, article_data: dict):
    try:
        article = get_article_by_id(db, article_id)

        for key, value in article_data.items():
            if not hasattr(article, key):
                raise ValidationError(f"Invalid field: {key}")
            setattr(article, key, value)

        db.commit()
        db.refresh(article)
        return article
    except SQLAlchemyError as e:
        db.rollback()
        raise DatabaseError(str(e))

def delete_article(db: Session, article_id: int):
    try:
        article = get_article_by_id(db, article_id)
        db.delete(article)
        db.commit()
        return {"message": f"Article with id {article_id} deleted successfully"}
    except SQLAlchemyError as e:
        db.rollback()
        raise DatabaseError(str(e))
