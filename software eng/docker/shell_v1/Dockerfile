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