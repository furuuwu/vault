from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import pandas as pd
from airflow.models import DagRun

def get_filename_from_conf(**kwargs) -> str:
    dagrun_instance: DagRun = kwargs['dag_run']
    # The dag_run key represents the DagRun object of the currently executing DAG run
    file_name = dagrun_instance.conf.get('file_name')
    return file_name


def load_and_print_dataframe(file_name: str):
    file_path = f"/opt/airflow/data/{file_name}"
    df = pd.read_csv(file_path)
    print(f"DataFrame from file {file_name}:")
    print(df)


def handler(**kwargs):
    file_name = get_filename_from_conf(**kwargs)
    load_and_print_dataframe(file_name)

with DAG(
    dag_id = 'ex6_v3_child',
    schedule_interval=None,
    start_date=datetime(2023, 1, 1),
    catchup=False,
) as child_dag:
    pull_task = PythonOperator(
        task_id='pull_file_name',
        python_callable=handler,
    )
