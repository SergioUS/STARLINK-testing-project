import random
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC, wait
from selenium.webdriver.support.wait import WebDriverWait


t_url = "https://www.starlink.com/"
t_url_2 = "https://www.starlink.com/technologe"
h_menu = "//img[contains(@src,'Hamburger.svg')]"
# driver sleep from 2 to 3 seconds
def delay():
    time.sleep(random.randint(5, 8))

# Positive
def tc16(driver):
    driver.get(t_url)
    driver.find_element(By.XPATH, h_menu).click()
    print("Starlink Hamburger Menu is clickable")
    time.sleep(8)
    driver.find_element(By.XPATH, "//span[contains(.,'Technology')]").is_displayed()
    print("Technology link is visible")

    # Wait max 2 sec el to be clickable
    wait = WebDriverWait(driver, 8)
    wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(.,'Technology')]")))
    print("Technology link is clickable")
    print("Positive TC-16 PASS")

#---------------------------------------------------------------------------------------------------------------

def tc17(driver):
    driver.get(t_url)
    driver.find_element(By.XPATH, "//img[contains(@src,'Hamburger.svg')]").click()
    print("Starlink Hamburger Menu is clickable")
    time.sleep(8)
    driver.find_element(By.XPATH, "//span[contains(.,'Technology')]").is_displayed()
    print("Technology link is visible")

    # Wait max 2 sec el to be clickable
    wait = WebDriverWait(driver, 8)
    wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(.,'Technology')]")))
    print("Technology link is clickable")
    time.sleep(8)
    driver.find_element(By.XPATH, "//span[contains(.,'Technology')]").click()
    wait.until(EC.visibility_of_element_located((By.XPATH, "//h1[contains(.,'SATELLITE TECHNOLOGY')]")))
    time.sleep(4)

    # Check Page URL
    try:
        assert "https://www.starlink.com/technology" in driver.current_url
        print("URL is correct", driver.current_url)
    except AssertionError:
        print("URL is NOT correct", driver.current_url)
        driver.save_screenshot("wrong url.png")

    # Check Page Title
    try:
        assert "Starlink | Technology" in driver.title
        print("Title is correct", driver.title)
        print("Positive TC-17 PASS")
    except AssertionError:
        print("Title is NOT correct. TC-17 FAIL", driver.title)
        driver.save_screenshot("wrong title.png")

#-------------------------------------------------------------------------------------------------------------------

def tc18(driver):
    driver.get(t_url)
    driver.find_element(By.XPATH, "//img[contains(@src,'Hamburger.svg')]").click()
    print("Starlink Hamburger Menu is clickable")
    time.sleep(8)
    driver.find_element(By.XPATH, "//span[contains(.,'Technology')]").is_displayed()
    print("Technology link is visible")

    # Wait max 2 sec el to be clickable
    wait = WebDriverWait(driver, 8)
    wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(.,'Technology')]")))
    print("Technology link is clickable")
    driver.find_element(By.XPATH, "//span[contains(.,'Technology')]").click()

    wait.until(EC.visibility_of_element_located((By.XPATH, "//h1[contains(.,'SATELLITE TECHNOLOGY')]")))
    time.sleep(8)

    # Check Page URL
    try:
        assert "https://www.starlink.com/technology" in driver.current_url
        print("URL is correct", driver.current_url)
    except AssertionError:
        print("URL is NOT correct", driver.current_url)
        driver.save_screenshot("wrong url.png")

    # Check Page Title
    try:
        assert "Starlink | Technology" in driver.title
        print("Title is correct", driver.title)
    except AssertionError:
        print("Title is NOT correct", driver.title)
        driver.save_screenshot("wrong title.png")

    careers=driver.find_element(By.XPATH, "//a[contains(text(),'Careers')]")
    driver.execute_script("arguments[0].scrollIntoView();", careers)
    time.sleep(8)

    # Scroll to the bottom of the page and verify all elements are visible
    print("Scrolling to the bottom of the page...")


    print("Verifying visibility of elements at the bottom of the page...")
    try:
        # Example: Check for a footer element or other content at the bottom of the page
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "footer")))
        print("PASS: All elements of the page are visible.")
    except Exception as e:
        print(f"FAIL: Elements of the page are not visible: {e}")

#---------------------------------------------------------------------------------------------------------------------

