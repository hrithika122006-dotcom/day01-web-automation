import requests
import pytest

BASE_URL = "https://jsonplaceholder.typicode.com"

class TestPostsAPI:

    def test_get_single_post_status_code(self):
        response = requests.get(f"{BASE_URL}/posts/1")
        assert response.status_code == 200

    def test_get_single_post_data(self):
        response = requests.get(f"{BASE_URL}/posts/1")
        data = response.json()
        assert data["id"] == 1
        assert data["userId"] == 1
        assert data["title"] != ""
        assert data["body"] != ""

    def test_get_all_posts(self):
        response = requests.get(f"{BASE_URL}/posts")
        data = response.json()
        assert response.status_code == 200
        assert len(data) == 100

    def test_create_post(self):
        new_post = {
            "title": "QA Test Post",
            "body": "This is a test",
            "userId": 1
        }
        response = requests.post(f"{BASE_URL}/posts", json=new_post)
        data = response.json()
        assert response.status_code == 201
        assert data["title"] == "QA Test Post"

    def test_invalid_post_returns_404(self):
        response = requests.get(f"{BASE_URL}/posts/99999")
        assert response.status_code == 404


    def test_get_user(self):
        response = requests.get(f"{BASE_URL}/users/1")
        data = response.json()
        assert response.status_code == 200
        assert data["id"] == 1
        assert data["email"] != ""

    def test_update_post(self):
        updated = {"title": "Updated Title"}
        response = requests.patch(
            f"{BASE_URL}/posts/1", json=updated
        )
        assert response.status_code == 200
        assert response.json()["title"] == "Updated Title"

    def test_delete_post(self):
        response = requests.delete(f"{BASE_URL}/posts/1")
        assert response.status_code == 200 