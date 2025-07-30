# filepath: something-something-portfolio-app/app/data/card_factory.py

from flask import url_for
from app.utils.template_helpers import generate_card_data, generate_source_link

# DRY helper function for creating cards with consistent patterns
def _create_card(href, logo_filename, logo_alt, title, subtitle="", badge_text=""):
    """
    DRY helper for generating card data with consistent structure.
    Handles URL generation and optional parameters automatically.
    """
    return generate_card_data(
        href=href,
        logo_src=url_for('static', filename=f'images/logos/{logo_filename}'),
        logo_alt=logo_alt,
        title=title,
        subtitle=subtitle,
        badge_text=badge_text
    )

def _create_gcp_card(href, logo_filename, logo_alt, title, subtitle="Google Cloud Platform"):
    """DRY helper specifically for GCP cards with consistent subtitle"""
    return _create_card(href, logo_filename, logo_alt, title, subtitle, "View Badge")

def _create_tech_card(href, logo_filename, tech_name):
    """DRY helper for technology cards with minimal parameters"""
    return _create_card(href, logo_filename, tech_name, tech_name)

def get_certification_cards():
    """
    Centralized certification card data using DRY helpers.
    """
    return [
        _create_gcp_card(
            "https://www.credly.com/badges/acc75311-8a96-48e5-be8f-c928c9d52ca3",
            "logo-gcp-associate-engineer.png",
            "Google Cloud Associate Cloud Engineer",
            "Google Cloud Associate Cloud Engineer"
        ),
        _create_gcp_card(
            "https://www.credly.com/badges/85110e1e-ea27-4687-9080-f83eed5694a0",
            "logo-gcp-professional-architect.png", 
            "Google Cloud Professional Cloud Architect",
            "Professional Cloud Architect"
        ),
        _create_gcp_card(
            "https://www.credly.com/badges/9543b3ca-8ec4-4ca6-aa7b-b68853078cd9",
            "logo-gcp-devops-engineer-certification.png",
            "Google Cloud DevOps Engineer", 
            "Professional Cloud DevOps Engineer"
        ),
        _create_card(
            "https://www.credly.com/badges/5f4be6a1-71e2-48dc-8b6e-7fbcf26163f9",
            "logo-aws-certified-cloud-practitioner.png",
            "AWS Cloud Practitioner",
            "AWS Certified Cloud Practitioner",
            "Amazon Web Services",
            "View Badge"
        ),
        _create_card(
            "https://www.credly.com/badges/cdd46167-59b6-46be-9abd-29eebf7db00e",
            "logo-terraform.png",
            "HashiCorp Terraform Associate", 
            "Terraform Associate",
            "HashiCorp",
            "View Badge"
        )
    ]

def get_education_cards():
    """
    Centralized education card data using DRY helpers.
    """
    return [
        _create_card("#", "logo-york-u.png", "York University logo", 
                    "Kinesiology, B.A. Specialized Honours", "York University • 2005 - 2010"),
        _create_card("#", "logo-george-brown-college.svg", "George Brown College logo",
                    "Sport Marketing and Event Management", "George Brown College • 2010 - 2011"),
        _create_card("#", "logo-york-u.png", "York University logo",
                    "Full-Stack Web Development Certificate", "York University • 2018 - 2019"),
        _create_card("https://www.senecapolytechnic.ca/home.html", "logo-seneca.png", 
                    "Seneca Polytechnic logo", "Introduction to Databases", "Seneca Polytechnic • 2017")
    ]

def get_connect_cards():
    """
    Centralized connect/social card data using DRY helpers.
    """
    return [
        _create_card("https://www.linkedin.com/in/alan-smith-ca/", "logo-linkedin.png", 
                    "LinkedIn", "LinkedIn", "Professional Network"),
        _create_card("https://github.com/SmithAndGiggles", "logo-github.png",
                    "GitHub", "GitHub", "Code Repository"), 
        _create_card("mailto:alan@me2u.space", "logo-email.png",
                    "Email", "Email", "Direct Contact")
    ]

