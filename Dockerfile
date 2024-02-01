# Use a smaller base image
FROM python:3.9-slim

# Set the working directory within the container
WORKDIR /app

# Copy only the necessary files
COPY . .

# Copy requirements.txt to a temporary location
COPY requirements.txt /tmp/requirements.txt

# Install dependencies only if requirements.txt has changed
RUN pip install --no-cache -r /tmp/requirements.txt

# Remove the temporary requirements.txt
RUN rm /tmp/requirements.txt

# Expose the port on which the application will run
EXPOSE 8000

# Set environment variables for Flask and database connection
ENV FLASK_APP=com.project.controller.CwppController
ENV DB_HOST=127.0.0.1
ENV DB_PORT=3306
ENV DB_USER=root
ENV DB_PASSWORD=shreyas
ENV DB_NAME=ecommerce
ENV DB_SERVER_NAME=redberyl

# Command to run the Flask application
CMD ["python", "main.py"]
