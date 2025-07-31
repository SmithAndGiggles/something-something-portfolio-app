"""
Flask Application Factory
=========================

This module implements the Flask application factory pattern, providing clean
separation of concerns and enabling multiple application instances with different
configurations. This design supports:

- Testing with isolated application contexts
- Multiple environments (development, staging, production)
- Cloud-agnostic deployment across different platforms
- Modular architecture with clear component boundaries

Application Architecture:
- Blueprints: Organize routes by functionality (main routes, error handlers)
- Context Processors: Inject global template variables (navigation, footer)
- Configuration: Environment-aware settings management
- Static Assets: Efficient serving of CSS, JavaScript, and images

The factory pattern allows this application to be imported by WSGI servers
(like Gunicorn) or testing frameworks without side effects during import.
"""

from flask import Flask
from .routes import routes
from .error_handlers import errors
from .context_processor import inject_nav_links, inject_footer_links
from .config import apply_config


def create_app(test_config=None):
    """
    Create and configure a Flask application instance.

    This function implements the application factory pattern, allowing multiple
    app instances to be created with different configurations. Each call returns
    a fully configured Flask application ready for use.

    Args:
        test_config (dict, optional): Override configuration for testing.
                                    If provided, will be applied after default config.

    Returns:
        Flask: Configured Flask application instance with all components registered

    Components Registered:
        - Blueprint routes: Main application endpoints and navigation
        - Error handlers: Custom 404, 500 error pages with consistent styling
        - Context processors: Global template variables for navigation and footer
        - Configuration: Environment-aware settings from pyproject.toml and env vars
    """
    # Create the Flask application instance
    app = Flask(__name__)

    # Apply configuration from pyproject.toml with environment variable overrides
    apply_config(app)

    # Apply test configuration if provided (for testing environments)
    if test_config:
        app.config.update(test_config)

    # Register Blueprint modules for modular route organization
    app.register_blueprint(routes)  # Main application routes and pages
    app.register_blueprint(errors)  # Error handling (404, 500, etc.)

    # Register context processors for global template data
    # These functions run before every template render to inject common variables
    app.context_processor(inject_nav_links)  # Navigation menu items and links
    app.context_processor(inject_footer_links)  # Footer social media and external links

    return app
