from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from controllers.article_controller import get_all_articles, create_article, get_article_by_id, update_article, delete_article
from models import Article as ArticleModel
from schemas.article import Article, ArticleCreate, ArticleUpdate
from routes import get_db
from typing import List

article_router = APIRouter(
    prefix="/articles",
    tags=["articles"],
)

@article_router.get("/", response_model=List[Article])
def read_articles(db: Session = Depends(get_db)):
    return get_all_articles(db)

@article_router.get("/{article_id}", response_model=Article)
def read_article(article_id: int, db: Session = Depends(get_db)):
    return get_article_by_id(db, article_id)

@article_router.post("/", response_model=Article, status_code=201)
def add_article(article: ArticleCreate, db: Session = Depends(get_db)):
    db_article = ArticleModel(
        writer=article.writer,
        date=article.date,
        title=article.title,
        description=article.description,
        content=article.content,
        image=article.image
    )
    return create_article(db, db_article)

@article_router.put("/{article_id}", response_model=Article)
def update_article_endpoint(article_id: int, article_data: ArticleUpdate, db: Session = Depends(get_db)):
    return update_article(db, article_id, article_data.dict(exclude_unset=True))

@article_router.delete("/{article_id}")
def delete_article_endpoint(article_id: int, db: Session = Depends(get_db)):
    return delete_article(db, article_id)
