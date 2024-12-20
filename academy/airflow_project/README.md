Some exercises to practice:

1. 
> Create two tasks in a DAG:
> * Task 1: Print using a function defined in the DAG.
> * Task 2: Print using a function defined in a script located in the python_scripts folder.
> And call both tasks in sequence.

is the python_scripts folder inside dags or outside? If it's inside, it would look like this

```none
airflow_project/
├── dags/
│   ├── ex1_v1.py
|   |── python_scripts/
│       ├── __init__.py
│       ├── hello_from_module_inside_dags.py
```

Create a file with the DAG (`ex1.py`) inside the dags folder (`/dags`). The dags folder is where Airflow scans for DAG files.

Ensure Airflow is running (airflow scheduler and airflow webserver). Verify the DAG appears in the Airflow UI. It's the airflow scheduler that detects the new files. If that service is not running you can start it like

```bash
docker exec -it <scheduler-container-name> airflow scheduler
```

To interact with the UI, you need the webserver running. You can do it in the cli with

```bash
docker exec -it <webserver-container-name> airflow webserver
```

Trigger the DAG via the Airflow UI or CLI.

```bash
docker exec -it <scheduler-container-name> airflow dags trigger <dag_id>
```

The best practice is for helper code to be outside of /dags. In that case, it looks like this

```none
airflow_project/
├── dags/
│   ├── ex1_v2.py
|── python_scripts/
│   ├── __init__.py
│   ├── hello_from_module_outside_dags.py
```

for python to detect this code, it needs to exists on the container, and it needs to be added to the PATH

Adding to the PATH could be done in one of these ways

```python
task_internal_print = PythonOperator(
        task_id="internal_print_task",
        python_callable=lambda: __import__('python_scripts.hello_from_module_outside_dags').hello_from_module_outside_dags.say_hi,
    )
```

```python
python_scripts_path = '/opt/airflow/python_scripts'

def handler():
    sys.path.append(python_scripts_path)
    
    from python_scripts import titanic_to_mariadb
    titanic_to_mariadb.load_csv_to_mariadb()

# ...

task_external_print = PythonOperator(
        task_id="external_print_task",
        python_callable=handler,
    )
```

But you still need to move the files into the container, so it doesn't work. Instead, you need to add that folder as a volume in the docker compose file, like this

```yml
# ...
airflow-webserver:
    # ...
    volumes:
    # the already existin ones
    - ./dags:/opt/airflow/dags
    - ./logs:/opt/airflow/logs
    - ./plugins:/opt/airflow/plugins
    - ./data:/opt/airflow/data
    - ./airflow/config:/opt/airflow/config

    # the new one
    - ./python_scripts:/opt/airflow/python_scripts
```

By specifying the volumes section in your docker-compose.yml, you ensure that your python_scripts folder from the host machine is mounted into the Airflow container under the /opt/airflow/python_scripts path.

This approach means that you don't need to manually create directories or modify paths inside your DAG files. Instead, Airflow automatically detects modules located in ./python_scripts because the Docker volume mount brings that directory into the Airflow container as if it were native to the container.

In this case, the services that should have access to the python_scripts folder are the airflow-webserver, airflow-scheduler, and airflow-worker, as these are the ones that will likely need to access the custom Python scripts for tasks. The airflow-init service might not need this volume since it is used only to initialize the Airflow database.

As you can see, they are now here

![a](2024-12-19-18-43-17.png)

But to run the files, you still need to add them to the PATH, which could be done in one of these ways

```python
task_internal_print = PythonOperator(
        task_id="internal_print_task",
        python_callable=lambda: __import__('python_scripts.hello_from_module_outside_dags').hello_from_module_outside_dags.say_hi,
    )
```

```python
python_scripts_path = '/opt/airflow/python_scripts'

def handler():
    sys.path.append(python_scripts_path)
    
    from python_scripts import titanic_to_mariadb
    titanic_to_mariadb.load_csv_to_mariadb()

# ...

task_external_print = PythonOperator(
        task_id="external_print_task",
        python_callable=handler,
    )
```

<blockquote>
2. Create a DAG to import the dataset from data/titanic.csv into MariaDB

* Functions should be placed in the python_scripts folder.
* Load a CSV dataset into MariaDB using Airflow.
* Use the name load_titanic_2_mariadb.

</blockquote>

```none
airflow_project/
├── dags/
│   └── ex2.py  # The DAG file
├── python_scripts/
│   └── titanic_to_mariadb.py      # Script with the import logic
├── data/
│   └── titanic.csv                # The dataset
```

<blockquote>
3. Create a DAG to access MariaDB and query data from the join of client_details and client_contacts. Save the results into a .csv file in the data folder.
</blockquote>

<blockquote>
4. Create a DAG to copy a file, load, process, and save:
    
- In the /data folder, create a folder called file_source and another called file_destination (use the mkdir command inside the data directory or through the Windows interface).
- Use the command `chmod 777 -R <folder_name>` on both folders created.
- Copy the file to the file_source folder (using BashOperator).
- Load the file and apply preprocessing to the data.
- Save the file in the file_destination folder.
</blockquote>

Instead of changing permissions from within the container, you should change the permissions on the host machine where the data is stored (if it's mounted as a volume).

```bash
sudo chmod -R 777 data/file_source
sudo chmod -R 777 data/file_destination
```

Useless information - it's the Airflow worker container that needs the permissions, not the scheduler or webserver containers. The Airflow worker is responsible for executing the tasks in your DAGs. When you run a task like BashOperator, it is executed within the worker container.

use the BashOperator to perform the following:

* Copy the file from data/file_source/some_data.csv.
* Process the data (e.g., using bash commands or a script).
* Save the processed file in data/file_destination/some_data.csv

<blockquote>
5. Create a DAG that detects a macro value `{ds}`:

- Read the articles about macros.
- Pass the macro value to a Python function as an argument.
- [Link to article](https://medium.com/@laxmirathaur11/airflow-beyond-basics-part-4-6215e8e5d6be)
</blockquote>

The `{ds}` macro represents the execution date of the DAG run in the format YYYY-MM-DD. You can access this macro directly in your DAG definition.

<blockquote>
6. Create a parent DAG that triggers another DAG:

- The idea is to create a DAG that triggers the execution of another DAG.
- You can experiment with passing the file name from the parent DAG (e.g., titanic) to the child DAG.
- Print the dataframe.
- Use XCom.
</blockquote>

I think here we actually want to use a task to trigger another task...
* first Task: This will push the file name (titanic.csv) to XCom.
* second Task: This will pull the file name from XCom and use it to load the corresponding .csv file into a pandas DataFrame.


XComs (short for "Cross-Communication") in Apache Airflow. XComs are a way for tasks to exchange messages or small data between them, allowing tasks in a DAG to communicate with one another. XComs by default are only available within the context of a single DAG run.

To pass data between different DAGs, we can use a trigger mechanism (using ExternalTaskSensor or manually triggering a second DAG and passing the data via XCom from the parent to the child).

