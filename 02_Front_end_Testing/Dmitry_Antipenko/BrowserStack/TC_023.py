import time
import random
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager



def delay():
    time.sleep(random.randint(2, 5))

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://www.starlink.com//")
driver.maximize_window()

driver.find_element(By.XPATH, "(//a[@href='/business'])[2]").click()
delay()

try:
    assert driver.title == "STARLINK FOR BUSINESSES"
    print("----Title check: Page has, " + driver.title + " as Page title")
except AssertionError:
    print("ATTENTION! Title is different. Current Title is:", driver.title)

driver.find_element(By.XPATH, "//a[@href='/business/fixed-site']").click()
delay()

try:
    assert driver.title == "STARLINK FOR FIXED SITES"
    print("----Title check: Page has, " + driver.title + " as Page title")
except AssertionError:
    print("ATTENTION! Title is different. Current Title is:", driver.title)

driver.find_element(By.XPATH, "(//u[contains(.,'Schedule a consultation')])").click()
delay()

wait = WebDriverWait(driver, 3)
try:
    wait.until(EC.visibility_of_element_located((By.XPATH, "//u[contains(text(),'Schedule a consultation')]")))
    wait.until(EC.element_to_be_clickable((By.XPATH, "//u[contains(text(),'Schedule a consultation')]")))
    print("'Schedule a Consultation' button is clicked and visible")
    print("TC PASS")
except AssertionError:
    print("'Schedule a Consultation' button is not found it.TC FAIL")

delay()

driver.quit()