import pytest
import json
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestWebApp:
    def test_driver_setup(self, driver):
        """Test that driver is set up correctly"""
        assert driver is not None
        assert driver.current_url == "data:,"

    def test_api_data_display(self, driver):
        """Test displaying API data on a web page"""
        # Assuming there's a web page that displays the API data
        # For demo, navigate to a placeholder
        driver.get("https://httpbin.org/json")
        
        # Wait for JSON response
        json_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )
        
        # Parse JSON from page (assuming it's displayed)
        json_text = json_element.text
        data = json.loads(json_text)
        
        # Assert some data
        assert "slideshow" in data