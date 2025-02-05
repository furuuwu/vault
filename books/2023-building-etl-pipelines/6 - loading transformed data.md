# 6 - Loading Transformed Data

## Data loading

Data loading

* is the final step of the ETL process (L step) - to ensure the transformed data is seamlessly transitioned to its destination.
* implies choosing the load destination
  
  Depending on the nature of your project, you might be loading data into relational databases, cloud-based data warehouses, NoSQL stores, or other repositories. Consider factors such as data types, indexing, partitioning, and data distribution

### Types of load destinations

* **Relational databases** remain the most common locations for data storage and management. Python provides support for popular RDBMSs such as MySQL, PostgreSQL, SQLite, and Oracle. Utilizing libraries such as SQLAlchemy and database-specific drivers (for example, psycopg2 and pymysql) allows you to efficiently load data into structured tables. These databases offer the advantage of data integrity enforcement, transaction management, and support for complex querying.

* **Data warehouses** are primarily used for storing large data for long-term storage; they have gained popularity over the years as scalable repositories optimized for complex analytical queries and reporting. Python has a plethora of libraries, such as Pandas, and specialized connectors to efficiently load data into data warehouses such as Amazon Redshift, Google BigQuery, and Snowflake.

* **NoSQL stores** - For semi-structured and unstructured data, NoSQL databases such as MongoDB, Cassandra, and Couchbase provide flexible and schemaless data storage. Python tools such as pymongo and cassandra-driver enable seamless integration with these databases. NoSQL stores are wellsuited for scenarios that require high scalability, rapid data ingestion, and unstructured data types.

* **Filesystems and object storage** (for example, Amazon S3 and Azure Blob Storage) are also advantageous for archiving, making backups, and scenarios where direct database integration is not required.

### data loading method

* full load

  In theory, data pipeline design intends to load the output data in one pass. However, in many situations, a full data load might not be a viable option. These situations include client requirements for continuous access to the full dataset or working with daily updates for incredibly large and complex datasets

* incremental data loading

  consists of processing loading activities in smaller, more manageable chunks.
