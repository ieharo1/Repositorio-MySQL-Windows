import os
import random
import string
import time
from datetime import datetime, timedelta

import mysql.connector

MYSQL_HOST = os.getenv("MYSQL_HOST", "mysql")
MYSQL_PORT = int(os.getenv("MYSQL_PORT", "3306"))
MYSQL_USER = os.getenv("MYSQL_USER", "sales")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD", "salespass")
MYSQL_DB = os.getenv("MYSQL_DB", "salesdb")

REGIONS = ["NORTE", "SUR", "ESTE", "OESTE"]
PRODUCTS = ["LAPTOP", "MOUSE", "TECLADO", "MONITOR", "CELULAR", "IMPRESORA"]


def random_customer_id():
    return "C" + "".join(random.choices(string.digits, k=6))


def random_date(days_back=30):
    base = datetime.utcnow()
    delta = timedelta(days=random.randint(0, days_back))
    return base - delta


def generate_sales(n=1000):
    rows = []
    for _ in range(n):
        rows.append(
            (
                random_customer_id(),
                random.choice(PRODUCTS),
                random.choice(REGIONS),
                random.randint(1, 5),
                round(random.uniform(10, 1500), 2),
                random_date().strftime("%Y-%m-%d %H:%M:%S"),
            )
        )
    return rows


def main():
    print("Conectando a MySQL...")
    conn = mysql.connector.connect(
        host=MYSQL_HOST,
        port=MYSQL_PORT,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DB,
    )
    cursor = conn.cursor()

    while True:
        rows = generate_sales(500)
        cursor.executemany(
            """
            INSERT INTO sales (customer_id, product, region, quantity, price, sold_at)
            VALUES (%s, %s, %s, %s, %s, %s)
            """,
            rows,
        )
        conn.commit()
        print(f"Insertados {len(rows)} registros de ventas.")
        time.sleep(5)


if __name__ == "__main__":
    main()

