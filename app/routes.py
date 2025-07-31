"""
Flask Routes Module
==================

Defines all application routes for the portfolio website using Flask Blueprints.
This module implements a clean separation between routing logic and data access,
following Flask best practices for maintainable web applications.

Architecture:
- Blueprint pattern for modular route organization
- Data layer separation via dedicated data modules
- Template rendering with context-specific data injection
- URL generation support for dynamic content (carousels, images)

Route Structure:
- Core portfolio pages: /, /education, /certifications, /techstack, /connect
- Dynamic content: /achievements, /irl (with carousel support)
- Special landing page: /me2u-place for custom domain routing
"""

from flask import Blueprint, render_template, request, url_for
from .data.all_data import (
    get_education_cards, get_certification_cards, get_techstack_cards,
    get_connect_cards, get_home_card, get_shared_data
)
from .data.carousel_factory import get_achievement_slides, get_irl_slides
from .data.landing_data import get_landing_page_data

# Blueprint registration for modular route organization
# Enables clean separation of routing logic from application factory
routes = Blueprint('routes', __name__)

@routes.route('/')
def home():
    """
    Homepage route - Primary landing page for the portfolio
    
    Renders the main landing page with personal introduction card.
    This serves as the entry point for visitors and provides navigation
    to other portfolio sections.
    
    Returns:
        Rendered home.html template with home_card context
    """
    return render_template('pages/home.html', home_card=get_home_card())

@routes.route('/home')
def render_index():
    """
    Alternative homepage route for explicit /home navigation
    
    Provides same functionality as root route for users who explicitly
    navigate to /home. Maintains consistency in user experience.
    
    Returns:
        Rendered home.html template with home_card context
    """
    return render_template('pages/home.html', home_card=get_home_card())

@routes.route('/education')
def education():
    """
    Education showcase route
    
    Displays academic background, degrees, and formal education achievements.
    Renders cards showing educational institutions, degrees, and relevant coursework.
    
    Returns:
        Rendered education.html template with education cards data
    """
    return render_template('pages/education.html', cards=get_education_cards())

@routes.route('/achievements')
def achievements():
    """
    Professional achievements carousel route
    
    Showcases career highlights, projects, and accomplishments in an interactive
    carousel format. Uses url_for to generate dynamic image paths for achievements.
    
    Args:
        url_for: Flask URL generation function passed to data layer for dynamic content
        
    Returns:
        Rendered achievements.html template with carousel slides and configuration
    """
    slides = get_achievement_slides()
    return render_template('pages/achievements.html', slides=slides, carousel_id='achievementsCarousel')

@routes.route('/certifications')
def certifications():
    """
    Professional certifications showcase route
    
    Displays industry certifications, professional credentials, and skill validations.
    Presents certification cards with details about issuing organizations and dates.
    
    Returns:
        Rendered certifications.html template with certification cards data
    """
    return render_template('pages/certifications.html', cards=get_certification_cards())

@routes.route('/techstack')
def techstack():
    """
    Technology stack demonstration route
    
    Showcases technical skills organized by technology category (frontend, backend, infrastructure).
    Provides comprehensive view of development capabilities and tool proficiency.
    
    Returns:
        Rendered techstack.html template with categorized technology cards:
        - frontend_cards: Client-side technologies and frameworks
        - backend_cards: Server-side technologies and databases  
        - infra_cards: DevOps, cloud, and infrastructure tools
    """
    cards = get_techstack_cards()
    return render_template('pages/techstack.html', 
                         frontend_cards=cards['frontend'], 
                         backend_cards=cards['backend'], 
                         infra_cards=cards['infra'])

@routes.route('/irl')
def irl():
    """
    Personal interests and lifestyle carousel route
    
    Displays personal hobbies, interests, and "in real life" activities in an interactive
    carousel format. Shows the human side beyond professional accomplishments.
    
    Args:
        url_for: Flask URL generation function for dynamic image path generation
        
    Returns:
        Rendered irl.html template with personal interest slides and carousel configuration
    """
    slides = get_irl_slides()
    return render_template('pages/irl.html', slides=slides, carousel_id='irlCarousel')

@routes.route('/connect')
def connect():
    """
    Contact and networking route
    
    Provides contact information, social media links, and networking opportunities.
    Central hub for visitors to establish professional connections.
    
    Returns:
        Rendered connect.html template with contact cards and social links
    """
    return render_template('pages/connect.html', cards=get_connect_cards())

@routes.route('/me2u-place')
def me2u_place_landing():
    """
    Custom domain landing page route using DRY data approach
    
    Dedicated landing page for me2u.place domain visitors.
    Now uses centralized constants and data functions for maintainability.
    
    Note: This route enables multi-domain support while maintaining
    a single application codebase with DRY principles.
    
    Returns:
        Rendered landing.html template with landing page data from constants
    """
    return render_template('pages/landing.html', **get_landing_page_data())


@routes.route('/health')
def health():
    """
    Health check endpoint for monitoring and load balancers.
    
    This endpoint is used by:
    - Cloud Run health checks
    - Load balancer health probes  
    - Monitoring systems
    - CI/CD pipeline verification
    
    Returns:
        JSON response with health status and basic app info
    """
    import time
    from flask import jsonify
    
    health_data = {
        "status": "healthy",
        "timestamp": int(time.time()),
        "service": "portfolio-app",
        "version": "1.0.0",
        "checks": {
            "database": "not_applicable",
            "static_files": "ok",
            "templates": "ok"
        }
    }
    
    return jsonify(health_data), 200

