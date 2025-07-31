# filepath: something-something-portfolio-app/app/data/carousel_factory.py

from flask import url_for
from app.utils.template_helpers import generate_carousel_slide, generate_source_link
from .constants import EXTERNAL_URLS


# DRY helper function for creating carousel slides with consistent patterns
def _create_slide(
    media_path, alt, title, text, highlight=None, sources1=None, sources2=None
):
    """
    DRY helper for generating carousel slides with consistent structure.
    Automatically handles image vs video paths and URL generation.
    """
    # Determine if it's a video file and set appropriate path
    video_extensions = (".mp4", ".webm", ".mov", ".avi")
    is_video = any(media_path.lower().endswith(ext) for ext in video_extensions)

    if media_path.startswith("../"):
        # Logo path
        src = url_for("static", filename=f"images/{media_path[3:]}")
    elif is_video:
        # Video content path
        src = url_for("static", filename=f"videos/content/{media_path}")
    else:
        # Image content path
        src = url_for("static", filename=f"images/content/{media_path}")

    return generate_carousel_slide(
        src=src,
        alt=alt,
        title=title,
        text=text,
        highlight=highlight,
        sources1=sources1,
        sources2=sources2,
    )


def _create_source_links(sources_data):
    """DRY helper for creating source link arrays"""
    if not sources_data:
        return None
    return [generate_source_link(href, text) for href, text in sources_data]


# Predefined common sources for reusability using constants
COMMON_SOURCES = {
    "cancer_society": (EXTERNAL_URLS["cancer_society"], "Canadian Cancer Society"),
    "alberta_health": (EXTERNAL_URLS["alberta_health_apl"], "Alberta Health Services"),
    "leukemia_society": (
        EXTERNAL_URLS["leukemia_society"],
        "Leukemia & Lymphoma Society",
    ),
    "biomedcentral": (EXTERNAL_URLS["biomedcentral"], "BioMed Central"),
    "donkey_sanctuary": (EXTERNAL_URLS["donkey_sanctuary"], "More about the DSC"),
    "york_ace": (EXTERNAL_URLS["york_ace_article"], "Read full article here"),
}


