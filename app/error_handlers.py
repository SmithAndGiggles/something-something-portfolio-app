from flask import Blueprint, render_template, url_for
import importlib

error_400 = importlib.import_module('.data.400_error', __package__)
error_404 = importlib.import_module('.data.404_error', __package__)
error_500 = importlib.import_module('.data.500_error', __package__)

errors = Blueprint('errors', __name__)

@errors.app_errorhandler(400)
def bad_request_error(error):
    content = error_400.get_400_error_content(url_for)
    return render_template(
        "400-page.html",
        image_src=content["image_src"],
        image_alt=content["image_alt"],
        message=content["message"]
    ), 400

@errors.app_errorhandler(404)
def not_found_error(error):
    content = error_404.get_400_error_content(url_for)
    return render_template(
        "404-page.html",
        image_src=content["image_src"],
        image_alt=content["image_alt"],
        message=content["message"]
    ), 404

@errors.app_errorhandler(500)
def internal_server_error(error):
    content = error_500.get_500_error_content(url_for)
    return render_template(
        "500-page.html",
        image_src=content["image_src"],
        image_alt=content["image_alt"],
        message=content["message"]
    ), 500


