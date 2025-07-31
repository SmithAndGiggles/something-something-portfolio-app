"""
Template Factory Module - Ultra-DRY Template Generation
=======================================================

Provides centralized template data structure generation for maximum DRY (Don't Repeat Yourself)
principles. This factory eliminates template repetition by providing standardized layouts,
components, and configuration patterns used across the entire portfolio application.

Features:
- Centralized page layout configuration management
- Reusable component factory patterns
- Pre-configured template type definitions
- Consistent styling and behavior patterns
- Automatic media type detection and configuration

Architecture:
- Factory pattern for template data structure generation
- Static methods for stateless template configuration
- Component-based design for reusable UI elements
- Template type abstraction for consistent page layouts

Design Philosophy:
Single source of truth for all template layouts and components.
Eliminates code duplication across routes and templates while
ensuring consistent user experience and maintainable codebase.

Usage:
Used by routes and data modules to generate consistent template
contexts without duplicating layout and styling configuration.
"""

from ..data.constants import UI_CONFIG

# CSS Constants - Centralized styling patterns
# ===========================================
BASE_CONTAINER = "container py-4 px-2 md:px-8 mx-auto"
WIDTH_SMALL = "max-w-[1100px]"
WIDTH_MEDIUM = "max-w-6xl"
WIDTH_LARGE = "max-w-4xl xl:max-w-5xl"
FADE_ANIMATION = "animate-fade-in"
PAGE_TITLE_CLASSES = "text-3xl font-bold mb-8 animate-fade-in"


class TemplateFactory:
    """
    Factory class for generating consistent template data structures

    Provides standardized page layout configurations and template data
    generation for consistent presentation across all portfolio pages.
    Eliminates template configuration duplication and ensures design consistency.
    """

    @staticmethod
    def page_layout(title, content_class=BASE_CONTAINER, max_width=WIDTH_SMALL):
        """
        Generate standard page layout configuration

        Creates base layout structure used across all portfolio pages
        with consistent spacing, responsiveness, and animation patterns.

        Args:
            title (str): Page title for browser and SEO
            content_class (str, optional): Base CSS classes for content container
            max_width (str, optional): Responsive max-width constraint

        Returns:
            dict: Base layout configuration for template rendering
        """
        return {
            "title": title,
            "content_class": f"{content_class} {max_width}",
            "fade_in": FADE_ANIMATION,
        }

    @staticmethod
    def card_grid_page(title, cards, grid_cols="row-cols-1 row-cols-md-3 g-4"):
        """
        Generate complete card grid page configuration

        Creates full page layout for card-based content (education, certifications,
        techstack, connect pages) with responsive grid layout and consistent styling.

        Args:
            title (str): Page title and heading
            cards (list): Card data structures for grid rendering
            grid_cols (str, optional): Bootstrap grid column configuration

        Returns:
            dict: Complete card grid page configuration for template rendering
        """
        layout = TemplateFactory.page_layout(title)
        return {
            **layout,
            "cards": cards,
            "grid_class": f"row {grid_cols}",
            "template": "layouts/card_grid.html",
        }

    @staticmethod
    def carousel_page(title, slides, carousel_id):
        """
        Generate complete carousel page configuration

        Creates full page layout for carousel-based content (achievements, irl pages)
        with interactive slide navigation and multimedia content support.

        Args:
            title (str): Page title and heading
            slides (list): Slide data structures for carousel rendering
            carousel_id (str): Unique carousel identifier for JavaScript functionality

        Returns:
            dict: Complete carousel page configuration for template rendering
        """
        layout = TemplateFactory.page_layout(title)
        return {
            **layout,
            "slides": slides,
            "carousel_id": carousel_id,
            "template": "layouts/carousel.html",
        }

    @staticmethod
    def horizontal_card_page(title, card_data):
        """
        Generate complete horizontal card page configuration

        Creates full page layout for large horizontal card content (home page)
        with extended width constraints for featured content presentation.

        Args:
            title (str): Page title and heading
            card_data (dict): Card data structure for horizontal rendering

        Returns:
            dict: Complete horizontal card page configuration for template rendering
        """
        layout = TemplateFactory.page_layout(title, max_width=WIDTH_LARGE)
        return {
            **layout,
            "card_data": card_data,
            "template": "layouts/horizontal_card.html",
        }


class ComponentFactory:
    """
    Factory class for generating reusable component configurations

    Provides standardized UI component configurations for consistent
    behavior and styling across portfolio application components.
    """

    @staticmethod
    def carousel_config(
        carousel_id, slides, interval=UI_CONFIG["carousel"]["interval"]
    ):
        """
        Generate standard carousel component configuration

        Creates consistent carousel setup with standardized timing,
        styling, and behavior patterns for multimedia content presentation.

        Args:
            carousel_id (str): Unique identifier for carousel instance
            slides (list): Slide data structures for carousel content
            interval (int, optional): Auto-advance interval in milliseconds

        Returns:
            dict: Complete carousel configuration for component rendering
        """
        return {
            "id": carousel_id,
            "slides": slides,
            "interval": interval,
            "classes": "carousel carousel-fixed-size slide rounded-4 overflow-hidden position-relative mb-4 p-2 p-md-4 border border-secondary",
            "inner_classes": "carousel-inner h-full",
            "item_classes": "carousel-item h-full",
            "indicators_classes": "carousel-indicators",
        }

    @staticmethod
    def media_config(src, alt="", media_type=None):
        """
        Generate media component configuration with auto-detection

        Creates media configuration with automatic type detection based on
        file extension. Supports both image and video content with consistent
        responsive styling and accessibility features.

        Args:
            src (str): Media source path (image or video)
            alt (str, optional): Alt text for accessibility
            media_type (str, optional): Override media type detection

        Returns:
            dict: Media configuration for component rendering

        Features:
            - Automatic media type detection from file extension
            - Consistent responsive styling across media types
            - Accessibility support with alt text
        """
        if media_type is None:
            media_type = "video" if src.endswith(".mp4") else "image"

        return {
            "type": media_type,
            "src": src,
            "alt": alt,
            "classes": "w-full h-full object-contain",
        }


# Pre-configured Page Template Definitions
# ========================================
# Centralized template type configurations for consistent page layouts
# across the portfolio application. Each template type defines the
# template path and associated styling/layout configuration.

PAGE_TEMPLATES = {
    "card_grid": {
        "template": "layouts/card_grid.html",
        "content_class": f"{BASE_CONTAINER} {WIDTH_MEDIUM}",
        "description": "Grid layout for card-based content (education, certifications, techstack)",
    },
    "carousel": {
        "template": "layouts/carousel.html",
        "content_class": f"{BASE_CONTAINER} {WIDTH_SMALL}",
        "description": "Interactive carousel for multimedia content (achievements, irl)",
    },
    "horizontal_card": {
        "template": "layouts/horizontal_card.html",
        "content_class": f"{BASE_CONTAINER} {WIDTH_LARGE}",
        "description": "Large horizontal card layout for featured content (home page)",
    },
    "landing": {
        "template": "layouts/landing.html",
        "content_class": f"{BASE_CONTAINER} {WIDTH_LARGE}",
        "description": "Landing page layout for custom domain entry points",
    },
    "error": {
        "template": "layouts/error.html",
        "content_class": "flex justify-center items-center min-h-[70vh]",
        "description": "Error page layout for 400/404/500 error handling",
    },
}
