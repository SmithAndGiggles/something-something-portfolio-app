# filepath: something-something-portfolio-app/app/data/shared_data.py

from flask import url_for

def get_shared_data():
    """
    Centralized data that appears across multiple templates.
    This reduces duplication and makes updates easier.
    """
    return {
        'education_institutions': {
            'york_university': {
                'name': 'York University',
                'logo_src': url_for('static', filename='images/logos/logo-york-u.png'),
                'logo_alt': 'York University logo'
            },
            'george_brown': {
                'name': 'George Brown College',
                'logo_src': url_for('static', filename='images/logos/logo-george-brown-college.svg'),
                'logo_alt': 'George Brown College logo'
            },
            'humber_college': {
                'name': 'Humber College',
                'logo_src': url_for('static', filename='images/logos/logo-humber-college.svg'),
                'logo_alt': 'Humber College logo'
            },
            'centennial_college': {
                'name': 'Centennial College',
                'logo_src': url_for('static', filename='images/logos/logo-centennial-college.jpg'),
                'logo_alt': 'Centennial College logo'
            }
        },
        'tech_logos': {
            'python': {
                'src': url_for('static', filename='images/logos/logo-python-logo-notext.png'),
                'alt': 'Python'
            },
            'javascript': {
                'src': url_for('static', filename='images/logos/logo-js.svg'),
                'alt': 'JavaScript'
            },
            'html5': {
                'src': url_for('static', filename='images/logos/logo-html.svg'),
                'alt': 'HTML5'
            },
            'css3': {
                'src': url_for('static', filename='images/logos/logo-css.svg'),
                'alt': 'CSS3'
            },
            'flask': {
                'src': url_for('static', filename='images/logos/logo-horn-flask.png'),
                'alt': 'Flask'
            },
            'docker': {
                'src': url_for('static', filename='images/logos/logo-docker-mark-blue.png'),
                'alt': 'Docker'
            },
            'kubernetes': {
                'src': url_for('static', filename='images/logos/logo-kubernetes-logo-without-workmark.png'),
                'alt': 'Kubernetes'
            },
            'terraform': {
                'src': url_for('static', filename='images/logos/logo-terraform.png'),
                'alt': 'Terraform'
            },
            'gcp': {
                'src': url_for('static', filename='images/logos/logo-gcp-associate-engineer.png'),
                'alt': 'Google Cloud Platform'
            }
        },
        'common_styles': {
            'card_default': 'card rounded-4 bg-dark text-white h-100 hover-shadow',
            'achievement_image': 'w-100 h-100 achievement-media',
            'media_container': 'achievement-media w-100 h-100'
        },
        'external_links': {
            'linkedin_profile': 'https://www.linkedin.com/in/alan-smith-ca/',
            'github_profile': 'https://github.com/SmithAndGiggles',
            'credly_base': 'https://www.credly.com/badges/',
            'mayo_clinic_picc': 'https://www.mayoclinic.org/tests-procedures/picc-line/about/pac-20468748'
        }
    }
