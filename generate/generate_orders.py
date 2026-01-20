import time
import random
import psycopg2
import os

products = [
    ("Laptop", "Electronics", 1000),
    ("Phone", "Electronics", 500),
    ("Shoes", "Fashion", 80),
    ("T-shirt", "Fashion", 20),
    ("Book", "Books", 15)
]

cities = ["Moscow", "Saint Petersburg", "Kazan", "Novosibirsk"]

conn = psycopg2.connect(
    host="postgres",
    database=os.environ.get("POSTGRES_DB"),
    user=os.environ.get("POSTGRES_USER"),
    password=os.environ.get("POSTGRES_PASSWORD")
)
cur = conn.cursor()

while True:
    product_name, category, price = random.choice(products)
    quantity = random.randint(1, 5)
    city = random.choice(cities)
    cur.execute(
        "INSERT INTO orders (product_name, category, price, quantity, city) VALUES (%s,%s,%s,%s,%s)",
        (product_name, category, price, quantity, city)
    )
    conn.commit()
    time.sleep(1)
