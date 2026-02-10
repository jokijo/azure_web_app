"""Tests for application factory and configuration."""
from app import create_app

def test_create_app():
    """Test that the application factory creates an app instance."""
    app = create_app()
    assert app is not None
    assert app.name == 'app'

def test_app_has_blueprints():
    """Test that the app has registered blueprints."""
    app = create_app()
    assert 'main' in app.blueprints