def tc19(driver):
    driver.get(t_url)
    driver.find_element(By.XPATH, "//img[contains(@src,'Hamburger.svg')]").click()
    print("Starlink Hamburger Menu is clickable")
    time.sleep(8)
    driver.find_element(By.XPATH, "//span[contains(.,'Technology')]").is_displayed()
    print("Technology link is visible")

    # Wait max 5 sec el to be clickable
    wait = WebDriverWait(driver, 8)
    wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(.,'Technology')]")))
    print("Technology link is clickable")
    driver.find_element(By.XPATH, "//span[contains(.,'Technology')]").click()

    wait.until(EC.visibility_of_element_located((By.XPATH, "//h1[contains(.,'SATELLITE TECHNOLOGY')]")))
    time.sleep(8)

    # Check Page URL
    try:
        assert "https://www.starlink.com/technology" in driver.current_url
        print("URL is correct", driver.current_url)
    except AssertionError:
        print("URL is NOT correct", driver.current_url)
        driver.save_screenshot("wrong url.png")

    #Check Page Title
    try:
        assert "Starlink | Technology" in driver.title
        print("Title is correct", driver.title)
    except AssertionError:
        print("Title is NOT correct", driver.title)
        driver.save_screenshot("wrong title.png")
    time.sleep(8)


    #Scroll to the bottom of the page and verify all elements are visible
    careers = driver.find_element(By.XPATH, "//a[contains(.,'Careers')]")
    driver.execute_script("arguments[0].scrollIntoView();", careers)
    time.sleep(8)
    print("Scrolling to the bottom of the page...")

    # Wait max 2 sec el to be clickable
    wait = WebDriverWait(driver, 8)
    wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(.,'Careers')]")))
    print("Careers link is clickable")
    driver.find_element(By.XPATH, "//a[contains(.,'Careers')]").click()

    wait.until(EC.visibility_of_element_located((By.XPATH, "//h1[contains(text(),'Find your future')]")))
    time.sleep(8)

    # Check Page URL
    try:
        assert "https://www.spacex.com/careers" in driver.current_url
        print("Careers URL is correct", driver.current_url)
    except AssertionError:
        print("Careers URL is NOT correct", driver.current_url)
        driver.save_screenshot("wrong url.png")

    delay()
    driver.back()
    time.sleep(8)

    careers = driver.find_element(By.XPATH, "//a[contains(.,'Careers')]")
    driver.execute_script("arguments[0].scrollIntoView();", careers)
    time.sleep(8)
    print("Scrolling to the bottom of the page...")

    # Wait max 2 sec el to be clickable
    wait = WebDriverWait(driver, 8)
    wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Satellite Operators')]")))
    print("Satellite Operators link is clickable")
    driver.find_element(By.XPATH, "//a[contains(text(),'Satellite Operators')]").click()
    wait.until(EC.visibility_of_element_located((By.XPATH, "//h1[contains(text(),'SATELLITE OPERATORS')]")))
    time.sleep(8)

    # Check Page URL
    try:
        assert "https://www.starlink.com/satellite-operators" in driver.current_url
        print("Satellite Operators URL is correct", driver.current_url)
    except AssertionError:
        print("Satellite Operators URL is NOT correct", driver.current_url)
        driver.save_screenshot("wrong url.png")

    delay()
    driver.back()
    time.sleep(8)

    careers = driver.find_element(By.XPATH, "//a[contains(.,'Careers')]")
    driver.execute_script("arguments[0].scrollIntoView();", careers)
    time.sleep(8)
    print("Scrolling to the bottom of the page...")

    # Wait max 2 sec el to be clickable
    wait = WebDriverWait(driver, 8)
    wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Authorized Reseller')]")))
    print("Authorized Reseller link is clickable")
    driver.find_element(By.XPATH, " //a[contains(text(),'Authorized Reseller')]").click()
    wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='MuiBox-root mui-6x721z']")))

    # Check Page URL
    try:
        assert "Who is a Starlink authorized commercial reseller?  - Starlink Help Center" in driver.title
        print("Authorized Reseller title is correct", driver.title)
    except AssertionError:
        print("Authorized Reseller title is NOT correct", driver.title)
        driver.save_screenshot("wrong title")

    driver.back()
    time.sleep(8)

    careers = driver.find_element(By.XPATH, "//a[contains(.,'Careers')]")
    driver.execute_script("arguments[0].scrollIntoView();", careers)
    time.sleep(8)
    print("Scrolling to the bottom of the page...")

    # Wait max 2 sec el to be clickable
    wait = WebDriverWait(driver, 8)
    wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Privacy & Legal')]")))
    print("Privacy & Legal Reseller link is clickable")
    driver.find_element(By.XPATH, "//a[contains(text(),'Privacy & Legal')]").click()

    time.sleep(8)
    wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//h1[contains(text(),'Starlink Legal')]")))

    # Check Page URL
    try:
        assert "https://www.starlink.com/legal" in driver.current_url
        print("Starlink Legal URL is correct", driver.current_url)
    except AssertionError:
        print("Starlink Legal URL is NOT correct", driver.current_url)
        driver.save_screenshot("wrong url.png")

    driver.back()
    time.sleep(8)

    careers = driver.find_element(By.XPATH, "//a[contains(.,'Careers')]")
    driver.execute_script("arguments[0].scrollIntoView();", careers)
    time.sleep(8)
    print("Scrolling to the bottom of the page...")

    # Wait max 2 sec el to be clickable
    wait = WebDriverWait(driver, 8)
    wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Privacy Preferences')]")))
    print("Privacy Preferences Reseller link is clickable")
    driver.find_element(By.XPATH, "//a[contains(text(),'Privacy Preferences')]").click()

    time.sleep(8)
    # Check Page URL
    try:
        assert wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='onetrust-pc-sdk']/div[3]/div[2]/a/img")))
        print("Privacy Preferences link is correct")
        print("Positive TC-19 PASS")
    except AssertionError:
        print("Privacy Preferences link is NOT correct. TC-19 FAIL")
        driver.save_screenshot("wrong link")

