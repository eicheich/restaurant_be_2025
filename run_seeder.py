#!/usr/bin/env python
"""
Script untuk menjalankan database seeder di lingkungan cPanel
"""
import os
import sys

# Set environment variable agar berjalan di lingkungan production
os.environ["ENVIRONMENT"] = "production"

try:
    from db_seeder import seed_database
    print("Running database seeder in production environment...")
    seed_database()
    print("Database seeded successfully!")
except Exception as e:
    print(f"Error seeding database: {e}")
    sys.exit(1)
