"""
Idk why but, Xcoms don't seem to work. Namely:
* the parent dag indeed sends the XCom message. It shows up in Admin>XComs
* the child dag however, always reads the value None

ex6_v2_parent.py and ex6_v2_child.py exemplify that. 
"""

from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from airflow.models import BaseOperator

# same as before
def push_filename_to_xcom(**kwargs) -> None:
    file_name = 'titanic.csv'
    task_instance: BaseOperator = kwargs['ti']
    task_instance.xcom_push(key='file_name', value=file_name)
    print(f"Pushed file name {file_name} to XCom")

with DAG(
    dag_id = 'ex6_v2_parent',
    schedule_interval=None,
    start_date=datetime(2023, 1, 1),
    catchup=False,
) as parent_dag:
    push_task = PythonOperator(
        task_id='push_file_name',
        python_callable=push_filename_to_xcom,
    )
