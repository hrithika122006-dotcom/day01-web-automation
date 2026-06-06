import pytest
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

@pytest.fixture
def api_client():
    session = requests.Session()
    session.base_url = BASE_URL
    yield session
    session.close()

@pytest.fixture
def sample_post():
    return {
        "title": "QA Test Post",
        "body": "This is automated test data",
        "userId": 1
    }