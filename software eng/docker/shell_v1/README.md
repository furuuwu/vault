create a Dockerfile that just runs a shell script

1. create the shell script

```bash
#!/bin/bash

echo "Hello from inside the container!"
# Add any other commands you'd like to run here
```

2. create the Dockerfile

```Dockerfile
# Use an official Python image as a base
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the shell script into the container
COPY run.sh .

# Make sure the shell script is executable
RUN chmod +x run.sh

# Default command to run the shell script
CMD ["./run.sh"]
```

We are still using that same ython image, but we install bash to interact with iut later

3. Build and run it

`docker build -t shell-script-container .`

`docker run shell-script-container`

Optional: Debugging or Interacting with the Container
If you want to interact with the container (e.g., to test or debug the shell script), you can override the CMD and start a shell instead:

`docker run -it shell-script-container /bin/sh`

This will give you access to an interactive shell (-it flag) inside the container. From there, you can manually run the script or other commands.

If you wanted to use bash instead of sh, install that

```Dockerfile
FROM python:3.10-slim

# Install bash
RUN apt-get update && apt-get install -y bash

# ...

```

`docker run -it shell-script-container /bin/bash`