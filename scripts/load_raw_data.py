import pandas as pd
from sqlalchemy import create_engine
import os

engine = create_engine("postgresql://postgres:postgres@localhost:5432/flowmaster_ent")
print("connected to postgresql")

tables = {
         "salesTransaction.csv": "sales_transaction",
          "Product.csv": "product",
          "PurchaseTransaction.csv": "purchase_transaction",
          "Store.csv": "store",
          "Vendor.csv": "vendor"
}

for filename, table_name in tables.items():
    try:
        filepath = os.path.join("data", filename)
        print(f"\n Reading {filename}...")
        df = pd.read_csv(filepath)
        print(f"Loaded {len(df)} rows from {filename}")

        print(f"uploading to raw.{table_name}...")
        df.to_sql(table_name, engine, schema='raw', if_exists = 'replace', index=False)
        print(f"{table_name} loaded into raw schema.")

    except Exception as e:
        print(f"failed to load {filename}: {e}")

print("script done")