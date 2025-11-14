E-Commerce Data Ingestion Project

This project loads multiple e-commerce CSV files into a SQLite database and performs analytics. It demonstrates clean backend structure, data processing, SQL skills, and Python scripting.

Folder Structure:

     data - CSV datasets
     db - SQLite database and schema
     scripts - Ingestion scripts (basic, pandas, sqlalchemy)
     analytics - SQL queries
     diagrams - ER diagram 

How to Run:
Install required libraries:

    1.	pip install -r requirements.txt
Run ingestion scripts:

	2.	python3 scripts/ingest_basic.py
	python3 scripts/ingest_pandas.py
	python3 scripts/ingest_sqlalchemy.py
Open the SQLite database:

	3.	sqlite3 db/ecommerce.db
Run analytics:

	4.	.read analytics/top_customers.sql


Key Features:
  
    •   Loads customers, products, orders, order items, and payments data.
	•	Creates relational tables in SQLite.
	•	Supports basic ingestion, pandas ingestion, and sqlalchemy ingestion.
	•	Includes analytics such as top customers and revenue summary.
	•	Clean and interview-ready project structure.

Example SQL Query (Top Customers):

    SELECT c.customer_id, c.name, SUM(oi.subtotal) AS total_spent
    FROM customers c
    JOIN orders o ON c.customer_id = o.customer_id
    JOIN order_items oi ON o.order_id = oi.order_id
    GROUP BY c.customer_id
    ORDER BY total_spent DESC;

