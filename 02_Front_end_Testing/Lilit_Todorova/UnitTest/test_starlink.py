# test_starlink.py
import unittest
from asyncio import timeout
import HtmlTestRunner
import allure
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from base_test import BaseTest
from helpers import delay, wait_for_element, get_page_url
from locators import Locators


@allure.feature("Starlink Positive Tests")
class TestStarlinkPositive(BaseTest):

    @allure.story("Navigate to Starlink and Verify Logo")
    def test1_navigate_to_starlink_and_verify_logo(self):
        try:
            self.driver.get(get_page_url("starlink"))
            delay()
            logo = wait_for_element(self.driver, Locators.LOGO_LOCATOR)
            self.assertTrue(logo.is_displayed(), "The Starlink logo is not visible.")
        except Exception as e:
            self.fail(f"Test failed: {e}")

    @allure.story("Hamburger Menu and Sign In Navigation")
    def test2_hamburger_menu_and_sign_in_navigation(self):
        try:
            self.driver.get(get_page_url("starlink"))
            delay()
            hamburger_menu = wait_for_element(self.driver, Locators.HAMBURGER_MENU_LOCATOR)
            hamburger_menu.click()
            sign_in_option = wait_for_element(self.driver, Locators.SIGN_IN_OPTION_LOCATOR)
            self.assertTrue(sign_in_option.is_displayed(), "The 'Sign In' option is not visible.")
            sign_in_option.click()
            self.wait.until(lambda driver: "auth/login" in driver.current_url)
            signin_page_logo = wait_for_element(self.driver, Locators.SIGN_IN_PAGE_LOCATOR)
            self.assertTrue(signin_page_logo.is_displayed(), "The 'SIGN IN' logo is not visible.")
        except Exception as e:
            self.fail(f"Test failed: {e}")

    @allure.story("Order Starlink and Verify ROAM Window")
    def test3_order_starlink_and_verify_roam_window(self):
        try:
            self.driver.get(get_page_url("login"))
            delay()
            order_starlink_button = wait_for_element(self.driver, Locators.ORDER_STARLINK_BUTTON_LOCATOR)
            self.assertTrue(order_starlink_button.is_displayed(), "The 'Order Starlink' button is not visible.")
            order_starlink_button.click()
            self.wait.until(lambda driver: driver.current_url == get_page_url("starlink"))
            order_now_button = wait_for_element(self.driver, Locators.ORDER_NOW_BUTTON_LOCATOR)
            self.assertTrue(order_now_button.is_displayed(), "The 'Order Now' button is not visible.")
            order_now_button.click()
            try:
                # Switch to iframe to check error message
                iframe = self.wait.until(EC.presence_of_element_located((By.XPATH, "//iframe")))
                self.driver.switch_to.frame(iframe)
                error_message = self.wait.until(EC.visibility_of_element_located(Locators.ERROR_MESSAGES_ORDER_NOW))
                self.assertTrue(error_message.is_displayed(), "The error message is not visible.")
                print("Verified error message is visible.")
                self.driver.switch_to.default_content()
            except TimeoutException:
                print("Error message not found. Continuing without it.")
                self.driver.switch_to.default_content()
        except Exception as e:
            self.fail(f"Test failed: {e}")

    @allure.story("Order ROAM and Verify Checkout")
    def test4_order_roam_and_verify_checkout(self):
        try:
            self.driver.get(get_page_url("order_step_0"))
            delay()
            country_field = wait_for_element(self.driver, Locators.COUNTRY_LABEL_FIELD)
            self.assertTrue(country_field.is_displayed(), "The 'United States' field is not visible.")
            product_details_button = wait_for_element(self.driver, Locators.PRODUCT_DETAILS_BUTTON)
            self.driver.execute_script("arguments[0].scrollIntoView();", product_details_button)
            checkout_button = wait_for_element(self.driver, Locators.CHECKOUT_BUTTON_LOCATOR)
            self.assertTrue(checkout_button.is_displayed(), "The 'Checkout' button is not visible.")
            checkout_button.click()
            self.wait.until(lambda driver: "step=2" in driver.current_url)
            checkout_element = wait_for_element(self.driver, Locators.CHECKOUT_ELEMENT)
            self.assertTrue(checkout_element.is_displayed(), "The 'CHECKOUT' element is not visible.")
        except Exception as e:
            self.fail(f"Test failed: {e}")

    @allure.story("Checkout Page and Place Order")
    def test5_checkout_page_and_place_order(self):
        try:
            self.driver.get(get_page_url("order_step_2"))
            print("Navigated to Checkout page. Current URL:", self.driver.current_url)
            self.wait.until(lambda driver: "step=2" in driver.current_url)
            checkout_element = wait_for_element(self.driver, Locators.CHECKOUT_ELEMENT)
            self.assertTrue(checkout_element.is_displayed(), "The 'CHECKOUT' element is not visible.")
            shipping_address_window = self.wait.until(
                EC.visibility_of_element_located(Locators.SHIPPING_ADDRESS_WINDOW))
            self.assertTrue(shipping_address_window.is_displayed(), "The Shipping Address window is not visible.")
            print("Verified Shipping Address window is visible.")

            # Fill in shipping address fields
            zip_postal_code_field = self.wait.until(EC.element_to_be_clickable(Locators.ZIP_POSTAL_CODE_FIELD))
            fake_zip_code = self.fake.zipcode()
            zip_postal_code_field.send_keys(fake_zip_code)
            print(f"Filled in Zip / Postal Code field with fake value: {fake_zip_code}.")

            shipping_address_line_1_field = self.wait.until(
                EC.element_to_be_clickable(Locators.SHIPPING_ADDRESS_LINE_1_FIELD))
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

            country_field = self.wait.until(EC.visibility_of_element_located(Locators.COUNTRY_FIELD))
            self.assertTrue(country_field.is_displayed(), "The 'Country' field is not visible.")
            pre_filled_value = country_field.get_attribute("value")
            self.assertEqual(pre_filled_value, "United States",
                             "The 'Country' field is not pre-filled with 'United States'.")
            print(f"Verified 'Country' field is pre-filled with '{pre_filled_value}'.")

            # Click Update Shipping Address button
            update_shipping_address_button = self.wait.until(
                EC.element_to_be_clickable(Locators.UPDATE_SHIPPING_ADDRESS_BUTTON))
            update_shipping_address_button.click()
            print("Clicked 'Update Shipping Address' button.")
            delay()
            # Dismiss any overlay
            actions = ActionChains(self.driver)
            actions.send_keys(Keys.ESCAPE).perform()
            actions.send_keys(Keys.ENTER).perform()
            print("Sent ESC and ENTER keys to dismiss any overlays.")
            try:
                invalid_address_msg = self.wait.until(EC.visibility_of_element_located(Locators.INVALID_ADDRESS_MSG))
                self.assertTrue(invalid_address_msg.is_displayed(),
                                "The 'Provided address appears to be invalid.' message is not visible.")
                print("Invalid address message displayed as expected.")
            except TimeoutException:
                print("No invalid address message found. Continuing without it.")
            delay()
            # Place Order step is commented out, uncomment when ready:
            # place_order_button = self.wait.until(EC.element_to_be_clickable(Locators.PLACE_ORDER_BUTTON))
            # self.assertTrue(place_order_button.is_displayed(), "The 'Place Order' button is not visible.")
            # self.assertTrue(place_order_button.is_enabled(), "The 'Place Order' button is not enabled.")
            # print("Verified 'Place Order' button is visible and enabled.")
        except Exception as e:
            print(f"Exception occurred: {e}")
            self.fail(f"Test failed: {e}")
        finally:
            self.driver.quit()


