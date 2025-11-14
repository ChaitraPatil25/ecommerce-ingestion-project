
import sqlite3, csv, os

db_path = os.path.join(os.path.dirname(__file__), "..", "db", "ecom.db")
data_dir = os.path.join(os.path.dirname(__file__), "..", "data")

conn = sqlite3.connect(db_path)
cur = conn.cursor()

tables = {
    "customers": "customer_id INT, customer_name TEXT, email TEXT, city TEXT",
    "products": "product_id INT, name TEXT, category TEXT, price REAL",
    "orders": "order_id INT, customer_id INT, order_date TEXT, status TEXT",
    "order_items": "item_id INT, order_id INT, product_id INT, quantity INT",
    "payments": "payment_id INT, order_id INT, method TEXT, amount REAL"
}

for table, schema in tables.items():
    cur.execute(f"CREATE TABLE IF NOT EXISTS {table} ({schema});")

for table in tables:
    with open(os.path.join(data_dir, f"{table}.csv"), "r") as f:
        reader = csv.DictReader(f)
        cols = reader.fieldnames
        for r in reader:
            placeholders=",".join(["?"]*len(cols))
            cur.execute(f"INSERT INTO {table} ({','.join(cols)}) VALUES ({placeholders})", list(r.values()))

conn.commit()
conn.close()
print("Basic ingestion complete.")
