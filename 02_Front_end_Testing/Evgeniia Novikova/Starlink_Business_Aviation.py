from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import unittest
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.edge.service import Service
from faker import Faker
import Helpers as h
import HtmlTestRunner
import AllureReports


class ChromeTests(TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument(
            "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.3")
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)
        self.url = h.url_starlink_business_aviation
        self.driver.get(self.url)
        self.windows = self.driver.window_handles
        self.faker = Faker()

        options.page_load_strategy = 'eager'

        # Enable performance logging
        options.add_argument("--enable-logging")
        options.add_argument("--log-level=0")
        options.set_capability("goog:loggingPrefs", {"performance": "ALL"})

        # Using a running Chrome with remote debugging
        options.add_experimental_option("debuggerAddress", "localhost:9222")

        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("useAutomationExtension", False)

    def test_TC_61_PT_verify_title(self):

        h.verify_title(self.driver, h.title_starlink_business_aviation)

    def test_TC_62_verify_PT_main_heading(self):

        h.verify_heading(self.driver, h.heading_main_str, h.heading_main_xpath)

    def test_TC_63_PT_verify_contact_us_buttons_functionality(self):

        h.verify_contact_us_buttons_functionality(self.driver, self.wait, h.buttons_dict, h.url_starlink_aviation_info)

    def test_TC_64_PT_verify_high_speed_internet_section(self):
        h.verify_high_speed_internet_section(self.driver, self.wait, h.locators_high_speed_internet_in_flight)

    def test_TC_65_PT_navigation_arrows_functionality(self):
        h.verify_navigation_arrows_functionality(
            self.driver,
            self.wait,
            h.carousel_container,
            h.arrow_right,
            h.arrow_left,
            h.get_active_slide
        )

    def test_TC_60_60_NT_unsecured_connection(self):

        h.verify_unsecured_connection(h.url_starlink_business_aviation_http, self.url)

    def test_TC_61_61_NT_404_page_behavior(self):

        h.verify_page_behavior(h.url_starlink_business_aviation_404, h.url_starlink)

    def test_TC_62_62_NT_keyboard_accessibility(self):
        h.verify_keyboard_accessibility(
            self.driver,
            self.wait,
            h.elements_dict,
            h.get_css_properties
        )

    def test_TC_63_63_NT_page_load_under_3g(self):
        dom_load_time, finish_time = h.verify_page_load_under_3g(self.driver)

        # Verify that page loads within reasonable time under 3G conditions
        if dom_load_time <= 20:
            print(f'DOM Load Time is acceptable: {dom_load_time} seconds')
        else:
            print(f"DOM Load Time too high: {dom_load_time} seconds")

        if finish_time <= 30:
            print(f'Finish Time is acceptable: {finish_time} seconds')
        else:
            print(f"Finish Time too high: {finish_time} seconds")

    def test_TC_64_64_NT_email_field_validation(self):

        h.verify_email_field_validation(
            self.driver,
            self.wait,
            h.email_field,
            h.error_message_xpath,
            h.error_message_text,
            self.faker
        )

    def tearDown(self):
        self.driver.quit()


