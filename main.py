"""
Portfolio Application Entry Point
================================

This is the main entry point for the Flask portfolio application.
When run directly, it starts the development server with configuration
loaded from pyproject.toml and environment variables.

For production deployment, use a WSGI server like gunicorn:
    gunicorn main:app

Architecture Overview:
- Flask application factory pattern (app/__init__.py)
- Centralized configuration management (app/config.py)
- Cloud-agnostic design with environment-based configuration
- Docker containerization for consistent deployment across platforms
"""

# ----------------------
# IMPORTS
# ----------------------

from app import create_app
from app.config import config

# ----------------------
# APPLICATION INSTANCE
# ----------------------

# Create Flask app instance using the application factory pattern
# This allows for easy testing and multiple app configurations
app = create_app()

# ----------------------
# DEVELOPMENT SERVER
# ----------------------

# Only run the development server if this file is executed directly
# In production, this app instance is imported by WSGI servers (gunicorn)
if __name__ == "__main__":
    print(f"🚀 Starting {config.app_name} v{config.version}")
    print(f"🌐 Server running on {config.host}:{config.port}")
    print(f"🔧 Debug mode: {config.debug}")
    print(f"📱 Access at: http://{config.host}:{config.port}")
    
    # Start Flask development server
    # Note: Never use this in production - use gunicorn or similar WSGI server
    app.run(
        host=config.host,
        port=config.port,
        debug=config.debug
    )


