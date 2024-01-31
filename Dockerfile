# Use a smaller base image
FROM python:3.9-slim

# Set the working directory within the container
WORKDIR /app

# Copy only the necessary files
COPY . .

# Install dependencies and clean up
RUN apt-get update && \
    apt-get install -y --no-install-recommends build-essential && \
    pip install --no-cache -r requirements.txt && \
    apt-get purge -y --auto-remove build-essential && \
    rm -rf /var/lib/apt/lists/*

# Expose the port on which the application will run
EXPOSE 8000

# Set environment variables for Flask and database connection
ENV FLASK_APP=com.project.controller.CwppController
ENV DB_HOST=127.0.0.1 
ENV DB_PORT=3306
ENV DB_USER=ecomm
ENV DB_PASSWORD=shreyas
ENV DB_NAME=ecommerce

# Command to run the Flask applicatio
CMD ["python", "main.py"]
 
