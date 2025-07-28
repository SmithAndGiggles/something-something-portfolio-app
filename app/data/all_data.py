"""
Consolidated data module for maximum DRY.
All card data, slides, and content in one place.
"""

from flask import url_for

def get_education_cards():
    """Education cards with DRY logo helper."""
    def edu_card(href, logo_name, logo_alt, title, subtitle):
        return {
            "href": href,
            "logo_src": url_for('static', filename=f'images/logos/{logo_name}'),
            "logo_alt": logo_alt,
            "title": title,
            "subtitle": subtitle,
            "badge_text": "Learn More"
        }
    
    return [
        edu_card("https://www.yorku.ca/", "logo-york-u.png", "York University logo", 
                 "Kinesiology, B.A. Specialized Honours", "York University • 2005 - 2010"),
        edu_card("https://www.georgebrown.ca/", "logo-george-brown-college.svg", "George Brown College logo", 
                 "Sport Marketing and Event Management, Certificate", "George Brown College • 2010 - 2011"),
        edu_card("https://www.georgebrown.ca/", "logo-george-brown-college.svg", "George Brown College logo", 
                 "Introduction to Web Design and Development, Course", "George Brown College • 2012"),
        edu_card("https://www.georgebrown.ca/", "logo-george-brown-college.svg", "George Brown College logo", 
                 "Web Page I – XHTML, Course", "George Brown College • 2013"),
        edu_card("https://www.georgebrown.ca/", "logo-george-brown-college.svg", "George Brown College logo", 
                 "Web Page II – JavaScript/jQuery, Course", "George Brown College • 2013"),
        edu_card("https://www.centennialcollege.ca/", "logo-centennial-college.jpg", "Centennial College logo", 
                 "Introduction to Unix/Linux, Course", "Centennial College • 2015"),
        edu_card("https://humber.ca/", "logo-humber-college.svg", "Humber College logo", 
                 "Red Hat Enterprise Linux System Admin, Course", "Humber College • 2015"),
        edu_card("https://www.georgebrown.ca/", "logo-george-brown-college.svg", "George Brown College logo", 
                 "Foundations of PHP, Course", "George Brown College • 2017"),
        edu_card("https://www.yorku.ca/", "logo-york-u.png", "York University logo", 
                 "Full-Stack Web Development, Certificate", "York University • 2018 - 2019")
    ]

def get_certification_cards():
    """Certification cards with DRY helper."""
    def cert_card(href, logo_name, logo_alt, title, subtitle):
        return {
            "href": href,
            "logo_src": url_for('static', filename=f'images/logos/{logo_name}'),
            "logo_alt": logo_alt,
            "title": title,
            "subtitle": subtitle,
            "badge_text": "View Badge <i class='fas fa-external-link-alt'></i>"
        }
    
    return [
        cert_card("https://www.credly.com/badges/acc75311-8a96-48e5-be8f-c928c9d52ca3", 
                 "logo-gcp-associate-engineer.png", "Google Cloud Associate Cloud Engineer",
                 "Google Cloud", "Associate Cloud Engineer"),
        cert_card("https://www.credly.com/badges/85110e1e-ea27-4687-9080-f83eed5694a0", 
                 "logo-gcp-professional-architect.png", "Google Cloud Professional Cloud Architect",
                 "Google Cloud", "Professional Cloud Architect"),
        cert_card("https://www.credly.com/badges/9543b3ca-8ec4-4ca6-aa7b-b68853078cd9/public_url", 
                 "logo-gcp-devops-engineer-certification.png", "Google Cloud DevOps Engineer",
                 "Google Cloud", "Professional Cloud DevOps Engineer"),
        cert_card("https://www.credly.com/badges/5f4be6a1-71e2-48dc-8b6e-7fbcf26163f9", 
                 "logo-aws-certified-cloud-practitioner.png", "AWS Cloud Practitioner",
                 "AWS", "Certified Cloud Practitioner"),
        cert_card("https://www.credly.com/badges/cdd46167-59b6-46be-9abd-29eebf7db00e", 
                 "logo-terraform.png", "HashiCorp Terraform Associate",
                 "HashiCorp", "Terraform Associate")
    ]

