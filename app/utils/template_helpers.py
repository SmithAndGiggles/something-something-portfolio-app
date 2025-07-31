"""
Template Helper Utilities Module
================================

Provides DRY (Don't Repeat Yourself) utility functions for consistent data
structure generation across portfolio templates. This module centralizes
common template data patterns to reduce code duplication and ensure
consistent presentation formatting.

Features:
- Standardized card data structure generation
- Carousel slide data formatting utilities
- Media content helper functions
- Source citation and link generation utilities
- Template variable creation helpers

Architecture:
- Pure utility functions with no side effects
- Consistent parameter patterns across helper functions
- Template-ready data structure generation
- Flexible optional parameter support

Design Philosophy:
Eliminates repetitive data structure creation code throughout
the application by providing reusable utility functions that
generate consistent, template-ready data structures.

Usage:
Imported by data modules and potentially used in templates
for consistent data formatting and structure generation.
"""


def generate_card_data(
    href: str,
    logo_src: str,
    logo_alt: str,
    title: str,
    subtitle: str = "",
    badge_text: str = "",
    card_class: str = "card rounded-4 bg-dark text-white h-100 hover-shadow",
) -> dict:
    """
    Generate standardized card data structure for template rendering

    Creates consistent card data dictionary used across all portfolio
    sections (certifications, education, techstack, connect pages).

    Args:
        href: Target URL for card click navigation
        logo_src: Path to card logo/icon image
        logo_alt: Alt text for logo accessibility
        title: Primary card title text
        subtitle: Secondary descriptive text (optional)
        badge_text: Badge/label text for actions (optional)
        card_class: CSS classes for card styling (optional)

    Returns:
        Template-ready card data structure
    """
    return {
        "href": href,
        "logo_src": logo_src,
        "logo_alt": logo_alt,
        "title": title,
        "subtitle": subtitle,
        "badge_text": badge_text,
        "card_class": card_class,
    }


def generate_carousel_slide(
    src: str, alt: str, title: str, text: str, 
    sources1: list | None = None, sources2: list | None = None, highlight: str | None = None
) -> dict:
    """
    Generate standardized carousel slide data structure with automatic video detection

    Creates consistent slide data for achievements.html and irl.html carousels.
    Automatically detects video files and adds media_type information.

    Args:
        src: Image or video source path for slide content
        alt: Alt text for media accessibility
        title: Slide headline/title
        text: Main slide content/description
        sources1: Primary source citation links (optional)
        sources2: Secondary source citation links (optional)
        highlight: Key highlight or call-out text (optional)

    Returns:
        Template-ready carousel slide data structure with media_type
    """
    # Modern approach: use endswith with tuple directly
    video_extensions = (".mp4", ".webm", ".mov", ".avi")
    media_type = "video" if src.lower().endswith(video_extensions) else "image"

    # Use dictionary comprehension for optional fields
    slide = {
        "src": src,
        "alt": alt,
        "title": title,
        "text": text,
        "media_type": media_type,
        **{k: v for k, v in {
            "sources1": sources1,
            "sources2": sources2,
            "highlight": highlight
        }.items() if v is not None}
    }

    return slide


def generate_education_card(institution_key, program, period, href="#"):
    """
    Generate education-specific card with institution branding

    DRY helper for education cards that automatically handles
    institution logo paths and branding consistency.

    Args:
        institution_key (str): Institution identifier for logo lookup
        program (str): Program or course name
        period (str): Time period or duration
        href (str, optional): External link to institution

    Returns:
        dict: Education card data structure

    Note: Uses standardized logo naming convention for institution assets
    """
    return generate_card_data(
        href=href,
        logo_src=f"/static/images/logos/logo-{institution_key}.svg",
        logo_alt=f"{institution_key} logo",
        title=program,
        subtitle=period,
    )


def generate_tech_card(tech_key, href="#"):
    """
    Generate technology stack card with standardized formatting

    DRY helper for tech stack cards with automatic logo path
    generation and title formatting from technology identifiers.

    Args:
        tech_key (str): Technology identifier for logo and title
        href (str, optional): External link to technology documentation

    Returns:
        dict: Technology card data structure

    Note: Automatically formats tech names and resolves logo paths
    """
    return generate_card_data(
        href=href,
        logo_src=f"/static/images/logos/logo-{tech_key}.png",
        logo_alt=tech_key,
        title=tech_key.replace("-", " ").title(),
    )


def generate_source_link(href, text):
    """
    Generate standardized source citation link structure

    Creates consistent source link format for carousel slides
    and content that requires external source attribution.

    Args:
        href (str): URL to source material
        text (str): Display text for source link

    Returns:
        dict: Source link data structure for template rendering
    """
    return {"href": href, "text": text}


def create_media_vars(media_type, src, alt=None, poster=None, style=None):
    """
    Generate media template variables for dynamic content

    Creates standardized media variable structure for templates
    that need to handle both image and video content dynamically.
    Reduces repetitive template variable creation.

    Args:
        media_type (str): Type of media ('image' or 'video')
        src (str): Media source path
        alt (str, optional): Alt text for accessibility
        poster (str, optional): Video poster image path
        style (str, optional): CSS styling for media element

    Returns:
        dict: Media template variables ready for Jinja rendering

    Template Usage:
        Eliminates repetitive {% set %} blocks in templates by
        providing pre-structured media variable dictionaries.
    """
    return {
        "media_type": media_type,
        "media_src": src,
        "media_alt": alt,
        "media_poster": poster,
        "media_style": style,
    }
