from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import pandas as pd
from airflow.models import BaseOperator

def pull_filename_from_xcom(**kwargs) -> str:
    task_instance: BaseOperator = kwargs['ti']

    # this changes
    file_name = task_instance.xcom_pull(
        dag_id='ex6_v2_parent',  # Specify the parent DAG's ID
        task_ids='push_file_name',  # Task ID in the parent DAG
        key='file_name'  # Key used when pushing data
    )
    print(f"Pulled file name from XCom: {file_name}")
    return file_name

def load_and_print_dataframe(file_name: str) -> None:

    file_path = f"/opt/airflow/data/{file_name}"
    df = pd.read_csv(file_path)
    print(f"DataFrame from file {file_name}:")
    print(df)

def handler(**kwargs) -> None:
    file_name = pull_filename_from_xcom(**kwargs)
    load_and_print_dataframe(file_name)

with DAG(
    dag_id = 'ex6_v2_child',
    schedule_interval=None,
    start_date=datetime(2023, 1, 1),
    catchup=False,
) as child_dag:
    pull_task = PythonOperator(
        task_id='pull_file_name',
        python_callable=handler,
    )
