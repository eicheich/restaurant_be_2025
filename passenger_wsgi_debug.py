#!/usr/bin/env python3
import sys
import os

print("Python Diagnostic Information")
print("-" * 40)
print(f"Python version: {sys.version}")
print(f"Python executable: {sys.executable}")
print(f"Current working directory: {os.getcwd()}")

try:
    from main import app
    print("✅ Successfully imported main app")
except Exception as e:
    print(f"❌ Error importing main app: {e}")
    print(f"Error type: {type(e).__name__}")

try:
    import fastapi
    print(f"✅ FastAPI version: {fastapi.__version__}")
except Exception as e:
    print(f"❌ Error importing FastAPI: {e}")

try:
    from models import create_tables
    print("✅ Successfully imported models")
except Exception as e:
    print(f"❌ Error importing models: {e}")
    print(f"Error type: {type(e).__name__}")

print("\nEnvironment Variables:")
for key, value in os.environ.items():
    if "PATH" in key or "SECRET" in key.upper() or "PASSWORD" in key.upper():
        print(f"{key}=[HIDDEN]")
    else:
        print(f"{key}={value}")

print("\nChecking module paths:")
for path in sys.path:
    print(f"- {path}")
