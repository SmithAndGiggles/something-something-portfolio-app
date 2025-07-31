"""
Test configuration and fixtures for the portfolio application.
"""

import pytest
import tempfile
import os
from app import create_app


@pytest.fixture
def app():
    """Create and configure a new app instance for each test."""
    # Create a temporary file to isolate the database for each test
    db_fd, db_path = tempfile.mkstemp()

    app = create_app({"TESTING": True, "SECRET_KEY": "test-secret-key"})

    with app.app_context():
        yield app

    os.close(db_fd)
    os.unlink(db_path)


@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()


@pytest.fixture
def runner(app):
    """A test runner for the app's Click commands."""
    return app.test_cli_runner()


class AuthActions:
    """Helper class for authentication actions in tests."""

    def __init__(self, client):
        self._client = client

    def login(self, username="test", password="test"):
        """Login with test credentials."""
        return self._client.post(
            "/auth/login", data={"username": username, "password": password}
        )

    def logout(self):
        """Logout current user."""
        return self._client.get("/auth/logout")


@pytest.fixture
def auth(client):
    """Authentication helper fixture."""
    return AuthActions(client)
