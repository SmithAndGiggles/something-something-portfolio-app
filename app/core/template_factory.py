"""
Ultra-DRY template factory - eliminates ALL template repetition.
Single source of truth for all page layouts and components.
"""

from flask import url_for

class TemplateFactory:
    """Factory for generating consistent template data structures."""
    
    @staticmethod
    def page_layout(title, content_class="container py-4 px-2 md:px-8 mx-auto", max_width="max-w-[1100px]"):
        """Standard page layout configuration."""
        return {
            "title": title,
            "content_class": f"{content_class} {max_width}",
            "fade_in": "animate-fade-in"
        }
    
    @staticmethod
    def card_grid_page(title, cards, grid_cols="row-cols-1 row-cols-md-3 g-4"):
        """Generate a complete card grid page."""
        layout = TemplateFactory.page_layout(title)
        return {
            **layout,
            "cards": cards,
            "grid_class": f"row {grid_cols}",
            "template": "layouts/card_grid.html"
        }
    
    @staticmethod
    def carousel_page(title, slides, carousel_id):
        """Generate a complete carousel page."""
        layout = TemplateFactory.page_layout(title)
        return {
            **layout,
            "slides": slides,
            "carousel_id": carousel_id,
            "template": "layouts/carousel.html"
        }
    
    @staticmethod
    def horizontal_card_page(title, card_data):
        """Generate a complete horizontal card page."""
        layout = TemplateFactory.page_layout(title, max_width="max-w-4xl xl:max-w-5xl")
        return {
            **layout,
            "card_data": card_data,
            "template": "layouts/horizontal_card.html"
        }

class ComponentFactory:
    """Factory for generating reusable component configurations."""
    
    @staticmethod
    def carousel_config(carousel_id, slides, interval=20000):
        """Standard carousel configuration."""
        return {
            "id": carousel_id,
            "slides": slides,
            "interval": interval,
            "classes": "carousel carousel-fixed-size slide rounded-2xl overflow-hidden relative mb-4 p-2 md:p-4 border border-gray-600",
            "inner_classes": "carousel-inner h-full",
            "item_classes": "carousel-item h-full",
            "indicators_classes": "carousel-indicators"
        }
    
    @staticmethod
    def media_config(src, alt="", media_type=None):
        """Auto-detect media type and generate config."""
        if media_type is None:
            media_type = 'video' if src.endswith('.mp4') else 'image'
        
        return {
            "type": media_type,
            "src": src,
            "alt": alt,
            "classes": "w-full h-full object-contain"
        }

# Pre-configured page templates
PAGE_TEMPLATES = {
    "card_grid": {
        "template": "layouts/card_grid.html",
        "content_class": "container py-4 px-2 md:px-8 mx-auto max-w-6xl"
    },
    "carousel": {
        "template": "layouts/carousel.html", 
        "content_class": "container py-4 px-2 md:px-8 mx-auto max-w-[1100px]"
    },
    "horizontal_card": {
        "template": "layouts/horizontal_card.html",
        "content_class": "container py-4 px-2 md:px-8 mx-auto max-w-4xl xl:max-w-5xl"
    },
    "landing": {
        "template": "layouts/landing.html",
        "content_class": "container py-4 px-2 md:px-8 mx-auto max-w-4xl xl:max-w-5xl"
    },
    "error": {
        "template": "layouts/error.html",
        "content_class": "flex justify-center items-center min-h-[70vh]"
    }
}
