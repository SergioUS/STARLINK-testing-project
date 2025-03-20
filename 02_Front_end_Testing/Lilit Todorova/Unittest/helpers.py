# helpers.py
import time
import random
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException as WDE


@allure.step("Delay execution for a random period between 2 and 6 seconds")
def delay():
    """Generate a random delay between 2 and 6 seconds."""
    time.sleep(random.randint(2, 6))

@allure.step("Waiting for element with locator: {locator}")
def wait_for_element(driver, locator, timeout=20):
    """Wait for an element to be visible and return it."""
    try:
        element = WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(locator))
        return element
    except WDE as e:
        print(f"WebDriverException occurred: {e}")
        raise

@allure.step("Getting page URL for page: {page_name}")
def get_page_url(page_name):
    """Return the URL for the specified page."""
    urls = {
        "starlink": "https://www.starlink.com/",
        "login": "https://www.starlink.com/auth/login",
        "order_step_0": "https://www.starlink.com/order?processorToken=5e3b06bb-23c7-4896-80c2-50f450bad4b8&step=0",
        "order_step_2": "https://www.starlink.com/order?processorToken=5e3b06bb-23c7-4896-80c2-50f450bad4b8&step=2",
    }
    return urls.get(page_name, "https://www.starlink.com/")

class Helpers:
    """Utility class for common WebDriver actions."""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 60)

    @allure.step("Clicking element located by: {locator}")
    def click_element(self, locator, timeout=None):
        wait_instance = WebDriverWait(self.driver, timeout) if timeout else self.wait
        element = wait_instance.until(EC.element_to_be_clickable(locator))
        element.click()

    @allure.step("Sending keys '{text}' to element located by: {locator}")
    def send_keys_to_element(self, locator, text):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    @allure.step("Waiting for element visibility with locator: {locator}")
    def wait_for_element_visibility(self, locator, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Clearing element located by: {locator}")
    def clear_element(self, locator):
        element = self.wait_for_element_visibility(locator)
        element.clear()

    @allure.step("Sending keys via JS to element located by: {locator}")
    def js_send_keys(self, locator, text):
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].value = '';", element)
        element.send_keys(text)

    @allure.step("Clearing field via JS for element located by: {locator}")
    def js_clear_field(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].value = '';", element)
