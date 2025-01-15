By default, any changes you make inside a Docker container (such as creating or editing a Jupyter Notebook) will not persist when the container is stopped or deleted. However, you can set up volumes in Docker to ensure that changes are saved and persist outside the container.

How Docker Volumes Work
A volume is a persistent storage location managed by Docker. By mounting a volume, you can map a directory from your host machine to a directory inside the container. This way, any changes made in the container (e.g., creating or modifying Jupyter Notebooks) will be saved in the volume, and those changes will persist even if the container is stopped or deleted.

Setting Up a Volume in Docker
There are two ways to persist your Jupyter Notebooks when using Docker: by using a bind mount or a Docker volume. I’ll show you how to set up both methods.

Option 1: Using a Bind Mount (recommended for local directories)

A bind mount allows you to map a directory from your host machine to a directory inside the container. This is useful if you want to save your notebooks directly on your host machine (e.g., in a specific directory on your local filesystem).

`docker run -it -p 8888:8888 -v /path/to/your/local/directory:/app jupyter-notebook-image`

This tells Docker to mount the local directory /path/to/your/local/directory to the /app directory inside the container. Replace /path/to/your/local/directory with the path where you want to store your Jupyter Notebooks on your local machine.

For example, if you want to store your notebooks in a folder called notebooks in the current directory, you can use:

`docker run -it -p 8888:8888 -v $(pwd)/notebooks:/app jupyter-notebook-image`


Option 2: Using Docker Volumes

Alternatively, you can use Docker volumes, which are managed by Docker and can be shared between containers. Volumes are useful for persistent data that should be managed by Docker itself.

To use a volume, you can modify the docker run command like this:

`docker run -it -p 8888:8888 -v jupyter_notebooks:/app jupyter-notebook-image`

-v jupyter_notebooks:/app: This tells Docker to create a volume named jupyter_notebooks and mount it at /app inside the container. Any changes made in the /app directory inside the container will persist in the volume.

If you're using Docker Compose, here’s how to set it up:

```yml
services:
  jupyter:
    image: jupyter-notebook-image
    build: .
    ports:
      - "8888:8888"
    volumes:
      - jupyter_notebooks:/app  # Use a Docker volume
    environment:
      - JUPYTER_TOKEN=your-token-here

volumes:
  jupyter_notebooks:
```

This configuration will create a Docker-managed volume named jupyter_notebooks and mount it at /app inside the container.

With Docker volumes, you can inspect the volume with the following command:

```bash
docker volume ls
docker volume inspect jupyter_notebooks
```