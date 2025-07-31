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
    href,
    logo_src,
    logo_alt,
    title,
    subtitle="",
    badge_text="",
    card_class="card rounded-4 bg-dark text-white h-100 hover-shadow",
):
    """
    Generate standardized card data structure for template rendering

    Creates consistent card data dictionary used across all portfolio
    sections (certifications, education, techstack, connect pages).
    Ensures uniform card presentation and behavior.

    Args:
        href (str): Target URL for card click navigation
        logo_src (str): Path to card logo/icon image
        logo_alt (str): Alt text for logo accessibility
        title (str): Primary card title text
        subtitle (str, optional): Secondary descriptive text
        badge_text (str, optional): Badge/label text for actions
        card_class (str, optional): CSS classes for card styling

    Returns:
        dict: Template-ready card data structure

    Template Compatibility:
        Generated structure maps directly to cards.html template variables
        for consistent rendering across all portfolio card sections.
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
    src, alt, title, text, sources1=None, sources2=None, highlight=None
):
    """
    Generate standardized carousel slide data structure with automatic video detection

    Creates consistent slide data for achievements.html and irl.html carousels.
    Automatically detects video files from .mp4, .webm, .mov, .avi extensions
    and adds media_type information for templates to handle videos properly.

    Args:
        src (str): Image or video source path for slide content
        alt (str): Alt text for media accessibility
        title (str): Slide headline/title
        text (str): Main slide content/description
        sources1 (list, optional): Primary source citation links
        sources2 (list, optional): Secondary source citation links
        highlight (str, optional): Key highlight or call-out text

    Returns:
        dict: Template-ready carousel slide data structure with media_type

    Template Usage:
        Structure optimized for carousel.html template rendering
        with automatic video support and flexible optional metadata.
    """
    # Auto-detect video files from extensions
    video_extensions = (".mp4", ".webm", ".mov", ".avi")
    is_video = any(src.lower().endswith(ext) for ext in video_extensions)
    media_type = "video" if is_video else "image"

    slide = {
        "src": src,
        "alt": alt,
        "title": title,
        "text": text,
        "media_type": media_type,  # Auto-detected for template use
    }

    if sources1:
        slide["sources1"] = sources1
    if sources2:
        slide["sources2"] = sources2
    if highlight:
        slide["highlight"] = highlight

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
