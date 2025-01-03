#

## instructions

To run the Spark standalone cluster:

the way I'm doing it is i ran the build the first time

```bash
docker compose build

# and then
docker compose up -d

# or in one go,
# docker compose up --build -d
```

for more than one worker,

```bash
docker compose up --scale spark-worker=3 -d
```

To run a spark job:

* you could attach to the spark master and use

```bash
docker exec -it da-spark-master bash
python3 /opt/spark/apps/data_analysis_book/chapter03/word_non_null.py
```

* use this

```bash
docker exec da-spark-master env \
  PYSPARK_DRIVER_PYTHON=/usr/bin/python3 \
  PYSPARK_DRIVER_PYTHON_OPTS="" \
  spark-submit \
  --master spark://spark-master:7077 \
  --deploy-mode client \
  /opt/spark/apps/data_analysis_book/chapter03/word_non_null.py
```

this prepends the environment variables to the command. This is needed because the default, which is defined in the Dockerfile is:

```Dockerfile
ENV PYSPARK_DRIVER_PYTHON='jupyter'
ENV PYSPARK_DRIVER_PYTHON_OPTS='notebook --no-browser --port=8889'
```

You can verify that's what is set in the `/opt/spark/conf/spark-env.sh` in the spark master:

```bash
root@6410506b56e0:/opt/spark# env | grep PYSPARK
PYSPARK_DRIVER_PYTHON=jupyter
PYSPARK_DRIVER_PYTHON_OPTS=notebook --no-browser --port=8889
PYSPARK_PYTHON=python3
```

To run a jupyter notebook:

since jupyter is installed on the spark master, just create a `.ìpynb` inside `spark_apps/` and it should work
