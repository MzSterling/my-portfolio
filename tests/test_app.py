# tests/test_app.py
import pytest
from app import app

# Use Flask's test client
@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home_route(client):
    """Test the home page returns 200"""
    response = client.get('/')
    assert response.status_code == 200

def test_download_pdf_route(client):
    """Test the PDF download route returns a PDF"""
    response = client.get('/download-pdf')
    assert response.status_code == 200
    assert response.headers['Content-Type'] == 'application/pdf'
