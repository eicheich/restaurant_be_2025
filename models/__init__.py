from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Replace with your actual MySQL credentials
DATABASE_URL = "mysql+pymysql://root:@localhost/pr_restaurant"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Import entities after Base is defined to avoid circular imports
from models.entities.menu import MenuCategory, MenuItem
from models.entities.article import Article

# Create all tables
def create_tables():
    Base.metadata.create_all(bind=engine)
