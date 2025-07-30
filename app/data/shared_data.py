# filepath: something-something-portfolio-app/app/data/shared_data.py

from flask import url_for
from .constants import INSTITUTIONS, TECHNOLOGIES

# DRY helper for creating consistent logo data structures
def _create_logo_data(filename, alt_text, name=None):
    """DRY helper for generating logo data with consistent structure"""
    return {
        'name': name or alt_text,
        'src': url_for('static', filename=f'images/logos/{filename}'),
        'alt': alt_text
    }

def get_shared_data():
    """
    Centralized data that appears across multiple templates.
    Uses DRY helpers and constants to reduce duplication and make updates easier.
    """
    
    # Generate education institutions using constants
    education_institutions = {
        key: _create_logo_data(inst['logo'], inst['alt'], inst['name'])
        for key, inst in INSTITUTIONS.items()
    }
    
    # Generate tech logos using constants
    tech_logos = {
        key: _create_logo_data(tech['logo'], tech['alt'], tech['name'])
        for key, tech in TECHNOLOGIES.items()
    }
    
    return {
        'education_institutions': education_institutions,
        'tech_logos': tech_logos,
        'common_styles': {
            'card_default': 'card rounded-4 bg-dark text-white h-100 hover-shadow',
            'achievement_image': 'w-100 h-100 achievement-media',
            'media_container': 'achievement-media w-100 h-100',
            'carousel_slide': 'carousel-item',
            'tech_card': 'tech-card h-100'
        },
        'external_links': {
            'linkedin_profile': 'https://www.linkedin.com/in/alan-smith-ca/',
            'github_profile': 'https://github.com/SmithAndGiggles',
            'credly_base': 'https://www.credly.com/badges/',
            'mayo_clinic_picc': 'https://www.mayoclinic.org/tests-procedures/picc-line/about/pac-20468748',
            'portfolio_email': 'mailto:alan@me2u.space'
        },
        'meta_data': {
            'site_title': 'Alan Smith - Portfolio',
            'site_description': 'Professional portfolio showcasing cloud engineering, full-stack development, and technical achievements.',
            'author': 'Alan Smith',
            'keywords': 'cloud engineer, full-stack developer, GCP, Python, Flask, DevOps'
        }
    }
