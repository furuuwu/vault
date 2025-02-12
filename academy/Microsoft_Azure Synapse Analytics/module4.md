# module 4

* Use Delta Lake in Azure Synapse Analytics
  * Understand Delta Lake
  * Create Delta Lake tables
  * Create catalog tables
  * Use Delta Lake with streaming data
  * Use Delta Lake in a SQL pool
  * [lab](https://microsoftlearning.github.io/dp-203-azure-data-engineer/Instructions/Labs/07-Use-delta-lake.html)

## Delta Lake

Linux foundation Delta Lake is an open-source storage layer for Spark that enables relational database capabilities for batch and streaming data. By using Delta Lake, you can implement a data lakehouse architecture in Spark to support SQL_based data manipulation semantics with support for transactions and schema enforcement. The result is an analytical data store that offers many of the advantages of a relational database system with the flexibility of data file storage in a data lake.

Delta Lake is supported in Azure Synapse Analytics Spark pools for PySpark, Scala, and .NET code. The version of Delta Lake available in an Azure Synapse Analytics pool depends on the version of Spark specified in the pool configuration. The information in this module reflects Delta Lake version 1.0, which is installed with Spark 3.1.

<https://docs.delta.io/latest/delta-apidoc.html>

## Create Delta Lake tables

You can create a Delta table either by converting an existing Parquet table or by defining a new table directly in Delta format.

```python
# Create a Delta table
data = spark.range(0, 5)
data.write.format("delta").save("/FileStore/tables/my_delta_table")

# Read and write data
# Append data to a Delta table using DataFrame API
new_data = spark.range(5, 10)
new_data.write.format("delta").mode("append").save("/FileStore/tables/my_delta_table")
```

### creating a Delta table with a defined schema

Create a Delta table with a specific schema either programmatically using Spark SQL or by using the DataFrame API.

```sql
-- Create a Delta table using Spark SQL
CREATE TABLE my_delta_table_schema (
    id INT,
    name STRING,
    age INT
);

-- Insert valid data
INSERT INTO my_delta_table_schema (id, name, age)
VALUES
(1, 'Alice', 30),
(2, 'Bob', 25);
```

### creating a Delta Lake table from a dataframe

Delta lake is built on tables, which provide a relational storage abstraction over files in a data lake.

One of the easiest ways to create a Delta Lake table is to save a dataframe in the delta format, specifying a path where the data files and related metadata information for the table should be stored.

For example, the following PySpark code loads a dataframe with data from an existing file, and then saves that dataframe to a new folder location in delta format:

```python
# Load a file into a dataframe
df = spark.read.load('/data/mydata.csv', format='csv', header=True)

# Save the dataframe as a delta table
delta_table_path = "/delta/mydata"
df.write.format("delta").save(delta_table_path)
```

After saving the delta table, the path location you specified includes parquet files for the data (regardless of the format of the source file you loaded into the dataframe) and a _delta_log folder containing the transaction log for the table.

The transaction log records all data modifications to the table. By logging each modification, transactional consistency can be enforced and versioning information for the table can be retained.

You can replace an existing Delta Lake table with the contents of a dataframe by using the overwrite mode, as shown here:

```python
new_df.write.format("delta").mode("overwrite").save(delta_table_path)
```

You can also add rows from a dataframe to an existing table by using the append mode:

```python
new_rows_df.write.format("delta").mode("append").save(delta_table_path)
```

### making conditional updates

While you can make data modifications in a dataframe and then replace a Delta Lake table by overwriting it, a more common pattern in a database is to insert, update or delete rows in an existing table as discrete transactional operations. To make such modifications to a Delta Lake table, you can use the DeltaTable object in the Delta Lake API, which supports update, delete, and merge operations. For example, you could use the following code to update the price column for all rows with a category column value of "Accessories":

```python
from delta.tables import *
from pyspark.sql.functions import *

# Create a deltaTable object
deltaTable = DeltaTable.forPath(spark, delta_table_path)

# Update the table (reduce price of accessories by 10%)
deltaTable.update(
    condition = "Category == 'Accessories'",
    set = { "Price": "Price * 0.9" })
```

The data modifications are recorded in the transaction log, and new parquet files are created in the table folder as required.

### querying a previous version of a table

Delta Lake tables support versioning through the transaction log. The transaction log records modifications made to the table, noting the timestamp and version number for each transaction. You can use this logged version data to view previous versions of the table - a feature known as time travel.

You can retrieve data from a specific version of a Delta Lake table by reading the data from the delta table location into a dataframe, specifying the version required as a versionAsOf option:

```python
df = spark.read.format("delta").option("versionAsOf", 0).load(delta_table_path)
```

Alternatively, you can specify a timestamp by using the timestampAsOf option:

```python
df = spark.read.format("delta").option("timestampAsOf", '2022-01-01').load(delta_table_path)
```

eg.

```sql
-- Create the Delta table
CREATE TABLE person_data (
    id INT,
    name STRING,
    age INT
);

-- Insert initial data
INSERT INTO person_data (id, name, age)
VALUES
(1, 'Alice', 30),
(2, 'Bob', 25);


-- Perform some updates on the table. Each update creates a new version of the Delta table.
-- Update age of Bob
UPDATE person_data
SET age = 26
WHERE name = 'Bob';

-- Insert a new record
INSERT INTO person_data (id, name, age)
VALUES
(3, 'Charlie', 28);

-- Query table history
-- You can view the history of the Delta table to see all the changes made to it. The DESCRIBE HISTORY command displays a list of all the versions of the table, along with details such as the operation performed, timestamp, and user who performed the operation.
DESCRIBE HISTORY person_data;

-- Time travel queries
-- You can query previous versions of the table using the VERSION AS OF or TIMESTAMP AS OF syntax.
-- Query data as of version 0
SELECT * FROM person_data VERSION AS OF 0;
-- Query data as of a specific timestamp
SELECT * FROM person_data TIMESTAMP AS OF '2024-07-22T10:00:00Z';

-- Revert to a previous version
-- If you need to revert the table to a previous state, you can use the RESTORE command.
-- Restore the table to version 0
RESTORE TABLE person_data TO VERSION AS OF 0;
-- Restore the table to a specific timestamp
RESTORE TABLE person_data TO TIMESTAMP AS OF '2024-07-22T10:00:00Z';
```

### handle schema mismatches

You can use the MERGE statement to handle updates and insertions in a way that accommodates schema changes.

```sql
-- Define a temporary view with new data
CREATE OR REPLACE TEMP VIEW my_new_delta_table_schema AS
SELECT * FROM VALUES
(3, 'Charlie', 28),
(4, 'Diana', 35)
AS my_new_delta_table_schema(id, name, age);

-- Use MERGE to upsert data
MERGE INTO my_delta_table_schema AS target
USING my_new_delta_table_schema AS source
ON target.id = source.id
WHEN MATCHED THEN
  UPDATE SET
    target.name = source.name,
    target.age = source.age
WHEN NOT MATCHED THEN
  INSERT (id, name, age)
  VALUES (source.id, source.name, source.age);
```

If the incoming data types are different but compatible, you can use the cast function to align the schemas.

```sql
-- Insert data with casting to match the schema
INSERT INTO my_delta_table_schema
SELECT
  cast(id as INT),
  cast(name as STRING),
  cast(age as INT)
FROM my_new_delta_table_schema;
```

## Create catalog tables

So far we've considered Delta Lake table instances created from dataframes and modified through the Delta Lake API. You can also define Delta Lake tables as catalog tables in the Hive metastore for your Spark pool, and work with them using SQL.

Tables in a Spark catalog, including Delta Lake tables, can be managed or external; and it's important to understand the distinction between these kinds of table.

* A managed table is defined without a specified location, and the data files are stored within the storage used by the metastore. Dropping the table not only removes its metadata from the catalog, but also deletes the folder in which its data files are stored.
* An external table is defined for a custom file location, where the data for the table is stored. The metadata for the table is defined in the Spark catalog. Dropping the table deletes the metadata from the catalog, but doesn't affect the data files.

There are several ways to create catalog tables.

### creating a catalog table from a dataframe

You can create managed tables by writing a dataframe using the saveAsTable operation as shown in the following examples:

```python
# Save a dataframe as a managed table
df.write.format("delta").saveAsTable("MyManagedTable")

## specify a path option to save as an external table
df.write.format("delta").option("path", "/mydata").saveAsTable("MyExternalTable")
```

### creating a catalog table using SQL

You can also create a catalog table by using the CREATE TABLE SQL statement with the USING DELTA clause, and an optional LOCATION parameter for external tables. You can run the statement using the SparkSQL API, like the following example:

```python
spark.sql("CREATE TABLE MyExternalTable USING DELTA LOCATION '/mydata'")
```

Alternatively you can use the native SQL support in Spark to run the statement:

```sql
%%sql

CREATE TABLE MyExternalTable
USING DELTA
LOCATION '/mydata'
```

In all of the examples so far, the table is created without an explicit schema. In the case of tables created by writing a dataframe, the table schema is inherited from the dataframe. When creating an external table, the schema is inherited from any files that are currently stored in the table location. However, when creating a new managed table, or an external table with a currently empty location, you define the table schema by specifying the column names, types, and nullability as part of the CREATE TABLE statement; as shown in the following example:

```sql
%%sql

CREATE TABLE ManagedSalesOrders
(
    Orderid INT NOT NULL,
    OrderDate TIMESTAMP NOT NULL,
    CustomerName STRING,
    SalesTotal FLOAT NOT NULL
)
USING DELTA
```

When using Delta Lake, table schemas are enforced - all inserts and updates must comply with the specified column nullability and data types.

### creating a catalog table using the DeltaTableBuilder API

You can use the DeltaTableBuilder API (part of the Delta Lake API) to create a catalog table, as shown in the following example:

```python
from delta.tables import *

DeltaTable.create(spark) \
  .tableName("default.ManagedProducts") \
  .addColumn("Productid", "INT") \
  .addColumn("ProductName", "STRING") \
  .addColumn("Category", "STRING") \
  .addColumn("Price", "FLOAT") \
  .execute()
```

Similarly to the CREATE TABLE SQL statement, the create method returns an error if a table with the specified name already exists. You can mitigate this behavior by using the createIfNotExists or createOrReplace method.

## Using catalog tables

You can use catalog tables like tables in any SQL-based relational database, querying and manipulating them by using standard SQL statements.

```sql
%%sql

SELECT orderid, salestotal
FROM ManagedSalesOrders
```

## Spark Structured Streaming

All of the data we've explored up to this point has been static data in files. However, many data analytics scenarios involve streaming data that must be processed in near real time. For example, you might need to capture readings emitted by internet-of-things (IoT) devices and store them in a table as they occur.

A typical stream processing solution involves constantly reading a stream of data from a source, optionally processing it to select specific fields, aggregate and group values, or otherwise manipulate the data, and writing the results to a sink.

Spark includes native support for streaming data through Spark Structured Streaming, an API that is based on a boundless dataframe in which streaming data is captured for processing. A Spark Structured Streaming dataframe can read data from many different kinds of streaming source, including network ports, real time message brokering services such as Azure Event Hubs or Kafka, or file system locations.

<https://spark.apache.org/docs/latest/structured-streaming-programming-guide.html>

## Use Delta Lake with streaming data

You can use a Delta Lake table as a source or a sink for Spark Structured Streaming. For example, you could capture a stream of real time data from an IoT device and write the stream directly to a Delta Lake table as a sink - enabling you to query the table to see the latest streamed data. Or, you could read a Delta Table as a streaming source, enabling you to constantly report new data as it is added to the table.

<https://docs.delta.io/latest/delta-streaming.html>

### using a Delta Lake table as a streaming source

In the following PySpark example, a Delta Lake table is used to store details of Internet sales orders. A stream is created that reads data from the Delta Lake table folder as new data is appended.

```python
from pyspark.sql.types import *
from pyspark.sql.functions import *

# Load a streaming dataframe from the Delta Table
stream_df = spark.readStream.format("delta") \
    .option("ignoreChanges", "true") \
    .load("/delta/internetorders")

# Now you can process the streaming data in the dataframe
# for example, show it:
stream_df.writeStream \
    .outputMode("append") \
    .format("console") \
    .start()
```

When using a Delta Lake table as a streaming source, only append operations can be included in the stream. Data modifications will cause an error unless you specify the `ignoreChanges` or `ignoreDeletes` option.

After reading the data from the Delta Lake table into a streaming dataframe, you can use the Spark Structured Streaming API to process it. In the example above, the dataframe is simply displayed; but you could use Spark Structured Streaming to aggregate the data over temporal windows (for example to count the number of orders placed every minute) and send the aggregated results to a downstream process for near-real-time visualization.

### using a Delta Lake table as a streaming sink

In the following PySpark example, a stream of data is read from JSON files in a folder. The JSON data in each file contains the status for an IoT device in the format `{"device":"Dev1","status":"ok"}`. New data is added to the stream whenever a file is added to the folder. The input stream is a boundless dataframe, which is then written in delta format to a folder location for a Delta Lake table.

```python
from pyspark.sql.types import *
from pyspark.sql.functions import *

# Create a stream that reads JSON data from a folder
inputPath = '/streamingdata/'
jsonSchema = StructType([
    StructField("device", StringType(), False),
    StructField("status", StringType(), False)
])
stream_df = spark.readStream.schema(jsonSchema).option("maxFilesPerTrigger", 1).json(inputPath)

# Write the stream to a delta table
table_path = '/delta/devicetable'
checkpoint_path = '/delta/checkpoint'
delta_stream = stream_df.writeStream.format("delta").option("checkpointLocation", checkpoint_path).start(table_path)
```

The `checkpointLocation` option is used to write a checkpoint file that tracks the state of the stream processing. This file enables you to recover from failure at the point where stream processing left off.

After the streaming process has started, you can query the Delta Lake table to which the streaming output is being written to see the latest data. For example, the following code creates a catalog table for the Delta Lake table folder and queries it:

```sql
%%sql

CREATE TABLE DeviceTable
USING DELTA
LOCATION '/delta/devicetable';

SELECT device, status
FROM DeviceTable;
```

To stop the stream of data being written to the Delta Lake table, you can use the `stop` method of the streaming query:

```python
delta_stream.stop()
```

## Use Delta Lake in a SQL pool

Delta Lake is designed as a transactional, relational storage layer for Apache Spark; including Spark pools in Azure Synapse Analytics. However, Azure Synapse Analytics also includes a serverless SQL pool runtime that enables data analysts and engineers to run SQL queries against data in a data lake or a relational database.

You can only query data from Delta Lake tables in a serverless SQL pool; you can't update, insert, or delete data.

### Querying delta formatted files with OPENROWSET

The serverless SQL pool in Azure Synapse Analytics includes support for reading delta format files; enabling you to use the SQL pool to query Delta Lake tables. This approach can be useful in scenarios where you want to use Spark and Delta tables to process large quantities of data, but use the SQL pool to run queries for reporting and analysis of the processed data.

In the following example, a SQL SELECT query reads delta format data using the `OPENROWSET` function.

```sql
SELECT *
FROM
    OPENROWSET(
        BULK 'https://mystore.dfs.core.windows.net/files/delta/mytable/',
        FORMAT = 'DELTA'
    ) AS deltadata
```

You could run this query in a serverless SQL pool to retrieve the latest data from the Delta Lake table stored in the specified file location.

You could also create a database and add a data source that encapsulates the location of your Delta Lake data files, as shown in this example:

```sql
CREATE DATABASE MyDB
      COLLATE Latin1_General_100_BIN2_UTF8;
GO;

USE MyDB;
GO

CREATE EXTERNAL DATA SOURCE DeltaLakeStore
WITH
(
    LOCATION = 'https://mystore.dfs.core.windows.net/files/delta/'
);
GO

SELECT TOP 10 *
FROM OPENROWSET(
        BULK 'mytable',
        DATA_SOURCE = 'DeltaLakeStore',
        FORMAT = 'DELTA'
    ) as deltadata;
```

When working with Delta Lake data, which is stored in Parquet format, it's generally best to create a database with a UTF-8 based collation in order to ensure string compatibility.

### Querying catalog tables

The serverless SQL pool in Azure Synapse Analytics has shared access to databases in the Spark metastore, so you can query catalog tables that were created using Spark SQL. In the following example, a SQL query in a serverless SQL pool queries a catalog table that contains Delta Lake data:

```sql
-- By default, Spark catalog tables are created in a database named "default"
-- If you created another database using Spark SQL, you can use it here
USE default;

SELECT * FROM MyDeltaTable;
```
