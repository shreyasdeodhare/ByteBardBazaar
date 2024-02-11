# Use a smaller base image
FROM python:3.9-slim

# Set the working directory within the container
WORKDIR /app

# Copy only the necessary files
COPY . .

# Copy requirements.txt to a temporary location
COPY requirements.txt /tmp/requirements.txt

# Upgrade pip and clear the cache
RUN pip install --no-cache-dir --upgrade pip && \
    pip cache purge

# Install dependencies only if requirements.txt has changed
RUN pip install --no-cache-dir -r /tmp/requirements.txt

# Remove the temporary requirements.txt
RUN rm /tmp/requirements.txt

# Expose the port on which the application will run
EXPOSE 8000

# Set environment variables for Flask and database connection
ENV FLASK_APP=com.project.controller.CwppController
# ENV DB_HOST=database-1.cdagy8kamvjs.ap-south-1.rds.amazonaws.com
# ENV DB_PORT=3306
# ENV DB_USER=admin
# ENV DB_PASSWORD=shreyas189
# ENV DB_NAME=ecommerce
# ENV DB_SERVER_NAME=aws

ENV DB_HOST=172.25.128.1
ENV DB_PORT=3306
ENV DB_USER=root
ENV DB_PASSWORD=shreyas
ENV DB_NAME=ecommerce
ENV DB_SERVER_NAME=redberyl


# ENV MYSQL_ROOT_PASSWORD=shreyas189
# ENV MYSQL_DATABASE=ecommerce
# ENV MYSQL_USER=admin
# ENV MYSQL_PASSWORD=shreyas189

ENV MYSQL_ROOT_PASSWORD=shreyas
ENV MYSQL_DATABASE=ecommerce
ENV MYSQL_USER=root
ENV MYSQL_PASSWORD=shreyas

# Copy the SQL dump file to initialize the database
COPY dump.sql /docker-entrypoint-initdb.d/

# Expose the port on which the MySQL database will run
EXPOSE 3306

# Command to run the Flask application
CMD ["python", "main.py"]
