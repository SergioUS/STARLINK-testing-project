import time
import random
import unittest
from time import sleep
import driver
import pytest
import Helpers_P as HP
import Helpers_N as HN
from unittest import TestCase
from selenium import webdriver
from selenium.common.exceptions import WebDriverException as WDE
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options



def delay():
    time.sleep(random.randint(1, 3))



class ChromePositiveTestes(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.page_load_strategy = 'eager'
        options.add_argument("--disable-blink-features=AutomationControlled")
        #options.add_argument('--headless')
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.driver.maximize_window()
        self.driver.minimize_window()
        self.driver.maximize_window()


    def test_Positive_Starlink_TC_031(self):
        driver = self.driver
        print("Positive TC-031")
        driver.get(HP.starlink_url)
        wait = WebDriverWait(driver, 3)
        wait.until(EC.visibility_of_element_located((By.XPATH, HP.home_page_logo)))

        # Check Starlink Url

        HP.check_starlink_url(driver)

        # Check Starlink title

        HP.assert_title(driver, "Starlink")

        # Check Residential button

        HP.check_residential_button(driver)


        driver.quit()

    def test_Positive_Starlink_TC_032(self):
        driver = self.driver
        print("Positive TC-032")
        driver.get(HP.starlink_url)
        wait = WebDriverWait(driver, 3)
        wait.until(EC.visibility_of_element_located((By.XPATH, HP.home_page_logo)))

        # Check Starlink Url

        HP.check_starlink_url(driver)

        # Check Starlink title

        HP.assert_title(driver, "Starlink")

        # Click Residential button

        HP.click_residential_button(driver)
        delay()

        # Check Starlink Residential Url

        HP.check_residential_url(driver)

        # Check Starlink Residential title

        HP.check_residential_title(driver)

        # Click Order Now button

        HP.check_oder_now_button(driver)

        driver.quit()

    def test_Positive_Starlink_TC_033(self):
        driver = self.driver
        print("Positive TC-033")
        driver.get(HP.starlink_url)
        wait = WebDriverWait(driver, 3)
        wait.until(EC.visibility_of_element_located((By.XPATH, HP.home_page_logo)))

        # Check Starlink Url

        HP.check_starlink_url(driver)

        # Check Starlink title

        HP.assert_title(driver, "Starlink")

        # Click Residential button

        HP.click_residential_button(driver)
        delay()

        # Check Starlink Residential Url

        HP.check_residential_url(driver)

        # Check Starlink Residential title

        HP.check_residential_title(driver)

        # Click View Availability & Speeds Map button

        HP.check_map_button(driver)

        driver.quit()

    def test_Positive_Starlink_TC_034(self):
        driver = self.driver
        print("Positive TC-034")
        driver.get(HP.starlink_url)
        wait = WebDriverWait(driver, 3)
        wait.until(EC.visibility_of_element_located((By.XPATH, HP.home_page_logo)))

        # Check Starlink Url

        HP.check_starlink_url(driver)

        # Check Starlink title

        HP.assert_title(driver, "Starlink")

        # Click Residential button

        HP.click_residential_button(driver)
        delay()

        # Check Starlink Residential Url

        HP.check_residential_url(driver)

        # Check Starlink Residential title

        HP.check_residential_title(driver)

        # Find elements to scroll to
        elements = driver.find_elements(By.XPATH,HP.all_plans )

        # Scroll to  element
        driver.find_element(By.XPATH, HP.all_plans).send_keys(Keys.PAGE_DOWN)
        delay()

        # Check  View All Plans button

        HP.check_all_plans_button(driver)

        driver.quit()

    def test_Positive_Starlink_TC_035(self):
        driver = self.driver
        print("Positive TC-035")
        driver.get(HP.starlink_url)
        wait = WebDriverWait(driver, 3)
        wait.until(EC.visibility_of_element_located((By.XPATH, HP.home_page_logo)))

        # Check Starlink Url

        HP.check_starlink_url(driver)

        # Check Starlink title

        HP.assert_title(driver, "Starlink")

        # Click Residential button

        HP.click_residential_button(driver)
        delay()

        # Check Starlink Residential Url

        HP.check_residential_url(driver)

        # Check Starlink Residential title

        HP.check_residential_title(driver)

        # Find elements to scroll to
        elements = driver.find_elements(By.XPATH, HP.service_plans)

        # Scroll to  element
        driver.find_element(By.XPATH, HP.service_plans).send_keys(Keys.PAGE_DOWN)
        delay()

        # Check  View All Plans button

        HP.check_service_plans_button(driver)

        driver.quit()

    def test_Positive_Starlink_TC_036(self):
        driver = self.driver
        print("Positive TC-036")
        driver.get(HP.starlink_url)
        wait = WebDriverWait(driver, 3)
        wait.until(EC.visibility_of_element_located((By.XPATH, HP.home_page_logo)))

        # Check Starlink Url

        HP.check_starlink_url(driver)

        # Check Starlink title

        HP.assert_title(driver, "Starlink")

        # Click Residential button

        HP.click_residential_button(driver)
        delay()

        # Check Starlink Residential Url

        HP.check_residential_url(driver)

        # Check Starlink Residential title

        HP.check_residential_title(driver)

        # Scroll to  element
        driver.find_element(By.XPATH,HP.specifications).send_keys(Keys.PAGE_DOWN)
        delay()
            # Check  View All Plans button

        HP.check_specifications_button(driver)

        driver.quit()

    def test_Positive_Starlink_TC_037(self):
        driver = self.driver
        print("Positive TC-037")
        driver.get(HP.starlink_url)
        wait = WebDriverWait(driver, 3)
        wait.until(EC.visibility_of_element_located((By.XPATH, HP.home_page_logo)))

        # Check Starlink Url

        HP.check_starlink_url(driver)

        # Check Starlink title

        HP.assert_title(driver, "Starlink")

        # Click Residential button

        HP.click_residential_button(driver)
        delay()

        # Check Starlink Residential Url

        HP.check_residential_url(driver)

        # Check Starlink Residential title

        HP.check_residential_title(driver)

        # Scroll to  element

        driver.find_element(By.XPATH,HP.faqs).send_keys(Keys.PAGE_DOWN)
        delay()

        # Check  FAQs button

        HP.check_faqs_button(driver)

        driver.quit()

    def test_Positive_Starlink_TC_038(self):
        driver = self.driver
        print("Positive TC-038")
        driver.get(HP.starlink_url)
        wait = WebDriverWait(driver, 3)
        wait.until(EC.visibility_of_element_located((By.XPATH, HP.home_page_logo)))

        # Check Starlink Url

        HP.check_starlink_url(driver)

        # Check Starlink title

        HP.assert_title(driver, "Starlink")

        # Click Residential button

        HP.click_residential_button(driver)
        delay()

        # Check Starlink Residential Url

        HP.check_residential_url(driver)

        # Check Starlink Residential title

        HP.check_residential_title(driver)

        # Scroll to  element

        driver.find_element(By.XPATH,HP.video).send_keys(Keys.PAGE_DOWN)
        delay()

        # Check Play Video button

        HP.check_video_button(driver)

        driver.quit()

    def test_Positive_Starlink_TC_039(self):
        driver = self.driver
        print("Positive TC-039")
        driver.get(HP.starlink_url)
        wait = WebDriverWait(driver, 3)
        wait.until(EC.visibility_of_element_located((By.XPATH, HP.home_page_logo)))

        # Check Starlink Url

        HP.check_starlink_url(driver)

        # Check Starlink title

        HP.assert_title(driver, "Starlink")

        # Click Residential button

        HP.click_residential_button(driver)
        delay()

        # Check Starlink Residential Url

        HP.check_residential_url(driver)

        # Check Starlink Residential title

        HP.check_residential_title(driver)

        # Scroll to element

        driver.find_element(By.XPATH,HP.android).send_keys(Keys.PAGE_DOWN)
        delay()

        # Check  Download for android button

        HP.check_download_for_android_button(driver)

        driver.quit()

    def test_Positive_Starlink_TC_040(self):
        driver = self.driver
        print("Positive TC-040")
        driver.get(HP.starlink_url)
        wait = WebDriverWait(driver, 3)
        wait.until(EC.visibility_of_element_located((By.XPATH, HP.home_page_logo)))

        # Check Starlink Url

        HP.check_starlink_url(driver)

        # Check Starlink title

        HP.assert_title(driver, "Starlink")

        # Click Residential button

        HP.click_residential_button(driver)
        delay()

        # Check Starlink Residential Url

        HP.check_residential_url(driver)

        # Check Starlink Residential title

        HP.check_residential_title(driver)

        # Scroll to  element

        driver.find_element(By.XPATH,HP.ios).send_keys(Keys.PAGE_DOWN)
        delay()

        # Check  Download for iOS button

        HP.check_download_for_ios_button(driver)

        driver.quit()

class ChromeNegativeTestes(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.page_load_strategy = 'eager'
        #options.add_argument("--disable-blink-features=AutomationControlled")
        #options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 Edg/132.0.0.")
        # options.add_argument('--headless')
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.driver.maximize_window()
        self.driver.minimize_window()
        self.driver.maximize_window()

    def test_Negative_Starlink_TC_031_31(self):
        driver = self.driver
        print("Negative TC-031-31")
        driver.get(HN.starlink_url)
        wait = WebDriverWait(driver, 3)
        wait.until(EC.visibility_of_element_located((By.XPATH, HP.home_page_logo)))

        # Check Starlink Url

        HN.check_starlink_url(driver)

        # Check Starlink title

        HN.assert_title(driver, "Starlink")

        # Click Residential button

        HN.click_residential_button(driver)
        delay()

        # Check Starlink Residential Url

        HN.check_residential_url(driver)

        # Check Starlink Residential title

        HN.check_residential_title(driver)

        # Check Order Now button

        HN.check_oder_now_button(driver)

        # Click Order Now button

        HN.click_oder_now_button(driver)
        delay()

        driver.quit()

    def test_Negative_Starlink_TC_032_32(self):
        driver = self.driver
        print("Positive TC-032")
        driver.get(HP.starlink_url)
        wait = WebDriverWait(driver, 3)
        wait.until(EC.visibility_of_element_located((By.XPATH, HP.home_page_logo)))

        # Check Starlink Url

        HN.check_starlink_url(driver)

        # Check Starlink title

        HN.assert_title(driver, "Starlink")

        # Click Residential button

        HN.click_residential_button(driver)
        delay()

        # Check Starlink Residential Url

        HN.check_residential_url(driver)

        # Check Starlink Residential title

        HN.check_residential_title(driver)

        # Check Order Now button

        HN.check_oder_now_button(driver)

        # Write down the wrong address in the Service Address window

        service_address = driver.find_element(By.ID, "hero-service-input")
        service_address.is_displayed()
        service_address.clear()
        service_address.send_keys(HN.wrong_address_1)
        delay()

        # Click Order Now button

        HN.click_oder_now_button_2(driver)
        delay()

        # Message

        HN.pup_message_icon(driver)
        delay()

        # Push Button Cancel

        HN.click_cancel_button(driver)
        delay()

        driver.quit()

    def test_Negative_Starlink_TC_033_33(self):
        driver = self.driver
        print("Positive TC-032")
        driver.get(HP.starlink_url)
        wait = WebDriverWait(driver, 3)
        wait.until(EC.visibility_of_element_located((By.XPATH, HP.home_page_logo)))

        # Check Starlink Url

        HN.check_starlink_url(driver)

        # Check Starlink title

        HN.assert_title(driver, "Starlink")

        # Click Residential button

        HN.click_residential_button(driver)
        delay()

        # Check Starlink Residential Url

        HN.check_residential_url(driver)

        # Check Starlink Residential title

        HN.check_residential_title(driver)

        # Check Order Now button

        HN.check_oder_now_button(driver)

        # Write down the wrong address in the Service Address window

        service_address = driver.find_element(By.ID, "hero-service-input")
        service_address.is_displayed()
        service_address.clear()
        service_address.send_keys(HN.random_symbols)
        delay()

        # Click Order Now button

        HN.click_oder_now_button(driver)
        delay()

        driver.quit()

    def test_Negative_Starlink_TC_034_34(self):
        driver = self.driver
        print("Positive TC-032")
        driver.get(HP.starlink_url)
        wait = WebDriverWait(driver, 3)
        wait.until(EC.visibility_of_element_located((By.XPATH, HP.home_page_logo)))

        # Check Starlink Url

        HN.check_starlink_url(driver)

        # Check Starlink title

        HN.assert_title(driver, "Starlink")

        # Click Residential button

        HN.click_residential_button(driver)
        delay()

        # Check Starlink Residential Url

        HN.check_residential_url(driver)

        # Check Starlink Residential title

        HN.check_residential_title(driver)

        # Check Order Now button

        HN.check_oder_now_button(driver)

        # Write down the wrong address in the Service Address window

        service_address = driver.find_element(By.ID, "hero-service-input")
        service_address.is_displayed()
        service_address.clear()
        service_address.send_keys(HN.wrong_address_2)
        delay()

        # Click Order Now button

        HN.click_oder_now_button_2(driver)
        delay()

        # Message

        HN.pup_message_icon(driver)
        delay()

        # Push Button Cancel

        HN.click_cancel_button(driver)
        delay()

        driver.quit()

    def test_Negative_Starlink_TC_035_35(self):
        driver = self.driver
        print("Positive TC-032")
        driver.get(HP.starlink_url)
        wait = WebDriverWait(driver, 3)
        wait.until(EC.visibility_of_element_located((By.XPATH, HP.home_page_logo)))

        # Check Starlink Url

        HN.check_starlink_url(driver)

        # Check Starlink title

        HN.assert_title(driver, "Starlink")

        # Click Residential button

        HN.click_residential_button(driver)
        delay()

        # Check Starlink Residential Url

        HN.check_residential_url(driver)

        # Check Starlink Residential title

        HN.check_residential_title(driver)

        # Check Order Now button

        HN.check_oder_now_button(driver)

        # Write down the random_numbers in the Service Address window

        service_address = driver.find_element(By.ID, "hero-service-input")
        service_address.is_displayed()
        service_address.clear()
        service_address.send_keys(HN.random_numbers)
        delay()

        # Click Order Now button

        HN.click_oder_now_button(driver)
        delay()

        driver.quit()

    def test_Negative_Starlink_TC_036_36(self):
        driver = self.driver
        print("Positive TC-032")
        driver.get(HP.starlink_url)
        wait = WebDriverWait(driver, 3)
        wait.until(EC.visibility_of_element_located((By.XPATH, HP.home_page_logo)))

        # Check Starlink Url

        HN.check_starlink_url(driver)

        # Check Starlink title

        HN.assert_title(driver, "Starlink")

        # Click Residential button

        HN.click_residential_button(driver)
        delay()

        # Check Starlink Residential Url

        HN.check_residential_url(driver)

        # Check Starlink Residential title

        HN.check_residential_title(driver)

        # Check Order Now button

        HN.check_oder_now_button(driver)

        # Write down the  address in the Service Address window

        service_address = driver.find_element(By.ID, "hero-service-input")
        service_address.is_displayed()
        service_address.clear()
        service_address.send_keys(HN.address)
        delay()

        # Click Order Now button

        HN.click_oder_now_button_2(driver)
        delay()

        # Message

        HN.pup_message_icon_2(driver)
        delay()

        # Click Order Now Button

        HN.click_oder_now_button_3(driver)
        sleep(10)

        driver.quit()






        

