def get_400_error_content(url_for):
    return {
        "image_src": url_for('static', filename='images/errors/400.png'),
        "image_alt": "400 Bad Request",
        "message": "400 Bad Request\nThe request could not be understood by the server due to malformed syntax or invalid input."
    }
