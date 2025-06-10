# app/data/achievements.py

def get_achievement_slides(url_for):
    return [
        {
            'src': url_for('static', filename='images/logos/logo-alan.png'),
            'alt': 'First slide',
            'title': 'Achievement One',
            'text': 'Description for achievement one.'
        },
        {
            'src': url_for('static', filename='images/logos/logo-york-u.png'),
            'alt': 'Second slide',
            'title': 'Achievement Two',
            'text': 'Description for achievement two.'
        },
        {
            'src': url_for('static', filename='images/content/linkedin-onix-genai-post.png'),
            'alt': 'Second slide',
            'title': 'Achievement Two',
            'text': 'Description for achievement two.'
        },
        {
            'src': url_for('static', filename='images/content/donkey-santuary-5k-alan.jpg'),
            'alt': 'Third slide',
            'title': 'Achievement Three',
            'text': 'Description for achievement three.'
        }
    ]
