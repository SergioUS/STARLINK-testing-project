# UnitTest, includes Positive and Negative tests for Starlink site, Business/Fixed Site
# prepared by Dmitry_Antipenko

import random
import time
import unittest

from selenium import webdriver
from selenium.common.exceptions import WebDriverException as WDE
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
#import HtmlTestRunner
import AllureReports

import Helpers_Business_Fixed_Site as H


#from faker import Faker

#faker = Faker()


# driver sleep from 1 to 5 seconds
def delay():
    time.sleep(random.randint(1, 5))


#def scroll_to_element(iframe):
#    pass

class ChromePositiveTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()


    # Test Case 021: Verify / Validate that the "FIXED SITE" on the "BUSINESS" page is button visible and clickable.
    def test_case_021(self):
        driver = self.driver
        print("Test Case 021")

        # 1.Opening Starlink site
        driver.get("https://www.starlink.com/")

        delay()

        # 2.Click on the "BUSINESS" button on the right side of the header
        H.click_Business_button(driver)

        delay()

        # 3.Click on the "FIXED SITE" button on the left side of the header
        H.click_FIXED_SITE_button(driver)

        delay()

        # 4.Check on the "FIXED SITE"
        H.check_FIXED_SITE_button(driver)

        delay()


    # Test Case 022: Verify / Validate that the main heading "STARLINK FOR FIXED SITES" is present and correct.
    def test_case_022(self):
        driver = self.driver
        print("Test Case 022")

        # 1.Opening Starlink site
        driver.get("https://www.starlink.com/")

        delay()

        # 2.Click on the "BUSINESS" button on the right side of the header
        H.click_Business_button(driver)

        delay()

        # 3.Click on the "FIXED SITE" button on the left side of the header
        H.click_FIXED_SITE_button(driver)

        delay()

        # 4.Check on the "STARLINK FOR FIXED SITES" header
        H.check_STARLINK_FOR_FIXED_SITES_header(driver)

        delay()


    # Test Case 023: Verify / Validate that the "Schedule a Consultation" on the "FIXED SITE" page button is visible and directs the user to the correct page.
    def test_case_023(self):
        driver = self.driver
        print("Test Case 023")

        # 1.Opening Starlink site
        driver.get("https://www.starlink.com/")

        delay()

        # 2.Click on the "BUSINESS" button on the right side of the header
        H.click_Business_button(driver)

        delay()

        # 3.Click on the "FIXED SITE" button on the left side of the header
        H.click_FIXED_SITE_button(driver)

        delay()

        # 4.Check on the "Schedule a Consultation" button
        H.check_Schedule_a_Consultation_form(driver)

        delay()

        # 5.Click "Schedule a Consultation" button
        H.click_Schedule_a_Consultation_button(driver)

        delay()


    # Test Case 024: Verify / Validate that the "SERVICE PLAN" button the "FIXED SITE" line functions correctly and direct the user to the correct page.
    def test_case_024(self):
        driver = self.driver
        print("Test Case 024")

        # 1.Opening Starlink site
        driver.get("https://www.starlink.com/")

        delay()

        # 2.Click on the "BUSINESS" button on the right side of the header
        H.click_Business_button(driver)

        delay()

        # 3.Click on the "FIXED SITE" button on the left side of the header
        H.click_FIXED_SITE_button(driver)

        delay()

        # 4.Scroll until "SERVICE PLANS" button in the line "FIXED SITE"
        driver.find_element(By.XPATH, H.ServicePlans_link).send_keys(Keys.PAGE_DOWN)
        delay()

        # 5.Check "SERVICE PLANS" in the line "FIXED SITE" button.
        H.check_SERVICE_PLANS_button(driver)

        delay()

        # 6.Click "SERVICE PLANS" in the line "FIXED SITE" button
        H.click_Service_Plans_button(driver)

        delay()

    # Test Case 025: Verify / Validate that the "Buyer's guide" on the "FIXED SITE" page button is visible and directs the user to the correct page.
    def test_case_025(self):
        driver = self.driver
        print("Test Case 025")

        # 1.Opening Starlink site
        driver.get("https://www.starlink.com/")

        delay()

        # 2.Click on the "BUSINESS" button on the right side of the header
        H.click_Business_button(driver)

        delay()

        # 3.Click on the "FIXED SITE" button on the left side of the header
        H.click_FIXED_SITE_button(driver)

        delay()

        # 4.Check on the "Buyer's guide" button
        H.check_Buyers_guide_button(driver)

        delay()

        # 5.Click "Buyer's guide" button
        H.click_Buyers_guide_button(driver)

        delay()


