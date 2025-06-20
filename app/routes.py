from flask import Blueprint, render_template, url_for, request
from .data.achievements import get_achievement_slides
from .data.home_card import get_home_card

routes = Blueprint('routes', __name__)


# @routes.route('/', methods=['GET'])
# def landing_page():
#     # Check if request is coming from me2u.place domain
#     if request.host == 'me2u.place':
#         return render_template('landing.html')
#     else:
#         # Default behavior for other domains
#         return render_template('index.html')

@routes.route('/')
def home():
    # Check if the request is coming from me2u.place
    if request.host.startswith('me2u.place'):
        return render_template('me2u_place_landing.html')
    return render_template('home.html', home_card=get_home_card())

@routes.route('/home')
def render_index():
    return render_template('home.html', home_card=get_home_card())

@routes.route('/education')
def education():
    education_cards = [
        {"href": "https://www.yorku.ca/", "logo_src": url_for('static', filename='images/logos/logo-york-u.png'), "logo_alt": "York University logo", "title": "Kinesiology, B.A. Specialized Honours", "subtitle": "York University • 2005 - 2010", "badge_text": "Learn More"},
        {"href": "https://www.georgebrown.ca/", "logo_src": url_for('static', filename='images/logos/logo-george-brown-college.svg'), "logo_alt": "George Brown College logo", "title": "Sport Marketing and Event Management, Certificate", "subtitle": "George Brown College • 2010 - 2011", "badge_text": "Learn More"},
        {"href": "https://www.georgebrown.ca/", "logo_src": url_for('static', filename='images/logos/logo-george-brown-college.svg'), "logo_alt": "George Brown College logo", "title": "Introduction to Web Design and Development, Course", "subtitle": "George Brown College • 2012", "badge_text": "Learn More"},
        {"href": "https://www.georgebrown.ca/", "logo_src": url_for('static', filename='images/logos/logo-george-brown-college.svg'), "logo_alt": "George Brown College logo", "title": "Web Page I – XHTML, Course", "subtitle": "George Brown College • 2013", "badge_text": "Learn More"},
        {"href": "https://www.georgebrown.ca/", "logo_src": url_for('static', filename='images/logos/logo-george-brown-college.svg'), "logo_alt": "George Brown College logo", "title": "Web Page II – JavaScript/jQuery, Course", "subtitle": "George Brown College • 2013", "badge_text": "Learn More"},
        {"href": "https://www.centennialcollege.ca/", "logo_src": url_for('static', filename='images/logos/logo-centennial-college.jpg'), "logo_alt": "Centennial College logo", "title": "Introduction to Unix/Linux, Course", "subtitle": "Centennial College • 2015", "badge_text": "Learn More"},
        {"href": "https://humber.ca/", "logo_src": url_for('static', filename='images/logos/logo-humber-college.svg'), "logo_alt": "Humber College logo", "title": "Red Hat Enterprise Linux System Admin, Course", "subtitle": "Humber College • 2015", "badge_text": "Learn More"},
        {"href": "https://www.georgebrown.ca/", "logo_src": url_for('static', filename='images/logos/logo-george-brown-college.svg'), "logo_alt": "George Brown College logo", "title": "Foundations of PHP, Course", "subtitle": "George Brown College • 2017", "badge_text": "Learn More"},
        {"href": "https://www.yorku.ca/", "logo_src": url_for('static', filename='images/logos/logo-york-u.png'), "logo_alt": "York University logo", "title": "Full-Stack Web Development, Certificate", "subtitle": "York University • 2018 - 2019", "badge_text": "Learn More"}
    ]
    return render_template('education.html', cards=education_cards)

@routes.route('/achievements')
def achievements():
    slides = get_achievement_slides(url_for)
    return render_template('achievements.html', slides=slides, carousel_id='achievementsCarousel')

@routes.route('/certifications')
def certifications():
    cert_cards = [
        {"href": "https://www.credly.com/badges/acc75311-8a96-48e5-be8f-c928c9d52ca3", "logo_src": url_for('static', filename='images/logos/logo-gcp-associate-engineer.png'), "logo_alt": "Google Cloud Associate Cloud Engineer", "title": "Google Cloud", "subtitle": "Associate Cloud Engineer", "badge_text": "View Badge <i class='fas fa-external-link-alt'></i>"},
        {"href": "https://www.credly.com/badges/85110e1e-ea27-4687-9080-f83eed5694a0", "logo_src": url_for('static', filename='images/logos/logo-gcp-professional-architect.png'), "logo_alt": "Google Cloud Professional Cloud Architect", "title": "Google Cloud", "subtitle": "Professional Cloud Architect", "badge_text": "View Badge <i class='fas fa-external-link-alt'></i>"},
        {"href": "https://www.credly.com/badges/cdd46167-59b6-46be-9abd-29eebf7db00e", "logo_src": url_for('static', filename='images/logos/logo-terraform.png'), "logo_alt": "HashiCorp Terraform Associate", "title": "HashiCorp", "subtitle": "Terraform Associate", "badge_text": "View Badge <i class='fas fa-external-link-alt'></i>"}
    ]
    return render_template('certifications.html', cards=cert_cards)

