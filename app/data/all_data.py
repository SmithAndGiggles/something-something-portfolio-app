"""
Portfolio Data Aggregation Module
==================================

Centralized data provider for all portfolio content sections. This module implements
the DRY (Don't Repeat Yourself) principle by consolidating all card data, content,
and portfolio information in a single maintainable location.

Features:
- Unified data access layer for all portfolio sections
- DRY helper functions for consistent card generation
- Dynamic URL generation for logos and assets
- Type-consistent data structures for template rendering
- Single source of truth for portfolio content

Architecture:
- Factory functions for each portfolio section (education, certifications, etc.)
- Internal helper functions for DRY card generation
- Flask url_for integration for dynamic asset paths
- Consistent card structure across all content types

Data Sections:
- Education: Academic background and formal learning
- Certifications: Professional credentials and validations  
- Tech Stack: Technology skills organized by category
- Connect: Contact information and social links
- Home: Personal introduction and portfolio overview

Design Philosophy:
This module prioritizes maintainability by centralizing all content data.
Updates to portfolio information require changes in only one location,
reducing maintenance overhead and ensuring consistency across the application.
"""

from flask import url_for

def get_education_cards():
    """
    Generate education and academic background cards
    
    Provides comprehensive academic history including degrees, certifications,
    and individual courses. Uses internal helper function for DRY card generation.
    
    Returns:
        list: Education card contexts for template rendering
        
    Card Structure:
        - University degrees and specialized programs
        - Professional development courses
        - Web development and technical training
        - Consistent "Learn More" badge for external links
        
    Template Usage:
        Cards render via cards.html template with logos, titles, and institutional links
    """
    def edu_card(href, logo_name, logo_alt, title, subtitle):
        """DRY helper for consistent education card generation"""
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
        edu_card("https://www.senecapolytechnic.ca/home.html", "logo-seneca.png", "Seneca Polytechnic logo", 
                 "Introduction to Databases", "Seneca Polytechnic • 2017"),
        edu_card("https://www.georgebrown.ca/", "logo-george-brown-college.svg", "George Brown College logo", 
                 "Foundations of PHP, Course", "George Brown College • 2017"),
        edu_card("https://www.yorku.ca/", "logo-york-u.png", "York University logo", 
                 "Full-Stack Web Development, Certificate", "York University • 2018 - 2019")
    ]

def get_certification_cards():
    """
    Generate professional certification and credential cards
    
    Provides industry certifications, professional validations, and skill credentials.
    Focuses on verifiable achievements with external badge links for validation.
    
    Returns:
        list: Certification card contexts for template rendering
        
    Card Features:
        - External links to certification validation pages
        - "View Badge" action with external link icon
        - Industry-recognized credentials and certifications
        - Professional skill validations
        
    Template Usage:
        Cards display with certification logos and link to verification pages
        for professional credential validation.
    """
    def cert_card(href, logo_name, logo_alt, title, subtitle):
        """DRY helper for consistent certification card generation"""
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
    """
    Generate technology stack cards organized by category
    
    Provides comprehensive technical skills showcase organized into frontend,
    backend, and infrastructure categories. Demonstrates full-stack development
    capabilities and DevOps proficiency.
    
    Returns:
        dict: Technology cards organized by category:
            - frontend: Client-side technologies and frameworks
            - backend: Server-side technologies and databases
            - infra: DevOps, cloud, and infrastructure tools
            
    Card Categories:
        - Frontend: JavaScript, React, HTML/CSS, UI frameworks
        - Backend: Python, Java, databases, server technologies
        - Infrastructure: Cloud platforms, containerization, CI/CD
        
    Template Usage:
        Returns categorized dictionary for separate rendering sections
        in techstack.html template with category-specific organization.
    """
    def tech_card(href, logo_name, logo_alt, title, subtitle):
        """DRY helper for standard technology card generation"""
        return {
            "href": href,
            "logo_src": url_for('static', filename=f'images/logos/{logo_name}'),
            "logo_alt": logo_alt,
            "title": title,
            "subtitle": subtitle,
            "badge_text": "Learn More"
        }
    
    def gcp_card(href, logo_name, logo_alt, title, subtitle):
        """DRY helper for Google Cloud Platform cards (different asset path)"""
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
    """
    Generate contact and social connection cards
    
    Provides professional networking and contact information cards.
    Features dynamic badge text based on platform type for appropriate
    call-to-action messaging.
    
    Returns:
        list: Contact card contexts for template rendering
        
    Connection Types:
        - LinkedIn: Professional networking profile
        - GitHub: Code repositories and development activity
        - Email: Direct contact method
        
    Card Features:
        - Platform-specific badge text for appropriate actions
        - Professional social media links
        - Direct contact options
        
    Template Usage:
        Cards render in connect.html with platform-specific styling and actions
    """
    def connect_card(href, logo_name, logo_alt, title, subtitle):
        """DRY helper with intelligent badge text based on platform"""
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
    """
    Generate homepage welcome card content
    
    Provides the main introduction content for the portfolio homepage.
    Features personal introduction, professional overview, and engaging
    call-to-action for visitors to explore the portfolio.
    
    Returns:
        dict: Home card context with image, title, and introduction text
        
    Content Features:
        - Cartoonized professional headshot
        - Personal welcome message with professional positioning
        - Portfolio exploration encouragement
        - Playful personality elements (emoji integration)
        - Growth mindset messaging (certification goals)
        
    Template Usage:
        Renders as the central hero content on home.html with image,
        title, and comprehensive introduction text.
        
    Design Notes:
        Balances professional presentation with personality to create
        an approachable and memorable first impression for visitors.
    """
    return {
        'image_src': 'images/content/cartoonized-alan-smith.png',
        'image_alt': 'Cartoonized Alan Smith',
        'card_title': 'Welcome to My Portfolio',
        'card_text': ("Hi, I'm Alan Smith—a technology enthusiast, lifelong learner, and passionate problem solver. "
                     "This website is a showcase of my journey, projects, and achievements, designed to give you a glimpse into my professional world and personal growth. "
                     "Explore my work, discover my story, and check out the certifications page—I'm hoping to have more than just three badges there soon!"
                     "<i class='fas fa-face-wink' style='color:#f7b731; font-size:1.3em; vertical-align:middle;'></i>")
    }
