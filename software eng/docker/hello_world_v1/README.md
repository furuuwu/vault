Run a hello world program

0. Make sure you have docker engine running

to do that, type any docker command

eg. `docker`, `docker info`, `docker ps`

or check the docker service status (on Linux)

`systemctl status docker`

If it's not running, 
* if you are using Docker Desktop, just "opening" that program should work
* if you are using only the docker engine, start that process

1. Create the Dockerfile and hello.py

```Dockerfile
# Use an official Python runtime as the base image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy your Python script into the container
COPY hello.py .

# Default command to run the script
CMD ["python", "hello.py"]
```

Explanation

`FROM python:3.10-slim` defines the base image. I'm using a python official image.
This is pulled from DockerHub - the online store of publicly available images

https://hub.docker.com/search?badges=official

In particular, you look for the python docker image

https://hub.docker.com/_/python

There's actually a lot of images available, identified by tags. You choose one...

The rest is self-explanatory i think

`WORKDIR /app` changes the working directory to /app.

Then you copy the relevant folders into the image

The `COPY hello.py .` instruction in the Dockerfile copies the hello.py file from the host machine (the build context) into the current working directory inside the Docker container.
In gernal, the copy command copies the files in the location in the first argument, which is the host machine to the 2nd argument, which is the docker container

2. Build the Docker Image

`docker build -t python-hello-world .`

python-hello-world is the name (or tag) of the Docker image you are building. You will create containers based on this image.

. refers to the build context, which is the current directory where the Dockerfile is located

`docker build` is the same as `docker image build` (newer syntax)

To list all Docker images on your system

`docker images` or `docker image ls` (newer syntax)

This will display a table with details about each image, including:

    REPOSITORY: The name of the image.
    TAG: The tag or version of the image.
    IMAGE ID: The unique ID assigned to the image.
    CREATED: When the image was created.
    SIZE: The size of the image.

To delete an image, use the docker rmi command followed by the image name or image ID

eg. `docker rmi python-hello-world`

If you want to remove all unused images (dangling images) `docker image prune`

To push a docker image tp a docker registry (eg. Docker Hub) use

`docker push` or `docker image push` (newer syntax)

eg. `docker image push username/my-image`

Requires that the image is tagged correctly (e.g., with your Docker Hub username). You haven’t worked with pushing images yet, but this would be the way to upload your image to share it or use it elsewhere.

3. Run the Docker Container

`docker run python-hello-world`

this will create and run a container based on the python-hello-world image. However, by default, Docker assigns a random name to the container, unless you explicitly specify a name.

`docker run` is the same as `docker container run` (newer syntax)

To list the running containers: `docker ps` or `docker container ls` (newer syntax)

To list the existing containers (including stopped ones): `docker ps -a`.

You can use these commands to see the name or id and manage the container.

Or, you can give it a name when you create it

`docker run --name my-container-name python-hello-world`

To stop a container, `docker stop <container_id_or_name>`

To delete a container, `docker rm <container_id_or_name>`. 
If you want to stop and remove a container in one command, use the -f flag (force) `docker rm -f <container_id_or_name>`. 
To remove all stopped containers `docker container prune`