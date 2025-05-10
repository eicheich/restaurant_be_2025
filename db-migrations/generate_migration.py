import os
import sys
from pathlib import Path

# Add parent directory to Python path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

def generate_migration(message):
    """Generate a new migration with the given message."""
    os.system(f'alembic -c alembic.ini revision --autogenerate -m "{message}"')

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python generate_migration.py \"Migration message\"")
        sys.exit(1)

    message = sys.argv[1]
    generate_migration(message)
