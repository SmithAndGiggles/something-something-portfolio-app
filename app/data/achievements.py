# app/data/achievements.py

def get_achievement_slides(url_for):
    return [
        {
            'src': url_for('static', filename='images/content/beat-cancer-bell.mp4'),
            'alt': 'First slide',
            'title': 'Acute Promyelocytic Leukemia (APL) Journey',
            'text': (
                'Acute promyelocytic leukemia (APL) is a rare subtype of acute myeloid leukemia (AML) in Canada. Based on national statistics, around 1,160 Canadians were diagnosed with AML in 2019, and with APL making up approximately 5–10% of these cases, it\'s estimated that 58 to 116 new APL cases occur each year. While APL is rare, it\'s one of the most treatable types of leukemia. Thanks to modern therapies, remission rates exceed 90%, and 5-year overall survival ranges from 80% to 90%, giving patients real hope for recovery.'
            )
        },
        {
            'src': url_for('static', filename='images/logos/logo-york-u.png'),
            'alt': 'Second slide',
            'title': 'York University ACE Graduate and Scholarship Recipient',
            'text': (
                'On Tuesday, May 31, 2005, the York University/Westview Partnership and the York University Faculty Association Trust co-hosted a gala celebration honouring 25 graduates of York\'s innovative Advance Credit Experience (ACE) Project. The program provides an opportunity for "at risk" secondary students at Toronto\'s Westview Centennial Secondary School and Emery Collegiate Institute to gain firsthand exposure to post-secondary education before they graduate from high school. This year\'s top four graduates of ACE are eligible for scholarships to York worth up to $5,000.'
            )
        },
        {
            'src': url_for('static', filename='images/content/linkedin-onix-genai-post.png'),
            'alt': 'LinkedIn Onix GenAI Post',
            'title': 'LinkedIn Onix GenAI Post',
            'text': 'See the full LinkedIn post about Onix GenAI and my work in the field.'
        },
        {
            'src': url_for('static', filename='images/content/donkey-santuary-5k-alan.jpg'),
            'alt': 'Third slide',
            'title': 'Donkey Sanctuary 5K',
            'text': (
                'I underwent intense chemotherapy treatments—six days a week, four weeks on and four weeks off—after a near-death experience in the ICU shortly following my diagnosis. Between October 2022 and June 2023, the incredible teams at Princess Margaret and Mount Sinai worked tirelessly to help me reach remission. Getting through this experience remains one of the most meaningful achievements of my life. Here\'s a photo from a 5K run I completed at The Donkey Sanctuary of Canada. After spending weeks unable to walk or even go to the washroom without help, crossing that finish line meant so much more than a race—it was proof of progress, resilience, and how far I\'ve come.'
            )
        }
    ]
