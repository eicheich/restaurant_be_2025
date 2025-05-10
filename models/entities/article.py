from sqlalchemy import Column, Integer, String, Text, Date
from models import Base

class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, index=True)
    writer = Column(String(255), nullable=True)
    date = Column(Date, nullable=False)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)
    content = Column(Text, nullable=False)
    image = Column(String(255), nullable=False)
