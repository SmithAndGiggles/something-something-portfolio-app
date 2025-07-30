# filepath: something-something-portfolio-app/app/data/constants.py

"""
Portfolio Constants Module
===========================

Centralized configuration for all portfolio content to eliminate duplication.
Single source of truth for logos, URLs, titles, and common strings.
"""

# =============================================================================
# CONFIGURATION CONSTANTS
# =======================
# Centralized configuration values used across the application
# These values can be overridden by environment variables in production

# UI Configuration
CAROUSEL_INTERVAL = 20000  # Carousel auto-advance interval in milliseconds
CARD_BACKGROUND_COLOR = '#111214'  # Dark card background color
ERROR_IMAGE_WIDTH = '600px'  # Error page image width
ERROR_IMAGE_MAX_WIDTH = '90vw'  # Error page responsive max width

# Contact Information
PORTFOLIO_EMAIL = 'alan@me2u.space'  # Primary contact email
PORTFOLIO_DOMAIN = 'portfolio.me2u.space'  # Portfolio domain
CONTACT_URL_PATH = '/connect'  # Contact page path

# Card Dimensions
CARD_MAX_WIDTH = '320px'
CARD_MIN_WIDTH = '220px'
CARD_LOGO_HEIGHT = '96px'
CARD_LOGO_MAX_HEIGHT = '60px'

# Carousel Dimensions  
CAROUSEL_HEIGHT = '60vh'
CAROUSEL_MIN_HEIGHT = '350px'
CAROUSEL_MAX_HEIGHT = '600px'

# INSTITUTIONAL DATA
# ==================

INSTITUTIONS = {
    'york_university': {
        'name': 'York University',
        'url': 'https://www.yorku.ca/',
        'logo': 'logo-york-u.png',
        'alt': 'York University logo'
    },
    'george_brown': {
        'name': 'George Brown College',
        'url': 'https://www.georgebrown.ca/',
        'logo': 'logo-george-brown-college.svg',
        'alt': 'George Brown College logo'
    },
    'humber_college': {
        'name': 'Humber College',
        'url': 'https://humber.ca/',
        'logo': 'logo-humber-college.svg',
        'alt': 'Humber College logo'
    },
    'centennial_college': {
        'name': 'Centennial College',
        'url': 'https://www.centennialcollege.ca/',
        'logo': 'logo-centennial-college.jpg',
        'alt': 'Centennial College logo'
    },
    'seneca_polytechnic': {
        'name': 'Seneca Polytechnic',
        'url': 'https://www.senecapolytechnic.ca/home.html',
        'logo': 'logo-seneca.png',
        'alt': 'Seneca Polytechnic logo'
    }
}

# =============================================================================
# TECHNOLOGY STACK
# =============================================================================

