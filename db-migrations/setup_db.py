import os
import sys
import pymysql

def create_database():
    try:
        # Connect to MySQL server without specifying database
        connection = pymysql.connect(
            host='localhost',
            user='root',
            password='',  # Ganti dengan password MySQL Anda jika ada
        )

        with connection.cursor() as cursor:
            # Cek apakah database sudah ada
            cursor.execute("SHOW DATABASES LIKE 'pr_restaurant'")
            result = cursor.fetchone()

            # Jika database belum ada, buat
            if not result:
                print("Creating database 'pr_restaurant'...")
                cursor.execute("CREATE DATABASE pr_restaurant")
                print("Database 'pr_restaurant' created successfully!")
            else:
                print("Database 'pr_restaurant' already exists.")

        connection.close()
        return True
    except Exception as e:
        print(f"Error creating database: {e}")
        return False

if __name__ == "__main__":
    # Buat database jika belum ada
    if create_database():
        # Jalankan migrasi Alembic
        print("\nRunning Alembic migrations...")
        os.system("alembic revision --autogenerate -m 'initial_migration'")
        os.system("alembic upgrade head")
        print("\nDatabase setup complete!")
    else:
        print("Failed to set up database.")
        sys.exit(1)
