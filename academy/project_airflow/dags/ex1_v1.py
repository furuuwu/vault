from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from python_scripts_v1 import hello_from_module_inside_dags

# Define a function inside the DAG
def hello_from_this_file():
    print("Hello!")
    print("This is printed from a function defined inside the DAG.")

# Define the DAG
with DAG(
    dag_id="ex1_v1",
    start_date=datetime(2023, 1, 1),
    schedule_interval=None,  # Trigger manually for now
    catchup=False
) as dag:

    # Task 1: Use the internal print function
    task_internal_print = PythonOperator(
        task_id="internal_print_task",
        python_callable=hello_from_this_file,
    )

    # Task 2: Use the external print function
    task_external_print = PythonOperator(
        task_id="external_print_task",
        python_callable=hello_from_module_inside_dags.say_hi,
    )

    # Set task sequence
    task_internal_print >> task_external_print