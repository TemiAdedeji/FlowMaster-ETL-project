import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("postgresql://postgres:postgres@localhost:5432/flowmaster_ent")
print("Connected to PostgreSQL")

df = pd.read_sql("SELECT * FROM raw.vendor", engine)
print(f"Loaded {len(df)} rows from raw.vendor")

df.dropna(subset=['VendorID'], inplace=True)
df.drop_duplicates(subset=['VendorID'], inplace=True)

df.to_sql('dim_vendor', engine, schema='edw', if_exists='replace', index=False)
print("Done: edw.dim_vendor created")
