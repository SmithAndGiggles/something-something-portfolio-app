from flask import Blueprint, render_template

routes = Blueprint('routes', __name__)

@routes.route('/')
def home():
    return render_template('home.html')

@routes.route('/home')
def render_index():
    return render_template('home.html')

@routes.route('/cars')
def cars():
    return render_template('coming_soon.html')

@routes.route('/travels')
def travels():
    return render_template('coming_soon.html')

@routes.route('/sports')
def sports():
    return render_template('coming_soon.html')

@routes.route('/education')
def education():
    return render_template('education.html')

@routes.route('/achievements')
def achievements():
    return render_template('achievements.html')

@routes.route('/pets')
def pets():
    return render_template('coming_soon.html')

@routes.route('/certifications')
def certifications():
    return render_template('certifications.html')

@routes.route('/techstack')
def techstack():
    return render_template('tech_stack.html')

@routes.route('/ping')
def ping():
    return "pong"