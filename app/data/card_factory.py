# filepath: something-something-portfolio-app/app/data/card_factory.py

from flask import url_for
from app.utils.template_helpers import generate_card_data, generate_source_link
from .constants import CERTIFICATIONS, INSTITUTIONS, EDUCATION_PROGRAMS, TECHNOLOGIES, SOCIAL_LINKS, BADGE_TEXT

# DRY helper function for creating cards with consistent patterns
def _create_card(href, logo_filename, logo_alt, title, subtitle="", badge_text=""):
    """
    DRY helper for generating card data with consistent structure.
    Handles URL generation and optional parameters automatically.
    """
    return generate_card_data(
        href=href,
        logo_src=url_for('static', filename=f'images/logos/{logo_filename}'),
        logo_alt=logo_alt,
        title=title,
        subtitle=subtitle,
        badge_text=badge_text
    )

def _create_card_from_constants(config, badge_text=BADGE_TEXT['learn_more']):
    """DRY helper for creating cards from constants configuration"""
    return _create_card(
        config['url'],
        config['logo'],
        config['alt'],
        config['name'],
        badge_text=badge_text
    )

def get_certification_cards():
    """
    Centralized certification card data using constants.
    """
    return [
        _create_card(
            cert['url'],
            cert['logo'],
            cert['alt'],
            cert['title'],
            cert['subtitle'],
            BADGE_TEXT['view_badge_icon']
        )
        for cert in CERTIFICATIONS.values()
    ]

def get_education_cards():
    """
    Centralized education card data using constants.
    """
    cards = []
    for program in EDUCATION_PROGRAMS:
        institution = INSTITUTIONS[program['institution']]
        cards.append(_create_card(
            institution['url'],
            institution['logo'],
            institution['alt'],
            program['program'],
            f"{institution['name']} • {program['years']}"
        ))
    return cards

def get_connect_cards():
    """
    Centralized connect/social card data using constants.
    """
    return [
        _create_card(
            social['url'],
            social['logo'],
            social['alt'],
            social['name'],
            social['description']
        )
        for social in SOCIAL_LINKS.values()
    ]

def get_frontend_tech_cards():
    """Frontend technology cards using constants."""
    return [
        _create_card_from_constants(tech)
        for tech in TECHNOLOGIES.values()
        if tech['category'] == 'frontend'
    ]

def get_backend_tech_cards():
    """Backend technology cards using constants."""
    return [
        _create_card_from_constants(tech)
        for tech in TECHNOLOGIES.values()
        if tech['category'] == 'backend'
    ]

def get_infra_tech_cards():
    """Infrastructure/Cloud technology cards using constants."""
    return [
        _create_card_from_constants(tech)
        for tech in TECHNOLOGIES.values()
        if tech['category'] == 'infra'
    ]

def get_common_sources():
    """
    Frequently used source citations using constants.
    """
    from .constants import EXTERNAL_URLS
    
    return {
        'mayo_clinic_picc': generate_source_link(
            EXTERNAL_URLS['mayo_clinic_picc'],
            'About PICC Lines (Mayo Clinic)'
        ),
        'cancer_ca_apl': generate_source_link(
            'https://cancer.ca/en/cancer-information/cancer-types/acute-myeloid-leukemia-aml/treatment/acute-promyelocytic-leukemia',
            'More on APL here'
        ),
        'alberta_health_apl': generate_source_link(
            EXTERNAL_URLS['alberta_health_apl'],
            'Alberta Health Services'
        ),
        'toronto_devops_meetup': generate_source_link(
            EXTERNAL_URLS['toronto_devops_meetup'],
            'Toronto Enterprise DevOps Group on Meetup'
        ),
        'valley_of_fire': generate_source_link(
            EXTERNAL_URLS['valley_of_fire'],
            'Valley of Fire State Park'
        )
    }
