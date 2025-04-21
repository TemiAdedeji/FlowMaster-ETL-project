import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("postgresql://postgres:postgres@localhost:5432/flowmaster_ent")
print("Connected to PostgreSQL")

df = pd.read_sql("SELECT * FROM raw.product", engine)
print(f"Loaded {len(df)} rows from raw.product")


df.dropna(subset=['ProductID'], inplace=True)
df.drop_duplicates(subset=['ProductID'], inplace=True)

df.to_sql('dim_product', engine, schema='edw', if_exists='replace', index=False)
print(" Done: edw.dim_product created")
