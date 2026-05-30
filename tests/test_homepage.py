import pytest
from utils.driver_factory import get_driver
from pages.home_page import HomePage

class TestHomePage:

    def setup_method(self):
        self.driver = get_driver()
        self.home = HomePage(self.driver)
        self.home.open()

    def teardown_method(self):
        self.driver.quit()

    def test_page_title(self):
       assert "Books to Scrape" in self.home.get_title()

    def test_books_are_displayed(self):
        books = self.home.get_books()
        assert len(books) > 0, "No books found on homepage"

    def test_nav_links_present(self):
        links = self.home.get_nav_links()
        assert len(links) > 0, "No navigation links found"