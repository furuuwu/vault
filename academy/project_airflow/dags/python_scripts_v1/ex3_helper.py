from sqlalchemy import create_engine
import pandas as pd
import pymysql

def run_query():

    engine = create_engine('mysql+pymysql://root:rootpassword@172.18.0.1:3306/cap_academy')

    q = '''
    SELECT *
    FROM client_details details
    JOIN client_contacts contacts
    ON details.customer_id = contacts.customer_id;
    '''

    df = pd.read_sql_query(q, engine)

    df.to_csv('/opt/airflow/data/merged_clients.csv', index=False)
    print('Query results saved!')