import sqlite3, csv, os

base_dir = os.path.dirname(os.path.abspath(__file__))
db_dir = os.path.join(base_dir, "..", "db")
data_dir = os.path.join(base_dir, "..", "data")

os.makedirs(db_dir, exist_ok=True)

db_path = os.path.join(db_dir, "ecom.db")

print(f"Using database at: {db_path}")
print(f"Reading CSV from: {data_dir}")


conn = sqlite3.connect(db_path)
cur = conn.cursor()


tables = {
    "customers": """
        customer_id INT,
        customer_name TEXT,
        email TEXT,
        city TEXT
    """,
    "products": """
        product_id INT,
        name TEXT,
        category TEXT,
        price REAL
    """,
    "orders": """
        order_id INT,
        customer_id INT,
        order_date TEXT,
        status TEXT
    """,
    "order_items": """
        item_id INT,
        order_id INT,
        product_id INT,
        quantity INT
    """,
    "payments": """
        payment_id INT,
        order_id INT,
        method TEXT,
        amount REAL
    """
}

print("\nCreating tables...")
for table, schema in tables.items():
    cur.execute(f"CREATE TABLE IF NOT EXISTS {table} ({schema});")
    print(f"✔ Table created: {table}")


print("\nInserting data from CSV...")

for table in tables:
    csv_path = os.path.join(data_dir, f"{table}.csv")

    if not os.path.exists(csv_path):
        print(f"⚠ CSV missing for {table}: {csv_path}")
        continue

    with open(csv_path, "r") as f:
        reader = csv.DictReader(f)
        cols = reader.fieldnames

        placeholders = ",".join(["?"] * len(cols))
        insert_sql = f"INSERT INTO {table} ({','.join(cols)}) VALUES ({placeholders})"

        count = 0
        for row in reader:
            cur.execute(insert_sql, list(row.values()))
            count += 1

        print(f"Inserted {count} rows into {table}")

# 
conn.commit()
conn.close()

print("\nBasic ingestion complete. Database is ready!")