# DRY Carousel Implementation (Card Factory Pattern)

## Overview
Carousel implementation following the exact same pattern as `card_factory.py` - simple, direct, and DRY using `generate_carousel_slide()` helper functions.

## Pattern Match with Card Factory

### Card Factory Pattern:
```python
# card_factory.py
def get_certification_cards():
    return [
        generate_card_data(
            href="...",
            logo_src=url_for('static', filename='...'),
            title="...",
            subtitle="..."
        ),
        generate_card_data(...)
    ]
```

### Carousel Factory Pattern (Same Structure):
```python
# achievements.py  
def get_achievement_slides():
    return [
        generate_carousel_slide(
            src=url_for('static', filename='images/content/image.jpg'),
            alt="...",
            title="...",
            text="..."
        ),
        generate_carousel_slide(...)
    ]
```

## Key Benefits
- ✅ **Identical Pattern**: Same structure as `card_factory.py`
- ✅ **DRY Helper**: Uses `generate_carousel_slide()` like `generate_card_data()`
- ✅ **Simple & Direct**: No complex factory classes needed
- ✅ **Automatic Video Support**: Helper detects .mp4 files automatically
- ✅ **Consistent**: Same approach across cards and carousels

## File Structure
```
app/data/
├── card_factory.py      # Cards using generate_card_data()
├── achievements.py      # Carousels using generate_carousel_slide()
└── irl.py              # Carousels using generate_carousel_slide()
```

## Video/Image Support
The `generate_carousel_slide()` helper automatically detects video files (.mp4, .webm, etc.) and handles them appropriately, just like the card factory handles different logo types.

## Usage in Routes
```python
from app.data.achievements import get_achievement_slides
from app.data.card_factory import get_certification_cards

@app.route('/achievements')
def achievements():
    return render_template('achievements.html', 
                         carousel_slides=get_achievement_slides(),
                         cert_cards=get_certification_cards())
```

This approach maintains the same simplicity and directness as the card factory while supporting both images and videos seamlessly!
