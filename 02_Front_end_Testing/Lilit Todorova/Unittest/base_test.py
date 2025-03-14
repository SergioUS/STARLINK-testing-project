import os
import unittest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from faker import Faker
from helpers import Helpers
from my_keys import BROWSERSTACK_USERNAME, BROWSERSTACK_ACCESS_KEY

class BaseTest(unittest.TestCase):
    """
    A base test class that handles:
      - WebDriver setup with either local Chrome or BrowserStack
      - Disabling Chrome's autofill/save prompts
      - Faker instance creation
      - Helpers instance creation
      - WebDriver teardown
    """

    def setUp(self):
        with allure.step("Configuring browser options and initializing the WebDriver"):
            # Configure Chrome options
            options = Options()
            options.page_load_strategy = 'eager'

            # Disable Chrome's save prompts for passwords/autofill
            prefs = {
                "credentials_enable_service": False,
                "profile.password_manager_enabled": False,
                "profile.default_content_setting_values": {"autofill": 2}
            }
            options.add_experimental_option("prefs", prefs)

            # Check if we need to run on BrowserStack
            if os.getenv("BROWSERSTACK"):
                # Set BrowserStack capabilities using bstack:options
                options.set_capability("browserName", "Chrome")
                options.set_capability("browserVersion", "latest")
                options.set_capability("bstack:options", {
                    "os": "Windows",
                    "osVersion": "10",
                    "buildName": "Build 1",
                    "sessionName": "Starlink Test",
                    # Use environment variables if set, otherwise fallback to my_keys.py values
                    "userName": os.getenv("BROWSERSTACK_USER", BROWSERSTACK_USERNAME),
                    "accessKey": os.getenv("BROWSERSTACK_KEY", BROWSERSTACK_ACCESS_KEY)
                })
                self.driver = webdriver.Remote(
                    command_executor="http://hub-cloud.browserstack.com/wd/hub",
                    options=options
                )
            else:
                # Otherwise, run tests locally using Chrome
                self.driver = webdriver.Chrome(
                    service=ChromeService(ChromeDriverManager().install()),
                    options=options
                )

        with allure.step("Maximizing browser window and setting up helper instances"):
            self.driver.maximize_window()
            self.wait = WebDriverWait(self.driver, 30)
            self.fake = Faker()
            self.helpers = Helpers(self.driver)

    def tearDown(self):
        with allure.step("Tearing down the WebDriver and closing the browser"):
            try:
                self.driver.quit()
            except Exception as e:
                print(f"Error during teardown: {e}")

