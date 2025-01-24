"""
This script handles the process of loading the Titanic dataset into MariaDB.
"""

import pandas as pd
import pymysql
from sqlalchemy import create_engine

def load_csv_to_mariadb():
    # Define the CSV path
    # this is the path to the .csv 
    # inside the scheduler ctn. Verify it is there
    # the container's root directory is /opt/airflow

    # so, the absolute path is
    csv_abs_path = '/opt/airflow/data/titanic.csv'
    # the relative path from the project's directory is
    csv_rel_path = 'data/titanic.csv'
    # these should both work!
    
    # Read the dataset
    df = pd.read_csv(csv_abs_path)
    
    # Database connection details
    db_url = '172.18.0.1'
    db_port = 3306
    db_name = 'titanic'
    db_user = 'root'
    db_password = 'rootpassword'

    # Create the SQLAlchemy engine
    engine = create_engine(f"mysql+pymysql://{db_user}:{db_password}@{db_url}:{db_port}/{db_name}")

    # Load dataset into MariaDB
    df.to_sql('titanic', con=engine, if_exists='replace', index=False)
    print("Titanic dataset loaded successfully into MariaDB!")