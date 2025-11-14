
import pandas as pd
import sqlite3, os

db_path = os.path.join(os.path.dirname(__file__), "..", "db", "ecom.db")
data_dir = os.path.join(os.path.dirname(__file__), "..", "data")

conn=sqlite3.connect(db_path)

files=["customers","products","orders","order_items","payments"]
for f in files:
    df=pd.read_csv(os.path.join(data_dir,f"{f}.csv"))
    df.to_sql(f,conn,if_exists="replace",index=False)

conn.close()
print("Pandas ingestion complete.")