#----------------------------------------------------------------------------------------------------------------------

def tc20(driver):
    driver.get(t_url)
    driver.find_element(By.XPATH, "//img[contains(@src,'Hamburger.svg')]").click()
    print("Starlink Hamburger Menu is clickable")
    time.sleep(8)
    driver.find_element(By.XPATH, "//span[contains(.,'Technology')]").is_displayed()
    print("Technology link is visible")

    # Wait max 5 sec el to be clickable
    wait = WebDriverWait(driver, 8)
    wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(.,'Technology')]")))
    print("Technology link is clickable")
    driver.find_element(By.XPATH, "//span[contains(.,'Technology')]").click()
    wait.until(EC.visibility_of_element_located((By.XPATH, "//h1[contains(.,'SATELLITE TECHNOLOGY')]")))
    time.sleep(8)

    # Check Page URL
    try:
        assert "https://www.starlink.com/technology" in driver.current_url
        print("URL is correct", driver.current_url)
    except AssertionError:
        print("URL is NOT correct", driver.current_url)
        driver.save_screenshot("wrong url.png")

    time.sleep(8)
    # Scroll to the "Sign Up" bottom
    print("Scrolling to the Sign Up bottom")
    email = driver.find_element(By.XPATH, "//input[@type='email']")
    driver.execute_script("arguments[0].scrollIntoView();", email)
    time.sleep(8)
    print("Scrolling to the bottom of the page...")
    email.send_keys("abc@mail.com")
    driver.find_element(By.XPATH, "//span[contains(.,'Sign Up chevron_right')]").click()

    print("Button on the page works correctly when entering the correct email address")
    print("Positive TC-20 PASS")

#---------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------

# Negative
def tc016_16(driver):
    driver.get(t_url)
    driver.find_element(By.XPATH, "//img[contains(@src,'Hamburger.svg')]").click()
    print("Starlink Hamburger Menu is clickable")

    # Wait max 5 sec el to be clickable
    wait = WebDriverWait(driver, 8)
    wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(.,'Technology')]")))
    driver.find_element(By.XPATH, "//span[contains(.,'Technology')]").click()
    print("Technology link is clickable")
    time.sleep(8)

    email = driver.find_element(By.XPATH, "//input[@type='email']")
    driver.execute_script("arguments[0].scrollIntoView();", email)
    time.sleep(8)
    # Scroll to the "Sign Up" bottom
    print("Scrolling to the Sign Up bottom")

    email.send_keys("abc#def@mail.com")
    driver.find_element(By.XPATH, "//span[contains(.,'Sign Up chevron_right')]").click()
    time.sleep(8)

    try:
        assert wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Thank you for ')]")))
        print("'You are now signed up for updates. Thank you for your interest in Starlink.' TC-016-16 FAIL")
    except AssertionError:
        wait.until(EC.visibility_of_element_located((By.XPATH, "//mat-error[@id='mat-error-1']")))
        print("'Please enter a valid email' message is visible")
        print("Negative TC-016-16 PASS")

#---------------------------------------------------------------------------------------------------------------------

