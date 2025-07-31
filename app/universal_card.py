"""
Universal Card Context Generator
================================

Provides standardized card data structure for consistent rendering across
the portfolio application. This module implements the data layer for the
universal cards.html Jinja template, ensuring consistent card presentation
throughout all portfolio sections.

Features:
- Type-safe card data structure with optional fields
- Standardized interface for all card-based content
- Template-ready data formatting
- Flexible badge and styling support
- Consistent logo and branding integration

Usage:
Used by data modules (education, certifications, techstack, etc.) to generate
card contexts that render consistently via the cards.html template.

Architecture:
- Single function interface for card generation
- Optional parameters for flexible card types
- Direct compatibility with Jinja template structure
- Type annotations for developer clarity
"""


def get_card_context(
    href: str,
    logo_src: str,
    logo_alt: str,
    title: str,
    subtitle: str | None = None,
    badge_text: str | None = None,
    card_class: str | None = None,
) -> dict:
    """
    Generate template-ready card context dictionary

    Creates standardized card data structure for rendering via cards.html template.
    All portfolio cards (education, certifications, tech stack, etc.) use this
    consistent format for unified presentation.

    Args:
        href (str): Target URL for card click navigation
        logo_src (str): Path to card logo/icon image
        logo_alt (str): Alt text for logo accessibility
        title (str): Primary card title text
        subtitle (str, optional): Secondary descriptive text
        badge_text (str, optional): Badge/label text for status/category
        card_class (str, optional): Additional CSS classes for styling

    Returns:
        dict: Template context with all card display properties

    Template Usage:
        This dictionary structure maps directly to cards.html template variables,
        enabling consistent card rendering across all portfolio sections.

    Example:
        card = get_card_context(
            href="https://example.com",
            logo_src="/static/images/logos/example.png",
            logo_alt="Example Logo",
            title="Example Title",
            subtitle="Example Description",
            badge_text="Featured",
            card_class="highlight-card"
        )
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