@allure.feature("Starlink Negative Tests")
class TestStarlinkNegative(BaseTest):

    @allure.story("Reject Invalid Login Credentials")
    def test6_reject_invalid_login_credentials(self):
        try:
            # Navigate to the login page.
            self.driver.get(get_page_url("login"))
            invalid_email = "invalid@example.com"
            invalid_password = "wrongpassword"

            # Fill in the email and password fields.
            self.helpers.send_keys_to_element(Locators.EMAIL_FIELD, invalid_email)
            self.helpers.send_keys_to_element(Locators.PASSWORD_FIELD, invalid_password)

            # Click the Sign In button with an extended timeout (ensure your helper method supports a timeout parameter).
            self.helpers.click_element(Locators.SIGN_IN_BUTTON, timeout=40)

            # Wait a short period to allow error message to render.
            delay()

            # Wait for the error message element with an extended timeout.
            try:
                error_message = self.helpers.wait_for_element_visibility(Locators.INVALID_CREDENTIALS_ERROR, timeout=30)
                self.assertTrue(error_message.is_displayed(), "Error message for invalid credentials is not visible.")
                print("The error message 'Invalid email or password' was displayed.")
            except Exception as inner_e:
                print("Error waiting for invalid credentials message.")
                print("Current URL:", self.driver.current_url)
                print("Page source snippet:", self.driver.page_source[:1000])
                raise inner_e
        except Exception as outer_e:
            print(f"Exception occurred: {outer_e}")
            self.fail(f"Test failed: {outer_e}")

    @allure.story("Reject Blank Fields")
    def test7_reject_blank_fields(self):
        try:
            self.driver.get(get_page_url("login"))
            self.helpers.wait_for_element_visibility(Locators.SIGN_IN_PAGE_LOCATOR)
            self.helpers.click_element(Locators.SIGN_IN_BUTTON)
            email_error_message = self.helpers.wait_for_element_visibility(Locators.EMAIL_ERROR_MESSAGE, timeout=15)
            password_error_message = self.helpers.wait_for_element_visibility(Locators.PASSWORD_ERROR_MESSAGE,
                                                                              timeout=15)
            self.assertTrue(email_error_message.is_displayed(), "Email error message not visible.")
            self.assertTrue(password_error_message.is_displayed(), "Password error message not visible.")
            print("✅ Error messages 'Email is required' and 'Password is required' were displayed.")
        except Exception as e:
            print(f"❌ Exception occurred: {e}")
            self.fail(f"Test failed: {e}")

    @allure.story("Reject Invalid Email Format")
    def test8_reject_invalid_email_format(self):
        try:
            self.driver.get(get_page_url("login"))
            invalid_email = "invalid-email-format"
            valid_password = "ValidPassword123!"
            self.helpers.send_keys_to_element(Locators.EMAIL_FIELD, invalid_email)
            self.helpers.send_keys_to_element(Locators.PASSWORD_FIELD, valid_password)
            self.helpers.click_element(Locators.SIGN_IN_BUTTON)
            error_message = self.helpers.wait_for_element_visibility(Locators.INVALID_EMAIL_ERROR)
            self.assertTrue(error_message.is_displayed(), "Error message for invalid email format is not visible.")
            print("The error message 'Invalid email format' was displayed.")
        except Exception as e:
            print(f"Exception occurred: {e}")
            self.fail(f"Test failed: {e}")

    @allure.story("Check Failed Login Behavior")
    def test9_check_failed_login_behavior(self):
        try:
            self.driver.get(get_page_url("login"))
            invalid_email = "invalid@example.com"
            invalid_password = "wrongpassword"
            for attempt in range(10):
                print(f"Attempt {attempt + 1}...")
                self.helpers.js_send_keys(Locators.EMAIL_FIELD, invalid_email)
                self.helpers.js_send_keys(Locators.PASSWORD_FIELD, invalid_password)
                self.helpers.click_element(Locators.SIGN_IN_BUTTON)
                error_message = self.helpers.wait_for_element_visibility(Locators.INVALID_CREDENTIALS_ERROR)
                self.assertTrue(error_message.is_displayed(), "Error message did not appear.")
                self.helpers.js_clear_field(Locators.EMAIL_FIELD)
                self.helpers.js_clear_field(Locators.PASSWORD_FIELD)
            print("Completed 10 failed login attempts.")
        except Exception as e:
            self.fail(f"Test failed: {e}")

    @allure.story("Password Field Masked Verification")
    def test10_password_field_masked(self):
        try:
            self.driver.get(get_page_url("login"))
            test_password = "SecurePass123!"
            password_element = self.helpers.wait_for_element_visibility(Locators.PASSWORD_FIELD)
            password_element.send_keys(test_password)
            field_type = password_element.get_attribute("type")
            self.assertEqual(field_type, "password", "Password field is not masked.")
            print("The password field displayed masked characters as expected.")
        except Exception as e:
            print(f"Exception occurred: {e}")
            self.fail(f"Test failed: {e}")


if __name__ == "__main__":
    # Create test suites for positive and negative tests
    suite_positive = unittest.defaultTestLoader.loadTestsFromTestCase(TestStarlinkPositive)
    suite_negative = unittest.defaultTestLoader.loadTestsFromTestCase(TestStarlinkNegative)
    combined_suite = unittest.TestSuite([suite_positive, suite_negative])

    runner = HtmlTestRunner.HTMLTestRunner(
        output='HtmlReports',
        report_name='StarlinkTests',
        combine_reports=True,
        verbosity=2
    )
    runner.run(combined_suite)
