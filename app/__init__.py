# app/__init__.py
from flask import Flask
from .routes import routes
from .error_handlers import errors
from .context_processor import inject_nav_links, inject_footer_links
from .config import apply_config

def create_app():
    app = Flask(__name__)
    apply_config(app)
    app.register_blueprint(routes)
    app.register_blueprint(errors)
    app.context_processor(inject_nav_links)
    app.context_processor(inject_footer_links)
    return app

