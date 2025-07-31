# filepath: something-something-portfolio-app/app/data/card_factory.py

from flask import url_for
from app.utils.template_helpers import generate_card_data, generate_source_link
from .constants import (
    CERTIFICATIONS,
    INSTITUTIONS,
    EDUCATION_PROGRAMS,
    TECHNOLOGIES,
    SOCIAL_LINKS,
    BADGE_TEXT,
)


def _create_card(href, logo_filename, logo_alt, title, subtitle="", badge_text=""):
    """Create card data with consistent structure"""
    return generate_card_data(
        href=href,
        logo_src=url_for("static", filename=f"images/logos/{logo_filename}"),
        logo_alt=logo_alt,
        title=title,
        subtitle=subtitle,
        badge_text=badge_text,
    )


def _create_card_from_constants(config, badge_text=BADGE_TEXT["learn_more"]):
    """Create cards from constants"""
    return _create_card(
        config["url"],
        config["logo"],
        config["alt"],
        config["name"],
        badge_text=badge_text,
    )


def get_certification_cards():
    """Get certification cards from constants"""
    return [
        _create_card(
            cert["url"],
            cert["logo"],
            cert["alt"],
            cert["title"],
            cert["subtitle"],
            BADGE_TEXT["view_badge_icon"],
        )
        for cert in CERTIFICATIONS.values()
    ]


def get_education_cards():
    """Get education cards from constants"""
    cards = []
    for program in EDUCATION_PROGRAMS:
        institution = INSTITUTIONS[program["institution"]]
        cards.append(
            _create_card(
                institution["url"],
                institution["logo"],
                institution["alt"],
                program["program"],
                f"{institution['name']} • {program['years']}",
            )
        )
    return cards


def get_connect_cards():
    """Get social/contact cards from constants"""
    return [
        _create_card(
            social["url"],
            social["logo"],
            social["alt"],
            social["name"],
            social["description"],
        )
        for social in SOCIAL_LINKS.values()
    ]


def get_frontend_tech_cards():
    """Get frontend tech cards from constants"""
    return [
        _create_card_from_constants(tech)
        for tech in TECHNOLOGIES.values()
        if tech["category"] == "frontend"
    ]


def get_backend_tech_cards():
    """Get backend tech cards from constants"""
    return [
        _create_card_from_constants(tech)
        for tech in TECHNOLOGIES.values()
        if tech["category"] == "backend"
    ]


def get_infra_tech_cards():
    """Get infrastructure tech cards from constants"""
    return [
        _create_card_from_constants(tech)
        for tech in TECHNOLOGIES.values()
        if tech["category"] == "infra"
    ]


def get_common_sources():
    """Get common source citations from constants"""
    from .constants import EXTERNAL_URLS

    sources = {
        ("mayo_clinic_picc", "About PICC Lines (Mayo Clinic)"),
        ("cancer_society", "More on APL here"),
        ("alberta_health_apl", "Alberta Health Services"),
        ("toronto_devops_meetup", "Toronto Enterprise DevOps Group on Meetup"),
        ("valley_of_fire", "Valley of Fire State Park"),
    }

    return {
        key: generate_source_link(EXTERNAL_URLS.get(key, "#"), text)
        for key, text in sources
    }
