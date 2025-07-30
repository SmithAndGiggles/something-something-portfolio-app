"""Portfolio data provider with shared utilities"""

from flask import url_for
from .constants import (
    INSTITUTIONS, EDUCATION_PROGRAMS, CERTIFICATIONS, 
    TECHNOLOGIES, GCP_TECHNOLOGIES, SOCIAL_LINKS, BADGE_TEXT,
    PORTFOLIO_EMAIL
)

# Shared data utilities
def _create_logo_data(filename, alt_text, name=None, path='images/logos'):
    """Create logo data structure"""
    return {
        'name': name or alt_text,
        'src': url_for('static', filename=f'{path}/{filename}'),
        'alt': alt_text
    }

def get_shared_data():
    """Get common data used across templates"""
    return {
        'education_institutions': {
            key: _create_logo_data(inst['logo'], inst['alt'], inst['name'])
            for key, inst in INSTITUTIONS.items()
        },
        'tech_logos': {
            key: _create_logo_data(tech['logo'], tech['alt'], tech['name'])
            for key, tech in TECHNOLOGIES.items()
        },
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
            'portfolio_email': f'mailto:{PORTFOLIO_EMAIL}'
        },
        'meta_data': {
            'site_title': 'Alan Smith - Portfolio',
            'site_description': 'Professional portfolio showcasing cloud engineering, full-stack development, and technical achievements.',
            'author': 'Alan Smith',
            'keywords': 'cloud engineer, full-stack developer, GCP, Python, Flask, DevOps'
        }
    }

def get_education_cards():
    """Generate education cards"""
    def _create_card(program_data):
        institution = INSTITUTIONS[program_data['institution']]
        return {
            "href": institution['url'],
            "logo_src": url_for('static', filename=f'images/logos/{institution["logo"]}'),
            "logo_alt": institution['alt'],
            "title": program_data['program'],
            "subtitle": f"{institution['name']} • {program_data['years']}",
            "badge_text": BADGE_TEXT['learn_more']
        }
    return [_create_card(program) for program in EDUCATION_PROGRAMS]

def get_certification_cards():
    """Generate certification cards"""
    def _create_card(cert_data):
        return {
            "href": cert_data['url'],
            "logo_src": url_for('static', filename=f'images/logos/{cert_data["logo"]}'),
            "logo_alt": cert_data['alt'],
            "title": cert_data['title'],
            "subtitle": cert_data['subtitle'],
            "badge_text": BADGE_TEXT['view_badge_icon']
        }
    return [_create_card(cert) for cert in CERTIFICATIONS.values()]

def get_techstack_cards():
    """Generate tech stack cards by category"""
    def _create_card(tech_data, logo_path='images/logos'):
        return {
            "href": tech_data['url'],
            "logo_src": url_for('static', filename=f'{logo_path}/{tech_data["logo"]}'),
            "logo_alt": tech_data['alt'],
            "title": tech_data['name'],
            "subtitle": tech_data['description'],
            "badge_text": BADGE_TEXT['learn_more']
        }
    
    frontend = [_create_card(tech) for tech in TECHNOLOGIES.values() if tech['category'] == 'frontend']
    backend = [_create_card(tech) for tech in TECHNOLOGIES.values() if tech['category'] == 'backend']
    infra = [_create_card(tech) for tech in TECHNOLOGIES.values() if tech['category'] == 'infra']
    infra.extend([_create_card(tech, 'images/google-cloud') for tech in GCP_TECHNOLOGIES.values()])
    
    return {"frontend": frontend, "backend": backend, "infra": infra}

def get_connect_cards():
    """Generate social connection cards"""
    def _create_card(social_data):
        badge_map = {"linkedin": "View Profile", "github": "View GitHub"}
        badge_text = next((text for key, text in badge_map.items() if key in social_data['url']), "Send Email")
        return {
            "href": social_data['url'],
            "logo_src": url_for('static', filename=f'images/logos/{social_data["logo"]}'),
            "logo_alt": social_data['alt'],
            "title": social_data['name'],
            "subtitle": social_data['description'],
            "badge_text": badge_text
        }
    return [_create_card(social) for social in SOCIAL_LINKS.values()]

def get_home_card():
    """Generate homepage welcome card"""
    return {
        'image_src': 'images/content/cartoonized-alan-smith.png',
        'image_alt': 'Cartoonized Alan Smith',
        'card_title': 'Welcome to My Portfolio',
        'card_text': ("Hi, I'm Alan Smith, a technology enthusiast, lifelong learner, and passionate problem solver. "
                     "This website showcases my journey and achievements, giving you a glimpse into my professional world and personal growth. "
                     "<i class='fas fa-face-wink' style='color:#f7b731; font-size:1.3em; vertical-align:middle;'></i>")
    }
