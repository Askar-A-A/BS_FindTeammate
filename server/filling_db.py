from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Player  # Import your Base and Player model
import random

# Database connection string
DATABASE_URL = "postgresql://username:password@localhost/dbname"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create tables (if they don't exist)
Base.metadata.create_all(bind=engine)

# Function to generate random players data
def generate_players_data(n):
    brawlers = ["Kit", "Pearl", "Charlie", "Maisie", "Mandy", "Sam", "Chuck",
                "Lola", "Ash", "Doug", "Colette", "Belle", "Willow", "Spike",
                "R-T", "Hank", "Meg", "Buster", "Leon", "Amber", "Chester",
                "Sandy", "Crow", "Gale", "Janet", "Nani", "Otis", "Bonnie",
                "Piper", "Cordelius", "Byron", "Squeak", "Mico", "Grom",
                "Gus", "Bibi", "Mr. P", "Gene", "Eve", "Sprout", "Tara",
                "Gray", "Max", "Pam", "Rico", "Griff", "Ruffs", "Edgar",
                "Buzz", "Mortis", "Tick", "Stu", "Penny", "Carl", "Fang",
                "Frank", "Bea", "Lou", "Darryl", "8-Bit", "Bo", "Emz",
                "Dynamike", "Rosa", "Bull", "Barley", "Surge", "Brock",
                "Colt", "Jacky", "Poco", "El Primo", "Jessie", "Nita",
                "Larry & Lawrie", "Shelly"]

    for _ in range(n):
        yield Player(
            username=f"user{random.randint(1000, 9999)}",
            trophies=random.randint(0, 10000),
            favorite_brawler=random.choice(brawlers),
            is_looking_for_clan=random.choice([True, False]),
            win_rate=round(random.uniform(0, 1), 2),
            games_won=random.randint(0, 500)
        )

def populate_db():
    db = SessionLocal()
    try:
        players = list(generate_players_data(100))  # Generate 100 random players
        db.add_all(players)
        db.commit()
    except Exception as e:
        print(f"An error occurred: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    populate_db()
    print("Database populated with random players data.")
