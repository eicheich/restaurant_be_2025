from fastapi import FastAPI
from routes import router
from models import create_tables

app = FastAPI(title="Restaurant API")

# Include all routes
app.include_router(router)

# Create database tables if they don't exist
create_tables()
