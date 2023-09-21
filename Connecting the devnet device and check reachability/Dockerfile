# Use an official Python runtime as a parent image
FROM python:3.8-slim

RUN pip install pyats[full]
RUN apt-get update && apt-get install -y openssh-client

# Set the working directory in the container
WORKDIR /pyats

# Copy the Python script to the container
COPY device_info.py /pyats/
COPY my_testbed.yaml /pyats/

# Run the Python script when the container launches
ENTRYPOINT ["python", "/pyats/device_info.py"]
