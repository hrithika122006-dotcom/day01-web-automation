from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from framework.config.config import Config
import os

def get_driver():
    options = webdriver.ChromeOptions()
    
    if Config.HEADLESS:
        options.add_argument("--headless")
    
    options.add_argument("--start-maximized")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver_path = ChromeDriverManager().install()
    
    if not driver_path.endswith(".exe"):
        driver_path = os.path.join(
            os.path.dirname(driver_path), 
            "chromedriver.exe"
        )

    driver = webdriver.Chrome(
        service=Service(driver_path),
        options=options
    )

    driver.implicitly_wait(Config.IMPLICIT_WAIT)
    driver.set_page_load_timeout(Config.PAGE_LOAD_TIMEOUT)
    
    return driver