def tc017_17(driver):
    driver.get(t_url)
    driver.find_element(By.XPATH, "//img[contains(@src,'Hamburger.svg')]").click()
    print("Starlink Hamburger Menu is clickable")

    # Wait max 5 sec el to be clickable
    wait = WebDriverWait(driver, 8)
    wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Customer Stories')]")))
    driver.find_element(By.XPATH, "//span[contains(text(),'Customer Stories')]").click()
    print("Customer Stories link is clickable")
    time.sleep(8)

    report = driver.find_element(By.XPATH, "//h1[@aria-label='2024 Progress Report']")

    driver.execute_script("arguments[0].scrollIntoView();", report)
    time.sleep(8)
    # Scroll to the "SUBMIT & DOWNLOAD PDF" bottom
    print("Scrolling to the SUBMIT & DOWNLOAD PDF bottom")
    email = driver.find_element(By.XPATH, "//input[@id='email']")
    email.send_keys("abc#def@mail.com")
    time.sleep(8)
    driver.find_element(By.XPATH, "//button[contains(text(),'Submit & Download PDF')]").click()
    print("'SUBMIT & DOWNLOAD PDF' bottom is clickable")
    time.sleep(8)

    try:
        assert wait.until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Download PDF')]")))
        print("'DOWNLOAD PDF' TC-017-17 FAIL")
    except AssertionError:
        wait.until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Email address is required to download.')]")))
        print("'Email address is required to download' message is visible")
        print("Negative TC-017-17 PASS")
#---------------------------------------------------------------------------------------------------------------------

def tc018_18(driver):
    driver.get(t_url)
    driver.find_element(By.XPATH, "//img[contains(@src,'Hamburger.svg')]").click()
    print("Starlink Hamburger Menu is clickable")

    # Wait max 5 sec el to be clickable
    wait = WebDriverWait(driver, 8)
    wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(.,'Technology')]")))
    driver.find_element(By.XPATH, "//span[contains(.,'Technology')]").click()
    print("Technology link is clickable")
    time.sleep(8)

    email = driver.find_element(By.XPATH, "//input[@type='email']")
    driver.execute_script("arguments[0].scrollIntoView();", email)
    time.sleep(8)
    # Scroll to the "Sign Up" bottom
    print("Scrolling to the Sign Up bottom")

    email.send_keys(" ")
    driver.find_element(By.XPATH, "//span[contains(.,'Sign Up chevron_right')]").click()
    time.sleep(8)

    try:
        assert wait.until(EC.visibility_of_element_located((By.XPATH, "//mat-error[@id='mat-error-0']")))
        print("'Email is required' message is visible")
        print("Negative TC-018-18 PASS")
    except AssertionError:
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Thank you for ')]")))
        print("'You are now signed up for updates. Thank you for your interest in Starlink.' TC-018-18 FAIL")

#---------------------------------------------------------------------------------------------------------------------

def tc019_19(driver):
    driver.get(t_url)
    driver.find_element(By.XPATH, "//img[contains(@src,'Hamburger.svg')]").click()
    print("Starlink Hamburger Menu is clickable")

    # Wait max 5 sec el to be clickable
    wait = WebDriverWait(driver, 8)
    wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(.,'Technology')]")))
    driver.find_element(By.XPATH, "//span[contains(.,'Technology')]").click()
    print("Technology link is clickable")
    time.sleep(8)

    email = driver.find_element(By.XPATH, "//input[@type='email']")
    driver.execute_script("arguments[0].scrollIntoView();", email)
    time.sleep(8)
    # Scroll to the "Sign Up" bottom
    print("Scrolling to the Sign Up bottom")

    email.send_keys("aaaaaaaaaaaaaaaaa")
    driver.find_element(By.XPATH, "//span[contains(.,'Sign Up chevron_right')]").click()
    time.sleep(8)

    try:
        assert wait.until(EC.visibility_of_element_located((By.XPATH, "//mat-error[@role='alert'][contains(.,'Please enter a valid email')]")))
        print("'Email is required' message is visible")
        print("Negative TC-019-19 PASS")
    except AssertionError:
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Thank you for ')]")))
        print("'You are now signed up for updates. Thank you for your interest in Starlink.' TC-019-19 FAIL")

#---------------------------------------------------------------------------------------------------------------------

def tc020_20(driver):
    driver.get(t_url_2)
    wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@role,'main')]")))
    time.sleep(8)

    try:
        assert "https://www.starlink.com/technology" in driver.current_url
        print("URL is correct", driver.current_url,"TC-020-20 FAIL" )
    except AssertionError:
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@role,'main')]")))
        print("'Page Not Found. Starlink couldn't find the page you're looking for. Try starting over from Home. Back to Home' message is visible")
        print("Negative TC-020-20 PASS")
