from airflow import DAG
from airflow.operators.empty import EmptyOperator
from datetime import datetime

# Define the DAG
with DAG(
    dag_id="my_first_dag",
    start_date=datetime(2024, 1, 1),  # Start date in the past to be picked up
    schedule_interval="@daily",  # Runs daily
    catchup=False,  # Avoid backfilling old runs
) as dag:

    start = EmptyOperator(task_id="start")
    end = EmptyOperator(task_id="end")

    start >> end  # Define task dependencies
