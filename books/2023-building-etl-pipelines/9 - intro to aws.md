# 9 - A Primer on AWS Tools for ETL Processes

## Services

* <https://aws.amazon.com/>
* <https://docs.aws.amazon.com/>
* decision guides - <https://aws.amazon.com/getting-started/decision-guides/>
* tutorials - <https://aws.amazon.com/getting-started/hands-on/>

### Compute

|AWS Tool| Use-Case Description|
|---|---|
|Amazon EC2|Provides scalable computing capacity in the cloud. Useful for running applications. EC2 allows users to quickly and easily launch and manage virtual servers (called instances) in the cloud, using a variety of operating systems, such as Linux, Windows, and macOS. EC2 provides a range of instance types, from general-purpose to high-performance, and offers various pricing options, including on-demand, reserved, and spot instances.|
|AWS Lambda| Run code without provisioning or managing servers. Great for event-driven data processing.|
|AWS Glue|Fully managed ETL service. Suitable for data cataloging and ETL jobs.|
|AWS Step Functions|Coordinate multiple AWS services into serverless workflows. Suitable for complex ETL tasks.|

### Storage

|AWS Tool| Use-Case Description|
|---|---|
|Amazon S3|Object storage service. Ideal for storing and retrieving large amounts of data.|
|Amazon Redshift|Data warehouse service. Ideal for large-scale data analytics. It provides a SQL-based interface, automatic compression, distribution, backup, and integration with various business intelligence (BI) tools such as Tableau and Power BI|

### ETL

|AWS Tool| Use-Case Description|
|---|---|
|Amazon Kinesis|Collect, process, and analyze real-time data streams. Suitable for real-time analytics.|
|Amazon Managed Workflows for Apache Airflow (MWAA)|Managed service for running Apache Airflow.|
|Amazon EMR| Managed big data platform for processing massive amounts of data. Easily run and scale Apache Spark, Hive, Presto, and other big data workloads|
|AWS Batch|Batch processing for ML model training, simulation, and analysis at any scale.|
|AWS Data Pipeline| Orchestrate and automate data movement and transformation. Suitable for complex ETL workflows. ⚠️**DEPRECATED** - You can migrate typical use cases of AWS Data Pipeline to either AWS Glue, AWS Step Functions, or Amazon MWAA.⚠️|

use cases:

* Serverless ETL: Use AWS Glue if you prefer a fully managed, serverless service.
* Complex Workflows and Orchestration: Use Amazon MWAA (Apache Airflow) if you need custom ETL workflows with complex dependencies.
* Real-time ETL: Use Kinesis if you need to process data in real-time.
* Big Data ETL: Use EMR for big data transformations that require distributed processing (e.g., Spark).
* Event-driven ETL: Use AWS Lambda if you prefer a serverless event-driven approach.
* Relational ETL: Use RDS/Aurora when working with relational databases.

## Creating a AWS account

Nothing interesting

## Tools

* AWS CLI

  CLI for AWS services. The AWS Command Line Interface (AWS CLI) is a unified tool to manage your AWS services. With just one tool to download and configure, you can control multiple AWS services from the command line and automate them through scripts.

  <https://docs.aws.amazon.com/cli/>

  ```shell
  aws --version
  ```

* AWS Serverless Application Model CLI (AWS SAM CLI)

  For building and deploying serverless applications

  Open source developer tool that simplifies and improves the experience of building and running serverless applications on AWS.

  <https://docs.aws.amazon.com/serverless-application-model>

  ```shell
  sam --version
  ```

* Docker

  Containerization platform for packaging and running applications

  ```shell
  docker --version
  ```

* LocalStack

  Local AWS cloud environment for testing and developing applications

  <https://docs.localstack.cloud/getting-started/installation/>
