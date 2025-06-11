# Use a minimal Python base image (Alpine for smallest footprint)
FROM python:3.13-alpine

LABEL time="2025-06-10-01:30" \
      description="A minimal Dockerfile for a Flask application with Gunicorn"

# Create a non-root user and group
RUN addgroup -S appgroup && adduser -S appuser -G appgroup

# Set the working directory in the container
WORKDIR /app

# Install build dependencies only if needed, then remove (uncomment if you need to build wheels)
# RUN apk add --no-cache build-base

# Copy requirements and install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy only necessary files
COPY app ./app
COPY main.py ./main.py

# Fix permissions for static files and all app content
RUN chown -R appuser:appgroup /app

# Set environment variables for Flask production
ENV FLASK_APP=main.py
ENV FLASK_ENV=production

# Expose the port that the app runs on
EXPOSE 8080

# Change to non-root user
USER appuser

# Command to run the application with Gunicorn
CMD ["gunicorn", "main:app", "--bind", "0.0.0.0:8080", "--workers=2"]