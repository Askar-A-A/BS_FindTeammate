import psycopg2
import random


dbname = "bsfind_db"
user = "postgres"
password = "plmoknijbuhvuhhu123"
host = "localhost"  


conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
cur = conn.cursor()


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
                "Larry & Lawrie", "Shelly"]  # Add all brawlers here
    for i in range(1, n + 1):
        username = f"user{i}"
        trophies = random.randint(0, 65000)
        favorite_brawler = random.choice(brawlers)
        is_looking_for_clan = random.choice([True, False])
        win_rate = round(random.uniform(0, 1), 2)
        games_won = random.randint(0, 100000)

        yield (username, trophies, favorite_brawler, is_looking_for_clan, win_rate, games_won)


try:
    cur.executemany("INSERT INTO players (username, trophies, favorite_brawler, is_looking_for_clan, win_rate, games_won) VALUES (%s, %s, %s, %s, %s, %s)", list(generate_players_data(10000)))
    conn.commit()
except Exception as e:
    print(f"An error occurred: {e}")
    conn.rollback()
finally:
    cur.close()
    conn.close()

print("Database populated with random players data.")
