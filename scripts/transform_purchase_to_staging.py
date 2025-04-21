import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("postgresql://postgres:postgres@localhost:5432/flowmaster_ent")
print("connected to db")

print("Reading raw.purchase_transaction...")
df=pd.read_sql("SELECT * FROM raw.purchase_transaction", engine)
print(f"Raw row count: {len(df)}")
print("columns:", df.columns.tolist())

df.columns = df.columns.str.strip()

print("Removing duplicates ...")
df = df.drop_duplicates(subset=['StoreID', 'VendorID', 'DeliveryDate'])

df['OrderDate'] = pd.to_datetime(df['OrderDate'], errors='coerce')
df['DeliveryDate'] = pd.to_datetime(df['DeliveryDate'], errors='coerce')

df = df.dropna(subset=['VendorID', 'StoreID', 'OrderDate', 'DeliveryDate'])

print(f"Cleaned row count: {len(df)}")

print("Loading to staging.purchase_transaction ...")
df.to_sql('purchase_transaction', engine, schema='staging', if_exists='replace', index=False)
print("Done: staging.purchase_transaction created.")