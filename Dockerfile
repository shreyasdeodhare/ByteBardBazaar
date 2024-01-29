# Use the official Python image as the base image
FROM python:3.9

# Set the working directory within the container
WORKDIR /app

# Copy the project files into the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port on which the application will run
EXPOSE 8000

# Set the environment variable for Flask
ENV FLASK_APP=com.project.controller.CwppController

# Command to run the Flask application
CMD ["python","CwppController.py"]
