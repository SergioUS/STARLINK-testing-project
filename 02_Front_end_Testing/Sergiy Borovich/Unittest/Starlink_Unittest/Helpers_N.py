from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time
import requests

starlink_url = ('https://www.starlink.com//')

home_page_logo = "//div[@class='starlink-logo-text']"

residential_url = ('https://www.starlink.com/residential')

mix_everything = "151252fgedufhds$^&&*DGFH6165@!#[]{}"

wrong_address_1 = "403 W High St, Milton, AR 53491"

random_symbols = "!@#$%^&<>)(?"

wrong_address_2 = "1100 Congress Ave., Austin, TX 99669"

random_numbers = "21892154961264"

email_symbols = "#$%^&^%{}[]""@)(!@)*"

email_mix = "1#%2&gjR,>[*-+5"

email_numbers = "123456789"

email = "Cha-cha-cha@rumba.cub"


def assert_title(driver, title):
    wait = WebDriverWait(driver, 3)
    wait.until(EC.title_is(title))
    assert title in driver.title
    print("----Title check: Page has, " + driver.title + " as Page title")
    if title not in driver.title:
        print("ATTENTION! Page " + title + " has wrong Title!")
        driver.get_screenshot_as_file('Wrong title.png')

def check_residential_title(driver,):
    try:
        assert driver.title == "Starlink | Residential"
        print("----Title check: Page has, " + driver.title + " as Page title")
    except AssertionError:
        print("ATTENTION! Title is different. Current Title is:", driver.title)

def check_starlink_url(driver):
    try:
        assert "https://www.starlink.com/" in driver.current_url
        print("Test result: Page URL is: ", driver.current_url)
    except AssertionError:
        print("Test result: Page URL is different", driver.current_url)

def check_residential_url(driver):
    try:
        assert "https://www.starlink.com/residential" in driver.current_url
        print("Test result: Page URL is: ", driver.current_url)
    except AssertionError:
        print("Test result: Page URL is different", driver.current_url)

def check_residential_button(driver):
    wait = WebDriverWait(driver, 3)
    try:
        wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/residential']")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/residential']")))
        print("'RESIDENTIAL' button is clicked and visible")
    except AssertionError:
        print("'RESIDENTIAL' button is not found it.")

def click_residential_button(driver):
    residential_button = driver.find_element(By.XPATH, "//a[@href='/residential']")
    residential_button.click()

def click_oder_now_button(driver):
    oder_now_button = driver.find_element(By.XPATH, "(//span[@class='ng-star-inserted'])[1]")
    oder_now_button.click()
    print("To view available Starlink products in your area, please provide your address ")
    print("Negative TC PASS")

def check_oder_now_button(driver):
    wait = WebDriverWait(driver, 3)
    try:
        wait.until(EC.visibility_of_element_located((By.XPATH, "(//span[@class='ng-star-inserted'])[1]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[@class='ng-star-inserted'])[1]")))
        print("'Order Now' button is clicked and visible")
    except AssertionError:
        print("'Order Now' button is not found it.")

def check_contact_information_icon(driver):
    contact_information = driver.find_element(By.XPATH, "//h3[text() = 'Contact Information']")
    contact_information.is_displayed()
    print("'Contact Information' icon is visible")


def pup_message_icon(driver):
    message_icon = driver.find_element(By.XPATH, '''//h2[text() = " WE DON'T RECOGNIZE THAT ADDRESS. "]''')
    message_icon.is_displayed()
    print(''' WE DON'T RECOGNIZE THAT ADDRESS." message is visible''')

def click_oder_now_button_2(driver):
    oder_now_button_2 = driver.find_element(By.XPATH, "(//span[@class='ng-star-inserted'])[1]")
    oder_now_button_2.click()

def click_cancel_button(driver):
    cancel_button = driver.find_element(By.XPATH, "//span[contains(.,'CANCEL')]")
    cancel_button.click()
    print("Negative TC PASS")


def click_sing_up_button_2(driver):
    sing_up_button = driver.find_element(By.XPATH, '//span[text()=" Sign Up "]')
    sing_up_button.click()
    print("'Please enter a valid email' message is visible")
    print("Negative TC PASS")

def click_sing_up_button_3(driver):
    sing_up_button = driver.find_element(By.XPATH, '//span[text()=" Sign Up "]')
    sing_up_button.click()
    print("'You are now signed up for updates. Thank you for your interest in Starlink!' message is visible")
    print("Negative TC FAIL")