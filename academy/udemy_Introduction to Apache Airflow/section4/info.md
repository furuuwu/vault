Here we add some DAGs

first, to have the correct context (and have your linter work), install airflow on the virtualenv

don't forget to activate the virtualenv and select the right interpreter

![](img/2024-12-18-17-01-13.png)


```bash
pip install apache-airflow
```

![](img/2024-12-18-16-39-03.png)

https://github.com/apache/airflow

Alternatively, instead of running the code locally (in Windows or your WSL), you can connect to the running docker container (airflow-webserver), which obviously already has those dependencies already there... so you don't need a virtualen/to install dependencies

Next, we also need the postgres provider

![](img/2024-12-18-17-21-05.png)

clicking the Use Provider button

```bash
pip install apache-airflow-providers-postgres==5.13.1
```

after defining DAGs (in the dags folder in this project setup), they show up on the web server

![](img/2024-12-18-18-04-17.png)

For any external operator (provider), you need to establish a connection to it. To do that, go to Admin>Connections

![](img/2024-12-18-18-05-41.png)

![](img/2024-12-18-18-07-19.png)

![](img/2024-12-18-18-08-36.png)

There's also the airflow cli

```bash
airflow --help
```

![](img/2024-12-18-18-16-58.png)

After you create a task, you can test it works right away by attaching to the scheduler container and running that task

You can attach to the container manually by identifying it
```
docker compose ps
```
![](img/2024-12-18-18-19-33.png)

mine is called section4-airflow-scheduler-1

and running a bash shell on it
```
docker exec -it section4-airflow-scheduler-1 bash
```
![](img/2024-12-18-18-23-49.png)

Or simply use the VSCode extension for that

![](img/2024-12-18-18-25-48.png)

then test the task

```bash
# airflow tasks test <name_of_the_task> <task_id> <a_date_in_the_past>

airflow tasks test user_processing create_table 2022-01-01
```

![](img/2024-12-18-18-36-11.png)