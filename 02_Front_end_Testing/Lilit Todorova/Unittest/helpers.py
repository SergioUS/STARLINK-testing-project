import time
import random
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException as WDE


def delay():
    """
    Generate a random delay between 1 and 4 seconds.
    Useful to simulate realistic user pauses or wait for animations.
    """
    time.sleep(random.randint(1, 4))


def setup_driver(browser_name):
    """
    Set up and return a WebDriver instance based on the specified browser.
    Uses webdriver_manager to automatically download and manage driver binaries.

    :param browser_name: The name of the browser ("chrome", "firefox", "edge").
    :return: An initialized WebDriver instance.
    :raises ValueError: If the specified browser is unsupported.
    """
    from webdriver_manager.chrome import ChromeDriverManager
    from webdriver_manager.firefox import GeckoDriverManager
    from webdriver_manager.microsoft import EdgeChromiumDriverManager

    options = None
    driver = None

    if browser_name.lower() == "chrome":
        from selenium.webdriver.chrome.service import Service as ChromeService
        from selenium.webdriver.chrome.options import Options
        options = Options()
        # Uncomment the following line to run Chrome in headless mode.
        # options.add_argument("--headless")
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
    """
    Wait for an element specified by the locator to become visible.

    :param driver: The WebDriver instance.
    :param locator: A tuple (By, value) to locate the element.
    :param timeout: Maximum time to wait (default is 20 seconds).
    :return: The WebElement once it is visible.
    :raises: WebDriverException if the element is not found within the timeout.
    """
    try:
        element = WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(locator))
        return element
    except WDE as e:
        print(f"WebDriverException occurred: {e}")
        raise


def get_page_url(page_name):
    """
    Returns the URL for the specified page.

    :param page_name: A key representing the page (e.g., 'starlink', 'login', 'order_step_0', 'order_step_2').
    :return: The corresponding URL as a string, or the homepage URL if the key is not found.
    """
    urls = {
        "starlink": "https://www.starlink.com/",
        "login": "https://www.starlink.com/auth/login",
        "order_step_0": "https://www.starlink.com/order?processorToken=22b4728c-68dc-4f4d-8be6-7d9c6ed719b1&step=0",
        "order_step_2": "https://www.starlink.com/order?processorToken=22b4728c-68dc-4f4d-8be6-7d9c6ed719b1&step=2",
    }
    return urls.get(page_name, "https://www.starlink.com/")


class Helpers:
    """
    Utility class for common WebDriver actions.
    Provides methods for clicking, sending keys, waiting for elements, and clearing fields.
    """

    def __init__(self, driver):
        """
        Initialize with the given WebDriver and set up a default wait.

        :param driver: The WebDriver instance.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 60)

    def click_element(self, locator):
        """
        Wait for an element to be clickable and click it.

        :param locator: A tuple (By, value) for locating the element.
        """
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def send_keys_to_element(self, locator, text):
        """
        Wait for an element to be visible, clear any existing text, and send new text.

        :param locator: A tuple (By, value) for locating the element.
        :param text: The text to be entered into the element.
        """
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def wait_for_element_visibility(self, locator, timeout=10):
        """
        Wait for an element to become visible within the specified timeout.

        :param locator: A tuple (By, value) for locating the element.
        :param timeout: Maximum time to wait (default is 10 seconds).
        :return: The WebElement once visible.
        """
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.visibility_of_element_located(locator))

    def clear_element(self, locator):
        """
        Wait for an element to be visible and clear its content.

        :param locator: A tuple (By, value) for locating the element.
        """
        element = self.wait_for_element_visibility(locator)
        element.clear()

    def js_send_keys(self, locator, text):
        """
        Use JavaScript to clear an element's value and then send keys to it.

        :param locator: A tuple (By, value) for locating the element.
        :param text: The text to be entered.
        """
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].value = '';", element)
        element.send_keys(text)

    def js_clear_field(self, locator):
        """
        Use JavaScript to clear the value of an element.

        :param locator: A tuple (By, value) for locating the element.
        """
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].value = '';", element)
