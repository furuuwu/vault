from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import pandas as pd

# Function to push the filename to XCom
def push_filename_to_xcom(**kwargs):
    # Push the file name to XCom
    file_name = 'titanic.csv'  # Example file name, can be dynamic as needed
    kwargs['ti'].xcom_push(key='file_name', value=file_name)
    print(f"Pushed file name {file_name} to XCom")

# Function to pull the filename from XCom
def pull_filename_from_xcom(**kwargs):
    # Pull the file name from XCom
    file_name = kwargs['ti'].xcom_pull(task_ids='push_file_name', key='file_name')
    return file_name

def load_and_print_dataframe(file_name: str):
    # Construct the full path to the file
    file_path = f"/opt/airflow/data/{file_name}"

    # Read the CSV into a pandas DataFrame
    df = pd.read_csv(file_path)
    
    # Print the DataFrame
    print(f"DataFrame from file {file_name}:")
    print(df)


def handler(**kwargs):
    
    file_name = pull_filename_from_xcom(**kwargs)
    load_and_print_dataframe(file_name)

dag = DAG(
    'ex6_v1',
    description='DAG that pushes and pulls data from XCom',
    schedule_interval=None,  # No schedule, manually triggered
    start_date=datetime(2024, 12, 20),
    catchup=False,
)

# Task 1: Push file name to XCom
push_file_task = PythonOperator(
    task_id='push_file_name',
    python_callable=push_filename_to_xcom,
    provide_context=True,  # Allows passing the context to the function
    dag=dag,
)

# Task 2: Pull file name from XCom and print the DataFrame
print_df_task = PythonOperator(
    task_id='print_dataframe',
    python_callable=handler,
    provide_context=True,
    dag=dag,
)

push_file_task >> print_df_task