def teardown(self):
    self.driver.quit()


class ChromeNegativeTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()


    # Test Case 021_21: Verify / Validate that the "Order Now" button is not working without an address in the "TYPE AND SELECT" line.
    def test_case_021_21(self):
        driver = self.driver
        print("Test Case 021_21")

        # 1.Opening Starlink site
        driver.get("https://www.starlink.com/")

        delay()

        # 2.Click on the "BUSINESS" button on the right side of the header
        H.click_Business_button(driver)

        delay()

        # 3.Click on the "FIXED SITE" button on the left side of the header
        H.click_FIXED_SITE_button(driver)

        delay()

        # 4.Check on the "Order Now" button
        H.check_Order_Now_button(driver)

        delay()

        # 5.Click on the "Order Now" button without selecting a shipping address
        H.click_Order_Now_button(driver)

        delay()


    # Test Case 022_22: Verify / Validate that "SIGN UP" button is not working with email address that the "FIXED SITE" page.
    def test_case_022_22(self):
        driver = self.driver
        print("Test Case 022_22")

        # 1.Opening Starlink site
        driver.get("https://www.starlink.com/")

        delay()

        # 2.Click on the "BUSINESS" button on the right side of the header
        H.click_Business_button(driver)

        time.sleep(5)

        # 3.Click on the "FIXED SITE" button on the left side of the header
        H.click_FIXED_SITE_button(driver)

        delay()

        # 4.Scroll down the page "Interested in staying up to date with Starlink?"
        footer=driver.find_element(By.CSS_SELECTOR,"footer")
        driver.execute_script("arguments[0].scrollIntoView();", footer)
        delay()
        email_input = driver.find_element(By.XPATH, '//input[@type="email"]')
        email_input.is_displayed()
        email_input.click()
        email_input.send_keys(H.Wrong_email_1)
        delay()

        # 5.Click on Sing Up button
        driver.find_element(By.XPATH, H.Click_SingUp_link).click()
        time.sleep(5)
        message=driver.find_element(By.XPATH, "//div[contains(text(),'Thank you for ')]")
        if message:
            print("Test 022_22 is failed")
        else:
            print("Test 022_22 is PASS")

        delay()


    # Test Case 023_23: Verify/Validate that "Place Order" button is not working with no "Contact Information"
    def test_case_023_23(self):
        driver = self.driver
        print("Test Case 023_23")

        # 1.Opening Starlink site
        driver.get("https://www.starlink.com/")

        delay()

        # 2.Click on the "BUSINESS" button on the right side of the header
        H.click_Business_button(driver)

        delay()

        # 3.Click on the "FIXED SITE" button on the left side of the header
        H.click_FIXED_SITE_button(driver)

        delay()

        # 4.Click on the "Order Now" button
        H.click_Order_Now_button(driver)

        time.sleep(5)

        message = driver.find_element(By.XPATH,"(//div[contains(.,'To view available Starlink products in your area, please provide your address or start with your current location.')])[9]")
        if message:
            print("Test 023_23 is PASS")
        else:
            print("Test 023_23 is failed")

        delay()

    # Test Case 024_24: Verify/Validate that "Place Order" button is not working with no "Contact Information"
    def test_case_024_24(self):
        driver = self.driver
        print("Test Case 024_24")

        # 1.Opening Starlink site
        driver.get("https://www.starlink.com/order?processorToken=ee4c13dc-0e6f-44b9-9891-58c68ca5c679&step=1")

        delay()

        # 2.Click on "Checkout" button
        H.click_Checkout_button(driver)
        delay()

        # 3.Input an incorrect email address in the "Email" field
        wrong_email2_input = driver.find_element(By.XPATH, "//input[@name='email']")
        wrong_email2_input.is_displayed()
        wrong_email2_input.clear()
        wrong_email2_input.send_keys(H.Wrong_email_2)
        driver.find_element(By.XPATH, "//input[@name='phone']").click()
        delay()

        try:
            message = driver.find_element(By.XPATH, "//span[@xpath='1']")
            if message:
                print("Test 024_24 is PASS")
            else:
                print("Test 024_24 is Failed")
        except WDE:
            print("Test 024_24 is Failed")

        delay()


    # Test Case 025_25: Verify/Validate that if you enter an incorrect phone number in the "Checkout" section, the site will say "Invalid phone number"
    def test_case_025_25(self):
        driver = self.driver
        print("Test Case 025_25")

        # 1.Opening Starlink site
        driver.get("https://www.starlink.com/order?processorToken=ee4c13dc-0e6f-44b9-9891-58c68ca5c679&step=1")

        delay()

        # 2.Click on "Checkout" button
        H.click_Checkout_button(driver)

        delay()

        # 3.Input an incorrect email address in the "Phone number" field
        wrong_phone_input = driver.find_element(By.XPATH, "//input[@name='phone']")
        wrong_phone_input.is_displayed()
        wrong_phone_input.clear()
        wrong_phone_input.send_keys(H.Wrong_PN)
        driver.find_element(By.XPATH, "//input[@name='email']").click()

        delay()

        message = driver.find_element(By.XPATH, "//span[contains(.,'Invalid phone number')]")
        if message:
           print("Test 025_25 is PASS")
        else:
           print("Test 025_25 is Failed")

        delay()


