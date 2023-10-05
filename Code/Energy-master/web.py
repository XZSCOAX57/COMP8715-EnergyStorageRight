from flask import Blueprint, render_template

web_bp = Blueprint('', __name__)


# Different urls stand for different pages
@web_bp.route('/')
def index():
    return render_template('index.html')


@web_bp.route('/about')
def about():
    return render_template('about.html')


@web_bp.route('/contact')
def contact():
    return render_template('contact.html')


@web_bp.route('/news')
def news():
    return render_template('news.html')


@web_bp.route('/faq')
def faq():
    return render_template('faq.html')


@web_bp.route('/tutorial')
def tutorial():
    return render_template('tutorial.html')


@web_bp.route('/opensolar')
def openSolar():
    return render_template('openSolar.html')


@web_bp.route('/panelboard')
def panelBoard():
    return render_template('panelboard.html')


@web_bp.route('/map_new')
def map_new():
    return render_template('map_new.html')
