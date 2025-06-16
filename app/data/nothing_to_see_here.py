def get_nothing_to_see_here_content(url_for):
    return {
        "image_src": url_for('static', filename='images/content/nothing-to-see-here.png'),
        "image_alt": "Nothing to see here",
        "message": "Nothing to see here"
    }
