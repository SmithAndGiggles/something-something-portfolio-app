# filepath: something-something-portfolio-app/app/data/card_factory.py

from flask import url_for
from app.utils.template_helpers import generate_card_data, generate_source_link

def get_certification_cards():
    """
    Centralized certification card data.
    Replaces repetitive card creation across multiple files.
    """
    return [
        generate_card_data(
            href="https://www.credly.com/badges/acc75311-8a96-48e5-be8f-c928c9d52ca3",
            logo_src=url_for('static', filename='images/logos/logo-gcp-associate-engineer.png'),
            logo_alt="Google Cloud Associate Cloud Engineer",
            title="Google Cloud Associate Cloud Engineer",
            subtitle="Google Cloud Platform",
            badge_text="View Badge"
        ),
        generate_card_data(
            href="https://www.credly.com/badges/professional-cloud-architect-badge-id",
            logo_src=url_for('static', filename='images/logos/logo-gcp-professional-architect.png'),
            logo_alt="Google Cloud Professional Cloud Architect",
            title="Professional Cloud Architect",
            subtitle="Google Cloud Platform",
            badge_text="View Badge"
        ),
        generate_card_data(
            href="https://www.credly.com/badges/terraform-associate-badge-id",
            logo_src=url_for('static', filename='images/logos/logo-terraform.png'),
            logo_alt="HashiCorp Terraform Associate",
            title="Terraform Associate",
            subtitle="HashiCorp",
            badge_text="View Badge"
        )
    ]

def get_education_cards():
    """
    Centralized education card data.
    """
    return [
        generate_card_data(
            href="#",
            logo_src=url_for('static', filename='images/logos/logo-york-u.png'),
            logo_alt="York University logo",
            title="Kinesiology, B.A. Specialized Honours",
            subtitle="York University • 2005 - 2010"
        ),
        generate_card_data(
            href="#",
            logo_src=url_for('static', filename='images/logos/logo-george-brown-college.svg'),
            logo_alt="George Brown College logo",
            title="Sport Marketing and Event Management",
            subtitle="George Brown College • 2010 - 2011"
        ),
        generate_card_data(
            href="#",
            logo_src=url_for('static', filename='images/logos/logo-york-u.png'),
            logo_alt="York University logo",
            title="Full-Stack Web Development Certificate",
            subtitle="York University • 2018 - 2019"
        ),
        generate_card_data(
            href="https://www.senecapolytechnic.ca/home.html",
            logo_src=url_for('static', filename='images/logos/logo-seneca.png'),
            logo_alt="Seneca Polytechnic logo",
            title="Introduction to Databases",
            subtitle="Seneca Polytechnic • 2017"
        )
    ]

def get_connect_cards():
    """
    Centralized connect/social card data.
    """
    return [
        generate_card_data(
            href="https://www.linkedin.com/in/alan-smith-ca/",
            logo_src=url_for('static', filename='images/logos/logo-linkedin.png'),
            logo_alt="LinkedIn",
            title="LinkedIn",
            subtitle="Professional Network"
        ),
        generate_card_data(
            href="https://github.com/SmithAndGiggles",
            logo_src=url_for('static', filename='images/logos/logo-github.png'),
            logo_alt="GitHub",
            title="GitHub",
            subtitle="Code Repository"
        ),
        generate_card_data(
            href="mailto:alan@me2u.space",
            logo_src=url_for('static', filename='images/logos/logo-email.png'),
            logo_alt="Email",
            title="Email",
            subtitle="Direct Contact"
        )
    ]

def get_frontend_tech_cards():
    """
    Frontend technology cards.
    """
    return [
        generate_card_data(
            href="https://developer.mozilla.org/en-US/docs/Web/HTML",
            logo_src=url_for('static', filename='images/logos/logo-html.svg'),
            logo_alt="HTML5",
            title="HTML5"
        ),
        generate_card_data(
            href="https://developer.mozilla.org/en-US/docs/Web/CSS",
            logo_src=url_for('static', filename='images/logos/logo-css.svg'),
            logo_alt="CSS3",
            title="CSS3"
        ),
        generate_card_data(
            href="https://developer.mozilla.org/en-US/docs/Web/JavaScript",
            logo_src=url_for('static', filename='images/logos/logo-js.svg'),
            logo_alt="JavaScript",
            title="JavaScript"
        )
    ]

def get_backend_tech_cards():
    """
    Backend technology cards.
    """
    return [
        generate_card_data(
            href="https://www.python.org/",
            logo_src=url_for('static', filename='images/logos/logo-python-logo-notext.png'),
            logo_alt="Python",
            title="Python"
        ),
        generate_card_data(
            href="https://flask.palletsprojects.com/",
            logo_src=url_for('static', filename='images/logos/logo-horn-flask.png'),
            logo_alt="Flask",
            title="Flask"
        ),
        generate_card_data(
            href="https://jinja.palletsprojects.com/",
            logo_src=url_for('static', filename='images/logos/logo-jinja-icon.svg'),
            logo_alt="Jinja2",
            title="Jinja2"
        )
    ]

def get_infra_tech_cards():
    """
    Infrastructure/Cloud technology cards.
    """
    return [
        generate_card_data(
            href="https://www.docker.com/",
            logo_src=url_for('static', filename='images/logos/logo-docker-mark-blue.png'),
            logo_alt="Docker",
            title="Docker"
        ),
        generate_card_data(
            href="https://kubernetes.io/",
            logo_src=url_for('static', filename='images/logos/logo-kubernetes-logo-without-workmark.png'),
            logo_alt="Kubernetes",
            title="Kubernetes"
        ),
        generate_card_data(
            href="https://www.terraform.io/",
            logo_src=url_for('static', filename='images/logos/logo-terraform.png'),
            logo_alt="Terraform",
            title="Terraform"
        ),
        generate_card_data(
            href="https://cloud.google.com/run",
            logo_src=url_for('static', filename='images/google-cloud/cloud-run.png'),
            logo_alt="Google Cloud Run",
            title="Google Cloud Run"
        )
    ]

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
