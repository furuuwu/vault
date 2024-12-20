from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import sys

def hello_from_this_file():
    print("Hello!")
    print("This is printed from a function defined inside the DAG.")

def handler():
    hello_from_module_outside_dags.say_hi()

with DAG(
    dag_id="ex1_v2",
    start_date=datetime(2023, 1, 1),
    schedule_interval=None,  # Trigger manually for now
    catchup=False
) as dag:
    
    # Define the path to the python_scripts folder
    python_scripts_path = '/opt/airflow/python_scripts'
    # python_scripts_path = '/opt/airflow'

    # Append the python_scripts path to sys.path if not already there
    if python_scripts_path not in sys.path:
        sys.path.append(python_scripts_path)

    # from python_scripts.hello_from_module_outside_dags import say_hi
    # from python_scripts import hello_from_module_outside_dags
    import hello_from_module_outside_dags
    

    # Task 1
    task_internal_print = PythonOperator(
        task_id="internal_print_task",
        python_callable=hello_from_this_file,
    )

    # Task 2
    task_external_print = PythonOperator(
        task_id="external_print_task",
        python_callable=handler,
    )

    task_internal_print >> task_external_print
