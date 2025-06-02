# app/__init__.py
from flask import Flask
from .routes import routes
from .error_handlers import errors

def create_app():
    app = Flask(__name__)
    app.register_blueprint(routes)
    app.register_blueprint(errors)
    return app

