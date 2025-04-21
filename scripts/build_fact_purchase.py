import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("postgresql://postgres:postgres@localhost:5432/flowmaster_ent")
print("connected to db")

df = pd.read_sql("SELECT * FROM staging.purchase_transaction", engine)
print(f"Loaded {len(df)} rows from staging.purchase_transaction")

df['DeliveryDays'] = (pd.to_datetime(df['DeliveryDate']) - pd.to_datetime(df['OrderDate'])).dt.days

fact_df = df[['TransactionID', 'TransactionNO', 'OrderDate', 'DeliveryDate', 'VendorID', 'StoreID',
              'ProductID', 'Quantity', 'LineAmount', 'TaxAmount', 'DeliveryDays']]

print("Uploading to edw.fact_purchase ...")
fact_df.to_sql('fact_purchase', engine, schema='edw', if_exists='replace', index=False)
print("Done: edw.fact_purchase created.")