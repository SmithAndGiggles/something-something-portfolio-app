"""
Portfolio Data Aggregation Module
==================================

Centralized data provider for all portfolio content sections. This module implements
the DRY (Don't Repeat Yourself) principle by consolidating all card data, content,
and portfolio information in a single maintainable location.

NOW USES CONSTANTS for maximum DRY approach - no more duplicate strings!

Features:
- Unified data access layer for all portfolio sections
- DRY helper functions for consistent card generation
- Dynamic URL generation for logos and assets
- Type-consistent data structures for template rendering
- Single source of truth for portfolio content via constants.py

Architecture:
- Factory functions for each portfolio section (education, certifications, etc.)
- Internal helper functions for DRY card generation
- Flask url_for integration for dynamic asset paths
- Consistent card structure across all content types
- Constants module for zero duplication

Data Sections:
- Education: Academic background and formal learning
- Certifications: Professional credentials and validations  
- Tech Stack: Technology skills organized by category
- Connect: Contact information and social links
- Home: Personal introduction and portfolio overview

Design Philosophy:
This module prioritizes maintainability by centralizing all content data.
Updates to portfolio information require changes in only one location (constants.py),
reducing maintenance overhead and ensuring consistency across the application.
"""

from flask import url_for
from .constants import (
    INSTITUTIONS, EDUCATION_PROGRAMS, CERTIFICATIONS, 
    TECHNOLOGIES, GCP_TECHNOLOGIES, SOCIAL_LINKS, BADGE_TEXT
)

def get_education_cards():
    """
    Generate education and academic background cards using CONSTANTS
    
    Now uses EDUCATION_PROGRAMS and INSTITUTIONS from constants.py
    No more hardcoded strings!
    """
    def edu_card_from_constants(program_data):
        """DRY helper using constants for education cards"""
        institution = INSTITUTIONS[program_data['institution']]
        return {
            "href": institution['url'],
            "logo_src": url_for('static', filename=f'images/logos/{institution["logo"]}'),
            "logo_alt": institution['alt'],
            "title": program_data['program'],
            "subtitle": f"{institution['name']} • {program_data['years']}",
            "badge_text": BADGE_TEXT['learn_more']
        }
    
    return [edu_card_from_constants(program) for program in EDUCATION_PROGRAMS]

def get_certification_cards():
    """
    Generate professional certification cards using CONSTANTS
    
    Now uses CERTIFICATIONS from constants.py - no more hardcoded strings!
    """
    def cert_card_from_constants(cert_data):
        """DRY helper using constants for certification cards"""
        return {
            "href": cert_data['url'],
            "logo_src": url_for('static', filename=f'images/logos/{cert_data["logo"]}'),
            "logo_alt": cert_data['alt'],
            "title": cert_data['title'],
            "subtitle": cert_data['subtitle'],
            "badge_text": BADGE_TEXT['view_badge_icon']
        }
    
    return [cert_card_from_constants(cert) for cert in CERTIFICATIONS.values()]

def get_techstack_cards():
    """
    Generate technology stack cards using CONSTANTS
    
    Now uses TECHNOLOGIES and GCP_TECHNOLOGIES from constants.py
    No more hardcoded strings! Much simpler and maintainable.
    """
    def tech_card_from_constants(tech_data):
        """DRY helper using constants for technology cards"""
        return {
            "href": tech_data['url'],
            "logo_src": url_for('static', filename=f'images/logos/{tech_data["logo"]}'),
            "logo_alt": tech_data['alt'],
            "title": tech_data['name'],
            "subtitle": tech_data['description'],
            "badge_text": BADGE_TEXT['learn_more']
        }
    
    def gcp_card_from_constants(tech_data):
        """DRY helper for GCP cards (different path)"""
        return {
            "href": tech_data['url'],
            "logo_src": url_for('static', filename=f'images/google-cloud/{tech_data["logo"]}'),
            "logo_alt": tech_data['alt'],
            "title": tech_data['name'],
            "subtitle": tech_data['description'],
            "badge_text": BADGE_TEXT['learn_more']
        }
    
    # Generate cards by category using constants
    frontend = [tech_card_from_constants(tech) for tech in TECHNOLOGIES.values() if tech['category'] == 'frontend']
    backend = [tech_card_from_constants(tech) for tech in TECHNOLOGIES.values() if tech['category'] == 'backend']
    infra = [tech_card_from_constants(tech) for tech in TECHNOLOGIES.values() if tech['category'] == 'infra']
    
    # Add GCP technologies to infrastructure
    infra.extend([gcp_card_from_constants(tech) for tech in GCP_TECHNOLOGIES.values()])
    
    return {"frontend": frontend, "backend": backend, "infra": infra}

def get_connect_cards():
    """
    Generate contact and social connection cards using CONSTANTS
    
    Now uses SOCIAL_LINKS from constants.py - no more hardcoded strings!
    """
    def connect_card_from_constants(social_data):
        """DRY helper using constants for social cards"""
        return {
            "href": social_data['url'],
            "logo_src": url_for('static', filename=f'images/logos/{social_data["logo"]}'),
            "logo_alt": social_data['alt'],
            "title": social_data['name'],
            "subtitle": social_data['description'],
            "badge_text": "View Profile" if "linkedin" in social_data['url'] else "View GitHub" if "github" in social_data['url'] else "Send Email"
        }
    
    return [connect_card_from_constants(social) for social in SOCIAL_LINKS.values()]

def get_home_card():
    """
    Generate homepage welcome card content
    
    Provides the main introduction content for the portfolio homepage.
    Features personal introduction, professional overview, and engaging
    call-to-action for visitors to explore the portfolio.
    
    Returns:
        dict: Home card context with image, title, and introduction text
        
    Content Features:
        - Cartoonized professional headshot
        - Personal welcome message with professional positioning
        - Portfolio exploration encouragement
        - Playful personality elements (emoji integration)
        - Growth mindset messaging (certification goals)
        
    Template Usage:
        Renders as the central hero content on home.html with image,
        title, and comprehensive introduction text.
        
    Design Notes:
        Balances professional presentation with personality to create
        an approachable and memorable first impression for visitors.
    """
    return {
        'image_src': 'images/content/cartoonized-alan-smith.png',
        'image_alt': 'Cartoonized Alan Smith',
        'card_title': 'Welcome to My Portfolio',
        'card_text': ("Hi, I'm Alan Smith—a technology enthusiast, lifelong learner, and passionate problem solver. "
                     "This website is a showcase of my journey, projects, and achievements, designed to give you a glimpse into my professional world and personal growth. "
                     "Explore my work, discover my story, and check out the certifications page—I'm hoping to have more than just three badges there soon!"
                     "<i class='fas fa-face-wink' style='color:#f7b731; font-size:1.3em; vertical-align:middle;'></i>")
    }
