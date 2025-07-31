def get_500_error_content(url_for):
    return {
        "image_src": url_for("static", filename="images/errors/500.png"),
        "image_alt": "500 Internal Server Error",
        "message": "Oops! Something went wrong on our end. We're working to fix it. Please try again later.",
    }