def teardown(self):
    self.driver.quit()


class FirefoxPositiveTests(unittest.TestCase):

    def setUp(self):
        options = webdriver.FirefoxOptions()
        self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
        self.driver.maximize_window()

    # Test Case 021: Verify / Validate that the "FIXED SITE" on the "BUSINESS" page is button visible and clickable.
    def test_case_021(self):
        driver = self.driver
        print("Test Case 021")

        # 1.Opening Starlink site
        driver.get("https://www.starlink.com/")

        delay()

        # 2.Click on the "BUSINESS" button on the right side of the header
        H.click_Business_button(driver)

        delay()

        # 3.Click on the "FIXED SITE" button on the left side of the header
        H.click_FIXED_SITE_button(driver)

        delay()

        # 4.Check on the "FIXED SITE"
        H.check_FIXED_SITE_button(driver)

        delay()
        driver.quit()

    # Test Case 022: Verify / Validate that the main heading "STARLINK FOR FIXED SITES" is present and correct.
    def test_case_022(self):
        driver = self.driver
        print("Test Case 022")

        # 1.Opening Starlink site
        driver.get("https://www.starlink.com/")

        delay()

        # 2.Click on the "BUSINESS" button on the right side of the header
        H.click_Business_button(driver)

        delay()

        # 3.Click on the "FIXED SITE" button on the left side of the header
        H.click_FIXED_SITE_button(driver)

        delay()

        # 4.Check on the "STARLINK FOR FIXED SITES" header
        H.check_STARLINK_FOR_FIXED_SITES_header(driver)

        delay()

        driver.quit()

    # Test Case 023: Verify / Validate that the "Schedule a Consultation" on the "FIXED SITE" page button is visible and directs the user to the correct page.
    def test_case_023(self):
        driver = self.driver
        print("Test Case 023")

        # 1.Opening Starlink site
        driver.get("https://www.starlink.com/")

        delay()

        # 2.Click on the "BUSINESS" button on the right side of the header
        H.click_Business_button(driver)

        delay()

        # 3.Click on the "FIXED SITE" button on the left side of the header
        H.click_FIXED_SITE_button(driver)

        delay()

        # 4.Check on the "Schedule a Consultation" button
        H.check_Schedule_a_Consultation_form(driver)

        delay()

        # 5.Click "Schedule a Consultation" button
        H.click_Schedule_a_Consultation_button(driver)

        delay()

        driver.quit()


    # Test Case 024: Verify / Validate that the "SERVICE PLAN" button the "FIXED SITE" line functions correctly and direct the user to the correct page.
    def test_case_024(self):
        driver = self.driver
        print("Test Case 024")

        # 1.Opening Starlink site
        driver.get("https://www.starlink.com/")

        delay()

        # 2.Click on the "BUSINESS" button on the right side of the header
        H.click_Business_button(driver)

        delay()

        # 3.Click on the "FIXED SITE" button on the left side of the header
        H.click_FIXED_SITE_button(driver)

        delay()

        # 4.Scroll until "SERVICE PLANS" button in the line "FIXED SITE"
        driver.find_element(By.XPATH, H.ServicePlans_link).send_keys(Keys.PAGE_DOWN)
        delay()

        # 5.Check "SERVICE PLANS" in the line "FIXED SITE" button.
        H.check_SERVICE_PLANS_button(driver)

        delay()

        # 6.Click "SERVICE PLANS" in the line "FIXED SITE" button
        H.click_Service_Plans_button(driver)

        delay()

        driver.quit()

    # Test Case 025: Verify / Validate that the "Buyer's guide" on the "FIXED SITE" page button is visible and directs the user to the correct page.
    def test_case_025(self):
        driver = self.driver
        print("Test Case 025")

        # 1.Opening Starlink site
        driver.get("https://www.starlink.com/")

        delay()

        # 2.Click on the "BUSINESS" button on the right side of the header
        H.click_Business_button(driver)

        delay()

        # 3.Click on the "FIXED SITE" button on the left side of the header
        H.click_FIXED_SITE_button(driver)

        delay()

        # 4.Check on the "Buyer's guide" button
        H.check_Buyers_guide_button(driver)

        delay()

        # 5.Click "Buyer's guide" button
        H.click_Buyers_guide_button(driver)

        delay()

        driver.quit()


