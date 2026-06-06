class Config:
    # Browser settings
    BROWSER = "chrome"
    HEADLESS = False
    IMPLICIT_WAIT = 10
    PAGE_LOAD_TIMEOUT = 30

    # URLs
    BASE_URL = "https://the-internet.herokuapp.com"
    LOGIN_URL = f"{BASE_URL}/login"

    # Test credentials
    VALID_USERNAME = "tomsmith"
    VALID_PASSWORD = "SuperSecretPassword!"

    # Reports
    SCREENSHOT_DIR = "framework/reports/screenshots"
