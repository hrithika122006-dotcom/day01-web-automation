import pytest
import csv
from utils.driver_factory import get_driver
from pages.login_page import LoginPage

def load_login_data():
    test_cases = []
    with open("test_data/login_data.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            test_cases.append((
                row["username"],
                row["password"],
                row["expected_result"],
                row["test_case"]
            ))
    return test_cases

class TestDataDriven:

    def setup_method(self):
        self.driver = get_driver()
        self.login = LoginPage(self.driver)
        self.login.open()

    def teardown_method(self):
        self.driver.quit()

    @pytest.mark.parametrize(
        "username, password, expected, test_case",
        load_login_data()
    )
    def test_login_data_driven(
        self, username, password, expected, test_case
    ):
        print(f"\nRunning: {test_case}")
        self.login.login(username, password)

        if expected == "success":
            message = self.login.get_success_message()
            assert "You logged into a secure area!" in message
        else:
            message = self.login.get_error_message()
            assert "invalid" in message.lower()