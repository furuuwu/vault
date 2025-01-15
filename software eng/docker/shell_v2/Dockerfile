# Use an official Ubuntu image as a base
FROM ubuntu:20.04

# Install bash (although it should be present by default in Ubuntu)
RUN apt-get update && apt-get install -y bash

# Set the working directory inside the container
WORKDIR /app

# Default command to run bash
CMD ["/bin/bash"]