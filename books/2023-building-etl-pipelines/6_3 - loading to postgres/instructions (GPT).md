#

## postgres in a docker container using docker compose

To run a **PostgreSQL database** in a **Docker container** using **Docker Compose**, create a `docker-compose.yml` file with the following configuration:

---

### **1. Create `docker-compose.yml`**

```yaml
services:
  postgres:
    image: postgres:15  # Use the latest or specific version
    container_name: postgres_container
    restart: always  # Ensures it restarts if it crashes
    environment:
      POSTGRES_USER: myuser
      POSTGRES_PASSWORD: mypassword
      POSTGRES_DB: mydatabase
    ports:
      - "5432:5432"  # Expose PostgreSQL port
    volumes:
      - pgdata:/var/lib/postgresql/data  # Persist data

volumes:
  pgdata:  # Named volume to persist database data
```

---

### **2. Run the PostgreSQL Container**

Make sure **Docker and Docker Compose** are installed, then run:

```sh
docker compose up -d
```

- The `-d` flag runs it in the background.
- PostgreSQL will be accessible on `localhost:5432`.

---

### **3. Connect to PostgreSQL**

#### **A. Using `psql` (PostgreSQL CLI)**

```sh
docker exec -it postgres_container psql -U myuser -d mydatabase
```

#### **B. Using a PostgreSQL Client**

- Host: `localhost`
- Port: `5432`
- Username: `myuser`
- Password: `mypassword`
- Database: `mydatabase`

---

### **4. Stop & Remove the Container**

To stop and remove everything:

```sh
docker compose down
```

If you want to remove all data as well:

```sh
docker compose down -v
```
