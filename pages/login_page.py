from selenium.webdriver.common.by import By

class LoginPage:
    URL = "https://the-internet.herokuapp.com/login"

    # Locators
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    SUCCESS_MSG = (By.CSS_SELECTOR, "div.flash.success")
    ERROR_MSG = (By.CSS_SELECTOR, "div.flash.error")
    LOGOUT_BUTTON = (By.CSS_SELECTOR, "a.button")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    def login(self, username, password):
        self.driver.find_element(*self.USERNAME).clear()
        self.driver.find_element(*self.USERNAME).send_keys(username)
        self.driver.find_element(*self.PASSWORD).clear()
        self.driver.find_element(*self.PASSWORD).send_keys(password)
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def get_success_message(self):
        return self.driver.find_element(*self.SUCCESS_MSG).text

    def get_error_message(self):
        return self.driver.find_element(*self.ERROR_MSG).text

    def logout(self):
        self.driver.find_element(*self.LOGOUT_BUTTON).click()
        