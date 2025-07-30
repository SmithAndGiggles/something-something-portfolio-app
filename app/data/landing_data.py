# filepath: something-something-portfolio-app/app/data/landing_data.py

from .constants import LANDING_PAGE, LANDING_CARDS

def get_landing_page_data():
    """Generate landing page data from constants"""
    cards = [
        {
            'icon': config['icon'],
            'title': config['title'],
            'description': config['description'],
            'button_text': config['button_text'],
            'button_class': config['button_class'],
            'url': LANDING_PAGE[config['url_key']]
        }
        for config in LANDING_CARDS.values()
    ]
    
    return {
        'page_config': LANDING_PAGE,
        'cards': cards,
        'professional': {
            'title': LANDING_PAGE['professional_title'],
            'description': LANDING_PAGE['professional_description'],
            'tech_badges': LANDING_PAGE['tech_badges']
        }
    }
