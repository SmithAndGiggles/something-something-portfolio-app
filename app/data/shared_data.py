# filepath: something-something-portfolio-app/app/data/shared_data.py

from flask import url_for

# DRY helper for creating consistent logo data structures
def _create_logo_data(filename, alt_text, name=None):
    """DRY helper for generating logo data with consistent structure"""
    return {
        'name': name or alt_text,
        'src': url_for('static', filename=f'images/logos/{filename}'),
        'alt': alt_text
    }

# Centralized logo configurations for reusability
LOGO_CONFIGS = {
    'york_university': ('logo-york-u.png', 'York University logo', 'York University'),
    'george_brown': ('logo-george-brown-college.svg', 'George Brown College logo', 'George Brown College'),
    'humber_college': ('logo-humber-college.svg', 'Humber College logo', 'Humber College'),
    'centennial_college': ('logo-centennial-college.jpg', 'Centennial College logo', 'Centennial College'),
    'python': ('logo-python-logo-notext.png', 'Python'),
    'javascript': ('logo-js.svg', 'JavaScript'),
    'html5': ('logo-html.svg', 'HTML5'),
    'css3': ('logo-css.svg', 'CSS3'),
    'flask': ('logo-horn-flask.png', 'Flask'),
    'docker': ('logo-docker-mark-blue.png', 'Docker'),
    'kubernetes': ('logo-kubernetes-logo-without-workmark.png', 'Kubernetes'),
    'terraform': ('logo-terraform.png', 'Terraform'),
    'gcp': ('logo-gcp-associate-engineer.png', 'Google Cloud Platform')
}

def get_shared_data():
    """
    Centralized data that appears across multiple templates.
    Uses DRY helpers to reduce duplication and make updates easier.
    """
    
    # Generate education institutions using DRY helper
    education_institutions = {
        key: _create_logo_data(*config) 
        for key, config in LOGO_CONFIGS.items() 
        if key in ['york_university', 'george_brown', 'humber_college', 'centennial_college']
    }
    
    # Generate tech logos using DRY helper  
    tech_logos = {
        key: _create_logo_data(*config[:2])  # Only filename and alt for tech logos
        for key, config in LOGO_CONFIGS.items()
        if key in ['python', 'javascript', 'html5', 'css3', 'flask', 'docker', 'kubernetes', 'terraform', 'gcp']
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