TECHNOLOGIES = {
    # Frontend Technologies
    'html5': {
        'name': 'HTML5',
        'url': 'https://developer.mozilla.org/en-US/docs/Web/HTML',
        'logo': 'logo-html.svg',
        'alt': 'HTML5',
        'category': 'frontend',
        'description': 'Markup Language'
    },
    'css3': {
        'name': 'CSS3',
        'url': 'https://developer.mozilla.org/en-US/docs/Web/CSS',
        'logo': 'logo-css.svg',
        'alt': 'CSS3',
        'category': 'frontend',
        'description': 'Stylesheet Language'
    },
    'javascript': {
        'name': 'JavaScript',
        'url': 'https://developer.mozilla.org/en-US/docs/Web/JavaScript',
        'logo': 'logo-js.svg',
        'alt': 'JavaScript',
        'category': 'frontend',
        'description': 'Programming Language'
    },
    'bootstrap': {
        'name': 'Bootstrap',
        'url': 'https://getbootstrap.com',
        'logo': 'logo-bootstrap.png',
        'alt': 'Bootstrap Logo',
        'category': 'frontend',
        'description': 'Responsive, mobile-first front-end web development framework.'
    },
    'tailwindcss': {
        'name': 'Tailwind CSS',
        'url': 'https://tailwindcss.com/',
        'logo': 'logo-tailwindcss.png',
        'alt': 'Tailwind CSS Logo',
        'category': 'frontend',
        'description': 'Utility-first CSS framework for rapid UI development.'
    },
    
    # Backend Technologies
    'python': {
        'name': 'Python',
        'url': 'https://www.python.org/',
        'logo': 'logo-python-logo-notext.png',
        'alt': 'Python',
        'category': 'backend',
        'description': 'Programming Language'
    },
    'flask': {
        'name': 'Flask',
        'url': 'https://flask.palletsprojects.com/',
        'logo': 'logo-horn-flask.png',
        'alt': 'Flask',
        'category': 'backend',
        'description': 'Web Framework'
    },
    'jinja2': {
        'name': 'Jinja2',
        'url': 'https://jinja.palletsprojects.com/',
        'logo': 'logo-jinja-icon.svg',
        'alt': 'Jinja2',
        'category': 'backend',
        'description': 'Template Engine'
    },
    'gunicorn': {
        'name': 'Gunicorn',
        'url': 'https://gunicorn.org/',
        'logo': 'logo-gunicorn.svg',
        'alt': 'Gunicorn',
        'category': 'backend',
        'description': 'WSGI Server'
    },
    'toml': {
        'name': 'TOML',
        'url': 'https://toml.io/en/',
        'logo': 'logo-toml.png',
        'alt': 'TOML Logo',
        'category': 'backend',
        'description': 'Tom\'s Obvious, Minimal Language for config files.'
    },
    
    # Infrastructure & DevOps
    'docker': {
        'name': 'Docker',
        'url': 'https://www.docker.com/',
        'logo': 'logo-docker-mark-blue.png',
        'alt': 'Docker',
        'category': 'infra',
        'description': 'Containerization'
    },
    'kubernetes': {
        'name': 'Kubernetes',
        'url': 'https://kubernetes.io/',
        'logo': 'logo-kubernetes-logo-without-workmark.png',
        'alt': 'Kubernetes',
        'category': 'infra',
        'description': 'Container Orchestration'
    },
    'terraform': {
        'name': 'Terraform',
        'url': 'https://www.terraform.io/',
        'logo': 'logo-terraform.png',
        'alt': 'Terraform',
        'category': 'infra',
        'description': 'IaC Tool'
    },
    'github': {
        'name': 'GitHub',
        'url': 'https://github.com',
        'logo': 'logo-github.png',
        'alt': 'GitHub',
        'category': 'infra',
        'description': 'Source Code Hosting & Collaboration'
    },
    'github_actions': {
        'name': 'GitHub Actions',
        'url': 'https://github.com/features/actions',
        'logo': 'logo-github-actions.png',
        'alt': 'GitHub Actions',
        'category': 'infra',
        'description': 'CI/CD'
    },
    'terragrunt': {
        'name': 'Terragrunt',
        'url': 'https://terragrunt.gruntwork.io/',
        'logo': 'logo-terragrunt.png',
        'alt': 'Terragrunt',
        'category': 'infra',
        'description': 'IaC Wrapper'
    },
    'yamlscript': {
        'name': 'Yamlscript',
        'url': 'https://yamlscript.org',
        'logo': 'logo-yamlscript.svg',
        'alt': 'Yamlscript',
        'category': 'infra',
        'description': 'YAML-based Scripting Language'
    },
    'cloud_run': {
        'name': 'Google Cloud Run',
        'url': 'https://cloud.google.com/run',
        'logo': 'logo-gcp-cloud-run.png',
        'alt': 'Cloud Run',
        'category': 'infra',
        'description': 'Serverless Platform'
    }
}

# =============================================================================
# CERTIFICATIONS
# =============================================================================

