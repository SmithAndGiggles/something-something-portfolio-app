from flask import url_for, current_app

def inject_nav_links():
    nav_links = [
        {"href": url_for('routes.education'), "icon": "fas fa-graduation-cap", "label": "EDUCATION"},
        {"href": url_for('routes.certifications'), "icon": "fas fa-certificate", "label": "CERTIFICATIONS"},
        {"href": url_for('routes.achievements'), "icon": "fas fa-trophy", "label": "ACHIEVEMENTS"},
        {"href": url_for('routes.techstack'), "icon": "fas fa-laptop-code", "label": "PORTFOLIO TECH STACK"},
        {"href": url_for('routes.irl'), "icon": "fas fa-users", "label": "IRL"},
        {"href": url_for('routes.connect'), "icon": "fas fa-link", "label": "CONNECT"},
    ]
    return dict(nav_links=nav_links, app_name=current_app.config.get("APP_NAME", "me2u Portfolio"))

def inject_footer_links():
    footer_links = [
        {"href": "https://www.linkedin.com/in/alan-r-smith/", "logo": url_for('static', filename='images/logos/logo-linkedin.png'), "label": "LinkedIn"},
        {"href": "https://github.com/SmithAndGiggles", "logo": url_for('static', filename='images/logos/logo-github-dark.png'), "label": "GitHub"},
    ]
    return dict(footer_links=footer_links)

# Register with your Flask app in __init__.py:
# app.context_processor(inject_nav_links)
# app.context_processor(inject_footer_links)