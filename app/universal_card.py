# universal_card.py
"""
Universal card context generator for use with cards.html Jinja template.
"""

def get_card_context(
    href: str,
    logo_src: str,
    logo_alt: str,
    title: str,
    subtitle: str = None,
    badge_text: str = None,
    card_class: str = None
) -> dict:
    """
    Returns a dictionary suitable for rendering a card in the cards.html template.
    """
    return {
        "href": href,
        "logo_src": logo_src,
        "logo_alt": logo_alt,
        "title": title,
        "subtitle": subtitle,
        "badge_text": badge_text,
        "card_class": card_class
    }
x