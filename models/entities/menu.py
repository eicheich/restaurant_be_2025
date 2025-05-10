from sqlalchemy import Column, Integer, String, Float, Text
from models import Base

class MenuCategory(Base):
    __tablename__ = "menu_categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)

class MenuItem(Base):
    __tablename__ = "menu_items"

    id = Column(Integer, primary_key=True, index=True)
    category_id = Column(Integer, nullable=False)
    image = Column(String(255), nullable=False)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)
    rate = Column(Float, nullable=False)
    total_review = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)
