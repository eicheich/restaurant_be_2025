#!/usr/bin/env python
# Standar WSGI wrapper untuk digunakan dengan Apache atau Gunicorn

import os
import sys
from main import app as application

# Untuk debugging
if __name__ == "__main__":
    print(f"Python version: {sys.version}")
    print(f"Python executable: {sys.executable}")
    print("WSGI application loaded successfully!")