def teardown(self):
    self.driver.quit()


class FirefoxNegativeTests(unittest.TestCase):

    def setUp(self):
        options = webdriver.FirefoxOptions()
        self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
        self.driver.maximize_window()

    # Test Case 021_21: Verify / Validate that the "Order Now" button is not working without an address in the "TYPE AND SELECT" line.
    def test_case_021_21(self):
        driver = self.driver
        print("Test Case 021_21")

        # 1.Opening Starlink site
        driver.get("https://www.starlink.com/")

        delay()

        # 2.Click on the "BUSINESS" button on the right side of the header
        H.click_Business_button(driver)

        delay()

        # 3.Click on the "FIXED SITE" button on the left side of the header
        H.click_FIXED_SITE_button(driver)

        delay()

        # 4.Check on the "Order Now" button
        H.check_Order_Now_button(driver)

        delay()

        # 5.Click on the "Order Now" button without selecting a shipping address
        H.click_Order_Now_button(driver)

        delay()
        driver.quit()


    # Test Case 022_22: Verify / Validate that "SIGN UP" button is not working with email address that the "FIXED SITE" page.
    def test_case_022_22(self):
        driver = self.driver
        print("Test Case 022_22")

        # 1.Opening Starlink site
        driver.get("https://www.starlink.com/")

        delay()

        # 2.Click on the "BUSINESS" button on the right side of the header
        H.click_Business_button(driver)

        time.sleep(5)

        # 3.Click on the "FIXED SITE" button on the left side of the header
        H.click_FIXED_SITE_button(driver)

        delay()

        # 4.Scroll down the page "Interested in staying up to date with Starlink?"
        footer=driver.find_element(By.CSS_SELECTOR,"footer")
        driver.execute_script("arguments[0].scrollIntoView();", footer)
        delay()
        email_input = driver.find_element(By.XPATH, '//input[@type="email"]')
        email_input.is_displayed()
        email_input.click()
        email_input.send_keys(H.Wrong_email_1)
        delay()

        # 5.Click on Sing Up button
        driver.find_element(By.XPATH, H.Click_SingUp_link).click()
        time.sleep(5)
        try:
           message=driver.find_element(By.XPATH, "//div[contains(text(),'Thank you for ')]")
           if message:
              print("Test 022_22 is failed")
           else:
              print("Test 022_22 is PASS")
        except WDE:
              print("message is not visible")
        delay()
        driver.quit()


    # Test Case 023_23: Verify/Validate that "Place Order" button is not working with no "Contact Information"
    def test_case_023_23(self):
        driver = self.driver
        print("Test Case 023_23")

        # 1.Opening Starlink site
        driver.get("https://www.starlink.com/")

        delay()

        # 2.Click on the "BUSINESS" button on the right side of the header
        H.click_Business_button(driver)

        delay()

        # 3.Click on the "FIXED SITE" button on the left side of the header
        H.click_FIXED_SITE_button(driver)

        delay()

        # 4.Click on the "Order Now" button
        H.click_Order_Now_button(driver)

        time.sleep(5)

        message = driver.find_element(By.XPATH,"(//div[contains(.,'To view available Starlink products in your area, please provide your address or start with your current location.')])[9]")
        if message:
            print("Test 023_23 is PASS")
        else:
            print("Test 023_23 is failed")

        delay()
        driver.quit()

    # Test Case 024_24: Verify/Validate that "Place Order" button is not working with no "Contact Information"
    def test_case_024_24(self):
        driver = self.driver
        print("Test Case 024_24")

        # 1.Opening Starlink site
        driver.get("https://www.starlink.com/order?processorToken=ee4c13dc-0e6f-44b9-9891-58c68ca5c679&step=1")

        delay()

        # 2.Click on "Checkout" button
        H.click_Checkout_button(driver)
        delay()

        # 3.Input an incorrect email address in the "Email" field
        wrong_email2_input = driver.find_element(By.XPATH, "//input[@name='email']")
        wrong_email2_input.is_displayed()
        wrong_email2_input.clear()
        wrong_email2_input.send_keys(H.Wrong_email_2)
        driver.find_element(By.XPATH, "//input[@name='phone']").click()
        delay()

        try:
            message = driver.find_element(By.XPATH, "//span[@xpath='1']")
            if message:
                print("Test 024_24 is PASS")
            else:
                print("Test 024_24 is Failed")
        except WDE:
            print("Test 024_24 is Failed")

        delay()
        driver.quit()


    # Test Case 025_25: Verify/Validate that if you enter an incorrect phone number in the "Checkout" section, the site will say "Invalid phone number"
    def test_case_025_25(self):
        driver = self.driver
        print("Test Case 025_25")

        # 1.Opening Starlink site
        driver.get("https://www.starlink.com/order?processorToken=ee4c13dc-0e6f-44b9-9891-58c68ca5c679&step=1")

        delay()

        # 2.Click on "Checkout" button
        H.click_Checkout_button(driver)

        delay()

        # 3.Input an incorrect email address in the "Phone number" field
        wrong_phone_input = driver.find_element(By.XPATH, "//input[@name='phone']")
        wrong_phone_input.is_displayed()
        wrong_phone_input.clear()
        wrong_phone_input.send_keys(H.Wrong_PN)
        driver.find_element(By.XPATH, "//input[@name='email']").click()

        delay()

        message = driver.find_element(By.XPATH, "//span[contains(.,'Invalid phone number')]")
        if message:
           print("Test 025_25 is PASS")
        else:
           print("Test 025_25 is Failed")

        driver.quit()



