"""
Personal Interest and Lifestyle Data Module
===========================================

Provides carousel slide data for "In Real Life" (IRL) content showcasing
personal interests, life experiences, and the human side beyond professional
achievements. This module creates authentic personal storytelling content.

Features:
- Personal milestone and life event documentation
- Community engagement and networking experiences
- Creative personal projects and meaningful symbolism
- Authentic storytelling with personal context
- Balance between professional and personal identity

Architecture:
- Slide-based data structure for carousel presentation
- Dynamic URL generation for personal photography
- Rich narrative content with personal storytelling
- Meaningful context and backstory for life events

Content Philosophy:
Demonstrates authenticity, resilience, and personal growth through
real-life experiences. Shows the complete person behind the professional
achievements, creating genuine human connection with portfolio visitors.

Template Integration:
Generates slide data for irl.html carousel with personal photography
and narrative content for authentic personal brand presentation.
"""

def get_irl_slides(url_for):
    """
    Generate personal interest and lifestyle carousel slides
    
    Creates authentic personal content showcasing life experiences,
    community involvement, and meaningful personal projects that
    demonstrate character, interests, and personal growth.
    
    Args:
        url_for: Flask URL generation function for dynamic image paths
        
    Returns:
        list: Personal slide contexts for carousel rendering
        
    Slide Content:
        - Community Engagement: Professional networking and learning experiences
        - Life Milestones: Significant personal achievements and celebrations
        - Creative Expression: Personal projects with meaningful symbolism
        
    Storytelling Approach:
        Each slide combines visual content with authentic narrative,
        providing context and personal meaning behind life experiences.
        Balances vulnerability with inspiration to create genuine connection.
        
    Content Philosophy:
        Shows resilience, creativity, and authentic human experience
        beyond professional accomplishments, creating complete personal brand.
    """
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