def get_frontend_tech_cards():
    """Frontend technology cards using DRY helpers."""
    return [
        _create_tech_card("https://developer.mozilla.org/en-US/docs/Web/HTML", "logo-html.svg", "HTML5"),
        _create_tech_card("https://developer.mozilla.org/en-US/docs/Web/CSS", "logo-css.svg", "CSS3"),
        _create_tech_card("https://developer.mozilla.org/en-US/docs/Web/JavaScript", "logo-js.svg", "JavaScript")
    ]

def get_backend_tech_cards():
    """Backend technology cards using DRY helpers."""
    return [
        _create_tech_card("https://www.python.org/", "logo-python-logo-notext.png", "Python"),
        _create_tech_card("https://flask.palletsprojects.com/", "logo-horn-flask.png", "Flask"),
        _create_tech_card("https://jinja.palletsprojects.com/", "logo-jinja-icon.svg", "Jinja2")
    ]

def get_infra_tech_cards():
    """Infrastructure/Cloud technology cards using DRY helpers.""" 
    return [
        _create_tech_card("https://www.docker.com/", "logo-docker-mark-blue.png", "Docker"),
        _create_tech_card("https://kubernetes.io/", "logo-kubernetes-logo-without-workmark.png", "Kubernetes"),
        _create_tech_card("https://www.terraform.io/", "logo-terraform.png", "Terraform"),
        _create_card("https://cloud.google.com/run", "logo-cloud-run.png", 
                    "Google Cloud Run", "Google Cloud Run")
    ]

def get_common_sources():
    """
    Frequently used source citations using DRY helper.
    """
    return {
        'mayo_clinic_picc': generate_source_link(
            'https://www.mayoclinic.org/tests-procedures/picc-line/about/pac-20468748',
            'About PICC Lines (Mayo Clinic)'
        ),
        'cancer_ca_apl': generate_source_link(
            'https://cancer.ca/en/cancer-information/cancer-types/acute-myeloid-leukemia-aml/treatment/acute-promyelocytic-leukemia',
            'More on APL here'
        ),
        'alberta_health_apl': generate_source_link(
            'https://www.albertahealthservices.ca/assets/info/hp/cancer/if-hp-cancer-guide-lyhe008-apl.pdf',
            'Alberta Health Services'
        ),
        'toronto_devops_meetup': generate_source_link(
            'https://www.meetup.com/toronto-enterprise-devops-user-group/',
            'Toronto Enterprise DevOps Group on Meetup'
        ),
        'valley_of_fire': generate_source_link(
            'https://parks.nv.gov/parks/valley-of-fire',
            'Valley of Fire State Park'
        )
    }

def get_common_sources():
    """
    Frequently used source citations.
    """
    return {
        'mayo_clinic_picc': generate_source_link(
            'https://www.mayoclinic.org/tests-procedures/picc-line/about/pac-20468748',
            'About PICC Lines (Mayo Clinic)'
        ),
        'cancer_ca_apl': generate_source_link(
            'https://cancer.ca/en/cancer-information/cancer-types/acute-myeloid-leukemia-aml/treatment/acute-promyelocytic-leukemia',
            'More on APL here'
        ),
        'alberta_health_apl': generate_source_link(
            'https://www.albertahealthservices.ca/assets/info/hp/cancer/if-hp-cancer-guide-lyhe008-apl.pdf',
            'Alberta Health Services'
        ),
        'toronto_devops_meetup': generate_source_link(
            'https://www.meetup.com/toronto-enterprise-devops-user-group/',
            'Toronto Enterprise DevOps Group on Meetup'
        ),
        'valley_of_fire': generate_source_link(
            'https://parks.nv.gov/parks/valley-of-fire',
            'Valley of Fire State Park'
        )
    }
