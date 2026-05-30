from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os

def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    
    driver_path = ChromeDriverManager().install()
    
    # Fix for WinError 193
    if not driver_path.endswith(".exe"):
        driver_path = os.path.join(
            os.path.dirname(driver_path), "chromedriver.exe"
        )
    
    driver = webdriver.Chrome(
        service=Service(driver_path),
        options=options
    )
    return driver