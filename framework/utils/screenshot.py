import os
from datetime import datetime
from framework.config.config import Config

def take_screenshot(driver, test_name):
    # Create screenshots folder if it doesn't exist
    os.makedirs(Config.SCREENSHOT_DIR, exist_ok=True)
    
    # Create filename with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{test_name}_{timestamp}.png"
    filepath = os.path.join(Config.SCREENSHOT_DIR, filename)
    
    # Save screenshot
    driver.save_screenshot(filepath)
    print(f"\nScreenshot saved: {filepath}")
    
    return filepath
    