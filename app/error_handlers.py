from flask import Blueprint, render_template

errors = Blueprint('errors', __name__)

# 404 or 401 → user tried to access something invalid or restricted
@errors.app_errorhandler(404)
@errors.app_errorhandler(401)
def not_found_error(error):
    return render_template("nothing_to_see_here.html", message="Nothing to see here"), error.code

# 5xx → something failed on your server
@errors.app_errorhandler(500)
@errors.app_errorhandler(502)
@errors.app_errorhandler(503)
@errors.app_errorhandler(504)
def server_error(error):
    return render_template("nothing_to_see_here.html", message="Oops, something went wrong on our end."), error.code
