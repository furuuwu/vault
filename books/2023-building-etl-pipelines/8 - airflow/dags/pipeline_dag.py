from airflow import DAG
# from datetime import datetime, timedelta
import datetime
from airflow.operators.python import PythonOperator
import pandas as pd

# Extract - extract.py
def extract_data(filepath: object, select_cols: list, rename_cols: dict) -> object:
    """
       Simple Extract Function in Python with Error Handling
       :param filepath: str, file path to CSV data
       :output: pandas dataframe, extracted from CSV data
    """
    try:
        # Read the CSV file and store it in a dataframe
        df = pd.read_csv(filepath)
        df = df[select_cols]
        df = df.rename(columns={rename_cols})

    # Handle exception if any of the files are missing
    except FileNotFoundError as e:
        print(f"Error: {e}")

    # Handle any other exceptions
    except Exception as e:
        print(f"Error: {e}")

    return df

# Transform - transform.py
# Transform Crash Data
def transform_crash_data(crashes_df):
    crashes_df['CRASH_DATE'] = pd.to_datetime(crashes_df['CRASH_DATE'])
    crashes_df = crashes_df[crashes_df['CRASH_DATE_EST_I'] != 'Y']
    crashes_df = crashes_df[crashes_df['LATITUDE'].notnull() & crashes_df['LONGITUDE'].notnull()]
    crashes_df = crashes_df.drop(columns=['CRASH_DATE_EST_I'])
    return crashes_df

# Transform Vehicle Data
def transform_vehicle_data(vehicles_df):
    vehicles_df['VEHICLE_MAKE'] = vehicles_df['VEHICLE_MAKE'].str.upper()
    vehicles_df['VEHICLE_MODEL'] = vehicles_df['VEHICLE_MODEL'].str.upper()
    vehicles_df = vehicles_df[vehicles_df['VEHICLE_YEAR'].notnull()]
    return vehicles_df

# Transform People Data
def transform_people_data(people_df):
    people_df = people_df[people_df['PERSON_TYPE'].isin(['DRIVER', 'PASSENGER', 'PEDESTRIAN', 'BICYCLE', 'OTHER'])]
    people_df = people_df[people_df['PERSON_AGE'].notnull()]
    return people_df

# Load - load.py
# Define the load process as a Bonobo graph
def load_data(df: object, create_PSQL: str, insert_PSQL: str) -> object:

    config = configparser.ConfigParser()
    config.read('config.ini')
    conn = psycopg2.connect(
        host=config['POSTGRESQL']['host'],
        port=config['POSTGRESQL']['port'],
        dbname=config['POSTGRESQL']['database'],
        user=config['POSTGRESQL']['user'],
        password=config['POSTGRESQL']['password']
    )
    cursor = conn.cursor()
    cursor.execute(create_PSQL)
    conn.commit()

import psycopg2
import configparser
import yaml

# import pipeline configuration
with open('../config.yaml', 'r') as file:
    config_data = yaml.safe_load(file)

# Define the DAG
default_args = {
    'owner': 'first_airflow_pipeline',
    'depends_on_past': False,
    'start_date': datetime(2023, 8, 13),
    'retry_delay': datetime.timedelta(minutes=5),
    'catchup': False,
}
dag = DAG('chicago_dmv', default_args=default_args, schedule_interval=datetime.timedelta(days=1))

# Define the tasks
task_extract_crashes = PythonOperator(
    task_id='extract_crashes',
    op_kwargs={'filepath': config_data['crash_filepath'],
               'select_cols': config_data['crash_columns_list'],
               'rename_cols': config_data['crash_columns_rename_dict']},
    dag=dag
)
task_extract_vehicles = PythonOperator(
    task_id='extract_vehicles',
    python_callable=extract_data,
    op_kwargs={'filepath': config_data['vehicle_filepath'],
               'select_cols': config_data['vehicle_columns_list'],
               'rename_cols': config_data['vehicle_columns_rename_dict']},
    dag=dag
)
task_extract_people = PythonOperator(
    task_id='extract_people',
    python_callable=extract_data,
    op_kwargs={'filepath': config_data['people_filepath'],
               'select_cols': config_data['people_columns_list'],
               'rename_cols': config_data['people_columns_rename_dict']},
    dag=dag
)
task_transform_crashes = PythonOperator(
    task_id='transform_crashes',
    python_callable=transform_crash_data,
    op_kwargs={'crash_df': "{{ task_instance.xcom_pull(task_ids='extract_crashes') }}"},
    dag=dag
)
task_transform_vehicles = PythonOperator(
    task_id='transform_vehicles',
    python_callable=transform_vehicle_data,
    op_kwargs={'vehicle_df': "{{ task_instance.xcom_pull(task_ids='extract_vehicles') }}"},
    dag=dag
)
task_transform_people = PythonOperator(
    task_id='transform_people',
    python_callable=transform_people_data,
    op_kwargs={'people_df': "{{ task_instance.xcom_pull(task_ids='extract_people') }}"},
    dag=dag
)
task_load_crash = PythonOperator(
    task_id='load_crash',
    python_callable=load_data,
    op_kwargs={'df': "{{ task_instance.xcom_pull(task_ids='transform_crash') }}",
               'create_PSQL': config_data['crash_create_PSQL'],
               'insert_PSQL': config_data['crash_insert_PSQL']},
    dag=dag
)
task_load_vehicle = PythonOperator(
    task_id='load_vehicle',
    python_callable=load_data,
    op_kwargs={'df': "{{ task_instance.xcom_pull(task_ids='transform_vehicle') }}",
               'create_PSQL': config_data['vehicle_create_PSQL'],
               'insert_PSQL': config_data['vehicle_insert_PSQL']},
    dag=dag
)
task_load_people = PythonOperator(
    task_id='load_people',
    python_callable=load_data,
    op_kwargs={'df': "{{ task_instance.xcom_pull(task_ids='transform_people') }}",
               'create_PSQL': config_data['crash_create_PSQL'],
               'insert_PSQL': config_data['crash_insert_PSQL']},
    dag=dag
)


# Define the task dependencies
task_extract_crashes >> task_transform_crashes
task_extract_vehicles >> task_transform_vehicles
task_extract_people >> task_transform_people
task_transform_crashes >> task_load_crash
task_transform_vehicles >> task_load_vehicle
task_transform_people >> task_load_people