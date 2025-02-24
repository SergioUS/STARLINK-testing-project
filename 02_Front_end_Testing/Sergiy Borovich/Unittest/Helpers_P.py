from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time
import requests

starlink_url = ('https://www.starlink.com//')

home_page_logo = "//div[@class='starlink-logo-text']"

residential_url = ('https://www.starlink.com/residential')


all_plans = "//button[contains(.,'View All Plans')]"

service_plans =  "(//a[@href='/service-plans'])[2]"

specifications = "(//a[@href='/specifications?spec=4'])[2]"

faqs =  "(//a[@href='/faq'])[2]"

video =  '//button[@aria-label="Play Video"]'

android = '//button[@aria-label="Play Video"]'

ios = '//button[@aria-label="Play Video"]'

type_and_select = "//input[@id='hero-service-input']"

wrong_address_1 = "403 W High St, Milton, AR 53491"

wrong_address_2 = "!@#$%^&<>)(?"

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
        print("TC-031 PASS")
    except AssertionError:
        print("'RESIDENTIAL' button is not found it.TC-031 FAIL")

def click_residential_button(driver):
    residential_button = driver.find_element(By.XPATH, "//a[@href='/residential']")
    residential_button.click()

def check_oder_now_button(driver):
    wait = WebDriverWait(driver, 3)
    try:
        wait.until(EC.visibility_of_element_located((By.XPATH, "(//span[@class='ng-star-inserted'])[1]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[@class='ng-star-inserted'])[1]")))
        print("'Order Now' button is clicked and visible")
        print("TC-032 PASS")
    except AssertionError:
        print("'Order Now' button is not found it.TC-032 FAIL")

def check_map_button(driver):
    wait = WebDriverWait(driver, 3)
    try:
        wait.until(EC.visibility_of_element_located((By.XPATH, "(//span[@class='mat-button-wrapper'])[5]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[@class='mat-button-wrapper'])[5]")))
        print("'View Availability & Speeds Map' button is clicked and visible")
        print("TC-033 PASS")
    except AssertionError:
        print("'View Availability & Speeds Map' button is not found it.TC-033 FAIL")

def check_all_plans_button(driver):
    wait = WebDriverWait(driver, 3)
    try:
        wait.until(EC.visibility_of_element_located((By.XPATH, "//button[contains(.,'View All Plans')]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'View All Plans')]")))
        print("' View All Plans ' button is clicked and visible")
        print("TC-034 PASS")
    except AssertionError:
        print("' View All Plans ' button is not found it.TC-034 FAIL")

def check_service_plans_button(driver):
    wait = WebDriverWait(driver, 3)
    try:
        wait.until(EC.visibility_of_element_located((By.XPATH, "(//a[@href='/service-plans'])[2]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//a[@href='/service-plans'])[2]")))
        print("'Service Plans' button is clicked and visible")
        print("TC-035 PASS")
    except AssertionError:
        print("'Service Plans' button is not found it.TC-035 FAIL")

def check_specifications_button(driver):
    wait = WebDriverWait(driver, 3)
    try:
        wait.until(EC.visibility_of_element_located((By.XPATH, "(//a[@href='/specifications?spec=4'])[2]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//a[@href='/specifications?spec=4'])[2]")))
        print("'Specifications' button is clicked and visible")
        print("TC-036 PASS")
    except AssertionError:
        print("'Specifications' button is not found it.TC-036 FAIL")

def check_faqs_button(driver):
    wait = WebDriverWait(driver, 3)
    try:
        wait.until(EC.visibility_of_element_located((By.XPATH, "(//a[@href='/faq'])[2]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//a[@href='/faq'])[2]")))
        print("'Faqs' button is clicked and visible")
        print("TC-037 PASS")
    except AssertionError:
        print("'Faqs' button is not found it.TC-037 FAIL")

def check_video_button(driver):
    wait = WebDriverWait(driver, 3)
    try:
        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@aria-label="Play Video"]')))
        wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@aria-label="Play Video"]')))
        print("'Video' button is clicked and visible")
        print("TC-038 PASS")
    except AssertionError:
        print("'Video' button is not found it.TC-038 FAIL")

def check_download_for_android_button(driver):
    wait = WebDriverWait(driver, 3)
    try:
        wait.until(EC.visibility_of_element_located((By.XPATH, "(//span[@class='mat-button-wrapper'])[11]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[@class='mat-button-wrapper'])[11]")))
        print("'Download for android' button is clicked and visible")
        print("TC-039 PASS")
    except AssertionError:
        print("'Download for android' button is not found it.TC-039 FAIL")

def check_download_for_ios_button(driver):
    wait = WebDriverWait(driver, 3)
    try:
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[text()="Download for iOS"]')))
        wait.until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Download for iOS"]')))
        print("'Download for iOS' button is clicked and visible")
        print("TC-040 PASS")
    except AssertionError:
        print("'Download for iOS' button is not found it.TC-040 FAIL")