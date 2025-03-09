import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager



def delay():
    time.sleep(random.randint(2, 5))

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://www.starlink.com//")
driver.maximize_window()

try:
    assert driver.title == "Starlink"
    print("----Title check: Page has, " + driver.title + " as Page title")
except AssertionError:
    print("ATTENTION! Title is different. Current Title is:", driver.title)

driver.find_element(By.XPATH, "//a[@href='/residential']").click()
delay()

try:
    assert driver.title == "Starlink | Residential"
    print("----Title check: Page has, " + driver.title + " as Page title")
except AssertionError:
    print("ATTENTION! Title is different. Current Title is:", driver.title)

service_address = driver.find_element(By.ID, "hero-service-input")
service_address.is_displayed()
service_address.clear()
service_address.send_keys("1100 Congress Ave., Austin, TX 99669")
delay()

oder_now_button = driver.find_element(By.XPATH, "(//span[@class='ng-star-inserted'])[1]")
oder_now_button.click()
delay()

cancel_button = driver.find_element(By.XPATH, "//span[contains(.,'CANCEL')]")
cancel_button.click()
delay()

video_button = driver.find_element(By.XPATH, '//button[@aria-label="Play Video"]')
video_button.send_keys(Keys.PAGE_DOWN)
video_button.click()
delay()

driver.quit()