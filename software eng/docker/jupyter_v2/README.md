This is the TLRD

using bind mounts, you could do it like this

`docker build -t jupyter-notebook-image .`

`docker run -it -p 8888:8888 -v $(pwd)/notebooks:/app jupyter-notebook-image`

however, i ran into some problems later. I recommend just using docker compose

```yml
services:
  jupyter:
    image: jupyter-notebook-image # Use the prebuilt image from the previous step
    build: . # This is only needed if you want to build the image via Compose instead of using the prebuilt image
    ports:
      - "8888:8888"
    volumes:
      - ./notebooks:/app # Mount the notebooks directory on the local machine
    environment:
      - JUPYTER_TOKEN=your-token-here # Set the token for authentication (optional)

```

`docker-compose up`

and access the jupyter notebook on 

http://localhost:8888

don't forget to set the JUPYTER_TOKEN. The default is your-token-here