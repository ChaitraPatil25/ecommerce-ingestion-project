
from sqlalchemy import create_engine
import pandas as pd
import os

db_path = os.path.join(os.path.dirname(__file__), "..","db","ecom.db")
data_dir = os.path.join(os.path.dirname(__file__), "..","data")

engine=create_engine(f"sqlite:///{db_path}")

tables=["customers","products","orders","order_items","payments"]
for t in tables:
    df=pd.read_csv(os.path.join(data_dir,f"{t}.csv"))
    df.to_sql(t,engine,if_exists="replace",index=False)

print("SQLAlchemy ingestion complete.")
