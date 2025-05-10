from pydantic import BaseModel
from typing import Optional, List

# Category schemas
class CategoryBase(BaseModel):
    name: str

class CategoryCreate(CategoryBase):
    pass

class CategoryUpdate(BaseModel):
    name: Optional[str] = None

class CategoryInDB(CategoryBase):
    id: int

    class Config:
        orm_mode = True

class Category(CategoryInDB):
    pass

# Menu item schemas
class MenuItemBase(BaseModel):
    category_id: int
    image: str
    title: str
    description: str
    rate: float
    total_review: int
    price: float

class MenuItemCreate(MenuItemBase):
    pass

class MenuItemUpdate(BaseModel):
    category_id: Optional[int] = None
    image: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    rate: Optional[float] = None
    total_review: Optional[int] = None
    price: Optional[float] = None

class MenuItemInDB(MenuItemBase):
    id: int

    class Config:
        orm_mode = True

class MenuItem(MenuItemInDB):
    pass
