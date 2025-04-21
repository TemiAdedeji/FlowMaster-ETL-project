import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("postgresql://postgres:postgres@localhost:5432/flowmaster_ent")
print("connected to db")

df= pd.read_sql("SELECT * FROM staging.sales_transaction", engine)
print(f"{len(df)} rows loaded from staging")

df['UnitPrice'] = df['LineAmount']/df['Quantity']

fact_df = df[['TransactionID', 'TransactionNO', 'TransDate', 'ProductID', 'StoreID',
             'Quantity', 'LineAmount', 'TaxAmount', 'LineDiscountAmount', 'UnitPrice']]

print("Loading to edw.fact_sales ...")
fact_df.to_sql('fact_sales', engine, schema='edw', if_exists='replace', index=False)

print("Done: edw.fact_sales created.")