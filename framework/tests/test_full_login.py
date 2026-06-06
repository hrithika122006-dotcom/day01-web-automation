import pytest
from framework.tests.base_test import BaseTest
from framework.pages.login_page import LoginPage
from framework.config.config import Config

class TestFullLogin(BaseTest):

    def setup_method(self):
        super().setup_method()
        self.login_page = LoginPage(self.driver)
        self.login_page.open()

    def test_valid_login(self):
        self.login_page.login(
            Config.VALID_USERNAME,
            Config.VALID_PASSWORD
        )
        message = self.login_page.get_success_message()
        assert "You logged into a secure area!" in message

    def test_invalid_login(self):
        self.login_page.login("wronguser", "wrongpass")
        message = self.login_page.get_error_message()
        assert "invalid" in message.lower()

    def test_logout_flow(self):
        self.login_page.login(
            Config.VALID_USERNAME,
            Config.VALID_PASSWORD
        )
        self.login_page.logout()
        assert self.login_page.is_login_page()

    def test_empty_credentials(self):
        self.login_page.login("", "")
        message = self.login_page.get_error_message()
        assert "invalid" in message.lower()