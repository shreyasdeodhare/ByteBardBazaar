# Use a smaller base image
FROM python:3.9-slim

# Set the working directory within the container
WORKDIR /app

# Copy only the necessary files
# Copy the rest of the project files
COPY . .

#RUN pip install -r requirements.txt 

# Install dependencies
RUN pip install  --no-cache -r requirements.txt



# Expose the port on which the application will run
EXPOSE 8000

# Set the environment variable for Flask
ENV FLASK_APP=com.project.controller.CwppController

# Command to run the Flask application
CMD ["python", "CwppController.py"]
