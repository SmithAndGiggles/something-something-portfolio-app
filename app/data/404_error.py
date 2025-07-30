def get_404_error_content(url_for):
    return {
        "image_src": url_for('static', filename='images/errors/404.png'),
        "image_alt": "404 Page Not Found",
        "message": "Oops! The page you're looking for doesn't exist. Let's get you back on track."
    }
