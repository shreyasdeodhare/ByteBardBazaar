# Use a smaller base image
FROM python:3.9-slim

# Set the working directory within the container
WORKDIR /app

# Copy only the necessary files
COPY . .

# Install dependencies
RUN pip install --no-cache -r requirements.txt

# Expose the port on which the application will run
EXPOSE 8000

# Set environment variables for Flask and database connection
ENV FLASK_APP=com.project.controller.CwppController
ENV DB_HOST=192.168.1.1
ENV DB_PORT=3306
ENV DB_USER=ecom
ENV DB_PASSWORD=shreyas
ENV DB_NAME=ecommerce

# Command to run the Flask application
CMD ["python", "main.py"]
