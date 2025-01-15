The program will generate a histogram using Matplotlib and save it as histogram.png in the working directory (/app inside the container).

Steps:

1. Create a histogram program

2. Create the Dockerfile (and docker-compose.yml - optional)

```Dockerfile
# Use an official Python image as a base
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all the code into the container
COPY . .

# Default command to run the script
CMD ["python", "histogram.py"]
```

The difference from the previous ones is now we run pip to install the stuff we need when the container is built. 

Also, instead of copying just one file, we copy everything (except, as mentioned below, what is listed in the .dockerignore file) 

3. Create a .dockerignore file to exclude files from being copied into the Docker image

You can exclude your virtual environment (venv), the folder with the data, the git folder, etc...


4. Run as usual


`docker build -t python-histogram-image .`

`docker run --name python-hist-ctn python-histogram-image`

Besides the console output, you can copy the file created to the host for verification

`docker cp python-hist-ctn:/app/histogram.png .`