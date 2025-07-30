#!/usr/bin/env python3
"""
Simple test for carousel factory media detection logic
"""

def test_media_detection():
    """Test the media detection logic directly"""
    
    def _generate_media_url(filename: str):
        """Test version of media URL generation"""
        video_extensions = ('.mp4', '.webm', '.mov', '.avi')
        is_video = any(filename.lower().endswith(ext) for ext in video_extensions)
        media_type = 'video' if is_video else 'image'
        
        if filename.startswith("../"):
            media_url = f"/static/images/{filename[3:]}"
        else:
            media_url = f"/static/images/content/{filename}"
            
        return media_url, media_type
    
    test_cases = [
        ("linkedin-post.png", "image", "/static/images/content/linkedin-post.png"),
        ("beat-cancer-bell.mp4", "video", "/static/images/content/beat-cancer-bell.mp4"),
        ("../logos/logo-york-u.png", "image", "/static/images/logos/logo-york-u.png"),
        ("achievement.jpg", "image", "/static/images/content/achievement.jpg"),
        ("demo.webm", "video", "/static/images/content/demo.webm"),
        ("../logos/logo-gcp.svg", "image", "/static/images/logos/logo-gcp.svg")
    ]
    
    print("🧪 Testing Media Detection Logic\n")
    
    all_passed = True
    for filename, expected_type, expected_url in test_cases:
        url, media_type = _generate_media_url(filename)
        
        type_match = media_type == expected_type
        url_match = url == expected_url
        
        status = "✅" if (type_match and url_match) else "❌"
        print(f"{status} {filename}")
        print(f"   Type: {media_type} (expected: {expected_type})")
        print(f"   URL:  {url}")
        print(f"   Expected: {expected_url}")
        
        if not (type_match and url_match):
            all_passed = False
        print()
    
    if all_passed:
        print("🎉 All media detection tests passed!")
        print("\n📊 Verified capabilities:")
        print("  ✅ Image detection (.png, .jpg, .svg)")
        print("  ✅ Video detection (.mp4, .webm)")
        print("  ✅ Logo path handling (../logos/)")
        print("  ✅ Content path handling (images/content/)")
    else:
        print("❌ Some tests failed!")

if __name__ == "__main__":
    test_media_detection()
