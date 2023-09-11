# Use an official Python runtime as a parent image
FROM python:3.8-slim
ENV FLASK_APP movies.py
# Set the working directory in the container
WORKDIR /app


# Copy the current directory contents into the container at /app
COPY movies.py /app

# Install Flask
RUN pip install flask

# Expose port 5000
EXPOSE 5000

# Run the Flask application
CMD ["flask", "run", "--host", "0.0.0.0"]
