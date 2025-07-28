from flask import Blueprint, render_template, request, url_for
from .data.all_data import (
    get_education_cards, get_certification_cards, get_techstack_cards, 
    get_connect_cards, get_home_card
)
from .data.achievements import get_achievement_slides
from .data.irl import get_irl_slides

routes = Blueprint('routes', __name__)

@routes.route('/')
def home():
    return render_template('pages/home.html', home_card=get_home_card())

@routes.route('/home')
def render_index():
    return render_template('pages/home.html', home_card=get_home_card())

@routes.route('/education')
def education():
    return render_template('pages/education.html', cards=get_education_cards())

@routes.route('/achievements')
def achievements():
    slides = get_achievement_slides(url_for)
    return render_template('pages/achievements.html', slides=slides, carousel_id='achievementsCarousel')

@routes.route('/certifications')
def certifications():
    return render_template('pages/certifications.html', cards=get_certification_cards())

@routes.route('/techstack')
def techstack():
    cards = get_techstack_cards()
    return render_template('pages/techstack.html', 
                         frontend_cards=cards['frontend'], 
                         backend_cards=cards['backend'], 
                         infra_cards=cards['infra'])

@routes.route('/irl')
def irl():
    slides = get_irl_slides(url_for)
    return render_template('pages/irl.html', slides=slides, carousel_id='irlCarousel')

@routes.route('/connect')
def connect():
    return render_template('pages/connect.html', cards=get_connect_cards())

@routes.route('/me2u-place')
def me2u_place_landing():
    """Dedicated route for me2u.place landing page"""
    return render_template('pages/me2u_place_landing.html')

