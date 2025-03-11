import unittest
from selenium.webdriver.support.wait import WebDriverWait
from faker import Faker
from helpers import setup_driver, Helpers


class BaseTest(unittest.TestCase):
    """
    BaseTest sets up the common environment for all tests.
    It initializes the WebDriver using a helper function,
    maximizes the browser window, sets up an explicit wait,
    and creates instances of Faker and Helpers for use in tests.
    """

    def setUp(self):
        # Initialize the WebDriver (local setup; for cross-browser, change the argument)
        self.driver = setup_driver("chrome")

        # Maximize the browser window
        self.driver.maximize_window()

        # Set up an explicit wait (30 seconds)
        self.wait = WebDriverWait(self.driver, 30)

        # Create a Faker instance for generating fake data
        self.fake = Faker()

        # Instantiate the Helpers class for common actions
        self.helpers = Helpers(self.driver)

    def tearDown(self):
        # Quit the WebDriver and close the browser
        self.driver.quit()