@routes.route('/techstack')
def techstack():
    frontend_cards = [
        {"href": "https://developer.mozilla.org/en-US/docs/Web/HTML", "logo_src": url_for('static', filename='images/logos/logo-html.svg'), "logo_alt": "HTML5", "title": "HTML5", "subtitle": "Markup Language", "badge_text": "Learn More"},
        {"href": "https://developer.mozilla.org/en-US/docs/Web/CSS", "logo_src": url_for('static', filename='images/logos/logo-css.svg'), "logo_alt": "CSS3", "title": "CSS3", "subtitle": "Stylesheet Language", "badge_text": "Learn More"},
        {"href": "https://developer.mozilla.org/en-US/docs/Web/JavaScript", "logo_src": url_for('static', filename='images/logos/logo-js.svg'), "logo_alt": "JavaScript", "title": "JavaScript", "subtitle": "Programming Language", "badge_text": "Learn More"},
        {"href": "https://getbootstrap.com", "logo_src": url_for('static', filename='images/logos/logo-bootstrap.png'), "logo_alt": "Bootstrap Logo", "title": "Bootstrap", "subtitle": "Responsive, mobile-first front-end web development framework.", "badge_text": "Learn More"}
    ]
    backend_cards = [
        {"href": "https://www.python.org/", "logo_src": url_for('static', filename='images/logos/logo-python-logo-notext.png'), "logo_alt": "Python", "title": "Python", "subtitle": "Programming Language", "badge_text": "Learn More"},
        {"href": "https://flask.palletsprojects.com/", "logo_src": url_for('static', filename='images/logos/logo-horn-flask.png'), "logo_alt": "Flask", "title": "Flask", "subtitle": "Web Framework", "badge_text": "Learn More"},
        {"href": "https://jinja.palletsprojects.com/", "logo_src": url_for('static', filename='images/logos/logo-jinja-icon.svg'), "logo_alt": "Jinja2", "title": "Jinja2", "subtitle": "Template Engine", "badge_text": "Learn More"},
        {"href": "https://gunicorn.org/", "logo_src": url_for('static', filename='images/logos/logo-gunicorn.svg'), "logo_alt": "Gunicorn", "title": "Gunicorn", "subtitle": "WSGI Server", "badge_text": "Learn More"}
    ]
    infra_cards = [
        {"href": "https://www.docker.com/", "logo_src": url_for('static', filename='images/logos/logo-docker-mark-blue.png'), "logo_alt": "Docker", "title": "Docker", "subtitle": "Containerization", "badge_text": "Learn More"},
        {"href": "https://cloud.google.com/run", "logo_src": url_for('static', filename='images/google-cloud/cloud-run.png'), "logo_alt": "Cloud Run", "title": "Google Cloud Run", "subtitle": "Serverless Platform", "badge_text": "Learn More"},
        {"href": "https://www.terraform.io/", "logo_src": url_for('static', filename='images/logos/logo-terraform.png'), "logo_alt": "Terraform", "title": "Terraform", "subtitle": "IaC Tool", "badge_text": "Learn More"},
        # {"href": "https://kubernetes.io/", "logo_src": url_for('static', filename='images/logos/logo-kubernetes-logo-without-workmark.png'), "logo_alt": "Kubernetes", "title": "Kubernetes", "subtitle": "Container Orchestration", "badge_text": "Learn More"},
        {"href": "https://github.com/features/actions", "logo_src": url_for('static', filename='images/logos/logo-github-actions.png'), "logo_alt": "GitHub Actions", "title": "GitHub Actions", "subtitle": "CI/CD", "badge_text": "Learn More"},
        {"href": "https://github.com", "logo_src": url_for('static', filename='images/logos/logo-github.png'), "logo_alt": "GitHub", "title": "GitHub", "subtitle": "Source Code Hosting & Collaboration", "badge_text": "Learn More"},
        {"href": "https://terragrunt.gruntwork.io/", "logo_src": url_for('static', filename='images/logos/logo-terragrunt.png'), "logo_alt": "Terragrunt", "title": "Terragrunt", "subtitle": "IaC Wrapper", "badge_text": "Learn More"},
        {"href": "https://yamlscript.org", "logo_src": url_for('static', filename='images/logos/logo-yamlscript.svg'), "logo_alt": "Yamlscript", "title": "Yamlscript", "subtitle": "YAML-based Scripting Language", "badge_text": "Learn More"}
    ]
    return render_template('techstack.html', frontend_cards=frontend_cards, backend_cards=backend_cards, infra_cards=infra_cards)

@routes.route('/irl')
def irl():
    from .data.irl import get_irl_slides
    slides = get_irl_slides(url_for)
    return render_template('irl.html', slides=slides, carousel_id='irlCarousel')

@routes.route('/connect')
def connect():
    connect_cards = [
        {
            "href": "https://www.linkedin.com/in/alan-r-smith/",
            "logo_src": url_for('static', filename='images/logos/logo-linkedin-blue.png'),
            "logo_alt": "LinkedIn Logo",
            "title": "LinkedIn",
            "subtitle": "Connect with me on LinkedIn",
            "badge_text": "View Profile"
        },
        {
            "href": "https://github.com/SmithAndGiggles",
            "logo_src": url_for('static', filename='images/logos/logo-github.png'),
            "logo_alt": "GitHub Logo",
            "title": "GitHub",
            "subtitle": "See my projects on GitHub",
            "badge_text": "View GitHub"
        },
        {
            "href": "mailto:42-daisy-focuses@icloud.com",
            "logo_src": url_for('static', filename='images/logos/logo-gmail.png'),
            "logo_alt": "Gmail Logo",
            "title": "Email",
            "subtitle": "Email me!",
            "badge_text": "Send Email"
        }
    ]
    return render_template('connect.html', cards=connect_cards)

@routes.route('/me2u-place')
def me2u_place_landing():
    """Dedicated route for me2u.place landing page"""
    return render_template('me2u_place_landing.html')

