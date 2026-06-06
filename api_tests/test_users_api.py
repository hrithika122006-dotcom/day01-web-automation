import requests
import pytest

BASE_URL = "https://jsonplaceholder.typicode.com"

class TestUsersAPI:

    def test_get_all_users(self, api_client):
        response = api_client.get(f"{BASE_URL}/users")
        assert response.status_code == 200
        assert len(response.json()) == 10

    def test_get_single_user(self, api_client):
        response = api_client.get(f"{BASE_URL}/users/1")
        data = response.json()
        assert response.status_code == 200
        assert data["id"] == 1
        assert data["name"] != ""
        assert data["email"] != ""

    def test_create_post_with_fixture(
        self, api_client, sample_post
    ):
        response = api_client.post(
            f"{BASE_URL}/posts",
            json=sample_post
        )
        data = response.json()
        assert response.status_code == 201
        assert data["title"] == sample_post["title"]

    def test_response_time(self, api_client):
        response = api_client.get(f"{BASE_URL}/users")
        assert response.elapsed.total_seconds() < 3