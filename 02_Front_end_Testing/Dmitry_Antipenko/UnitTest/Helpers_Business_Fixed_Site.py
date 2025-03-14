from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time
import requests



# ------------------------------Helpers for Business/Fixed site-------------------------------

# Starlink url
Starlink_url= "https://www.starlink.com/"

# Business link
Business_link = "(//a[@href='/business'])[2]"

# Starlink | Business/Fixed site link
FixedSite_link = "//a[@href='/business/fixed-site']"

# Fixed site/Service_plans link
ServicePlans_link =  "(//a[@href='/service-plans'])[2]"

# Fixed site/Schedule a consultation link
Schedule_a_Consultation_link = "(//u[contains(.,'Schedule a consultation')])"

# Fixed site/Buyer's guide link
BuyersGuide_link = '(@FindBy(xpath = "1"))'

# Fixed site/Order Now link
OrderNow_link = "(//button[contains(.,'ORDER NOW')])[1]"

# Click Sing Up
Click_SingUp_link = "//span[contains(.,'Sign Up chevron_right')]"

# Email (Sign Up) link
Email_SignUp_link = "//input[@id='email-input-footer-483']"

# Fixed site/type_and_select link
type_and_select = "//input[contains(@id,'footer-service-input')]"

# Fixed site/Type and Select link
Type_And_Select_link = "//input[@id='hero-service-input']"

# Business/Fixed Site/Checkout link
Checkout_link = "(//span[contains(.,'Checkout')])[2]"

# Place Order link
PlaceOrder_link = "(//span[contains(.,'Place Order')])[2]"



# Email and Phone number for registration form
Email_link = "//input[@name='email']"
PN_link = "//input[@name='phone']"

Wrong_email_1 = "dq@vin.яя"
Wrong_email_2 = "2406@й"
Wrong_PN = "786241053"
Address_Type = "16787 Eastern Shores Blvd, North Miami Beach, FL 33160, USA"


def check_starlink_url(driver):
    try:
        assert "https://www.starlink.com/" in driver.current_url
        print("Test result: Page URL is: ", driver.current_url)
    except AssertionError:
        print("Test result: Page URL is different", driver.current_url)

def check_BUSINESS_title(driver):
    try:
        assert driver.title == "Starlink | BUSINESS"
        print("----Title check: Page has, " + driver.title + " as Page title")
    except AssertionError:
        print("ATTENTION! Title is different. Current Title is:", driver.title)

def check_BUSINESS_url(driver):
    try:
        assert "https://www.starlink.com/business" in driver.current_url
        print("Test result: Page URL is: ", driver.current_url)
    except AssertionError:
        print("Test result: Page URL is different", driver.current_url)

def click_Business_button(driver):
    FixedSite_button = driver.find_element(By.XPATH, "(//a[@href='/business'])[2]")
    FixedSite_button.click()

def check_FIXED_SITE_url(driver):
    try:
        assert "https://www.starlink.com/business/fixed-site" in driver.current_url
        print("Test result: Page URL is: ", driver.current_url)
    except AssertionError:
        print("Test result: Page URL is different", driver.current_url)


def check_FIXED_SITE_button(driver):
    wait = WebDriverWait(driver, 3)
    try:
        wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Fixed Site')]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Fixed Site')]")))
        print("'FIXED SITE' button is clicked and visible")
        print("TC-021 PASS")
    except AssertionError:
        print("'FIXED SITE' button is not found it.TC-021 FAIL")

def click_FIXED_SITE_button(driver):
    FixedSite_button = driver.find_element(By.XPATH, "//a[contains(text(),'Fixed Site')]")
    FixedSite_button.click()

def check_STARLINK_FOR_FIXED_SITES_header(driver):
    wait = WebDriverWait(driver, 3)
    try:
        wait.until(EC.visibility_of_element_located((By.XPATH, "//h1[contains(.,'STARLINK FOR FIXED SITES')]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "//h1[contains(.,'STARLINK FOR FIXED SITES')]")))
        print("'STARLINK FOR FIXED SITES' is present and correct")
        print("TC-022 PASS")
    except AssertionError:
        print("'STARLINK FOR FIXED SITES' is not found it.TC-022 FAIL")

def click_Schedule_a_Consultation_button(driver):
    Schedule_a_Consultation_button = driver.find_element(By.XPATH, "//u[contains(text(),'Schedule a consultation')]")
    Schedule_a_Consultation_button.click()

def check_Schedule_a_Consultation_form(driver):
    wait = WebDriverWait(driver, 3)
    try:
        wait.until(EC.visibility_of_element_located((By.XPATH, "//u[contains(text(),'Schedule a consultation')]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "//u[contains(text(),'Schedule a consultation')]")))
        print("'Schedule a Consultation' button is clicked and visible")
        print("TC-023 PASS")
    except AssertionError:
        print("'Schedule a Consultation' button is not found it.TC-023 FAIL")

def click_Service_Plans_button(driver):
    Service_Plans_button = driver.find_element(By.XPATH, "(//a[@href='/service-plans'])[2]")
    Service_Plans_button.click()

def check_SERVICE_PLANS_button(driver):
    wait = WebDriverWait(driver, 3)
    try:
        wait.until(EC.visibility_of_element_located((By.XPATH, "(//a[@href='/service-plans'])[2]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//a[@href='/service-plans'])[2]")))
        print("'SERVICE PLANS' button is clicked and visible")
        print("TC-024 PASS")
    except AssertionError:
        print("'SERVICE PLANS' button is not found it.TC-024 FAIL")

def click_Buyers_guide_button(driver):
    Buyers_guide_button = driver.find_element(By.XPATH, '''//u[contains(text(),"buyer's guide")]''')
    Buyers_guide_button.click()

def check_Buyers_guide_button(driver):
    wait = WebDriverWait(driver, 3)
    try:
        wait.until(EC.visibility_of_element_located((By.XPATH, '''//u[contains(text(),"buyer's guide")]''')))
        wait.until(EC.element_to_be_clickable((By.XPATH, '''//u[contains(text(),"buyer's guide")]''')))
        print("'Buyer's guide' button is clicked and visible")
        print("TC-025 PASS")
    except AssertionError:
        print("'Buyer's guide' button is not found it.TC-025 FAIL")

def click_Type_And_Select_button(driver):
    TAS_button = driver.find_element(By.XPATH, "//input[@id='hero-service-input']")
    TAS_button.click()

def click_Order_Now_button(driver):
    Service_Plans_button = driver.find_element(By.XPATH, "(//button[contains(.,'ORDER NOW')])[1]")
    Service_Plans_button.click()

def check_Order_Now_button(driver):
    wait = WebDriverWait(driver, 3)
    try:
        wait.until(EC.visibility_of_element_located((By.XPATH, "(//button[contains(.,'ORDER NOW')])[1]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[contains(.,'ORDER NOW')])[1]")))
        print("'Order Now' button is not working without an address")
        print("TC-021-21 PASS")
    except AssertionError:
        print("'Order Now' button is working without an address.TC-021-21 FAIL")

def click_Checkout_button(driver):
    Checkout_button = driver.find_element(By.XPATH, "(//span[contains(.,'Checkout')])[2]")
    Checkout_button.click()

def click_Place_Order_button(driver):
    Place_Order_button = driver.find_element(By.XPATH, "(//span[contains(.,'Place Order')])[2]")
    Place_Order_button.click()



#class Starlink_url:
#    pass