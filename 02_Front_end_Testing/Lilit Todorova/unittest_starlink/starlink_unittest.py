import unittest

from faker import Faker
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers import setup_driver, delay, wait_for_element, get_page_url, Helpers
from locators import Locators

class TestStarlinkPositive(unittest.TestCase):
    def setUp(self):
        # Set up WebDriver before each test.
        # Change to "firefox" or "edge" for cross-browser testing
        self.driver = setup_driver("chrome")
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 30)
        self.fake = Faker()

    def tearDown(self):
        # Close the browser after each test.
        self.driver.quit()

    def test1_navigate_to_starlink_and_verify_logo(self):

        # Test Case 1: Navigate to Starlink and verify the logo is visible.
        try:
            self.driver.get(get_page_url("starlink"))
            delay()
            logo = wait_for_element(self.driver, Locators.LOGO_LOCATOR)
            self.assertTrue(logo.is_displayed(), "The Starlink logo is not visible.")
        except Exception as e:
            self.fail(f"Test failed: {e}")

    def test2_hamburger_menu_and_sign_in_navigation(self):
        # Test Case 2: Open the hamburger menu, click "Sign In," and verify navigation to the login page.
        try:
            self.driver.get(get_page_url("starlink"))
            delay()

            # Click the hamburger menu
            hamburger_menu = wait_for_element(self.driver, Locators.HAMBURGER_MENU_LOCATOR)
            hamburger_menu.click()

            # Verify and click the "Sign In" option
            sign_in_option = wait_for_element(self.driver, Locators.SIGN_IN_OPTION_LOCATOR)
            self.assertTrue(sign_in_option.is_displayed(), "The 'Sign In' option is not visible.")
            sign_in_option.click()

            # Verify navigation to the login page
            self.wait.until(lambda driver: "auth/login" in driver.current_url)
            signin_page_logo = wait_for_element(self.driver, Locators.SIGN_IN_PAGE_LOCATOR)
            self.assertTrue(signin_page_logo.is_displayed(), "The 'SIGN IN' logo is not visible.")
        except Exception as e:
            self.fail(f"Test failed: {e}")

    def test3_order_starlink_and_verify_roam_window(self):
       # Test Case 3: Navigate to the Starlink homepage, order Starlink, and verify the ROAM window.
        try:
            self.driver.get(get_page_url("login"))
            delay()

            # Verify and click the "Order Starlink" button
            order_starlink_button = wait_for_element(self.driver, Locators.ORDER_STARLINK_BUTTON_LOCATOR)
            self.assertTrue(order_starlink_button.is_displayed(), "The 'Order Starlink' button is not visible.")
            order_starlink_button.click()

            # Verify navigation to the homepage
            self.wait.until(lambda driver: driver.current_url == get_page_url("starlink"))

            # Verify and click the "Order Now" button in the ROAM window
            order_now_button = wait_for_element(self.driver, Locators.ORDER_NOW_BUTTON_LOCATOR)
            self.assertTrue(order_now_button.is_displayed(), "The 'Order Now' button is not visible.")
            order_now_button.click()

            # Verify the error message (if applicable)
            try:
                # Step 1: Locate the iframe and switch to it
                iframe = self.wait.until(EC.presence_of_element_located((By.XPATH, "//iframe")))
                self.driver.switch_to.frame(iframe)

                # Step 2: Locate the error message inside the iframe
                error_message = self.wait.until(EC.visibility_of_element_located(Locators.ERROR_MESSAGE_LOCATOR))
                self.assertTrue(error_message.is_displayed(), "The error message is not visible.")
                print("Verified error message is visible.")

                # Step 3: Switch back to the default content
                self.driver.switch_to.default_content()

            except TimeoutException:
                # If the iframe or error message is not found, handle the exception
                print("Error message not found. Continuing without verifying the error message.")
                self.driver.switch_to.default_content()  # Ensure we switch back to the default content even if an exception occurs
        except Exception as e:
            self.fail(f"Test failed: {e}")

    def test4_order_roam_and_verify_checkout(self):
        # Test Case 4: Order ROAM and verify the checkout process.
        try:
            self.driver.get(get_page_url("order_step_0"))
            delay()

            # Verify country field
            country_field = wait_for_element(self.driver, Locators.COUNTRY_LABEL_FIELD)
            self.assertTrue(country_field.is_displayed(), "The 'United States' field is not visible.")

            # Scroll down to product details
            product_details_button = wait_for_element(self.driver, Locators.PRODUCT_DETAILS_BUTTON)
            self.driver.execute_script("arguments[0].scrollIntoView();", product_details_button)

            # Verify and click the "Checkout" button
            checkout_button = wait_for_element(self.driver, Locators.CHECKOUT_BUTTON_LOCATOR)
            self.assertTrue(checkout_button.is_displayed(), "The 'Checkout' button is not visible.")
            checkout_button.click()

            # Verify navigation to the checkout page
            self.wait.until(lambda driver: "step=2" in driver.current_url)
            checkout_element = wait_for_element(self.driver, Locators.CHECKOUT_ELEMENT)
            self.assertTrue(checkout_element.is_displayed(), "The 'CHECKOUT' element is not visible.")
        except Exception as e:
            self.fail(f"Test failed: {e}")

    def test5_checkout_page_and_place_order(self):
        try:
            # Step 1: Navigate to the "Checkout" page
            self.driver.get(get_page_url("order_step_2"))
            print("Navigated to Checkout page. Current URL:", self.driver.current_url)

            # Step 2: Verify that the checkout page loads successfully
            shipping_address_window = self.wait.until(EC.visibility_of_element_located(Locators.SHIPPING_ADDRESS_WINDOW))
            self.assertTrue(shipping_address_window.is_displayed(), "The Shipping Address window is not visible.")
            print("Verified Shipping Address window is visible.")

            # Step 3: Fill in the Shipping Address fields with fake credentials using Faker
            zip_postal_code_field = self.wait.until(EC.element_to_be_clickable(Locators.ZIP_POSTAL_CODE_FIELD))
            fake_zip_code = self.fake.zipcode()
            zip_postal_code_field.send_keys(fake_zip_code)
            print(f"Filled in Zip / Postal Code field with fake value: {fake_zip_code}.")

            shipping_address_line_1_field = self.wait.until(EC.element_to_be_clickable(Locators.SHIPPING_ADDRESS_LINE_1_FIELD))
            fake_street_address = self.fake.street_address()
            shipping_address_line_1_field.send_keys(fake_street_address)
            print(f"Filled in Shipping Address Line 1 field with fake value: {fake_street_address}.")

            city_field = self.wait.until(EC.element_to_be_clickable(Locators.CITY_FIELD))
            fake_city = self.fake.city()
            city_field.send_keys(fake_city)
            print(f"Filled in City field with fake value: {fake_city}.")

            state_province_field = self.wait.until(EC.element_to_be_clickable(Locators.STATE_PROVINCE_FIELD))
            fake_state = self.fake.state()
            state_province_field.send_keys(fake_state)
            print(f"Filled in State / Province field with fake value: {fake_state}.")

            # Step 4: Verify the Country field is pre-filled with "United States"
            country_field = self.wait.until(EC.visibility_of_element_located(Locators.COUNTRY_FIELD))
            self.assertTrue(country_field.is_displayed(), "The 'Country' field is not visible.")

            pre_filled_value = country_field.get_attribute("value")
            self.assertEqual(pre_filled_value, "United States",
                             "The 'Country' field is not pre-filled with 'United States'.")
            print(f"Verified 'Country' field is pre-filled with '{pre_filled_value}'.")

            # Step 5: Verify that the "Update Shipping Address" button is visible and click on it
            update_shipping_address_button = self.wait.until(EC.element_to_be_clickable(Locators.UPDATE_SHIPPING_ADDRESS_BUTTON))
            self.assertTrue(update_shipping_address_button.is_displayed(),
                            "The 'Update Shipping Address' button is not visible.")
            update_shipping_address_button.click()
            print("Clicked 'Update Shipping Address' button.")

            delay()

            # # In a small window, click on the "Close" button if it exists
            # try:
            #     close_button = self.wait.until(EC.element_to_be_clickable(Locators.CLOSE_BUTTON))
            #     close_button.click()
            #     print("Clicked 'Close' button.")
            # except TimeoutException:
            #     print("Close button not found. Continuing without clicking it.")
            #
            # # Step 6: Verify that the "Place Order" button is visible and activated
            # place_order_button = self.wait.until(EC.element_to_be_clickable(Locators.PLACE_ORDER_BUTTON))
            # self.assertTrue(place_order_button.is_displayed(), "The 'Place Order' button is not visible.")
            # self.assertTrue(place_order_button.is_enabled(), "The 'Place Order' button is not enabled.")
            # print("Verified 'Place Order' button is visible and enabled.")

        except Exception as e:
            print(f"Exception occurred: {e}")
            self.fail(f"Test failed: {e}")

        finally:
            self.driver.quit()

