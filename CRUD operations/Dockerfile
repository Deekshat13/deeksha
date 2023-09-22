# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Define environment variables for MySQL
ENV MYSQL_ROOT_PASSWORD=deeksha
ENV MYSQL_DATABASE=flask
ENV MYSQL_USER=root
ENV MYSQL_PASSWORD=
# Install necessary packages
RUN apt-get update && apt-get install -y mariadb-server default-libmysqlclient-dev

# Install Flask and mysql-connector-python
RUN pip install flask mysql-connector-python

# Set the working directory in the container
WORKDIR /app

# Copy your Flask application code into the container
COPY flaskdb.py /app/

# Expose the MySQL port
EXPOSE 3306

# Make port 80 available to the world outside this container
EXPOSE 5000

# Define environment variables for Flask
ENV FLASK_APP=flaskdb.py
ENV FLASK_RUN_HOST=0.0.0.0

# Run your Flask application
CMD ["flask", "run"]
