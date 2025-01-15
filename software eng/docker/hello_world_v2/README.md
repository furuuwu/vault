This is another way of using docker, jumping straight into another technology, docker-compose

This is a simpler way (in the long run) but it is optional. I'll have a example using just Dockerfile and a docker-compose for each anyway. 

0. Make sure you have docker engine running

1. Create the Dockerfile and hello.py, and the new docker-compose.yml file

```yml
services:
  # Defines the services (containers) to be run.
  hello-world:
    # Name of the service. You can name it anything
    build:
      # Build the image from the Dockerfile
      context: . # Use the current directory as the build context
      # that means, the Dockerfile in the current directory will be used
    command: python hello.py # Override the default command (optional)
    # in this case, it's optional because the Dockerfile already specifies CMD ["python", "hello.py"]
```

2. Start the Service

`docker-compose up`

and see the output

To stop the service, run `docker-compose down`

Explanation

When you run docker-compose up, it starts the services defined in your docker-compose.yml file.

You can start the services with `docker-compose up -d` to run them in the background.

`docker-compose ps -a` shows the status of all services in the current Compose project

The current Compose project refers to the group of services, networks, and volumes managed collectively by Docker Compose within the scope of a single docker-compose.yml file. Each Compose project is identified by a project name, which defaults to the name of the directory containing the docker-compose.yml file.