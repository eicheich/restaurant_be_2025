import pymysql
import sys

# Print Python version and location
print(f"Python version: {sys.version}")
print(f"Python executable: {sys.executable}")

# Connection parameters
db_config = {
    "host": "localhost",
    "user": "houselab_restaurant",
    "password": "restaurantAdmin",
    "database": "houselab_restaurant_be_2025"
}

try:
    print(f"Connecting to MySQL with parameters: {db_config}")
    connection = pymysql.connect(**db_config)

    with connection.cursor() as cursor:
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()
        print("Tables in database:")
        for table in tables:
            print(f"- {table[0]}")

    connection.close()
    print("Database connection test: SUCCESS")
except Exception as e:    print(f"Database connection test: FAILED")
    print(f"Error: {e}")
    print(f"Error type: {type(e).__name__}")
    print(f"Error type: {type(e).__name__}")
