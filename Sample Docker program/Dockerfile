# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /testwork

# Copy the Python script to the container
COPY test.py /testwork/

# Run the Python script when the container launches
ENTRYPOINT ["python", "/testwork/test.py"]
