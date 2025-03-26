
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

def delay():
    time.sleep(random.randint(1, 3))

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://www.starlink.com/")
driver.find_element(By.XPATH, "//img[contains(@src,'Hamburger.svg')]").click()
print("Starlink Hamburger Menu is clickable")

# Wait max 5 sec el to be clickable
time.sleep(5)
#driver.find_element(By.XPATH, "//span[contains(.,'Technology')]")
driver.find_element(By.XPATH, "//span[contains(.,'Technology')]").click()
print("Technology link is clickable")
time.sleep(5)

email = driver.find_element(By.XPATH, "//input[@type='email']")
driver.execute_script("arguments[0].scrollIntoView();", email)
time.sleep(5)
# Scroll to the "Sign Up" bottom
print("Scrolling to the Sign Up bottom")

email.send_keys("abc#def@mail.com")
driver.find_element(By.XPATH, "//span[contains(.,'Sign Up chevron_right')]").click()
time.sleep(5)

try:
    assert driver.find_element(By.XPATH, "//div[contains(text(),'Thank you for ')]")
    print("When entered an incorrect email address registration was successful.")
    print("'You are now signed up for updates. Thank you for your interest in Starlink.' TC-016-16 FAIL")
except AssertionError:
    driver.find_element(By.XPATH, "//mat-error[@id='mat-error-1']")
    print("'Please enter a valid email' message is visible")
    print("Negative TC-016-16 PASS")