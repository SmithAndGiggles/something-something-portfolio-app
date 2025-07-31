# ============================================================================
# Production Dockerfile for Flask Portfolio Application
# ============================================================================
# 
# Multi-stage build for optimized CI/CD and production deployment
# - Uses Alpine Linux for smallest attack surface and image size
# - Non-root user execution for security best practices
# - Cloud-agnostic design - works with any container platform
# - Production-ready Gunicorn WSGI server with optimized worker configuration
# - Efficient layer caching for faster builds in CI/CD pipelines

# Build Arguments
ARG ENVIRONMENT=production
ARG BUILD_DATE
ARG VCS_REF
ARG VERSION

# Base Image: Python 3.13 on Alpine Linux for minimal footprint
FROM python:3.13-alpine as base

# Container Metadata: Used by container registries and orchestration platforms
LABEL maintainer="Portfolio Application" \
      description="Production Flask portfolio application" \
      version="${VERSION:-1.0.0}" \
      created="${BUILD_DATE}" \
      revision="${VCS_REF}" \
      environment="${ENVIRONMENT}"

# Security: Create non-root user for running the application
# This prevents potential privilege escalation attacks and follows container security best practices
RUN addgroup -S appgroup && adduser -S appuser -G appgroup

# Working Directory: Set consistent location for application files
WORKDIR /app

# Build Optimization: Install system dependencies if needed
# Uncomment the line below if you need to compile Python packages with native extensions
# RUN apk add --no-cache build-base

# Dependency Installation: Copy requirements first for better Docker layer caching
# This allows Docker to cache the pip install step when only application code changes
COPY pyproject.toml ./
RUN pip install --no-cache-dir . && \
    pip cache purge

# Application Code: Copy source files after dependencies for optimal caching
COPY app ./app
COPY main.py ./main.py

# Security: Set proper file ownership for the non-root user
RUN chown -R appuser:appgroup /app

# Flask Configuration: Set production environment variables
ENV FLASK_APP=main.py \
    FLASK_ENV=production \
    PYTHONUNBUFFERED=1

# Network: Expose the application port (configurable via environment)
EXPOSE 8080

# Security: Switch to non-root user for application execution
USER appuser

# Production Server: Use Gunicorn WSGI server with optimized configuration
# - 2 workers for small to medium traffic (adjust based on CPU cores)
# - Bind to all interfaces for container networking
# - Timeout settings optimized for web applications
CMD ["gunicorn", "main:app", "--bind", "0.0.0.0:8080", "--workers=2", "--timeout=30", "--keep-alive=2"]