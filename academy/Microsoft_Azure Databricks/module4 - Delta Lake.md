# module 4

* Manage data with Delta Lake

  * Get started with Delta Lake
  * Manage ACID transactions
  * Implement schema enforcement
  * Data versioning and time travel in Delta Lake
  * Data integrity with Delta Lake
  * [lab](https://microsoftlearning.github.io/mslearn-databricks/Instructions/Exercises/LA-04-Explore-Delta-Lake.html)

## lab

For this one, import the products.csv file

```python
urls = [
    "https://raw.githubusercontent.com/MicrosoftLearning/mslearn-databricks/main/data/products.csv",
]

dbutils.fs.mkdirs("/delta_lab")

import requests

for url in urls:
    file_name = url.split("/")[-1]
    response = requests.get(url)
    
    dbutils.fs.put(f"/delta_lab/{file_name}", response.text, overwrite=True)
    print(f"Saved {file_name} to /delta_lab/")

df = spark.read.load('/delta_lab/products.csv', format='csv', header=True)
display(df.limit(10))
```

* Load the file data into a delta table

```python
delta_table_path = "/delta/products-delta"
df.write.format("delta").save(delta_table_path)
```

The data for a delta lake table is stored in Parquet format. A log file is also created to track modifications made to the data.

The file data in Delta format can be loaded into a DeltaTable object, which you can use to view and update the data in the table. Run the following code in a new cell to update the data; reducing the price of product 771 by 10%.

```python
from delta.tables import *
from pyspark.sql.functions import *
   
# Create a deltaTable object
deltaTable = DeltaTable.forPath(spark, delta_table_path)
# Update the table (reduce price of product 771 by 10%)
deltaTable.update(
    condition = "ProductID == 771",
    set = { "ListPrice": "ListPrice * 0.9" })
# View the updated data as a dataframe
deltaTable.toDF().show(10)
```

The update is persisted to the data in the delta folder, and will be reflected in any new dataframe loaded from that location.

Run the following code to create a new dataframe from the delta table data:

```python
new_df = spark.read.format("delta").load(delta_table_path)
new_df.show(10)
```

* Explore logging and time-travel

```python
# view the original version of the product data:
new_df = spark.read.format("delta").option("versionAsOf", 0).load(delta_table_path)
new_df.show(10)

# The log contains a full history of modifications to the data. Use the following code to see a record of the last 10 changes:
deltaTable.history(10).show(10, False, True)
```

* Create catalog tables

So far you’ve worked with delta tables by loading data from the folder containing the parquet files on which the table is based. You can define catalog tables that encapsulate the data and provide a named table entity that you can reference in SQL code. Spark supports two kinds of catalog tables for delta lake:

* External tables that are defined by the path to the files containing the table data.
* Managed tables, that are defined in the metastore.

Create an external table

Use the following code to create a new database named AdventureWorks and then creates an external table named ProductsExternal in that database based on the path to the Delta files you defined previously:

```python
spark.sql("CREATE DATABASE AdventureWorks")
spark.sql("CREATE TABLE AdventureWorks.ProductsExternal USING DELTA LOCATION '{0}'".format(delta_table_path))
spark.sql("DESCRIBE EXTENDED AdventureWorks.ProductsExternal").show(truncate=False)
```

Note that the Location property of the new table is the path you specified.
Use the following code to query the table:

```sql
%sql
USE AdventureWorks;
SELECT * FROM ProductsExternal;
```

Create a managed table

Run the following code to create (and then describe) a managed table named ProductsManaged based on the dataframe you originally loaded from the products.csv file (before you updated the price of product 771).

```python
df.write.format("delta").saveAsTable("AdventureWorks.ProductsManaged")
spark.sql("DESCRIBE EXTENDED AdventureWorks.ProductsManaged").show(truncate=False)
```

You did not specify a path for the parquet files used by the table - this is managed for you in the Hive metastore, and shown in the Location property in the table description.

```sql
%sql
USE AdventureWorks;
SELECT * FROM ProductsManaged;
```

* Optimize table layout

use the following code to optimize the layout and clean up old versions of data files in the delta table:

```python
 spark.sql("OPTIMIZE Products")
 spark.conf.set("spark.databricks.delta.retentionDurationCheck.enabled", "false")
 spark.sql("VACUUM Products RETAIN 24 HOURS")
```

If you run VACUUM on a delta table, you lose the ability to time travel back to a version older than the specified data retention period.
