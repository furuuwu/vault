import urllib3
import certifi
import json
import sqlite3
import pandas as pd
import logging
import os

# Define top-level module logger
logger = logging.getLogger(__name__)

# Create a /logs directory if it doesn't exist
log_directory = 'logs'
os.makedirs(log_directory, exist_ok=True)

# Define the log file path
log_file = os.path.join(log_directory, 'data_extraction.log')

# Set up logging to a file
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_file),  # Log to a file
        logging.StreamHandler()  # Also log to console
    ]
)

def source_data_from_parquet(parquet_file_name):
    try:
        df_parquet = pd.read_parquet(parquet_file_name)
        logger.info(f'{parquet_file_name} : extracted {df_parquet.shape[0]} records from the parquet file')
    except Exception as e:
        logger.exception(f'{parquet_file_name} : exception {e} encountered while extracting the parquet file')
        df_parquet = pd.DataFrame()
    return df_parquet


def source_data_from_csv(csv_file_name):
    try:
        df_csv = pd.read_csv(csv_file_name)
        logger.info(f'{csv_file_name} : extracted {df_csv.shape[0]} records from the CSV file')
    except Exception as e:
        logger.exception(f'{csv_file_name} : exception {e} encountered while extracting the CSV file')
        df_csv = pd.DataFrame()
    return df_csv


def source_data_from_api(api_endpoint):
    try:
        # Create a PoolManager to handle HTTP requests
        http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
        api_response = http.request('GET', api_endpoint)
        api_status = api_response.status
        if api_status == 200:
            logger.info(f'{api_status} - OK: while invoking the API {api_endpoint}')
            data = json.loads(api_response.data.decode('utf-8'))
            df_api = pd.json_normalize(data)
            logger.info(f'{api_endpoint} : extracted {df_api.shape[0]} records from the API')
        else:
            logger.error(f'{api_status} - error: while invoking the API {api_endpoint}')
            df_api = pd.DataFrame()  # Fixed typo: `pd.Dataframe()` to `pd.DataFrame()`
    except Exception as e:
        logger.exception(f'Exception {e} encountered while reading data from the API: {api_endpoint}')
        df_api = pd.DataFrame()
    return df_api


def source_data_from_table(db_name, table_name):
    try:
        with sqlite3.connect(db_name) as conn:
            df_table = pd.read_sql(f"SELECT * FROM {table_name}", conn)
            logger.info(f'{db_name} : read {df_table.shape[0]} records from the table: {table_name}')
    except Exception as e:
        logger.exception(f'{db_name} : exception {e} encountered while reading data from the table: {table_name}')
        df_table = pd.DataFrame()
    return df_table


def source_data_from_webpage(web_page_url, matching_keyword):
    try:
        df_html = pd.read_html(web_page_url, match=matching_keyword)
        df_html = df_html[0]  # Extract the first matching table
        logger.info(f'{web_page_url} : read {df_html.shape[0]} records from the webpage')
    except Exception as e:
        logger.exception(f'{web_page_url} : exception {e} encountered while reading data from the webpage')
        df_html = pd.DataFrame()
    return df_html


def extract_data():
    parquet_file_name = "data/yellow_tripdata_2022-01.parquet"
    csv_file_name = "data/h9gi-nx95.csv"
    api_endpoint = "https://data.cityofnewyork.us/resource/h9gi-nx95.json?$limit=500"
    db_name = "movies.sqlite"
    table_name = "movies"
    web_page_url = "https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)"
    matching_keyword = "by country"

    # Extract data from all source systems
    df_parquet, df_csv, df_api, df_table, df_html = (
        source_data_from_parquet(parquet_file_name),
        source_data_from_csv(csv_file_name),
        source_data_from_api(api_endpoint),
        source_data_from_table(db_name, table_name),
        source_data_from_webpage(web_page_url, matching_keyword),
    )
    return df_parquet, df_csv, df_api, df_table, df_html


# Call the function to test and log outputs
if __name__ == "__main__":
    df_parquet, df_csv, df_api, df_table, df_html = extract_data()

    # Print previews
    print("Parquet DataFrame:")
    print(df_parquet.head())
    print("\nCSV DataFrame:")
    print(df_csv.head())
    print("\nAPI DataFrame:")
    print(df_api.head())
    print("\nTable DataFrame:")
    print(df_table.head())
    print("\nHTML DataFrame:")
    print(df_html.head())
