#

## instructions

the way I'm doing it is i ran the build the first time

```bash
docker compose up --build
```

and after that,

```bash
docker compose up --scale spark-worker=3 -d
```

For now, there's no mariadb ctn tho
