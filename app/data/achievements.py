# app/data/achievements.py

def get_achievement_slides(url_for):
    return [
        {
            'src': url_for('static', filename='images/content/beat-cancer-bell.mp4'),
            'alt': 'First slide',
            'title': 'Acute Promyelocytic Leukemia (APL) Journey',
            'text': (
                'Acute promyelocytic leukemia (APL) is a rare subtype of acute myeloid leukemia (AML) in Canada. Based on national statistics, around 1,160 Canadians were diagnosed with AML in 2019, and with APL making up approximately 5–10% of these cases, it\'s estimated that 58 to 116 new APL cases occur each year.'
            ),
            'highlight': (
                "While APL is rare, it's one of the most treatable types of leukemia. Thanks to modern therapies, remission rates exceed 90%, and 5-year overall survival ranges from 80% to 90%, giving patients real hope for recovery."
            ),
            'sources1': [
                {'href': 'https://cancer.ca/en/cancer-information/cancer-types/acute-myeloid-leukemia-aml/statistics', 'text': 'Canadian Cancer Society'},
                {'href': 'https://www.albertahealthservices.ca/assets/info/hp/cancer/if-hp-cancer-guide-lyhe008-apl.pdf', 'text': 'Alberta Health Services'}
            ],
            'sources2': [
                {'href': 'https://www.albertahealthservices.ca/assets/info/hp/cancer/if-hp-cancer-guide-lyhe008-apl.pdf', 'text': 'Alberta Health Services'},
                {'href': 'https://www.bloodcancers.ca/sites/default/files/2023-02/LSC22103_LLS1001E_AML%20Brochure_E_m4.pdf', 'text': 'Leukemia & Lymphoma Society'},
                {'href': 'https://bmccancer.biomedcentral.com/articles/10.1186/s12885-023-10612-z', 'text': 'BioMed Central'}
            ]
        },
        {
            'src': url_for('static', filename='images/logos/logo-york-u.png'),
            'alt': 'Second slide',
            'title': 'York University ACE Graduate and Scholarship Recipient',
            'text': (
                "On Tuesday, May 31, 2005, the York University/Westview Partnership and the York University Faculty Association Trust co-hosted a gala celebration honouring 25 graduates of York's innovative Advance Credit Experience (ACE) Project. The program provides an opportunity for \"at risk\" secondary students at Toronto's Westview Centennial Secondary School and Emery Collegiate Institute to gain firsthand exposure to post-secondary education before they graduate from high school.\n\nThis year’s top four graduates of ACE are eligible for scholarships to York worth up to $5,000. Last year’s scholarship recipients are: Mohammed Ahmad, Claudine Reid, Ladonna Taylor and Alan Smith."
            ),
            'sources1': [
                {'href': 'https://news.yorku.ca/2005/05/30/york-u-honours-2005-ace-graduates-with-5000-scholarships/', 'text': 'Read full article here'}
            ]
        },
        {
            'src': url_for('static', filename='images/content/linkedin-onix-genai-post.png'),
            'alt': 'LinkedIn Onix GenAI Post',
            'title': 'LinkedIn Onix GenAI Post',
            'text': (
                "We're proud to announce that Onix has achieved the Google Cloud Generative AI – Services Specialization as part of the Google Cloud Partner Advantage program! This recognition highlights our expertise in designing, deploying, and scaling cutting-edge generative AI solutions that drive real business transformation.\n\nOnix now holds 8 Google Cloud specializations—demonstrating our commitment to delivering innovative solutions that help businesses harness the power of hashtag#AI to improve productivity, efficiency, and creativity.\n\nAnd a huge 'thank you' to the team to helped bring this across the finish line: Steve Berrey Dan Ehlers Sean Gilley Ricardo de Andrade 🌎 Doug Hayden ♻️ James Vandermost Alan Smith Ronald deLara Kyle Clark Carolina (Ninna) Sampaio Paula Mannarino Dr. Ramnish Singh"
            ),
            'team_links': {
                'Alan Smith': 'https://www.linkedin.com/in/alan-r-smith'
            },
            'sources1': [
                {'href': 'https://www.linkedin.com/feed/update/urn:li:activity:7285343139874140160?updateEntityUrn=urn%3Ali%3Afs_updateV2%3A%28urn%3Ali%3Aactivity%3A7285343139874140160%2CFEED_DETAIL%2CEMPTY%2CDEFAULT%2Cfalse%29', 'text': 'Full LinkedIn post here'}
            ]
        },
        {
            'src': url_for('static', filename='images/content/donkey-santuary-5k-alan.jpg'),
            'alt': 'Third slide',
            'title': 'Donkey Sanctuary 5K',
            'text': (
                "I underwent intense chemotherapy treatments—six days a week, four weeks on and four weeks off—after a near-death experience in the ICU shortly following my diagnosis. Between October 2022 and June 2023, the incredible teams at Princess Margaret and Mount Sinai worked tirelessly to help me reach remission.\n\nGetting through this experience remains one of the most meaningful achievements of my life. Here's a photo from a 5K run I completed at The Donkey Sanctuary of Canada. After spending weeks unable to walk or even go to the washroom without help, crossing that finish line meant so much more than a race—it was proof of progress, resilience, and how far I've come."
            ),
            'sources1': [
                {'href': 'https://www.thedonkeysanctuary.ca', 'text': 'More about the DSC'}
            ]
        }
    ]
