from selenium.webdriver.common.by import By
from framework.pages.base_page import BasePage
from framework.config.config import Config

class LoginPage(BasePage):
    
    # Locators
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    SUCCESS_MSG = (By.CSS_SELECTOR, "div.flash.success")
    ERROR_MSG = (By.CSS_SELECTOR, "div.flash.error")
    LOGOUT_BUTTON = (By.CSS_SELECTOR, "a.button")

    def open(self):
        self.driver.get(Config.LOGIN_URL)

    def login(self, username, password):
        self.type_text(self.USERNAME, username)
        self.type_text(self.PASSWORD, password)
        self.click(self.LOGIN_BUTTON)

    def get_success_message(self):
        return self.get_text(self.SUCCESS_MSG)

    def get_error_message(self):
        return self.get_text(self.ERROR_MSG)

    def logout(self):
        self.click(self.LOGOUT_BUTTON)

    def is_login_page(self):
        return self.is_visible(self.LOGIN_BUTTON)