from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from extract_load import run as extract_load_run

default_args = {
    'owner': 'yomi',
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
    dag_id='sales_pipeline',
    default_args=default_args,
    description='ELT pipeline: extract, load, and transform sales data',
    schedule_interval='@daily',
    start_date=datetime(2026, 1, 1),
    catchup=False
) as dag:

    extract_load_task = PythonOperator(
        task_id='extract_and_load',
        python_callable=extract_load_run
    )

    dbt_run_task = BashOperator(
        task_id='dbt_run',
        bash_command='cd /opt/airflow/dbt/analytics && dbt run --profiles-dir /opt/airflow/dbt'
    )

    dbt_test_task = BashOperator(
        task_id='dbt_test',
        bash_command='cd /opt/airflow/dbt/analytics && dbt test --profiles-dir /opt/airflow/dbt'
    )

    extract_load_task >> dbt_run_task >> dbt_test_task