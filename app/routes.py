from flask import Blueprint, render_template, url_for
from .data.achievements import get_achievement_slides
from .data.home_card import get_home_card

routes = Blueprint('routes', __name__)

@routes.route('/')
def home():
    return render_template('home.html', home_card=get_home_card())

@routes.route('/home')
def render_index():
    return render_template('home.html', home_card=get_home_card())

@routes.route('/education')
def education():
    return render_template('education.html')

@routes.route('/achievements')
def achievements():
    slides = get_achievement_slides(url_for)
    return render_template('achievements.html', slides=slides, carousel_id='achievementsCarousel')

@routes.route('/certifications')
def certifications():
    return render_template('certifications.html')

@routes.route('/techstack')
def techstack():
    return render_template('techstack.html')