import pytest
from app import app

# Fixture to create a test client
@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home_route(client):
    """Test the home page '/' route"""
    response = client.get('/')
    assert response.status_code == 200
    # Optional: check content
    assert b"<!DOCTYPE html>" in response.data or b"<html" in response.data

def test_download_pdf_route(client):
    """Test the '/download-pdf' route"""
    response = client.get('/download-pdf')
    assert response.status_code == 200
    assert response.mimetype == 'application/pdf'
    # Optional: check if the PDF has content
    assert len(response.data) > 0
