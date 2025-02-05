#!/usr/bin/env python
# coding: utf-8

# # Creating a Data Extraction pipeline using Python

# Now its time to create a robust extraction pipeline using Python using the examples in previous chapter.
# Below is an example on how we can create an enterprise level pipeline.


# Make sure below packages have been installed 
# pip install pyarrow
# pip install certifi

import urllib3
import certifi
import json
import sqlite3
import pandas as pd


def source_data_from_parquet(parquet_file_name):
    try:
        df_parquet = pd.read_parquet(parquet_file_name)
    except Exception as e:
        print(f"Error reading parquet file: {e}")
        df_parquet = pd.DataFrame()
    return df_parquet


def source_data_from_csv(csv_file_name):
    try:
        df_csv = pd.read_csv(csv_file_name)
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        df_csv = pd.DataFrame()
    return df_csv


def source_data_from_api(api_endpoint):
    try:
        # Create a PoolManager to handle HTTP requests
        http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
        api_response = http.request('GET', api_endpoint)
        apt_status = api_response.status
        if apt_status == 200:
            data = json.loads(api_response.data.decode('utf-8'))
            df_api = pd.json_normalize(data)
        else:
            print(f"API call failed with status code: {apt_status}")
            df_api = pd.DataFrame()
    except Exception as e:
        print(f"Error retrieving data from API: {e}")
        df_api = pd.DataFrame()
    return df_api


def source_data_from_table(db_name, table_name):
    try:
        # Read SQLite query results into a pandas DataFrame
        with sqlite3.connect(db_name) as conn:
            df_table = pd.read_sql(f"SELECT * FROM {table_name}", conn)
    except Exception as e:
        print(f"Error reading data from table {table_name}: {e}")
        df_table = pd.DataFrame()
    return df_table


def source_data_from_webpage(web_page_url, matching_keyword):
    try:
        # Read webpage table into a pandas DataFrame
        df_html = pd.read_html(web_page_url, match=matching_keyword)
        df_html = df_html[0]  # Get the first matching table
    except Exception as e:
        print(f"Error reading data from webpage: {e}")
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
    # These dataframes are available for loading data into either a staging area or transformation pipelines.
    df_parquet, df_csv, df_api, df_table, df_html = (
        source_data_from_parquet(parquet_file_name),
        source_data_from_csv(csv_file_name),
        source_data_from_api(api_endpoint),
        source_data_from_table(db_name, table_name),
        source_data_from_webpage(web_page_url, matching_keyword),
    )
    return df_parquet, df_csv, df_api, df_table, df_html


# Call the function to test
df_parquet, df_csv, df_api, df_table, df_html = extract_data()

# Print a preview of the extracted data
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