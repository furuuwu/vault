"""
new things:
* instead of using XComs, send a static message on the config

this is very limited application tho, i'd say

* trigger the child dag with TriggerDagRunOperator
"""

from airflow import DAG
from airflow.operators.trigger_dagrun import TriggerDagRunOperator
from datetime import datetime

with DAG(
    dag_id = 'ex6_v3_parent',
    schedule_interval=None,
    start_date=datetime(2023, 1, 1),
    catchup=False,
) as parent_dag:

    # Trigger the child DAG
    trigger_child_dag = TriggerDagRunOperator(
        task_id='trigger_child_dag',
        trigger_dag_id='ex6_v3_child',  # ID of the child DAG
        conf={'file_name': 'titanic.csv'},  # Optional: Pass additional static data via `conf`
    )

    trigger_child_dag
