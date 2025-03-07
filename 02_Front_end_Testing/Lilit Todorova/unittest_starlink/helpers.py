import time
import random
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException as WDE

def delay():
    """Generate a random delay between 1 and 4 seconds."""
    time.sleep(random.randint(1, 4))

def setup_driver(browser_name):
    """Set up WebDriver with headless mode and eager page load strategy."""
    from selenium import webdriver
    from webdriver_manager.chrome import ChromeDriverManager
    from webdriver_manager.firefox import GeckoDriverManager
    from webdriver_manager.microsoft import EdgeChromiumDriverManager

    options = None
    driver = None

    if browser_name.lower() == "chrome":
        from selenium.webdriver.chrome.service import Service as ChromeService
        from selenium.webdriver.chrome.options import Options
        options = Options()
        #options.add_argument("--headless")
        options.page_load_strategy = 'eager'
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

    elif browser_name.lower() == "firefox":
        from selenium.webdriver.firefox.service import Service as FirefoxService
        from selenium.webdriver.firefox.options import Options
        options = Options()
        options.add_argument("--headless")
        options.page_load_strategy = 'eager'
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)

    elif browser_name.lower() == "edge":
        from selenium.webdriver.edge.service import Service as EdgeService
        from selenium.webdriver.edge.options import Options
        options = Options()
        options.add_argument("--headless")
        options.page_load_strategy = 'eager'
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=options)

    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    return driver

def wait_for_element(driver, locator, timeout=20):
    # Wait for an element to be visible and return it.
    try:
        element = WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(locator))
        return element
    except WDE as e:
        print(f"WebDriverException occurred: {e}")
        raise
# helpers.py

def get_page_url(page_name):
    """
    Returns the URL for the specified page.

    :param page_name: The name of the page (e.g., 'starlink', 'order', 'checkout').
    :return: The corresponding URL as a string.
    """
    urls = {
        "starlink": "https://www.starlink.com/",
        "login": "https://www.starlink.com/auth/login",
        "order_step_0": "https://www.starlink.com/order?processorToken=306598db-0d15-4b1a-9642-f84c787d027a&step=0",
        "order_step_2": "https://www.starlink.com/order?processorToken=306598db-0d15-4b1a-9642-f84c787d027a&step=2",
    }
    return urls.get(page_name, "https://www.starlink.com/")  # Default to homepage if page_name is invalid

class Helpers:
    """Utility class for common WebDriver actions."""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 60)

    def click_element(self, locator):
        """Wait for an element to be clickable and click it."""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def send_keys_to_element(self, locator, text):
        """Wait for an element to be visible and send text to it."""
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def wait_for_element_visibility(self, locator, timeout=10):
        """Wait for an element to be visible within the given timeout."""
        wait = WebDriverWait(self.driver, timeout)  # Use the specified timeout
        return wait.until(EC.visibility_of_element_located(locator))

    def clear_element(self, locator):
        """Clears the input field."""
        element = self.wait_for_element_visibility(locator)
        element.clear()

    def js_send_keys(self, locator, text):
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].value = '';", element)  # Clear field
        element.send_keys(text)

    def js_clear_field(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].value = '';", element)

