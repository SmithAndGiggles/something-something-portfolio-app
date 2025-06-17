def get_500_error_content(url_for):
    return {
        "image_src": url_for('static', filename='images/errors/500.png'),
        "image_alt": "500 Internal Server Error",
        "message": "It's nothing you did, it's something on our end. Please try again later"
    }
