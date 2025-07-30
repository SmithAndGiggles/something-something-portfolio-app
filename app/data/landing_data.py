# filepath: something-something-portfolio-app/app/data/landing_data.py

from .constants import LANDING_PAGE, LANDING_CARDS

def get_landing_page_data():
    """
    Generate landing page data using constants - DRY approach
    
    Returns comprehensive landing page configuration including cards,
    professional info, and tech badges using centralized constants.
    
    Returns:
        dict: Landing page context with cards, config, and professional data
    """
    # Generate cards using constants
    cards = []
    for card_key, card_config in LANDING_CARDS.items():
        cards.append({
            'icon': card_config['icon'],
            'title': card_config['title'],
            'description': card_config['description'],
            'button_text': card_config['button_text'],
            'button_class': card_config['button_class'],
            'url': LANDING_PAGE[card_config['url_key']]
        })
    
    return {
        'page_config': LANDING_PAGE,
        'cards': cards,
        'professional': {
            'title': LANDING_PAGE['professional_title'],
            'description': LANDING_PAGE['professional_description'],
            'tech_badges': LANDING_PAGE['tech_badges']
        }
    }
