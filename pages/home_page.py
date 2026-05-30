from selenium.webdriver.common.by import By

class HomePage:
    URL = "http://books.toscrape.com"
    
    # Locators
    TITLE = "Books to Scrape"
    HEADER = (By.CSS_SELECTOR, "div.page-header")
    BOOK_LIST = (By.CSS_SELECTOR, "article.product_pod")
    NAV_LINKS = (By.CSS_SELECTOR, "ul.nav-list li a")
    
    def __init__(self, driver):
        self.driver = driver
    
    def open(self):
        self.driver.get(self.URL)
    
    def get_title(self):
        return self.driver.title
    
    def get_books(self):
        return self.driver.find_elements(*self.BOOK_LIST)
    
    def get_nav_links(self):
        return self.driver.find_elements(*self.NAV_LINKS)