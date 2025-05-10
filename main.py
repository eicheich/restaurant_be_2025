from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routes import router
from models import create_tables

app = FastAPI(title="Restaurant API")

# Mount static files directory
app.mount("/static", StaticFiles(directory="static"), name="static")

# Include all routes
app.include_router(router)

# Create database tables if they don't exist
create_tables()
