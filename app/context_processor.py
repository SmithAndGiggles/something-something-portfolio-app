from flask import url_for

def inject_nav_links():
    nav_links = [
        {"href": url_for('routes.education'), "icon": "fas fa-graduation-cap", "label": "EDUCATION"},
        {"href": url_for('routes.certifications'), "icon": "fas fa-certificate", "label": "CERTIFICATIONS"},
        {"href": url_for('routes.achievements'), "icon": "fas fa-trophy", "label": "ACHIEVEMENTS"},
        {"href": url_for('routes.techstack'), "icon": "fas fa-laptop-code", "label": "PORTFOLIO TECH STACK"},
        {"href": url_for('routes.irl'), "icon": "fas fa-users", "label": "IRL"},
    ]
    return dict(nav_links=nav_links)

def inject_footer_links():
    footer_links = [
        {"href": "https://www.linkedin.com/in/alan-r-smith/", "logo": url_for('static', filename='images/logos/logo-linkedin.png'), "label": "LinkedIn"},
        {"href": "https://github.com/SmithAndGiggles", "logo": url_for('static', filename='images/logos/logo-github.png'), "label": "GitHub"},
        {"href": "https://www.credly.com/users/alan-smith.333907f0", "logo": url_for('static', filename='images/logos/logo-credly.svg'), "label": "Credly"},
    ]
    return dict(footer_links=footer_links)

# Register with your Flask app in __init__.py:
# app.context_processor(inject_nav_links)
# app.context_processor(inject_footer_links)