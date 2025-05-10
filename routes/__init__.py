from fastapi import APIRouter
from sqlalchemy.orm import Session
from models import SessionLocal

router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Import routers after the get_db dependency is defined
from routes.article_routes import article_router
from routes.menu_routes import menu_router

router.include_router(article_router)
router.include_router(menu_router)
