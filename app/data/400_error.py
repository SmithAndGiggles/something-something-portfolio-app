def get_400_error_content(url_for):
    return {
        "image_src": url_for("static", filename="images/errors/400.png"),
        "image_alt": "400 Bad Request",
        "message": "Sorry, there was an issue with your request. Please check and try again.",
    }
