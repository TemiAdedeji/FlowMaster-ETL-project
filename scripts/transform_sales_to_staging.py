import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("postgresql://postgres:postgres@localhost:5432/flowmaster_ent")
print("Connected to PostgreSQL")

print("Reading raw.sales_transaction...")
df = pd.read_sql("SELECT * FROM raw.sales_transaction", engine)

print(f" Raw row count: {len(df)}")
print("🧾 Columns:", df.columns.tolist())

print("Cleaning data...")
df = df[(df['Quantity'] > 0) & (df['LineAmount'] > 0)]
df['TransDate'] = pd.to_datetime(df['TransDate'], errors='coerce')
df = df.dropna(subset=['TransDate'])

print(f"Cleaned row count:{len(df)}")

print("Uploading to staging.sales_transaction...")
df.to_sql('sales_transaction', engine, schema = 'staging', if_exists = 'replace', index = False)

print("Done: staging.sales_transaction is ready.")