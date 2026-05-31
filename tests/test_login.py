import pytest
from utils.driver_factory import get_driver
from pages.login_page import LoginPage

class TestLogin:

    def setup_method(self):
        self.driver = get_driver()
        self.login = LoginPage(self.driver)
        self.login.open()

    def teardown_method(self):
        self.driver.quit()

    def test_valid_login(self):
        self.login.login("tomsmith", "SuperSecretPassword!")
        message = self.login.get_success_message()
        assert "You logged into a secure area!" in message

    def test_invalid_password(self):
        self.login.login("tomsmith", "wrongpassword")
        message = self.login.get_error_message()
        assert "Your password is invalid!" in message

    def test_invalid_username(self):
        self.login.login("wronguser", "SuperSecretPassword!")
        message = self.login.get_error_message()
        assert "Your username is invalid!" in message

    def test_empty_fields(self):
        self.login.login("", "")
        message = self.login.get_error_message()
        assert "Your username is invalid!" in message

    def test_logout(self):
        self.login.login("tomsmith", "SuperSecretPassword!")
        self.login.logout()
        assert "login" in self.driver.current_url