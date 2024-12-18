from airflow import DAG
from datetime import datetime
from airflow.providers.postgres.operators.postgres import PostgresOperator
# from airflow.providers.common.sql.operators.sql import BaseSQLOperator

with DAG(
    dag_id="user_processing", # Set unique identifier for the DAG
    start_date=datetime(2023, 1, 1), # Start on 1st january 2023
    schedule_interval="@daily", # Run every day at midnight using a cron preset
    catchup=False # Have catchup=False as we don't want to backfill missed runs (yet)
) as dag:
    
    # use the postgres operator to create a table in postgres
    create_table = PostgresOperator(
        task_id = 'create_table',
        postgres_conn_id = 'postgres',
        sql = '''
            CREATE TABLE IF NOT EXISTS users(
            firstname TEXT NOT NULL,
            lastname TEXT NOT NULL,
            country TEXT NOT NULL,
            username TEXT NOT NULL,
            password TEXT NOT NULL,
            email TEXT NOT NULL
            );
            '''
    )