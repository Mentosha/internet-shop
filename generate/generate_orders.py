import time
import random
import psycopg2
import os
from psycopg2 import OperationalError

# Переменные окружения
POSTGRES_HOST = "postgres"
POSTGRES_DB = os.getenv("POSTGRES_DB")
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")


products = [
    ("Laptop", "Electronics", 1000),
    ("Phone", "Electronics", 500),
    ("Shoes", "Fashion", 80),
    ("T-shirt", "Fashion", 20),
    ("Book", "Books", 15)
]

cities = ["Moscow", "Saint Petersburg", "Kazan", "Novosibirsk"]

# Ждём готовности Postgres
while True:
    try:
        conn = psycopg2.connect(
            host=POSTGRES_HOST,
            database=POSTGRES_DB,
            user=POSTGRES_USER,
            password=POSTGRES_PASSWORD
        )
        print("Postgres доступен!")
        break
    except OperationalError:
        print("Postgres ещё не готов, ждём 3 секунды...")
        time.sleep(3)

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
    print(f"Создан заказ: {product_name} x{quantity} в {city}")
    time.sleep(1)
