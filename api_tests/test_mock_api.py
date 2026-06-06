import requests
import responses
import pytest

BASE_URL = "https://jsonplaceholder.typicode.com"

class TestMockAPI:

    @responses.activate
    def test_mock_get_post(self):
        # Set up fake response
        responses.add(
            responses.GET,
            f"{BASE_URL}/posts/1",
            json={
                "id": 1,
                "title": "Mocked Post",
                "body": "This is a mocked response",
                "userId": 1
            },
            status=200
        )

        # Make the request
        response = requests.get(f"{BASE_URL}/posts/1")
        data = response.json()

        # Assert
        assert response.status_code == 200
        assert data["title"] == "Mocked Post"

    @responses.activate
    def test_mock_server_error(self):
        # Simulate server error
        responses.add(
            responses.GET,
            f"{BASE_URL}/posts/1",
            json={"error": "Internal Server Error"},
            status=500
        )

        response = requests.get(f"{BASE_URL}/posts/1")
        assert response.status_code == 500

    @responses.activate
    def test_mock_payment_declined(self):
        # Simulate payment API declining
        responses.add(
            responses.POST,
            "https://fake-payment-api.com/pay",
            json={
                "status": "declined",
                "reason": "insufficient funds"
            },
            status=402
        )

        response = requests.post(
            "https://fake-payment-api.com/pay",
            json={"amount": 1000}
        )
        data = response.json()

        assert response.status_code == 402
        assert data["status"] == "declined"
        assert data["reason"] == "insufficient funds"

    @responses.activate
    def test_mock_slow_api_timeout(self):
        # Simulate API being unavailable
        responses.add(
            responses.GET,
            f"{BASE_URL}/posts",
            json={"error": "Service Unavailable"},
            status=503
        )

        response = requests.get(f"{BASE_URL}/posts")
        assert response.status_code == 503