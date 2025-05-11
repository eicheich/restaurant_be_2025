# Restaurant API Backend

This is a FastAPI backend for managing restaurant data, including menu categories, menu items, and articles.

## Features

- Menu management (categories and items)
- Article/news management
- Image upload and processing
- Database migrations using Alembic

## Development Setup

1. Clone the repository
2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Set up the database:
   ```
   cd db-migrations
   python setup_db.py
   ```
5. Run the application:
   ```
   uvicorn main:app --reload
   ```

## API Documentation

Once the server is running, visit:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Deployment

For deployment instructions, see the [Deployment Guide](DEPLOYMENT-GUIDE.md).
