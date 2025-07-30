# filepath: something-something-portfolio-app/app/data/landing_data.py

from .constants import LANDING_PAGE_CONFIG, LANDING_CARDS

def get_landing_page_data():
    """Generate landing page data from constants"""
    cards = [
        {
            'icon': config['icon'],
            'title': config['title'],
            'description': config['description'],
            'button_text': config['button_text'],
            'button_class': config['button_class'],
            'url': LANDING_PAGE_CONFIG[config['url_key']]
        }
        for config in LANDING_CARDS.values()
    ]
    
    return {
        'page_config': LANDING_PAGE_CONFIG,
        'cards': cards,
        'professional': {
            'title': LANDING_PAGE_CONFIG['professional_title'],
            'description': LANDING_PAGE_CONFIG['professional_description'],
            'tech_badges': LANDING_PAGE_CONFIG['tech_badges']
        }
    }
