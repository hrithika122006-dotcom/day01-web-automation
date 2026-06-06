import pytest
from framework.utils.driver_factory import get_driver
from framework.utils.screenshot import take_screenshot

class BaseTest:

    def setup_method(self):
        self.driver = get_driver()

    def teardown_method(self):
        if hasattr(self, '_test_failed') and self._test_failed:
            take_screenshot(
                self.driver,
                self.__class__.__name__
            )
        self.driver.quit()

    @pytest.hookimpl(tryfirst=True, hookwrapper=True)
    def pytest_runtest_makereport(self, item, call):
        outcome = yield
        result = outcome.get_result()
        if result.when == "call" and result.failed:
            self._test_failed = True