CERTIFICATIONS = {
    'gcp_associate': {
        'title': 'Google Cloud Associate Cloud Engineer',
        'subtitle': 'Google Cloud',
        'short_title': 'Associate Cloud Engineer',
        'url': 'https://www.credly.com/badges/acc75311-8a96-48e5-be8f-c928c9d52ca3',
        'logo': 'logo-gcp-associate-engineer.png',
        'alt': 'Google Cloud Associate Cloud Engineer'
    },
    'gcp_architect': {
        'title': 'Google Cloud Professional Cloud Architect',
        'subtitle': 'Google Cloud',
        'short_title': 'Professional Cloud Architect',
        'url': 'https://www.credly.com/badges/85110e1e-ea27-4687-9080-f83eed5694a0',
        'logo': 'logo-gcp-professional-architect.png',
        'alt': 'Google Cloud Professional Cloud Architect'
    },
    'gcp_devops': {
        'title': 'Google Cloud Professional Cloud DevOps Engineer',
        'subtitle': 'Google Cloud',
        'short_title': 'Professional Cloud DevOps Engineer',
        'url': 'https://www.credly.com/badges/9543b3ca-8ec4-4ca6-aa7b-b68853078cd9/public_url',
        'logo': 'logo-gcp-devops-engineer-certification.png',
        'alt': 'Google Cloud DevOps Engineer'
    },
    'aws_practitioner': {
        'title': 'AWS Certified Cloud Practitioner',
        'subtitle': 'Amazon Web Services',
        'short_title': 'Certified Cloud Practitioner',
        'url': 'https://www.credly.com/badges/5f4be6a1-71e2-48dc-8b6e-7fbcf26163f9',
        'logo': 'logo-aws-certified-cloud-practitioner.png',
        'alt': 'AWS Cloud Practitioner'
    },
    'terraform_associate': {
        'title': 'HashiCorp Terraform Associate',
        'subtitle': 'HashiCorp',
        'short_title': 'Terraform Associate',
        'url': 'https://www.credly.com/badges/cdd46167-59b6-46be-9abd-29eebf7db00e',
        'logo': 'logo-terraform.png',
        'alt': 'HashiCorp Terraform Associate'
    }
}

# =============================================================================
# EDUCATION COURSES & PROGRAMS
# =============================================================================

EDUCATION_PROGRAMS = [
    {
        'institution': 'york_university',
        'program': 'Kinesiology, B.A. Specialized Honours',
        'years': '2005 - 2010'
    },
    {
        'institution': 'george_brown',
        'program': 'Sport Marketing and Event Management, Certificate',
        'years': '2010 - 2011'
    },
    {
        'institution': 'george_brown',
        'program': 'Introduction to Web Design and Development, Course',
        'years': '2012'
    },
    {
        'institution': 'george_brown',
        'program': 'Web Page I – XHTML, Course',
        'years': '2013'
    },
    {
        'institution': 'george_brown',
        'program': 'Web Page II – JavaScript/jQuery, Course',
        'years': '2013'
    },
    {
        'institution': 'centennial_college',
        'program': 'Introduction to Unix/Linux, Course',
        'years': '2015'
    },
    {
        'institution': 'humber_college',
        'program': 'Red Hat Enterprise Linux System Admin, Course',
        'years': '2015'
    },
    {
        'institution': 'seneca_polytechnic',
        'program': 'Introduction to Databases',
        'years': '2017'
    },
    {
        'institution': 'george_brown',
        'program': 'Foundations of PHP, Course',
        'years': '2017'
    },
    {
        'institution': 'york_university',
        'program': 'Full-Stack Web Development, Certificate',
        'years': '2018 - 2019'
    }
]

# =============================================================================
# SOCIAL & CONTACT LINKS
# =============================================================================

SOCIAL_LINKS = {
    'linkedin': {
        'name': 'LinkedIn',
        'url': 'https://www.linkedin.com/in/alan-smith-ca/',
        'logo': 'logo-linkedin.png',  # or logo-linkedin-blue.png depending on usage
        'alt': 'LinkedIn Logo',
        'description': 'Connect with me on LinkedIn'
    },
    'github': {
        'name': 'GitHub',
        'url': 'https://github.com/SmithAndGiggles',
        'logo': 'logo-github.png',
        'alt': 'GitHub Logo',
        'description': 'See my projects on GitHub'
    },
    'email': {
        'name': 'Email',
        'url': f'mailto:{PORTFOLIO_EMAIL}',  # Use centralized email
        'logo': 'logo-gmail.png',  # or logo-email.png
        'alt': 'Gmail Logo',
        'description': 'Email me!'
    }
}

