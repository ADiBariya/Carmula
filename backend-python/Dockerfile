# Dockerfile for Flask API Server

# Use the official Python image from the Docker Hub
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container
copy requirements.txt ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
cOPY . .

# Expose the port the app runs on
EXPOSE 5000

# Specify the command to run the app
CMD ["flask", "run", "--host=0.0.0.0"]