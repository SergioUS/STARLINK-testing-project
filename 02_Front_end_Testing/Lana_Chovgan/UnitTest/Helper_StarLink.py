from selenium.webdriver.common.by import By
import time
import random
import driver
from selenium import webdriver

#name = driver.find_element(By.XPATH, "//input[contains(@id,'name')]")

def delay():
    time.sleep(random.randint(2,3))

def StarLink(driver):
    driver.get("https://www.starlink.com/")
    delay()

def hamburger_menu(driver):
    driver.find_element(By.XPATH, "//img[contains(@class,'avatar')]").click()

def customer_stories(driver):
    driver.find_element(By.XPATH, "//span[contains(.,'Customer Stories')]").click()
    delay()

def SubmitAStory_button(driver):
    driver.find_element(By.XPATH, "//button[text()='Submit a Story']").click()

def name(driver):
    driver.find_element(By.XPATH, "//input[contains(@id,'name')]").click()

def username(driver):
    driver.find_element(By.XPATH, "//input[contains(@id,'handle')]").click()

def submit_button(driver):
    driver.find_element(By.XPATH, "(//button[@type='submit'][contains(.,'Submit')])[2]").click()

def nameMia(driver):
    driver.find_element(By.XPATH, "//input[contains(@id,'name')]").send_keys("Mia")
    delay()

def usernameMia(driver):
    driver.find_element(By.XPATH, "//input[contains(@id,'handle')]").send_keys("@Mia")
    delay()