# =============================================================================
# COMMON STRINGS & BADGES
# =============================================================================

BADGE_TEXT = {
    'learn_more': 'Learn More',
    'view_badge': 'View Badge',
    'view_badge_icon': 'View Badge <i class="fas fa-external-link-alt"></i>',
    'connect': 'Connect',
    'visit': 'Visit'
}

# =============================================================================
# EXTERNAL REFERENCE URLS
# =============================================================================

EXTERNAL_URLS = {
    'mayo_clinic_picc': 'https://www.mayoclinic.org/tests-procedures/picc-line/about/pac-20468748',
    'cancer_society': 'https://cancer.ca/en/cancer-information/cancer-types/acute-myeloid-leukemia-aml/statistics',
    'alberta_health_apl': 'https://www.albertahealthservices.ca/assets/info/hp/cancer/if-hp-cancer-guide-lyhe008-apl.pdf',
    'leukemia_society': 'https://www.bloodcancers.ca/sites/default/files/2023-02/LSC22103_LLS1001E_AML%20Brochure_E_m4.pdf',
    'biomedcentral': 'https://bmccancer.biomedcentral.com/articles/10.1186/s12885-023-10612-z',
    'donkey_sanctuary': 'https://www.thedonkeysanctuary.ca',
    'york_ace_article': 'https://news.yorku.ca/2005/05/30/york-u-honours-2005-ace-graduates-with-5000-scholarships/',
    'toronto_devops_meetup': 'https://www.meetup.com/toronto-enterprise-devops-user-group/',
    'valley_of_fire': 'https://parks.nv.gov/parks/valley-of-fire'
}

# =============================================================================
# LANDING PAGE CONFIGURATION
# =============================================================================

LANDING_PAGE_CONFIG = {
    'title': 'Welcome to me2u.place',
    'subtitle': 'Alan Smith - Portfolio & Professional Experience',
    'portfolio_url': f'https://{PORTFOLIO_DOMAIN}/',
    'contact_url': f'https://{PORTFOLIO_DOMAIN}{CONTACT_URL_PATH}',
    'domain_text': 'This domain redirects to my main portfolio at',
    'professional_title': 'Cloud & DevOps Engineer',
    'professional_description': 'Specializing in Google Cloud Platform, Terraform, Kubernetes, and modern DevOps practices',
    'tech_badges': [
        {'name': 'GCP', 'class': 'bg-primary'},
        {'name': 'Terraform', 'class': 'bg-secondary'},
        {'name': 'Kubernetes', 'class': 'bg-info'}
    ]
}

LANDING_CARDS = {
    'portfolio': {
        'icon': 'fas fa-user-tie fa-3x text-primary mb-3',
        'title': 'Portfolio',
        'description': 'Explore my professional journey, skills, and achievements',
        'button_text': 'View Portfolio',
        'button_class': 'btn btn-primary',
        'url_key': 'portfolio_url'
    },
    'contact': {
        'icon': 'fas fa-envelope fa-3x text-success mb-3',
        'title': 'Contact',
        'description': 'Get in touch for opportunities and collaborations',
        'button_text': 'Contact Me',
        'button_class': 'btn btn-success',
        'url_key': 'contact_url'
    }
}

# =============================================================================
# HELPER FUNCTIONS TO GET CATEGORIZED DATA
# =============================================================================

def get_technologies_by_category(category):
    """Get all technologies in a specific category"""
    return {k: v for k, v in TECHNOLOGIES.items() if v['category'] == category}

def get_frontend_technologies():
    """Get all frontend technologies"""
    return get_technologies_by_category('frontend')

def get_backend_technologies():
    """Get all backend technologies"""
    return get_technologies_by_category('backend')

def get_infra_technologies():
    """Get all infrastructure technologies"""
    return get_technologies_by_category('infra')
