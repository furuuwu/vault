#

## Create a pipeline in Python using AWS Lambda and Step Functions

### **1. Setting up the AWS CLI in a Local Environment**

Before you begin working with AWS resources like Lambda and Step Functions, you'll need to set up the AWS Command Line Interface (CLI) on your local machine.

#### **Install AWS CLI**

- **Windows**:
  - You can download the [AWS CLI MSI installer for Windows](https://aws.amazon.com/cli/).
  
- **Linux / macOS**:
  - Use the following command to install the AWS CLI:

    ```bash
    pip install awscli
    ```

#### **Configure AWS CLI**

After installation, configure your AWS CLI by running:

```bash
aws configure
```

It will prompt you for the following information:

- **AWS Access Key ID**: You can get it from the [AWS IAM console](https://console.aws.amazon.com/iam).
- **AWS Secret Access Key**: Found in the IAM console, just like the Access Key ID.
- **Default Region Name**: Choose a region where you want to deploy the resources (e.g., `us-west-2`).
- **Default Output Format**: Set this to `json` or any preferred format.

### **2. Creating S3 Buckets in AWS via the AWS Console**

S3 will be used for storing the input data and possibly the output data for your Lambda functions.

#### Steps to create an S3 bucket

1. Go to the [S3 Console](https://s3.console.aws.amazon.com/s3).
2. Click on **Create bucket**.
3. Provide a **Bucket name** (e.g., `my-lambda-input-bucket`).
4. Choose a region.
5. Click **Create bucket**.

Repeat the process to create a bucket for output data (e.g., `my-lambda-output-bucket`).

### **3. Creating Python Script for Each Lambda Function**

You’ll need to create one or more Lambda functions that will execute specific parts of your ETL pipeline. Let’s start by creating a basic Lambda function.

#### **Create a Python Lambda Function**

- **Create a Python script for Lambda** (e.g., `lambda_function.py`):
  - For example, you can create a Lambda function to read from an S3 bucket, process the data, and then store the result in another bucket.

```python
import json
import boto3

s3 = boto3.client('s3')

def lambda_handler(event, context):
    # Extract input bucket and file from the event
    input_bucket = event['input_bucket']
    input_file = event['input_file']
    
    # Download the file from S3
    s3.download_file(input_bucket, input_file, '/tmp/input_data.txt')
    
    # Perform some data transformation (For illustration, just read the file)
    with open('/tmp/input_data.txt', 'r') as file:
        data = file.read()

    # For example, transform the data by converting it to uppercase
    transformed_data = data.upper()

    # Upload the transformed data to an output S3 bucket
    output_bucket = event['output_bucket']
    s3.put_object(Body=transformed_data, Bucket=output_bucket, Key='output_data.txt')

    return {
        'statusCode': 200,
        'body': json.dumps('Transformation Complete')
    }
```

- **Deploying Lambda Function**:
  - **Go to the Lambda Console**: [Lambda Console](https://console.aws.amazon.com/lambda).
  - **Create Function**: Click on **Create function** and choose **Author from scratch**.
    - Name the function (e.g., `DataTransformFunction`).
    - Choose Python 3.x runtime.
    - Set permissions by creating a new role or choosing an existing role (ensure it has S3 permissions).
  - **Upload the Python script** to the Lambda function.
  - Save the function.

- **Test Lambda Function**:
  - Create a test event with the following JSON format:

```json
{
    "input_bucket": "my-lambda-input-bucket",
    "input_file": "data/input.txt",
    "output_bucket": "my-lambda-output-bucket"
}
```

Click **Test** to run the Lambda function.

### **4. Creating a JSON Script for a Step Functions State Machine**

Now, you'll need to create a Step Functions state machine to orchestrate the Lambda function(s).

#### **Step Functions State Machine Example**

Step Functions will help you manage the workflow by chaining Lambda functions or adding decision branches.

- **Create State Machine in the AWS Console**:
  - Go to the [Step Functions Console](https://console.aws.amazon.com/states/).
  - Click on **Create state machine**.
  - Choose **Author with code** or **Design your workflow**.
  - Use the following example JSON definition for a state machine:

```json
{
  "StartAt": "LambdaTransformTask",
  "States": {
    "LambdaTransformTask": {
      "Type": "Task",
      "Resource": "arn:aws:lambda:us-west-2:YOUR_ACCOUNT_ID:function:DataTransformFunction",
      "InputPath": "$",
      "OutputPath": "$",
      "ResultPath": "$.result",
      "End": true
    }
  }
}
```

- **Replace `YOUR_ACCOUNT_ID`** with your AWS account ID and update the Lambda function ARN (you can get this from the Lambda console).

- **IAM Role**:
  - When creating the state machine, you need an IAM role with permissions to invoke the Lambda function.
  - Create a role in the IAM console with the `AWSLambdaRole` policy and assign it to your Step Functions state machine.

- **Start the State Machine**:
  - Once the state machine is created, click **Start execution** and provide input in the following JSON format:

```json
{
  "input_bucket": "my-lambda-input-bucket",
  "input_file": "data/input.txt",
  "output_bucket": "my-lambda-output-bucket"
}
```

This will trigger the Lambda function, which processes the input data and stores the result in the output bucket.

### **5. Automating the Workflow**

You can also trigger Step Functions from other services (e.g., AWS S3 events, DynamoDB updates, etc.) to automatically start the pipeline.

#### Example: Triggering from S3

- **Set up an S3 Event Notification**:
  - Go to the **S3 Console**.
  - Choose your **input bucket** and go to the **Properties** tab.
  - Under **Event notifications**, create a new event to trigger a Lambda function whenever new files are uploaded.
  - This Lambda can trigger Step Functions by calling the `StartExecution` API.

### **6. Full Example**

Here's a full example of a Step Functions workflow that involves:

- Uploading a file to an S3 bucket.
- Triggering a Lambda function to process it.
- Storing the result in another S3 bucket.

```json
{
  "StartAt": "InvokeLambda",
  "States": {
    "InvokeLambda": {
      "Type": "Task",
      "Resource": "arn:aws:lambda:us-west-2:YOUR_ACCOUNT_ID:function:DataTransformFunction",
      "Input": {
        "input_bucket": "my-lambda-input-bucket",
        "input_file": "uploaded_file.txt",
        "output_bucket": "my-lambda-output-bucket"
      },
      "End": true
    }
  }
}
```

### **Final Steps**

- Monitor your Lambda functions and Step Functions executions through the AWS Console.
- Check the logs in Amazon CloudWatch for debugging purposes.
- Set up proper IAM roles and permissions to ensure that each service can access the required resources.

---

This process should give you the foundation for building an ETL pipeline using AWS Lambda and Step Functions. You can expand this architecture by adding more Lambda functions for different steps in your pipeline, adding error handling, and integrating with other AWS services as needed.

## Create a scalable ETL pipeline using EC2, and RDS

Yes, you can create a scalable ETL pipeline using EC2 and RDS by leveraging the scalability and flexibility of both services. Here's how you can design and implement a scalable ETL pipeline that can handle large volumes of data, process it efficiently, and store it in Amazon RDS.

### **Architecture Overview**

1. **Amazon EC2** will run your ETL jobs (extract, transform, and load). EC2 instances can scale vertically (bigger instances) or horizontally (multiple instances).
2. **Amazon RDS** (Relational Database Service) will be the storage layer for the processed data. RDS supports multiple databases like MySQL, PostgreSQL, SQL Server, and more, which will store the final transformed data.
3. **S3** (optional) can be used for storing raw data or intermediate results, enabling easy scalability for the ETL pipeline.
4. **Auto Scaling**: You can set up an Auto Scaling group for EC2 to dynamically scale based on the workload.
5. **Amazon CloudWatch**: Use for monitoring the EC2 instances and ETL jobs.

---

### **Steps to Build the ETL Pipeline Using EC2 and RDS**

#### **1. Set up RDS for Data Storage**

Start by setting up Amazon RDS, where the transformed data will be stored.

##### Steps to set up RDS

1. **Go to the Amazon RDS Console** and click **Create Database**.
2. Select your preferred database engine (e.g., **PostgreSQL**, **MySQL**, etc.).
3. Choose **Standard Create** and configure database settings:
   - **DB Instance Class**: Select an instance size (you can start small and scale later).
   - **Storage Type**: Choose between **General Purpose SSD (gp2)** or **Provisioned IOPS (io1)** for better performance.
   - **VPC**: Choose the correct VPC for security and networking.
4. **Database Credentials**: Create a database username and password.
5. **Set Up Security**: Create a security group that allows your EC2 instance to connect to the RDS instance.
6. **Create Database**: Click **Create database**.

Make sure you note down the **Endpoint**, **Username**, and **Password** for later use when connecting your EC2 instance to the database.

#### **2. Set up EC2 for Running ETL Jobs**

EC2 will handle the extraction, transformation, and loading of the data. Depending on your workload, you can set up EC2 Auto Scaling to dynamically scale the instances as required.

##### Steps to set up EC2

1. **Go to the EC2 Console** and click **Launch Instance**.
2. Select an AMI (Amazon Machine Image). For this ETL pipeline, you can use a standard **Amazon Linux 2** or **Ubuntu** instance.
3. **Choose an Instance Type**: You can start with a `t2.micro` for testing and scale up to more powerful instances like `t3.medium` or larger as the data grows.
4. **Configure Instance**: Set up networking and IAM roles (e.g., allow EC2 to read from S3 if necessary).
5. **Add Storage**: Attach an Elastic Block Store (EBS) volume to the instance for temporary storage of intermediate results.
6. **Configure Security Group**: Allow access from your IP and allow communication to the RDS instance on the database port (e.g., 3306 for MySQL).
7. **Launch Instance**: Launch the instance and note the public IP and SSH key to connect to it.

#### **3. Install Required Tools on EC2**

Once your EC2 instance is up, connect to it via SSH and install necessary tools such as `Python`, `pip`, and libraries for ETL tasks, and the RDS database connector (e.g., `psycopg2` for PostgreSQL or `mysql-connector-python` for MySQL).

```bash
# SSH into your EC2 instance
ssh -i your-ec2-key.pem ec2-user@<EC2_PUBLIC_IP>

# Install Python and pip
sudo yum install python3
pip3 install boto3 psycopg2 pandas sqlalchemy

# If you are dealing with S3 data, install AWS CLI
pip3 install awscli
```

#### **4. Develop the ETL Script on EC2**

Your ETL script will extract data, process it, and load it into the RDS instance. The script can be triggered manually, by a cron job, or integrated into an Auto Scaling group with monitoring.

Here’s an example Python ETL script that connects to S3, processes the data, and stores the transformed data into an RDS database.

```python
import boto3
import pandas as pd
import psycopg2
from sqlalchemy import create_engine

# AWS S3 Configuration
s3 = boto3.client('s3')
bucket_name = "my-etl-data-bucket"
input_key = "raw_data.csv"
output_key = "processed_data.csv"

# Download data from S3
s3.download_file(bucket_name, input_key, '/tmp/raw_data.csv')

# Load raw data into a pandas DataFrame
raw_data = pd.read_csv('/tmp/raw_data.csv')

# Perform data transformation (for example, converting to uppercase)
transformed_data = raw_data.applymap(lambda x: x.upper() if isinstance(x, str) else x)

# Save transformed data locally (can also upload to S3)
transformed_data.to_csv('/tmp/processed_data.csv', index=False)

# Database Connection Settings (RDS)
rds_host = "my-rds-endpoint.amazonaws.com"
rds_user = "my_db_user"
rds_password = "my_db_password"
db_name = "my_database"

# Create a SQLAlchemy engine for database connection
engine = create_engine(f'postgresql://{rds_user}:{rds_password}@{rds_host}/{db_name}')

# Load the transformed data into RDS (PostgreSQL in this case)
transformed_data.to_sql('processed_table', engine, if_exists='replace', index=False)

# Optionally upload processed data back to S3
s3.upload_file('/tmp/processed_data.csv', bucket_name, output_key)
```

#### **5. Automate the ETL Pipeline**

You can automate your ETL pipeline by setting up a cron job on EC2 or using AWS services like **Amazon CloudWatch** and **AWS Lambda** to schedule and trigger your ETL jobs.

1. **Set up Cron Jobs**:
   - To run the ETL job at specific intervals, add the following cron job entry:

     ```bash
     crontab -e
     ```

     Then add a line like:

     ```none
     0 * * * * /usr/bin/python3 /home/ec2-user/etl_script.py
     ```

     This would run the ETL script every hour.

2. **Use CloudWatch Events**:
   - You can trigger your EC2 instances based on schedules using CloudWatch Events. Create a rule that invokes an EC2 instance at specific intervals.

#### **6. Set Up Auto Scaling for EC2**

For scalability, set up an **Auto Scaling Group** to automatically scale the number of EC2 instances based on the workload. This is useful if the ETL job is expected to process large data volumes.

##### Steps

1. **Go to the EC2 Console** and navigate to **Auto Scaling Groups**.
2. Create a new Auto Scaling Group based on a launch configuration you created earlier.
3. Define scaling policies (e.g., scale up when CPU utilization > 70% or queue length increases).
4. Monitor the scaling activity using **CloudWatch** metrics.

#### **7. Monitor the Pipeline with CloudWatch**

CloudWatch is used to monitor the performance of EC2, RDS, and Lambda (if used). Set up CloudWatch Alarms to get notified when the pipeline is underperforming or has failed.

#### **8. (Optional) Use Step Functions to Orchestrate**

You can use AWS **Step Functions** to orchestrate the entire pipeline. This allows you to define workflows where each step (e.g., Extract, Transform, and Load) can be represented as a state in the state machine. If any of the tasks fail, you can easily retry or handle errors.

---

### **Conclusion**

This architecture provides a scalable ETL pipeline using EC2, RDS, and S3. As your data volume increases, you can scale your EC2 instances (vertically or horizontally) and your RDS database (by upgrading instance types or using Aurora with read replicas).

Key features of the solution:

- **EC2 Auto Scaling**: Scales the ETL computation based on workload.
- **RDS**: Stores the transformed data in a relational database.
- **S3**: Stores raw and intermediate data.
- **CloudWatch**: Monitors and triggers alarms for scaling and failures.
- **Step Functions**: Orchestrates complex ETL workflows.

This solution can be extended to meet even more complex ETL needs by adding additional processing steps, error handling, and distributed processing.
