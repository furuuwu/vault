"""
This DAG calls the function to load the Titanic dataset.
"""

from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from python_scripts_v1.titanic_to_mariadb import load_csv_to_mariadb

def handler():
    load_csv_to_mariadb()

with DAG(
    dag_id="ex2",
    start_date=datetime(2023, 1, 1),
    schedule_interval=None,  # Trigger manually
    catchup=False,
) as dag:

    # Task: Load CSV to MariaDB
    load_csv_task = PythonOperator(
        task_id="load_csv_to_mariadb",
        python_callable=handler,
    )

    load_csv_task