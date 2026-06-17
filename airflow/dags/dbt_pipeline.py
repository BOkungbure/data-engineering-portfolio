from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="dbt_pipeline",
    start_date=datetime(2024, 1, 1),
    schedule_interval="@daily",
    catchup=False
) as dag:

    dbt_seed = BashOperator(
        task_id="dbt_seed",
        bash_command="cd /path/to/my_pipeline && dbt seed"
    )

    dbt_run = BashOperator(
        task_id="dbt_run",
        bash_command="cd /path/to/my_pipeline && dbt run"
    )

    dbt_test = BashOperator(
        task_id="dbt_test",
        bash_command="cd /path/to/my_pipeline && dbt test"
    )

    dbt_seed >> dbt_run >> dbt_test