def teardown(self):
    self.driver.quit()


class EdgePositiveTests(unittest.TestCase):

    def setUp(self):
        options = webdriver.EdgeOptions()
        self.driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=options)
        self.driver.maximize_window()


    # Test Case 021: Verify / Validate that the "FIXED SITE" on the "BUSINESS" page is button visible and clickable.
    def test_case_021(self):
        driver = self.driver
        print("Test Case 021")

        # 1.Opening Starlink site
        driver.get("https://www.starlink.com/")

        delay()

        # 2.Click on the "BUSINESS" button on the right side of the header
        H.click_Business_button(driver)

        delay()

        # 3.Click on the "FIXED SITE" button on the left side of the header
        H.click_FIXED_SITE_button(driver)

        delay()

        # 4.Check on the "FIXED SITE"
        H.check_FIXED_SITE_button(driver)

        delay()


    # Test Case 022: Verify / Validate that the main heading "STARLINK FOR FIXED SITES" is present and correct.
    def test_case_022(self):
        driver = self.driver
        print("Test Case 022")

        # 1.Opening Starlink site
        driver.get("https://www.starlink.com/")

        delay()

        # 2.Click on the "BUSINESS" button on the right side of the header
        H.click_Business_button(driver)

        delay()

        # 3.Click on the "FIXED SITE" button on the left side of the header
        H.click_FIXED_SITE_button(driver)

        delay()

        # 4.Check on the "STARLINK FOR FIXED SITES" header
        H.check_STARLINK_FOR_FIXED_SITES_header(driver)

        delay()


    # Test Case 023: Verify / Validate that the "Schedule a Consultation" on the "FIXED SITE" page button is visible and directs the user to the correct page.
    def test_case_023(self):
        driver = self.driver
        print("Test Case 023")

        # 1.Opening Starlink site
        driver.get("https://www.starlink.com/")

        delay()

        # 2.Click on the "BUSINESS" button on the right side of the header
        H.click_Business_button(driver)

        delay()

        # 3.Click on the "FIXED SITE" button on the left side of the header
        H.click_FIXED_SITE_button(driver)

        delay()

        # 4.Check on the "Schedule a Consultation" button
        H.check_Schedule_a_Consultation_form(driver)

        delay()

        # 5.Click "Schedule a Consultation" button
        H.click_Schedule_a_Consultation_button(driver)

        delay()


    # Test Case 024: Verify / Validate that the "SERVICE PLAN" button the "FIXED SITE" line functions correctly and direct the user to the correct page.
    def test_case_024(self):
        driver = self.driver
        print("Test Case 024")

        # 1.Opening Starlink site
        driver.get("https://www.starlink.com/")

        delay()

        # 2.Click on the "BUSINESS" button on the right side of the header
        H.click_Business_button(driver)

        delay()

        # 3.Click on the "FIXED SITE" button on the left side of the header
        H.click_FIXED_SITE_button(driver)

        delay()

        # 4.Scroll until "SERVICE PLANS" button in the line "FIXED SITE"
        driver.find_element(By.XPATH, H.ServicePlans_link).send_keys(Keys.PAGE_DOWN)
        delay()

        # 5.Check "SERVICE PLANS" in the line "FIXED SITE" button.
        H.check_SERVICE_PLANS_button(driver)

        delay()

        # 6.Click "SERVICE PLANS" in the line "FIXED SITE" button
        H.click_Service_Plans_button(driver)

        delay()

    # Test Case 025: Verify / Validate that the "Buyer's guide" on the "FIXED SITE" page button is visible and directs the user to the correct page.
    def test_case_025(self):
        driver = self.driver
        print("Test Case 025")

        # 1.Opening Starlink site
        driver.get("https://www.starlink.com/")

        delay()

        # 2.Click on the "BUSINESS" button on the right side of the header
        H.click_Business_button(driver)

        delay()

        # 3.Click on the "FIXED SITE" button on the left side of the header
        H.click_FIXED_SITE_button(driver)

        delay()

        # 4.Check on the "Buyer's guide" button
        H.check_Buyers_guide_button(driver)

        delay()

        # 5.Click "Buyer's guide" button
        H.click_Buyers_guide_button(driver)

        delay()


