import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("postgresql://postgres:postgres@localhost:5432/flowmaster_ent")
print("Connected to PostgreSQL")

df = pd.read_sql("SELECT * FROM raw.store", engine)
print(f"Loaded {len(df)} rows from raw.store")

df.dropna(subset=['StoreID'], inplace=True)
df.drop_duplicates(subset=['StoreID'], inplace=True)

df.to_sql('dim_store', engine, schema='edw', if_exists='replace', index=False)
print("Done: edw.dim_store created")
