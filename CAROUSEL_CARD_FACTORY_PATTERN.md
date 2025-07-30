# DRY Carousel Implementation (Card Factory Pattern)

## Overview
Carousel implementation following the exact same pattern as `card_factory.py` - simple, direct, and DRY using `generate_carousel_slide()` helper functions. Now consolidated into a single `carousel_factory.py` file like the card factory.

## Pattern Match with Card Factory

### Card Factory Pattern:
```python
# card_factory.py
def get_certification_cards():
    return [generate_card_data(...)]

def get_education_cards():
    return [generate_card_data(...)]

def get_frontend_tech_cards():
    return [generate_card_data(...)]
```

### Carousel Factory Pattern (Same Structure):
```python
# carousel_factory.py  
def get_achievement_slides():
    return [generate_carousel_slide(...)]

def get_irl_slides():
    return [generate_carousel_slide(...)]

# Future carousels can be added here
def get_projects_slides():
    return [generate_carousel_slide(...)]
```

## Key Benefits
- ✅ **Single File**: All carousels in one `carousel_factory.py` like card factory
- ✅ **Identical Pattern**: Same structure as `card_factory.py`
- ✅ **DRY Helper**: Uses `generate_carousel_slide()` like `generate_card_data()`
- ✅ **Video Support**: Automatically handles videos in `/static/videos/content/`
- ✅ **Scalable**: Add new carousel functions to same file

## File Structure
```
app/data/
├── card_factory.py      # All cards using generate_card_data()
└── carousel_factory.py  # All carousels using generate_carousel_slide()
```

## Video/Image Support
- **Images**: `/static/images/content/` and `/static/images/logos/`
- **Videos**: `/static/videos/content/` (automatically detected)
- The `generate_carousel_slide()` helper automatically detects video files (.mp4, .webm, etc.)

## Usage in Routes
```python
from app.data.carousel_factory import get_achievement_slides, get_irl_slides
from app.data.card_factory import get_certification_cards

@app.route('/achievements')
def achievements():
    return render_template('achievements.html', 
                         carousel_slides=get_achievement_slides(),
                         cert_cards=get_certification_cards())
```

This approach maintains the same simplicity and directness as the card factory while supporting both images and videos seamlessly!
