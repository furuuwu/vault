from airflow import DAG
from datetime import datetime
from airflow.operators.python import PythonOperator

from python_scripts_v1.ex3_helper import run_query

default_args = {
    'owner': 'airflow',
    'retries': 1,
}

with DAG(
    dag_id = 'ex3',
    default_args = default_args,
    start_date = datetime(2024, 12, 19),
    schedule_interval = None,
    catchup = False
) as dag:
    
    query_task = PythonOperator(
        task_id = 'query_with_a_join',
        python_callable = run_query,
    )