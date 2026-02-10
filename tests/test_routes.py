"""Tests for application routes."""
import json

def test_home_page(client):
    """Test that the home page loads successfully."""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Welcome to Azure Web App!' in response.data
    assert b'Python 3.14 | Linux' in response.data

def test_health_endpoint(client):
    """Test that the health check endpoint returns correct status."""
    response = client.get('/health')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['status'] == 'healthy'

def test_404_error(client):
    """Test that a 404 error is returned for non-existent routes."""
    response = client.get('/nonexistent')
    assert response.status_code == 404
