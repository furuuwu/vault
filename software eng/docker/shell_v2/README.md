`docker run -it ubuntu bash` runs you bash on the latest ubuntu but you can complicate things and define a custom image for that

1. create the Dockerfile

```Dockerfile
# Use an official Ubuntu image as a base
FROM ubuntu:20.04

# Install bash (although it should be present by default in Ubuntu)
RUN apt-get update && apt-get install -y bash

# Set the working directory inside the container
WORKDIR /app

# Default command to run bash
CMD ["/bin/bash"]
```

`FROM ubuntu:20.04`: This uses the official Ubuntu 20.04 image as a base.

`RUN apt-get update && apt-get install -y bash`: This ensures that bash is installed in the container (Ubuntu usually includes it by default, but this step ensures it's available).

`WORKDIR /app`: This sets the working directory inside the container to /app. You can change this if needed.

`CMD ["/bin/bash"]`: This is the default command that runs when the container starts. It opens a Bash shell (/bin/bash).

2. Build and run it

`docker build -t bash-container .`

`docker run -it bash-container`