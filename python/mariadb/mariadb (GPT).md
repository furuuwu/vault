# Running mariadb in a docker container

Running MariaDB in a Docker container is straightforward. Here's a step-by-step guide to get you up and running with MariaDB in Docker:

### 1. **Install Docker**:
   If you haven't already installed Docker, you can follow the instructions here to install it on your system:  
   [Install Docker](https://docs.docker.com/get-docker/)

### 2. **Pull the MariaDB Docker Image**:
   Once Docker is installed, open a terminal and pull the official MariaDB image:

   ```bash
   docker pull mariadb
   ```

### 3. **Run a MariaDB Container**:
   You can start a MariaDB container by running the following command. It will create and run a MariaDB container with a specified username, password, and database name:

   ```bash
   docker run --name mariadb-container -e MYSQL_ROOT_PASSWORD=my-secret-pw -e MYSQL_DATABASE=example_db -p 3306:3306 -d mariadb:latest
   ```

   **Explanation**:
   - `--name mariadb-container`: The name of the container (`mariadb-container` in this case).
   - `-e MYSQL_ROOT_PASSWORD=my-secret-pw`: Set the root password for MariaDB (`my-secret-pw`).
   - `-e MYSQL_DATABASE=example_db`: Create a database called `example_db` when the container starts.
   - `-p 3306:3306`: Map the MariaDB port `3306` from the container to `3306` on your host machine.
   - `-d`: Run the container in detached mode.
   - `mariadb:latest`: Use the latest MariaDB image.

   This will start a MariaDB container with the specified root password and the `example_db` database.

### 4. **Verify MariaDB Is Running**:
   You can check if the container is running by executing:

   ```bash
   docker ps
   ```

   You should see the container running, something like:

   ```bash
   CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                  NAMES
   abc1234efgh         mariadb:latest      "docker-entrypoint.s…"   10 seconds ago      Up 9 seconds        0.0.0.0:3306->3306/tcp mariadb-container
   ```

### 5. **Connect to MariaDB**:
   You can access the MariaDB server inside the container by running:

   ```bash
   docker exec -it mariadb-container mysql -u root -p
   ```

   Enter the password you set earlier (`my-secret-pw`). This will open the MariaDB shell.

   From here, you can verify the existence of the `example_db` database by running:

   ```sql
   SHOW DATABASES;
   USE example_db;
   SHOW TABLES;
   ```

### 6. **Update Your Python Code for Connection**:
   Now that you have the MariaDB container running, you can update your connection string in your Python code to connect to the MariaDB database running in Docker.

   Since the container is running on your local machine, the host will be `localhost` or `127.0.0.1`, and the port will be `3306` (which you mapped in the `docker run` command). The username will be `root`, and the password will be whatever you set (e.g., `my-secret-pw`).

   Here's the connection string to update in your code:

   ```python
   engine_url = "mysql+mysqlclient://root:my-secret-pw@localhost:3306/example_db"
   ```

### 7. **Test the Connection**:
   Run your Python script. If everything is set up correctly, it should be able to connect to the MariaDB instance running in Docker and execute the queries.

### 8. **Stopping and Removing the Container**:
   When you're done, you can stop the MariaDB container with:

   ```bash
   docker stop mariadb-container
   ```

   If you want to remove the container:

   ```bash
   docker rm mariadb-container
   ```

This setup will allow you to run MariaDB inside a Docker container and test your code with a real MariaDB database.


# Switching to a docker compose setup

Here’s how you can set up MariaDB using Docker Compose:

Docker Compose has evolved, and now it uses the `docker compose` command instead of the old `docker-compose` syntax. Also, the version field in `docker-compose.yml` is no longer required in newer versions of Docker Compose. Here's an updated guide using the newer syntax.

### Step 1: Create a `docker-compose.yml` File (Updated)

Create a `docker-compose.yml` file in your project directory with the following content:

```yaml
services:
  mariadb:
    image: mariadb:latest
    container_name: mariadb-container
    environment:
      MYSQL_ROOT_PASSWORD: my-secret-pw         # Root password
      MYSQL_DATABASE: example_db               # Database to be created
    ports:
      - "3306:3306"                            # Map container port 3306 to host port 3306
    volumes:
      - mariadb_data:/var/lib/mysql            # Persistent storage for database

volumes:
  mariadb_data:                             # Named volume for persistent storage
    driver: local
```

### Explanation:
- **services**: Defines the container services. In this case, only the `mariadb` service.
- **image**: Specifies the image to use (MariaDB latest).
- **container_name**: Sets a custom name for the container (`mariadb-container`).
- **environment**:
  - `MYSQL_ROOT_PASSWORD`: The root password for MariaDB (`my-secret-pw`).
  - `MYSQL_DATABASE`: The name of the database to be created (`example_db`).
- **ports**: Maps the container’s port 3306 to the host’s port 3306.
- **volumes**: Defines a persistent volume (`mariadb_data`) that stores database data on your local machine.

### Step 2: Start the MariaDB Service with Docker Compose

Once the `docker-compose.yml` file is created, you can start the service with the following command. This is the new `docker compose` command, replacing the old `docker-compose` syntax.

```bash
docker compose up -d
```

The `-d` flag runs the container in detached mode, meaning it runs in the background.

### Step 3: Verify the MariaDB Service is Running

To check if the MariaDB container is running, use the following command:

```bash
docker compose ps
```

You should see output like this:

```
       Name                     Command               State              Ports
--------------------------------------------------------------------------------
mariadb-container   docker-entrypoint.sh mysqld   Up 5 seconds         0.0.0.0:3306->3306/tcp
```

This indicates that the MariaDB container is running and accessible on port `3306`.

### Step 4: Access the MariaDB Container

To access the MariaDB instance, you can run the following command:

```bash
docker exec -it mariadb-container mysql -u root -p
```

Enter the password (`my-secret-pw`) when prompted.

Once inside the MariaDB shell, you can verify the database by running:

```sql
SHOW DATABASES;
USE example_db;
SHOW TABLES;
```

### Step 5: Update Your Python Code to Use the Dockerized MariaDB

Now that MariaDB is running inside Docker, update your Python connection string to use the `localhost` or `127.0.0.1` host and port `3306`.

```python
engine_url = "mysql+mysqlclient://root:my-secret-pw@localhost:3306/example_db"
```

### Step 6: Stop and Remove the Containers

When you're done testing, you can stop and remove the containers with:

```bash
docker compose down
```

This will stop the MariaDB container and remove it, but the data will persist due to the defined named volume (`mariadb_data`).

### Step 7: Restart the Containers (if needed)

To restart the containers later, run:

```bash
docker compose up -d
```

This will bring the containers back up with the existing configuration.

---

By using Docker Compose with the updated syntax (`docker compose`), you can easily manage your MariaDB container and integrate it into your development environment.


# ERROR - port is not available

```bash
$ docker compose up -d
[+] Running 1/2
 ✔ Network mariadb_default      Created                                                                 0.0s 
 - Container mariadb-container  Starting                                                                0.1s 
Error response from daemon: Ports are not available: exposing port TCP 0.0.0.0:3306 -> 0.0.0.0:0: listen tcp 0.0.0.0:3306: bind: Only one usage of each socket address (protocol/network address/port) is normally permitted.
```

The error you're encountering suggests that port `3306` on your host machine is already in use by another service (likely an existing MariaDB or MySQL instance running on your machine). Docker is unable to bind the port to the container because it is already occupied.

### To resolve this issue, you have a few options:

#### Option 1: Identify and Stop the Process Using Port 3306

1. **Find the process using port 3306**:
   You can find out which process is occupying port 3306 with the following command:

   - On **Windows**, open a command prompt or PowerShell window and run:
     ```bash
     netstat -ano | findstr :3306
     ```
     This will show you the process ID (PID) of the program using port 3306.

2. **Stop the process**:
   Once you have the PID, you can terminate the process that is using port 3306. You can do this by running:

   - On **Windows**:
     ```bash
     taskkill /PID <PID> /F
     ```
     Replace `<PID>` with the process ID you found earlier.

3. **Try running Docker Compose again**:
   After stopping the service using port 3306, run:
   ```bash
   docker compose up -d
   ```

#### Option 2: Change the Port Mapping in Docker Compose

If you don't want to stop the existing service on port 3306, you can modify the `docker-compose.yml` file to map the container’s port 3306 to a different port on your host machine.

For example, you could change the `ports` section in the `docker-compose.yml` file to something like this:

```yaml
ports:
  - "3307:3306"
```

This will map port `3306` inside the container to port `3307` on your host machine. After making this change, run:

```bash
docker compose up -d
```

You can then connect to the MariaDB instance using port `3307` instead of `3306`.

#### Option 3: Check if MariaDB is Running in Docker Already

If you've previously run a MariaDB container in Docker and it's still running, it could also be using port 3306. To list all running Docker containers, you can use:

```bash
docker ps
```

If you see a MariaDB container running, you can stop it with:

```bash
docker stop mariadb-container
```

After that, run:

```bash
docker compose up -d
```

This should resolve the issue and let Docker Compose bind port 3306 to your MariaDB container.


# ERROR - Can't load plugin: sqlalchemy.dialects:mysql.mysqlclient

The error message you're encountering indicates that SQLAlchemy is unable to load the plugin for the MySQL dialect (`mysqlclient`). This typically happens when the necessary database driver (`mysqlclient` or `PyMySQL`) is either not installed or not available in your environment.

Here’s how to resolve this:

### 1. Install the Required MySQL Client Library

You need to install a MySQL client library that SQLAlchemy can use to connect to your MariaDB database. You can install either `mysqlclient` or `PyMySQL`.

#### Option 1: Install `mysqlclient`
This is the recommended library for MySQL connections, but it requires compilation and may need some extra dependencies (like `libmysqlclient-dev` on Linux). To install it in your virtual environment, run:

```bash
pip install mysqlclient
```

#### Option 2: Install `PyMySQL`
If you have issues with `mysqlclient`, you can install `PyMySQL`, which is a pure Python library and is easier to install:

```bash
pip install PyMySQL
```

### 2. Update Your `create_engine` URL

After installing one of the client libraries, you may also need to adjust the connection URL in your `create_engine` statement. If you're using `PyMySQL`, you should modify your connection string to use `mysql+pymysql://` instead of `mysql://`.

For example:
```python
# If using PyMySQL
engine_url = "mysql+pymysql://root:my-secret-pw@127.0.0.1:3306/my_database"

# If using mysqlclient (this is the default)
engine_url = "mysql://root:my-secret-pw@127.0.0.1:3306/my_database"
```

### 3. Retry Running Your Code

Once you’ve installed the appropriate library (`mysqlclient` or `PyMySQL`) and updated your connection URL, try running your script again:

```bash
python c:/Users/ricga/OneDrive/obsidian_vaults/vault/python/mariadb/main.py
```

### Summary

- Install the `mysqlclient` or `PyMySQL` library using `pip`.
- Ensure your `create_engine` URL matches the library you installed (e.g., `mysql+pymysql://` for `PyMySQL` or `mysql://` for `mysqlclient`).
- Run your script again.

This should resolve the error you're encountering. Let me know if you need further assistance!