"""
Flask Context Processors Module
================================

Provides global template context variables for consistent navigation and branding
across all pages in the portfolio application. Context processors automatically
inject data into every template render, eliminating code duplication.

Features:
- Global navigation menu with dynamic URL generation
- Consistent footer links across all pages
- Application name injection from configuration
- Icon integration for visual navigation
- Social media and professional profile links

Architecture:
- Context processors run on every template render
- Dynamic URL generation ensures correct routing
- Configuration-driven app naming for easy branding updates
- Centralized link management for maintainability

Template Usage:
All templates automatically receive:
- nav_links: Array of navigation menu items with URLs and icons
- footer_links: Array of social/professional links with logos
- app_name: Configured application name for branding
"""

from flask import url_for, current_app

def inject_nav_links():
    """
    Inject navigation links and app name into all templates
    
    Creates the primary navigation menu structure used across all pages.
    Generates dynamic URLs using Flask's url_for to ensure correct routing
    even if route patterns change.
    
    Returns:
        dict: Template context containing:
            - nav_links: List of navigation items with href, icon, and label
            - app_name: Application name from configuration (fallback: "me2u Portfolio")
    
    Navigation Structure:
        - Education: Academic background and degrees
        - Certifications: Professional credentials and validations
        - Achievements: Career highlights and project showcases
        - Tech Stack: Technology skills and tool proficiency
        - IRL: Personal interests and lifestyle content
        - Connect: Contact information and social links
    """
    nav_links = [
        {"href": url_for('routes.education'), "icon": "fas fa-graduation-cap", "label": "EDUCATION"},
        {"href": url_for('routes.certifications'), "icon": "fas fa-certificate", "label": "CERTIFICATIONS"},
        {"href": url_for('routes.achievements'), "icon": "fas fa-trophy", "label": "ACHIEVEMENTS"},
        {"href": url_for('routes.techstack'), "icon": "fas fa-laptop-code", "label": "PORTFOLIO TECH STACK"},
        {"href": url_for('routes.irl'), "icon": "fas fa-users", "label": "IRL"},
        {"href": url_for('routes.connect'), "icon": "fas fa-link", "label": "CONNECT"},
    ]
    return dict(nav_links=nav_links, app_name=current_app.config.get("APP_NAME", "me2u Portfolio"))

def inject_footer_links():
    """
    Inject footer social/professional links into all templates
    
    Provides consistent footer with social media and professional profile links.
    Uses static file URL generation for logo images to ensure proper asset loading.
    
    Returns:
        dict: Template context containing:
            - footer_links: List of social links with href, logo image, and label
    
    Footer Links:
        - LinkedIn: Professional networking profile
        - GitHub: Code repositories and development activity
        
    Note: Logo images are served from static/images/logos/ directory
    Dark theme GitHub logo used for consistent visual design
    """
    footer_links = [
        {"href": "https://www.linkedin.com/in/alan-r-smith/", "logo": url_for('static', filename='images/logos/logo-linkedin.png'), "label": "LinkedIn"},
        {"href": "https://github.com/SmithAndGiggles", "logo": url_for('static', filename='images/logos/logo-github-dark.png'), "label": "GitHub"},
    ]
    return dict(footer_links=footer_links)

# Registration Instructions:
# These context processors must be registered in the Flask application factory (__init__.py):
# app.context_processor(inject_nav_links)
# app.context_processor(inject_footer_links)
#
# Once registered, all templates automatically receive these context variables
# without needing to pass them explicitly in route render_template() calls.