def get_achievement_slides():
    """
    Centralized achievement carousel data using DRY helpers.
    """
    linkedin_post_url = "https://www.linkedin.com/feed/update/urn:li:activity:7285343139874140160?updateEntityUrn=urn%3Ali%3Afs_updateV2%3A%28urn%3Ali%3Aactivity%3A7285343139874140160%2CFEED_DETAIL%2CEMPTY%2CDEFAULT%2Cfalse%29"

    return [
        _create_slide(
            "linkedin-onix-genai-post.png",
            "LinkedIn Onix GenAI Post",
            "LinkedIn Onix GenAI Post",
            "We're proud to announce that Onix has achieved the Google Cloud Generative AI – Services Specialization as part of the Google Cloud Partner Advantage program! This recognition highlights our expertise in designing, deploying, and scaling cutting-edge generative AI solutions that drive real business transformation.\n\nOnix now holds 8 Google Cloud specializations—demonstrating our commitment to delivering innovative solutions that help businesses harness the power of hashtag#AI to improve productivity, efficiency, and creativity.\n\nAnd a huge 'thank you' to the team to helped bring this across the finish line: Steve Berrey Dan Ehlers Sean Gilley Ricardo de Andrade 🌎 Doug Hayden ♻️ James Vandermost Alan Smith Ronald deLara Kyle Clark Carolina (Ninna) Sampaio Paula Mannarino Dr. Ramnish Singh",
            sources1=_create_source_links(
                [(linkedin_post_url, "Full LinkedIn post here")]
            ),
        ),
        _create_slide(
            "beat-cancer-bell.mp4",
            "Beat cancer bell ringing ceremony",
            "Acute Promyelocytic Leukemia (APL) Journey",
            "Acute promyelocytic leukemia (APL) is a rare subtype of acute myeloid leukemia (AML) in Canada. Based on national statistics, around 1,160 Canadians were diagnosed with AML in 2019, and with APL making up approximately 5–10% of these cases, it's estimated that 58 to 116 new APL cases occur each year.",
            highlight="While APL is rare, it's one of the most treatable types of leukemia. Thanks to modern therapies, remission rates exceed 90%, and 5-year overall survival ranges from 80% to 90%, giving patients real hope for recovery.",
            sources1=_create_source_links(
                [COMMON_SOURCES["cancer_society"], COMMON_SOURCES["alberta_health"]]
            ),
            sources2=_create_source_links(
                [
                    COMMON_SOURCES["alberta_health"],
                    COMMON_SOURCES["leukemia_society"],
                    COMMON_SOURCES["biomedcentral"],
                ]
            ),
        ),
        _create_slide(
            "donkey-santuary-5k-alan.jpg",
            "Alan completing 5K run at Donkey Sanctuary",
            "Donkey Sanctuary 5K",
            "I underwent intense chemotherapy treatments—six days a week, four weeks on and four weeks off—after a near-death experience in the ICU shortly following my diagnosis. Between October 2022 and June 2023, the incredible teams at Princess Margaret and Mount Sinai worked tirelessly to help me reach remission.\n\nGetting through this experience remains one of the most meaningful achievements of my life. Here's a photo from a 5K run I completed at The Donkey Sanctuary of Canada. After spending weeks unable to walk or even go to the washroom without help, crossing that finish line meant so much more than a race—it was proof of progress, resilience, and how far I've come.",
            sources1=_create_source_links([COMMON_SOURCES["donkey_sanctuary"]]),
        ),
        _create_slide(
            "../logos/logo-york-u.png",
            "York University ACE program logo",
            "York University ACE Graduate and Scholarship Recipient",
            "On Tuesday, May 31, 2005, the York University/Westview Partnership and the York University Faculty Association Trust co-hosted a gala celebration honouring 25 graduates of York's innovative Advance Credit Experience (ACE) Project. The program provides an opportunity for \"at risk\" secondary students at Toronto's Westview Centennial Secondary School and Emery Collegiate Institute to gain firsthand exposure to post-secondary education before they graduate from high school.\n\nThis year's top four graduates of ACE are eligible for scholarships to York worth up to $5,000. Last year's scholarship recipients are: Mohammed Ahmad, Claudine Reid, Ladonna Taylor and Alan Smith.",
            sources1=_create_source_links([COMMON_SOURCES["york_ace"]]),
        ),
    ]


def get_irl_slides():
    """
    Centralized IRL carousel data using DRY helpers.
    """
    return [
        _create_slide(
            "ingy-dot-net.jpg",
            "Ingy döt Net at a meetup",
            "Met the creator of YAML Script",
            "Met the creator of YAML at the Toronto Enterprise DevOps Group (Meetup). Learned how YS (YAML Script) brings real programming features right into YAML files, like variables, functions, and reusing code, while keeping everything readable and simple. Worth checking out if you ever work with YAML configs: yamlscript.org\n\nAbout the group: Toronto Enterprise DevOps Group is for people in the GTA interested in DevOps practices, automation, and modern infrastructure. All experience levels welcome.",
        ),
        _create_slide(
            "valley-of-fire-wedding.jpg",
            "Wedding photo at Valley of Fire",
            "Valley of Fire Wedding",
            "After being together for 13 years (2009–2022), we finally tied the knot! We both love visiting Vegas and years ago, we drove out to the Valley of Fire and thought it would be amazing to get married in 'Vegas.' In 2022, we made it happen with a beautiful ceremony surrounded by the stunning red rocks.",
        ),
        _create_slide(
            "pacman-tattoo.jpg",
            "Pacman tattoo",
            "Pacman Tattoo",
            "I have a few 'nerdy' tattoos, and Pacman is a fun addition to the collection. The circular scar on my arm is from a PICC line used during chemo, but I decided to give it a new meaning. Now, Pacman lives there—turning a medical reminder into something playful and positive.",
        ),
    ]
