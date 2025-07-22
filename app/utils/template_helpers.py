# filepath: something-something-portfolio-app/app/utils/template_helpers.py

def generate_card_data(href, logo_src, logo_alt, title, subtitle="", badge_text="", card_class="card rounded-4 bg-dark text-white h-100 hover-shadow"):
    """
    DRY helper function to generate consistent card data structures.
    Used across certifications, education, techstack, and connect pages.
    """
    return {
        'href': href,
        'logo_src': logo_src,
        'logo_alt': logo_alt,
        'title': title,
        'subtitle': subtitle,
        'badge_text': badge_text,
        'card_class': card_class
    }

def generate_carousel_slide(src, alt, title, text, sources1=None, sources2=None, highlight=None):
    """
    DRY helper function to generate consistent carousel slide data.
    Used in achievements.html and irl.html carousels.
    """
    slide = {
        'src': src,
        'alt': alt,
        'title': title,
        'text': text
    }
    
    if sources1:
        slide['sources1'] = sources1
    if sources2:
        slide['sources2'] = sources2
    if highlight:
        slide['highlight'] = highlight
        
    return slide

def generate_education_card(institution_key, program, period, href="#"):
    """
    DRY helper for education cards - reduces repetition in education data.
    """
    # This would use shared_data.py for institution logos
    return generate_card_data(
        href=href,
        logo_src=f"/static/images/logos/logo-{institution_key}.svg",
        logo_alt=f"{institution_key} logo",
        title=program,
        subtitle=period
    )

def generate_tech_card(tech_key, href="#"):
    """
    DRY helper for tech stack cards.
    """
    # This would use shared_data.py for tech logos
    return generate_card_data(
        href=href,
        logo_src=f"/static/images/logos/logo-{tech_key}.png",
        logo_alt=tech_key,
        title=tech_key.replace('-', ' ').title()
    )

def generate_source_link(href, text):
    """
    DRY helper for source citations.
    """
    return {'href': href, 'text': text}

def create_media_vars(media_type, src, alt=None, poster=None, style=None):
    """
    DRY helper for media template variables.
    Reduces repetitive {% set %} blocks in templates.
    """
    return {
        'media_type': media_type,
        'media_src': src,
        'media_alt': alt,
        'media_poster': poster,
        'media_style': style
    }
