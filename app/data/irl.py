def get_irl_slides(url_for):
    return [
        {
            "src": url_for('static', filename='images/content/ingy-dot-net.jpg'),
            "alt": "Ingy döt Net at a meetup",
            "title": "Met the creator of YAML Script",
            "text": "Met the creator of YAML at the Toronto Enterprise DevOps Group (Meetup). Learned how YS (YAML Script) brings real programming features right into YAML files, like variables, functions, and reusing code, while keeping everything readable and simple. Worth checking out if you ever work with YAML configs: yamlscript.org\n\nAbout the group: Toronto Enterprise DevOps Group is for people in the GTA interested in DevOps practices, automation, and modern infrastructure. All experience levels welcome."
        },
        {
            "src": url_for('static', filename='images/content/valley-of-fire-wedding.jpg'),
            "alt": "Wedding photo at Valley of Fire",
            "title": "Valley of Fire Wedding",
            "text": "After being together for 13 years (2009–2022), we finally tied the knot! We both love visiting Vegas and years ago, we drove out to the Valley of Fire and thought it would be amazing to get married in 'Vegas.' In 2022, we made it happen with a beautiful ceremony surrounded by the stunning red rocks."
        },
        {
            "src": url_for('static', filename='images/content/pacman-tattoo.jpg'),
            "alt": "Pacman tattoo",
            "title": "Pacman Tattoo",
            "text": "I have a few 'nerdy' tattoos, and Pacman is a fun addition to the collection. The circular scar on my arm is from a PICC line used during chemo, but I decided to give it a new meaning. Now, Pacman lives there—turning a medical reminder into something playful and positive."
        }
    ]
