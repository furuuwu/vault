Storing secrets in a file and importing them in Python can be done securely and efficiently using various methods. Here's a simple and safe approach:

---

### 1. **Use a `.env` File**
A `.env` file is a common method to store secrets such as API keys, passwords, or sensitive configurations. 

#### Steps:
1. **Create a `.env` file** (e.g., `secrets.env`):
    ```plaintext
    DB_HOST=localhost
    DB_USER=myuser
    DB_PASSWORD=mypassword
    API_KEY=myapikey12345
    ```

2. **Install the `python-dotenv` library**:
    ```bash
    pip install python-dotenv
    ```

3. **Load the `.env` file in Python**:
    ```python
    from dotenv import load_dotenv
    import os

    # Load environment variables from .env file
    load_dotenv('secrets.env')

    # Access variables
    db_host = os.getenv('DB_HOST')
    db_user = os.getenv('DB_USER')
    db_password = os.getenv('DB_PASSWORD')
    api_key = os.getenv('API_KEY')

    print(f"Database Host: {db_host}")
    ```

4. **Secure the `.env` file**:
   - Add it to `.gitignore` to prevent accidental upload to version control:
     ```
     # .gitignore
     *.env
     ```

---

### 2. **Use a JSON or YAML File**
If `.env` files aren't suitable, you can use a structured format like JSON or YAML.

#### For JSON:
1. **Create a JSON file** (e.g., `secrets.json`):
    ```json
    {
      "DB_HOST": "localhost",
      "DB_USER": "myuser",
      "DB_PASSWORD": "mypassword",
      "API_KEY": "myapikey12345"
    }
    ```

2. **Load it in Python**:
    ```python
    import json

    # Load secrets from the JSON file
    with open('secrets.json') as f:
        secrets = json.load(f)

    db_host = secrets['DB_HOST']
    db_user = secrets['DB_USER']
    db_password = secrets['DB_PASSWORD']
    api_key = secrets['API_KEY']

    print(f"API Key: {api_key}")
    ```

#### For YAML:
1. **Create a YAML file** (e.g., `secrets.yaml`):
    ```yaml
    DB_HOST: localhost
    DB_USER: myuser
    DB_PASSWORD: mypassword
    API_KEY: myapikey12345
    ```

2. **Install PyYAML**:
    ```bash
    pip install pyyaml
    ```

3. **Load it in Python**:
    ```python
    import yaml

    # Load secrets from the YAML file
    with open('secrets.yaml') as f:
        secrets = yaml.safe_load(f)

    db_host = secrets['DB_HOST']
    db_user = secrets['DB_USER']
    db_password = secrets['DB_PASSWORD']
    api_key = secrets['API_KEY']

    print(f"Database User: {db_user}")
    ```

---

### 3. **Use an Encrypted Secrets Manager**
For sensitive applications, consider a secrets manager like **AWS Secrets Manager**, **Azure Key Vault**, or **HashiCorp Vault**. These services provide secure storage and access via APIs.

#### Example with AWS Secrets Manager:
1. Install the AWS SDK:
    ```bash
    pip install boto3
    ```

2. Retrieve secrets in Python:
    ```python
    import boto3
    import json

    # Create a Secrets Manager client
    client = boto3.client('secretsmanager', region_name='your-region')

    # Fetch secret
    secret_name = 'your-secret-name'
    response = client.get_secret_value(SecretId=secret_name)
    secrets = json.loads(response['SecretString'])

    db_password = secrets['DB_PASSWORD']
    print(f"Database Password: {db_password}")
    ```

---

### 4. **Best Practices**
- **Never hard-code secrets** directly into your Python files.
- **Use environment variables** in production to store and manage secrets.
- **Restrict access** to secret files to only authorized users:
  ```bash
  chmod 600 secrets.env
  ```

Would you like a deeper example or assistance setting up one of these methods?