# Use an official Python runtime as a parent image
FROM python:3.13-slim

# Set the working directory in the container
WORKDIR /app

# Copy requirements file if you have one (optional)
# If you don't have a requirements.txt file, install Flask separately
# COPY requirements.txt requirements.txt

# Install any needed packages specified in requirements.txt
# RUN pip install --no-cache-dir -r requirements.txt

# Install Flask (since your site may become dynamic later)
RUN pip install Flask

# Copy the current directory contents into the container at /app
COPY . /app

# Set the environment variable to indicate that Flask should serve the app
ENV FLASK_APP=main.py

# Expose the port that the app runs on
EXPOSE 8080

# Command to run the application
CMD ["flask", "run", "--host=0.0.0.0", "--port=8080"]