def get_techstack_cards():
    """All tech stack cards organized by category."""
    def tech_card(href, logo_name, logo_alt, title, subtitle):
        return {
            "href": href,
            "logo_src": url_for('static', filename=f'images/logos/{logo_name}'),
            "logo_alt": logo_alt,
            "title": title,
            "subtitle": subtitle,
            "badge_text": "Learn More"
        }
    
    # Helper for Google Cloud images (different path)
    def gcp_card(href, logo_name, logo_alt, title, subtitle):
        return {
            "href": href,
            "logo_src": url_for('static', filename=f'images/google-cloud/{logo_name}'),
            "logo_alt": logo_alt,
            "title": title,
            "subtitle": subtitle,
            "badge_text": "Learn More"
        }
    
    frontend = [
        tech_card("https://developer.mozilla.org/en-US/docs/Web/HTML", "logo-html.svg", "HTML5", 
                 "HTML5", "Markup Language"),
        tech_card("https://developer.mozilla.org/en-US/docs/Web/CSS", "logo-css.svg", "CSS3", 
                 "CSS3", "Stylesheet Language"),
        tech_card("https://developer.mozilla.org/en-US/docs/Web/JavaScript", "logo-js.svg", "JavaScript", 
                 "JavaScript", "Programming Language"),
        tech_card("https://getbootstrap.com", "logo-bootstrap.png", "Bootstrap Logo", 
                 "Bootstrap", "Responsive, mobile-first front-end web development framework."),
        tech_card("https://tailwindcss.com/", "logo-tailwindcss.png", "Tailwind CSS Logo", 
                 "Tailwind CSS", "Utility-first CSS framework for rapid UI development.")
    ]
    
    backend = [
        tech_card("https://www.python.org/", "logo-python-logo-notext.png", "Python", 
                 "Python", "Programming Language"),
        tech_card("https://flask.palletsprojects.com/", "logo-horn-flask.png", "Flask", 
                 "Flask", "Web Framework"),
        tech_card("https://jinja.palletsprojects.com/", "logo-jinja-icon.svg", "Jinja2", 
                 "Jinja2", "Template Engine"),
        tech_card("https://gunicorn.org/", "logo-gunicorn.svg", "Gunicorn", 
                 "Gunicorn", "WSGI Server"),
        tech_card("https://toml.io/en/", "logo-toml.png", "TOML Logo", 
                 "TOML", "Tom's Obvious, Minimal Language for config files.")
    ]
    
    infra = [
        tech_card("https://www.docker.com/", "logo-docker-mark-blue.png", "Docker", 
                 "Docker", "Containerization"),
        gcp_card("https://cloud.google.com/run", "cloud-run.png", "Cloud Run", 
                "Google Cloud Run", "Serverless Platform"),
        tech_card("https://www.terraform.io/", "logo-terraform.png", "Terraform", 
                 "Terraform", "IaC Tool"),
        tech_card("https://github.com/features/actions", "logo-github-actions.png", "GitHub Actions", 
                 "GitHub Actions", "CI/CD"),
        tech_card("https://github.com", "logo-github.png", "GitHub", 
                 "GitHub", "Source Code Hosting & Collaboration"),
        tech_card("https://terragrunt.gruntwork.io/", "logo-terragrunt.png", "Terragrunt", 
                 "Terragrunt", "IaC Wrapper"),
        tech_card("https://yamlscript.org", "logo-yamlscript.svg", "Yamlscript", 
                 "Yamlscript", "YAML-based Scripting Language")
    ]
    
    return {"frontend": frontend, "backend": backend, "infra": infra}

def get_connect_cards():
    """Connect/social cards."""
    def connect_card(href, logo_name, logo_alt, title, subtitle):
        return {
            "href": href,
            "logo_src": url_for('static', filename=f'images/logos/{logo_name}'),
            "logo_alt": logo_alt,
            "title": title,
            "subtitle": subtitle,
            "badge_text": "View Profile" if "linkedin" in href else "View GitHub" if "github" in href else "Send Email"
        }
    
    return [
        connect_card("https://www.linkedin.com/in/alan-r-smith/", "logo-linkedin-blue.png", "LinkedIn Logo", 
                    "LinkedIn", "Connect with me on LinkedIn"),
        connect_card("https://github.com/SmithAndGiggles", "logo-github.png", "GitHub Logo", 
                    "GitHub", "See my projects on GitHub"),
        connect_card("mailto:42-daisy-focuses@icloud.com", "logo-gmail.png", "Gmail Logo", 
                    "Email", "Email me!")
    ]

def get_home_card():
    """Home page card data."""
    return {
        'image_src': 'images/content/cartoonized-alan-smith.png',
        'image_alt': 'Cartoonized Alan Smith',
        'card_title': 'Welcome to My Portfolio',
        'card_text': ("Hi, I'm Alan Smith—a technology enthusiast, lifelong learner, and passionate problem solver. "
                     "This website is a showcase of my journey, projects, and achievements, designed to give you a glimpse into my professional world and personal growth. "
                     "Explore my work, discover my story, and check out the certifications page—I'm hoping to have more than just three badges there soon!"
                     "<i class='fas fa-face-wink' style='color:#f7b731; font-size:1.3em; vertical-align:middle;'></i>")
    }