class EdgeTestes(TestCase):

    def setUp(self):
        options = webdriver.EdgeOptions()
        options.page_load_strategy = 'eager'
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument(
            "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 Edg/132.0.0.")
        options.add_argument('--headless')
        options.headless = True
        self.driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()), options=options)
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)
        self.url = h.url_starlink_business_aviation
        self.driver.get(self.url)
        self.windows = self.driver.window_handles
        self.faker = Faker()

        # Enable performance logging
        options.add_argument("--enable-logging")
        options.add_argument("--log-level=0")
        options.set_capability("goog:loggingPrefs", {"performance": "ALL"})

        # Using a running Edge with remote debugging
        options.add_experimental_option("debuggerAddress", "localhost:9222")

        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("useAutomationExtension", False)

    def test_TC_61_PT_verify_title(self):

        h.verify_title(self.driver, h.title_starlink_business_aviation)

    def test_TC_62_verify_PT_main_heading(self):

        h.verify_heading(self.driver, h.heading_main_str, h.heading_main_xpath)

    def test_TC_63_PT_verify_contact_us_buttons_functionality(self):

        h.verify_contact_us_buttons_functionality(self.driver, self.wait, h.buttons_dict, h.url_starlink_aviation_info)

    def test_TC_64_PT_verify_high_speed_internet_section(self):
        h.verify_high_speed_internet_section(self.driver, self.wait, h.locators_high_speed_internet_in_flight)

    def test_TC_65_PT_navigation_arrows_functionality(self):
        h.verify_navigation_arrows_functionality(
            self.driver,
            self.wait,
            h.carousel_container,
            h.arrow_right,
            h.arrow_left,
            h.get_active_slide
        )

    def test_TC_60_60_NT_unsecured_connection(self):

        h.verify_unsecured_connection(h.url_starlink_business_aviation_http, self.url)

    def test_TC_61_61_NT_404_page_behavior(self):

        h.verify_page_behavior(h.url_starlink_business_aviation_404, h.url_starlink)

    def test_TC_62_62_NT_keyboard_accessibility(self):
        h.verify_keyboard_accessibility(
            self.driver,
            self.wait,
            h.elements_dict,
            h.get_css_properties
        )

    def test_TC_63_63_NT_page_load_under_3g(self):
        dom_load_time, finish_time = h.verify_page_load_under_3g(self.driver)

        # Verify that page loads within reasonable time under 3G conditions
        if dom_load_time <= 20:
            print(f'DOM Load Time is acceptable: {dom_load_time} seconds')
        else:
            print(f"DOM Load Time too high: {dom_load_time} seconds")

        if finish_time <= 30:
            print(f'Finish Time is acceptable: {finish_time} seconds')
        else:
            print(f"Finish Time too high: {finish_time} seconds")

    def test_TC_64_64_NT_email_field_validation(self):

        h.verify_email_field_validation(
            self.driver,
            self.wait,
            h.email_field,
            h.error_message_xpath,
            h.error_message_text,
            self.faker
        )

    def tearDown(self):
        print("Closing browser after test.")
        self.driver.quit()


class FirefoxTestes(TestCase):

    def setUp(self):
        options = webdriver.FirefoxOptions()
        options.add_argument("--headless")
        options.add_argument(
            "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.3")

        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)

        self.url = h.url_starlink_business_aviation
        self.driver.get(self.url)
        self.windows = self.driver.window_handles
        self.faker = Faker()

        options.page_load_strategy = 'eager'

        options.add_argument("--enable-logging")
        options.add_argument("--log-level=0")

    def test_TC_61_PT_verify_title(self):
        h.verify_title(self.driver, h.title_starlink_business_aviation)

    def test_TC_62_verify_PT_main_heading(self):
        h.verify_heading(self.driver, h.heading_main_str, h.heading_main_xpath)

    def test_TC_63_PT_verify_contact_us_buttons_functionality(self):
        h.verify_contact_us_buttons_functionality(self.driver, self.wait, h.buttons_dict, h.url_starlink_aviation_info)

    def test_TC_64_PT_verify_high_speed_internet_section(self):
        h.verify_high_speed_internet_section(self.driver, self.wait, h.locators_high_speed_internet_in_flight)

    def test_TC_65_PT_navigation_arrows_functionality(self):
        h.verify_navigation_arrows_functionality(
            self.driver,
            self.wait,
            h.carousel_container,
            h.arrow_right,
            h.arrow_left,
            h.get_active_slide
        )

    def test_TC_60_60_NT_unsecured_connection(self):
        h.verify_unsecured_connection(h.url_starlink_business_aviation_http, self.url)

    def test_TC_61_61_NT_404_page_behavior(self):
        h.verify_page_behavior(h.url_starlink_business_aviation_404, h.url_starlink)

    def test_TC_62_62_NT_keyboard_accessibility(self):
        h.verify_keyboard_accessibility(
            self.driver,
            self.wait,
            h.elements_dict,
            h.get_css_properties
        )

    def test_TC_64_64_NT_email_field_validation(self):
        h.verify_email_field_validation(
            self.driver,
            self.wait,
            h.email_field,
            h.error_message_xpath,
            h.error_message_text,
            self.faker
        )

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
