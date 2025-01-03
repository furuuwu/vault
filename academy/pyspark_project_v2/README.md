#

## changes relative to pyspark_project/

* there's database containers now. That's it

    * Run the commands on `notebooks/initialize_db.ipynb` to set up the sakila database.
    * Run `spark_apps/spar_sakila.ipynb` to run Spark in that notebook


## instructions

* (Optional) Create a virtual environment and activate it

  this is useful if you want to install stuff

* To run the Spark standalone cluster:

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

* To run a spark job:

  ```bash
  docker exec da-spark-master env \
    PYSPARK_DRIVER_PYTHON=/usr/bin/python3 \
    PYSPARK_DRIVER_PYTHON_OPTS="" \
    spark-submit \
    --master spark://spark-master:7077 \
    --deploy-mode client \
    /opt/spark/apps/data_analysis_book/chapter03/word_non_null.py
  ```

* To run a jupyter notebook:

  since jupyter is installed on the spark master, just create a `.ìpynb` inside `spark_apps/` and it should work