class TestStarlinkNegative(unittest.TestCase):
    def __init__(self, methodName: str = "runTest"):
        super().__init__(methodName)
        self.helpers = None

    def setUp(self):
        # Set up WebDriver before each test.
        self.driver = setup_driver("chrome")  # Change to "firefox" or "edge" for cross-browser testing
        self.driver.maximize_window()
        self.helpers = Helpers(self.driver)
        self.fake = Faker()

    def tearDown(self):
        # Close the browser after each test.
        self.driver.quit()

    def test6_reject_invalid_login_credentials(self):

        # Ensure that the system rejects invalid login credentials.
        try:
            # Step 1: Navigate to the "Sign In" page
            self.driver.get(get_page_url("login"))

            # Step 2: Enter an invalid email and password
            invalid_email = "invalid@example.com"
            invalid_password = "wrongpassword"
            self.helpers.send_keys_to_element(Locators.EMAIL_FIELD, invalid_email)
            self.helpers.send_keys_to_element(Locators.PASSWORD_FIELD, invalid_password)

            # Step 3: Click the "Sign In" button
            self.helpers.click_element(Locators.SIGN_IN_BUTTON)

            # Step 4: Verify the error message displayed
            error_message = self.helpers.wait_for_element_visibility(Locators.INVALID_CREDENTIALS_ERROR)
            self.assertTrue(error_message.is_displayed(), "Error message for invalid credentials is not visible.")

            print("The error message 'Invalid email or password' was displayed.")

        except Exception as e:
            print(f"Exception occurred: {e}")
            self.fail(f"Test failed: {e}")

    def test7_reject_blank_fields(self):

         # Ensure that the system does not allow blank fields during sign-in.

        try:
            # Step 1: Navigate to the "Sign In" page
            self.driver.get(get_page_url("login"))

            # Step 2: Leave both email and password fields empty

            # Step 3: Click outside to trigger validation
            self.helpers.click_element(Locators.LOGIN_PAGE_TITLE)

            # Step 4: Click the "Sign In" button
            self.helpers.click_element(Locators.SIGN_IN_BUTTON)

            # Step 5: Wait for error messages to appear
            email_error_message = self.helpers.wait_for_element_visibility(Locators.EMAIL_ERROR_MESSAGE, timeout=15)
            password_error_message = self.helpers.wait_for_element_visibility(Locators.PASSWORD_ERROR_MESSAGE,
                                                                              timeout=15)

            # Assertions
            self.assertTrue(email_error_message.is_displayed(), "Email error message not visible.")
            self.assertTrue(password_error_message.is_displayed(), "Password error message not visible.")

            print("✅ Error messages 'Email is required' and 'Password is required' were displayed.")

        except Exception as e:
            print(f"❌ Exception occurred: {e}")
            self.fail(f"Test failed: {e}")

    def test8_reject_invalid_email_format(self):

        # Ensure that the system rejects invalid email formats during sign-in.

        try:
            # Step 1: Navigate to the "Sign In" page
            self.driver.get(get_page_url("login"))

            # Step 2: Enter an invalid email format and a valid password
            invalid_email = "invalid-email-format"
            valid_password = "ValidPassword123!"
            self.helpers.send_keys_to_element(Locators.EMAIL_FIELD, invalid_email)
            self.helpers.send_keys_to_element(Locators.PASSWORD_FIELD, valid_password)

            # Step 3: Click the "Sign In" button
            self.helpers.click_element(Locators.SIGN_IN_BUTTON)

            # Step 4: Verify the error message for invalid email format
            error_message = self.helpers.wait_for_element_visibility(Locators.INVALID_EMAIL_ERROR)
            self.assertTrue(error_message.is_displayed(), "Error message for invalid email format is not visible.")

            print("The error message 'Invalid email format' was displayed.")

        except Exception as e:
            print(f"Exception occurred: {e}")
            self.fail(f"Test failed: {e}")

    def test9_check_failed_login_behavior(self):

        # Ensure that the system handles multiple failed login attempts correctly.

        try:
            self.driver.get(get_page_url("login"))
            invalid_email = "invalid@example.com"
            invalid_password = "wrongpassword"

            for attempt in range(10):
                print(f"Attempt {attempt + 1}...")

                # Use JavaScript to clear and input values
                self.helpers.js_send_keys(Locators.EMAIL_FIELD, invalid_email)
                self.helpers.js_send_keys(Locators.PASSWORD_FIELD, invalid_password)

                self.helpers.click_element(Locators.SIGN_IN_BUTTON)
                error_message = self.helpers.wait_for_element_visibility(Locators.INVALID_CREDENTIALS_ERROR)
                self.assertTrue(error_message.is_displayed(), "Error message did not appear.")

                # Clear fields using JavaScript after error appears
                self.helpers.js_clear_field(Locators.EMAIL_FIELD)
                self.helpers.js_clear_field(Locators.PASSWORD_FIELD)

            print("Completed 10 failed login attempts.")

        except Exception as e:
            self.fail(f"Test failed: {e}")

    def test10_password_field_masked(self):

        # Ensure that the password field is masked during sign-in.

        try:
            # Step 1: Navigate to the "Sign In" page
            self.driver.get(get_page_url("login"))

            # Step 2: Enter a password in the password field
            test_password = "SecurePass123!"

            # Use an existing helper method to retrieve the element
            password_element = self.helpers.wait_for_element_visibility(Locators.PASSWORD_FIELD)
            password_element.send_keys(test_password)

            # Step 3: Verify that the password field is masked
            field_type = password_element.get_attribute("type")
            self.assertEqual(field_type, "password", "Password field is not masked.")

            print("The password field displayed masked characters as expected.")

        except Exception as e:
            print(f"Exception occurred: {e}")
            self.fail(f"Test failed: {e}")

if __name__ == "__main__":
    unittest.main()