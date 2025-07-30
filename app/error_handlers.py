"""
Flask Error Handlers Module
============================

Provides centralized error handling for the portfolio application using Flask Blueprints.
Implements custom error pages with consistent branding and user-friendly messaging
for common HTTP error scenarios.

Features:
- Custom error pages for 400, 404, and 500 errors
- Dynamic content loading via dedicated error data modules
- URL generation support for error page assets
- Consistent error page styling and messaging
- Graceful error handling that maintains user experience

Architecture:
- Blueprint pattern for modular error handling
- Separate data modules for each error type's content
- Template rendering with context-specific error information
- Maintains application branding even during error states
"""

from flask import Blueprint, render_template, url_for
import importlib

# Dynamic import of error data modules for better organization
# Each error type has its own data module for maintainable content management
error_400 = importlib.import_module('.data.400_error', __package__)
error_404 = importlib.import_module('.data.404_error', __package__)
error_500 = importlib.import_module('.data.500_error', __package__)

# Blueprint registration for modular error handling
# app_errorhandler ensures these handlers work application-wide
errors = Blueprint('errors', __name__)

@errors.app_errorhandler(400)
def bad_request_error(error):
    """
    Handle 400 Bad Request errors
    
    Triggered when client sends malformed requests or invalid data.
    Provides user-friendly error page instead of raw HTTP error response.
    
    Args:
        error: Flask error object containing request details
        
    Returns:
        Tuple of (rendered error template, 400 status code)
        Template includes custom image, alt text, and user message
    """
    content = error_400.get_400_error_content(url_for)
    return render_template(
        "400-page.html",
        image_src=content["image_src"],
        image_alt=content["image_alt"],
        message=content["message"]
    ), 400

@errors.app_errorhandler(404)
def not_found_error(error):
    """
    Handle 404 Not Found errors
    
    Triggered when users navigate to non-existent pages or resources.
    Most common error - provides helpful navigation back to main portfolio.
    
    Args:
        error: Flask error object containing request details
        
    Returns:
        Tuple of (rendered error template, 404 status code)
        Template includes custom image, alt text, and helpful user message
    """
    content = error_404.get_400_error_content(url_for)
    return render_template(
        "404-page.html",
        image_src=content["image_src"],
        image_alt=content["image_alt"],
        message=content["message"]
    ), 404

@errors.app_errorhandler(500)
def internal_server_error(error):
    """
    Handle 500 Internal Server errors
    
    Triggered when application encounters unexpected server-side errors.
    Provides graceful degradation instead of exposing technical error details.
    
    Args:
        error: Flask error object containing error details
        
    Returns:
        Tuple of (rendered error template, 500 status code)
        Template includes apologetic message and guidance for user
        
    Note: In production, this helps maintain professional appearance
    even when application encounters unexpected issues.
    """
    content = error_500.get_500_error_content(url_for)
    return render_template(
        "500-page.html",
        image_src=content["image_src"],
        image_alt=content["image_alt"],
        message=content["message"]
    ), 500


