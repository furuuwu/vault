from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

"""
You start with some_data.csv in the source folder (data/file_source).
You copy it to some_data_to_process.csv for processing.
After processing, you create some_data_processed.csv.
Finally, you move some_data_processed.csv to the destination folder (data/file_destination) and rename it back to some_data.csv.
You also want to delete the intermediate files (some_data_to_process.csv and some_data_processed.csv) after the process is complete.
"""

dag = DAG(
    dag_id = 'ex4',
    description='A DAG to process and move files with intermediate steps',
    schedule_interval=None,  # Set the schedule to None to run manually
    start_date=datetime(2024, 12, 20),
    catchup=False,
)

# 0: check if file exists
check_file_exists = BashOperator(
    task_id='check_file_exists',
    bash_command='ls /opt/airflow/data/file_source/some_data.csv',
    dag=dag,
)

# 1: make a copy of the file
copy_file_to_process = BashOperator(
    task_id='copy_file_to_process',
    bash_command='cp /opt/airflow/data/file_source/some_data.csv /opt/airflow/data/file_source/some_data_to_process.csv',
    dag=dag,
)

# 2: process the file (the copy)
process_file = BashOperator(
    task_id='process_file',
    bash_command="""
        # Example of processing the file using awk (you can replace this with any other logic)
        # Here, we are simply adding a header to the file and processing it.
        echo "id,name,age,city" > /opt/airflow/data/file_source/some_data_processed.csv
        tail -n +2 /opt/airflow/data/file_source/some_data_to_process.csv | awk -F, '{OFS=","} {print $1, $2, $3, $4}' >> /opt/airflow/data/file_source/some_data_processed.csv
    """,
    dag=dag,
)

# 3: move the processed file to data/file_destination and rename it as "some_data.csv"
move_processed_file = BashOperator(
    task_id='move_processed_file',
    bash_command='mv /opt/airflow/data/file_source/some_data_processed.csv /opt/airflow/data/file_destination/some_data.csv',
    dag=dag,
)

# 4: delete the intermediate files: "some_data_to_process.csv" and "some_data_processed.csv"
delete_intermediate_files = BashOperator(
    task_id='delete_intermediate_files',
    bash_command='rm /opt/airflow/data/file_source/some_data_to_process.csv /opt/airflow/data/file_source/some_data_processed.csv',
    dag=dag,
)

check_file_exists >> copy_file_to_process >> process_file >> move_processed_file >> delete_intermediate_files
