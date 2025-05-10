from datetime import date
from models import SessionLocal, create_tables
from models.entities.menu import MenuCategory, MenuItem
from models.entities.article import Article

def seed_database():
    db = SessionLocal()
    try:
        # Create database tables
        create_tables()

        # Check if data already exists
        if db.query(MenuCategory).count() > 0:
            print("Database already seeded, skipping...")
            return

        # Seed menu categories
        appetizers = MenuCategory(name="Appetizers")
        main_course = MenuCategory(name="Main Course")
        desserts = MenuCategory(name="Desserts")
        beverages = MenuCategory(name="Beverages")

        db.add_all([appetizers, main_course, desserts, beverages])
        db.commit()

        # Seed menu items
        menu_items = [
            # Appetizers
            MenuItem(
                category_id=1,  # Appetizers
                image="spring_rolls.jpg",
                title="Vegetable Spring Rolls",
                description="Crispy rolls filled with fresh vegetables",
                rate=4.5,
                total_review=120,
                price=5.99
            ),
            MenuItem(
                category_id=1,  # Appetizers
                image="chicken_wings.jpg",
                title="Spicy Chicken Wings",
                description="Crispy chicken wings with hot sauce",
                rate=4.7,
                total_review=150,
                price=8.99
            ),

            # Main Course
            MenuItem(
                category_id=2,  # Main Course
                image="grilled_salmon.jpg",
                title="Grilled Salmon",
                description="Fresh salmon with lemon and herbs",
                rate=4.8,
                total_review=200,
                price=16.99
            ),
            MenuItem(
                category_id=2,  # Main Course
                image="beef_steak.jpg",
                title="Beef Steak",
                description="Premium beef steak with side vegetables",
                rate=4.9,
                total_review=180,
                price=19.99
            ),

            # Desserts
            MenuItem(
                category_id=3,  # Desserts
                image="chocolate_cake.jpg",
                title="Chocolate Cake",
                description="Rich chocolate cake with vanilla ice cream",
                rate=4.6,
                total_review=90,
                price=6.99
            ),

            # Beverages
            MenuItem(
                category_id=4,  # Beverages
                image="iced_tea.jpg",
                title="Iced Tea",
                description="Refreshing iced tea with lemon",
                rate=4.3,
                total_review=70,
                price=2.99
            ),
        ]

        db.add_all(menu_items)
        db.commit()

        # Seed articles
        articles = [
            Article(
                writer="John Doe",
                date=date(2025, 5, 1),
                title="The Art of Cooking",
                description="Exploring the beauty of culinary arts",
                content="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed euismod, urna eu tincidunt consectetur, nisl nunc euismod nisi, eu porttitor nisl nisi eu nisi.",
                image="cooking_art.jpg"
            ),
            Article(
                writer=None,
                date=date(2025, 5, 7),
                title="Healthy Eating Habits",
                description="Tips for maintaining a healthy diet",
                content="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed euismod, urna eu tincidunt consectetur, nisl nunc euismod nisi, eu porttitor nisl nisi eu nisi.",
                image="healthy_eating.jpg"
            ),
        ]

        db.add_all(articles)
        db.commit()

        print("Database seeded successfully!")

    finally:
        db.close()

if __name__ == "__main__":
    seed_database()
