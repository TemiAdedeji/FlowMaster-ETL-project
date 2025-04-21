from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    'owner': 'Temi Adedeji',
    'start_date': datetime(2024, 1, 1),
    'retries': 1,
}

with DAG(
    dag_id='retail_sales_etl_pipeline',
    default_args=default_args,
    schedule_interval=None,
    catchup=False,
    tags=['flowmasters', 'etl', 'retail'],
) as dag:

    load_raw_data = BashOperator(
        task_id='load_raw_data',
        bash_command='python scripts/load_raw_data.py'
    )

    transform_sales = BashOperator(
        task_id='transform_sales_to_staging',
        bash_command='python scripts/transform_sales_to_staging.py'
    )

    transform_purchase = BashOperator(
        task_id='transform_purchase_to_staging',
        bash_command='python scripts/transform_purchase_to_staging.py'
    )

    transform_store = BashOperator(
        task_id='transform_store_to_edw',
        bash_command='python scripts/transform_store_to_edw.py'
    )

    transform_product = BashOperator(
        task_id='transform_product_to_edw',
        bash_command='python scripts/transform_product_to_edw.py'
    )

    transform_vendor = BashOperator(
        task_id='transform_vendor_to_edw',
        bash_command='python scripts/transform_vendor_to_edw.py'
    )

    build_fact_sales = BashOperator(
        task_id='build_fact_sales',
        bash_command='python scripts/build_fact_sales.py'
    )

    build_fact_purchase = BashOperator(
        task_id='build_fact_purchase',
        bash_command='python scripts/build_fact_purchase.py'
    )

    load_raw_data >> [transform_sales, transform_purchase]
    transform_sales >> build_fact_sales
    transform_purchase >> build_fact_purchase
    load_raw_data >> [transform_store, transform_product, transform_vendor]
