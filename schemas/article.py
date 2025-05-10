from pydantic import BaseModel
from typing import Optional
from datetime import date

class ArticleBase(BaseModel):
    writer: Optional[str] = None
    date: date
    title: str
    description: str
    content: str
    image: str

class ArticleCreate(ArticleBase):
    pass

class ArticleUpdate(BaseModel):
    writer: Optional[str] = None
    date: Optional[date] = None
    title: Optional[str] = None
    description: Optional[str] = None
    content: Optional[str] = None
    image: Optional[str] = None

class ArticleInDB(ArticleBase):
    id: int

    class Config:
        orm_mode = True

class Article(ArticleInDB):
    pass
