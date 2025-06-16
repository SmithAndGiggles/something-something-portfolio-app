from flask import Blueprint, render_template, url_for
from .data.nothing_to_see_here import get_nothing_to_see_here_content

errors = Blueprint('errors', __name__)

# 404 or 401 → user tried to access something invalid or restricted
@errors.app_errorhandler(404)
@errors.app_errorhandler(401)
def not_found_error(error):
    content = get_nothing_to_see_here_content(url_for)
    return render_template(
        "nothing_to_see_here.html",
        image_src=content["image_src"],
        image_alt=content["image_alt"],
        message=content["message"]
    ), error.code

# 5xx → something failed on your server
@errors.app_errorhandler(500)
@errors.app_errorhandler(502)
@errors.app_errorhandler(503)
@errors.app_errorhandler(504)
def server_error(error):
    return render_template("nothing_to_see_here.html", message="Oops, something went wrong on our end."), error.code
