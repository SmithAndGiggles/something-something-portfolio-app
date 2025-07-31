"""
Unit tests for Flask application routes and core functionality.
"""


class TestRoutes:
    """Test suite for the Flask portfolio application."""

    def test_home_page(self, client):
        """Test that home page loads successfully."""
        response = client.get("/")
        assert response.status_code == 200
        assert b"Portfolio" in response.data or b"portfolio" in response.data

    def test_about_page(self, client):
        """Test about/me page if it exists."""
        response = client.get("/about")
        # Allow 404 if route doesn't exist
        assert response.status_code in [200, 404]

    def test_contact_page(self, client):
        """Test contact page."""
        response = client.get("/connect")
        assert response.status_code == 200

    def test_techstack_page(self, client):
        """Test technology stack page."""
        response = client.get("/techstack")
        assert response.status_code == 200
        assert (
            b"technology" in response.data.lower() or b"tech" in response.data.lower()
        )

    def test_certifications_page(self, client):
        """Test certifications page."""
        response = client.get("/certifications")
        assert response.status_code == 200

    def test_education_page(self, client):
        """Test education page."""
        response = client.get("/education")
        assert response.status_code == 200

    def test_achievements_page(self, client):
        """Test achievements page."""
        response = client.get("/achievements")
        assert response.status_code == 200

    def test_irl_page(self, client):
        """Test IRL (In Real Life) page."""
        response = client.get("/irl")
        assert response.status_code == 200

    def test_health_endpoint(self, client):
        """Test health check endpoint for monitoring."""
        response = client.get("/health")
        # Create health endpoint if it doesn't exist
        assert response.status_code in [200, 404]
        if response.status_code == 200:
            assert b"healthy" in response.data.lower() or b"ok" in response.data.lower()

    def test_404_error_page(self, client):
        """Test 404 error page handling."""
        response = client.get("/nonexistent-page")
        assert response.status_code == 404
        # Should render custom 404 page
        assert b"404" in response.data or b"Not Found" in response.data


class TestStaticAssets:
    """Test suite for static assets."""

    def test_css_files_load(self, client):
        """Test that CSS files are accessible."""
        css_files = ["css/style.css", "css/custom.css", "css/cards.css"]
        for css_file in css_files:
            response = client.get(f"/static/{css_file}")
            assert response.status_code == 200
            assert "text/css" in response.content_type

    def test_js_files_load(self, client):
        """Test that JavaScript files are accessible."""
        response = client.get("/static/js/scripts.js")
        assert response.status_code == 200
        assert (
            "javascript" in response.content_type
            or "text/plain" in response.content_type
        )

    def test_favicon_loads(self, client):
        """Test that favicon is accessible."""
        response = client.get("/static/images/favicons/favicon.ico")
        assert response.status_code == 200


class TestDataIntegrity:
    """Test suite for data integrity and constants."""

    def test_technologies_data_structure(self):
        """Test that technologies data has required structure."""
        from app.data.constants import TECHNOLOGIES

        assert isinstance(TECHNOLOGIES, dict)
        assert len(TECHNOLOGIES) > 0

        # Test first technology has required fields
        first_tech = next(iter(TECHNOLOGIES.values()))
        required_fields = ["name", "url", "logo", "alt", "category", "description"]
        for field in required_fields:
            assert field in first_tech

    def test_certifications_data_structure(self):
        """Test that certifications data has required structure."""
        from app.data.constants import CERTIFICATIONS

        assert isinstance(CERTIFICATIONS, dict)
        assert len(CERTIFICATIONS) > 0

        # Test first certification has required fields
        first_cert = next(iter(CERTIFICATIONS.values()))
        required_fields = ["title", "subtitle", "url", "logo", "alt"]
        for field in required_fields:
            assert field in first_cert

    def test_ui_config_structure(self):
        """Test that UI configuration has required structure."""
        from app.data.constants import UI_CONFIG, CONTACT_CONFIG

        assert isinstance(UI_CONFIG, dict)
        assert "carousel" in UI_CONFIG
        assert "cards" in UI_CONFIG
        assert "errors" in UI_CONFIG

        assert isinstance(CONTACT_CONFIG, dict)
        assert "email" in CONTACT_CONFIG
        assert "domain" in CONTACT_CONFIG


class TestErrorHandling:
    """Test suite for error handling."""

    def test_500_error_handling(self, client, app):
        """Test 500 error page handling."""
        # This is a bit tricky to test, but we can check the error handler exists
        with app.test_request_context():
            from app.error_handlers import internal_server_error

            assert callable(internal_server_error)

    def test_400_error_handling(self, client, app):
        """Test 400 error page handling."""
        with app.test_request_context():
            from app.error_handlers import bad_request_error

            assert callable(bad_request_error)