def teardown(self):
    self.driver.quit()


class EdgeNegativeTests(unittest.TestCase):

    def setUp(self):
        options = webdriver.EdgeOptions()
        self.driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=options)
        self.driver.maximize_window()


    # Test Case 021_21: Verify / Validate that the "Order Now" button is not working without an address in the "TYPE AND SELECT" line.
    def test_case_021_21(self):
        driver = self.driver
        print("Test Case 021_21")

        # 1.Opening Starlink site
        driver.get("https://www.starlink.com/")

        delay()

        # 2.Click on the "BUSINESS" button on the right side of the header
        H.click_Business_button(driver)

        delay()

        # 3.Click on the "FIXED SITE" button on the left side of the header
        H.click_FIXED_SITE_button(driver)

        delay()

        # 4.Check on the "Order Now" button
        H.check_Order_Now_button(driver)

        delay()

        # 5.Click on the "Order Now" button without selecting a shipping address
        H.click_Order_Now_button(driver)

        delay()


    # Test Case 022_22: Verify / Validate that "SIGN UP" button is not working with email address that the "FIXED SITE" page.
    def test_case_022_22(self):
        driver = self.driver
        print("Test Case 022_22")

        # 1.Opening Starlink site
        driver.get("https://www.starlink.com/")

        delay()

        # 2.Click on the "BUSINESS" button on the right side of the header
        H.click_Business_button(driver)

        time.sleep(5)

        # 3.Click on the "FIXED SITE" button on the left side of the header
        H.click_FIXED_SITE_button(driver)

        delay()

        # 4.Scroll down the page "Interested in staying up to date with Starlink?"
        footer=driver.find_element(By.CSS_SELECTOR,"footer")
        driver.execute_script("arguments[0].scrollIntoView();", footer)
        delay()
        email_input = driver.find_element(By.XPATH, '//input[@type="email"]')
        email_input.is_displayed()
        email_input.click()
        email_input.send_keys(H.Wrong_email_1)
        delay()

        # 5.Click on Sing Up button
        driver.find_element(By.XPATH, H.Click_SingUp_link).click()
        time.sleep(5)
        message=driver.find_element(By.XPATH, "//div[contains(text(),'Thank you for ')]")
        if message:
            print("Test 022_22 is failed")
        else:
            print("Test 022_22 is PASS")

        delay()


    # Test Case 023_23: Verify/Validate that "Place Order" button is not working with no "Contact Information"
    def test_case_023_23(self):
        driver = self.driver
        print("Test Case 023_23")

        # 1.Opening Starlink site
        driver.get("https://www.starlink.com/")

        delay()

        # 2.Click on the "BUSINESS" button on the right side of the header
        H.click_Business_button(driver)

        delay()

        # 3.Click on the "FIXED SITE" button on the left side of the header
        H.click_FIXED_SITE_button(driver)

        delay()

        # 4.Click on the "Order Now" button
        H.click_Order_Now_button(driver)

        time.sleep(5)

        message = driver.find_element(By.XPATH,"(//div[contains(.,'To view available Starlink products in your area, please provide your address or start with your current location.')])[9]")
        if message:
            print("Test 023_23 is PASS")
        else:
            print("Test 023_23 is failed")

        delay()

    # Test Case 024_24: Verify/Validate that "Place Order" button is not working with no "Contact Information"
    def test_case_024_24(self):
        driver = self.driver
        print("Test Case 024_24")

        # 1.Opening Starlink site
        driver.get("https://www.starlink.com/order?processorToken=ee4c13dc-0e6f-44b9-9891-58c68ca5c679&step=1")

        delay()

        # 2.Click on "Checkout" button
        H.click_Checkout_button(driver)
        delay()

        # 3.Input an incorrect email address in the "Email" field
        wrong_email2_input = driver.find_element(By.XPATH, "//input[@name='email']")
        wrong_email2_input.is_displayed()
        wrong_email2_input.clear()
        wrong_email2_input.send_keys(H.Wrong_email_2)
        driver.find_element(By.XPATH, "//input[@name='phone']").click()
        delay()

        try:
            message = driver.find_element(By.XPATH, "//span[@xpath='1']")
            if message:
                print("Test 024_24 is PASS")
            else:
                print("Test 024_24 is Failed")
        except WDE:
            print("Test 024_24 is Failed")

        delay()


    # Test Case 025_25: Verify/Validate that if you enter an incorrect phone number in the "Checkout" section, the site will say "Invalid phone number"
    def test_case_025_25(self):
        driver = self.driver
        print("Test Case 025_25")

        # 1.Opening Starlink site
        driver.get("https://www.starlink.com/order?processorToken=ee4c13dc-0e6f-44b9-9891-58c68ca5c679&step=1")

        delay()

        # 2.Click on "Checkout" button
        H.click_Checkout_button(driver)

        delay()

        # 3.Input an incorrect email address in the "Phone number" field
        wrong_phone_input = driver.find_element(By.XPATH, "//input[@name='phone']")
        wrong_phone_input.is_displayed()
        wrong_phone_input.clear()
        wrong_phone_input.send_keys(H.Wrong_PN)
        driver.find_element(By.XPATH, "//input[@name='email']").click()

        delay()

        message = driver.find_element(By.XPATH, "//span[contains(.,'Invalid phone number')]")
        if message:
            print("Test 025_25 is PASS")
        else:
            print("Test 025_25 is Failed")


def teardown(self):
    self.driver.quit()

#if __name__ == '__main__':
#   unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./HtmlReports'))

if __name__ == "__main__":
    unittest.main(AllureReports)



# if __name__ == "__main__":
#    unittest.main()