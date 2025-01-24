from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

# Define a function to accept the execution date
def print_execution_date(ds):
    print(f"The execution date is: {ds}")


dag = DAG(
    dag_id = 'ex5',
    description='A DAG that detects the {ds} macro',
    schedule_interval=None,  # Set to None to trigger manually
    start_date=datetime(2024, 12, 20),
    catchup=False,
)

# PythonOperator to execute the function with the {ds} macro as argument
print_ds_task = PythonOperator(
    task_id='print_ds_task',
    python_callable=print_execution_date,
    op_args=['{{ ds }}'],  # Pass the macro value {ds} as an argument
    dag=dag,
)

print_ds_task
