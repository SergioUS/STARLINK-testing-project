import time
import unittest
import random
import Helper_StarLink as H

import HtmlTestRunner
import AllureReports

import os
os.environ['WDM_SSL_VERIFY'] = '0'
import warnings
from urllib3.exceptions import InsecureRequestWarning
# Suppress only the single InsecureRequestWarning from urllib3
warnings.filterwarnings("ignore", category=InsecureRequestWarning)
from webdriver_manager.core import driver


from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from selenium.common import WebDriverException as WDE, NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


def delay():
    time.sleep(random.randint(2,3))
# This function is for delay() it randomly pics time between 2 and 4 seconds

class ChromeTestsPositive(unittest.TestCase):
    def setUp(self):

        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        # options.add_argument("--headless")
        # options.add_argument(
        #     "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.3")
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

        self.driver.maximize_window()

        options.page_load_strategy = 'eager'
        #wait = WebDriverWait(driver, 5)

    # This is a class setUp. We will have 3 (chrome,firefox,edge)

    def test_chrome_001(self):
        driver = self.driver
# 1. Go to https://www.starlink.com/
        H.StarLink(driver)
# 2. Click on the hamburger menu in the top right corner
        H.hamburger_menu(driver)
# 3. Click on the 'Customer Stories' link/button
        H.customer_stories(driver)
# 4. Verify that the page is correct by checking if the 'Submit Story' button is present on the page
        submit_story = driver.find_element(By.XPATH, "//button[text()='Submit a Story']")
        if submit_story is not None:
            print("Button 'submit_story' is visible and displayed")
        else:
            print("Button 'submit_story' is not displayed")
# 5. Verify that the page is correct by checking if the 'Progress Report' image is displayed on the page
        Progress_report_image = driver.find_element(By.XPATH, "(//img[contains(@loading,'lazy')])[110]")
        driver.execute_script("return arguments[0].scrollIntoView(true);", Progress_report_image)
        if Progress_report_image:
            print("'Progress Report' image is displayed on the page")
        else:
            print("Image is not visible!")
# 6. Verify that the page is correct by checking the title
        try:
            assert "Starlink Stories | Starlink" in driver.title
            print("Title is correct!")
        except WDE:
            print("Title is wrong! Title is: ", driver.title)

    def test_chrome_002(self):
        driver = self.driver
# 1. Go to https://www.starlink.com/
        H.StarLink(driver)
# 2. Click on the hamburger menu in the top right corner
        H.hamburger_menu(driver)
# 3. Click on the 'Customer Stories' link/button
        H.customer_stories(driver)
# 4. Find story "Internet from space for global explorers", click on it
        image_GlobalExplorers = driver.find_element(By.XPATH, "//button[@aria-label='Open story preview: Internet from space for global explorers']")
        driver.execute_script("arguments[0].scrollIntoView();", image_GlobalExplorers)
        image_GlobalExplorers.click()
        delay()
# 5. Click on Read Full Story
        driver.find_element(By.XPATH, "//button[@tabindex='0'][contains(.,'Read Full Story')]").click()
        delay()
# 6. Verify link opens correct page by checking the title
        try:
            assert "Internet from space for global explorers | Starlink" in driver.title
            print('Title is correct!')
        except WDE:
            print('Title is wrong! Title is: ', driver.title)

    def test_chrome_003(self):
        driver = self.driver
# 1. Go to https://www.starlink.com/
        H.StarLink(driver)
# 2. Click on the hamburger menu in the top right corner
        H.hamburger_menu(driver)
# 3. Click on the 'Customer Stories' link/button
        H.customer_stories(driver)
#4. Click on the carousel arrow 6 times while verifying each picture
    #find the first picture in the carousel
        first_slide = driver.find_element(By.XPATH, "//img[contains(@alt,'Women holding a Starlink box ')]")
        action = ActionChains(driver)
        action.move_to_element(first_slide).perform()
    #click to the next element and verify each picture
        driver.find_element(By.XPATH, "//button[contains(@aria-label,'Go to next slide')]").click()
        delay()
        driver.find_element(By.XPATH, "//img[contains(@alt, 'Man interacts with a Starlink dish')]")

        driver.find_element(By.XPATH, "//button[contains(@aria-label,'Go to next slide')]").click()
        delay()
        driver.find_element(By.XPATH,"//img[contains(@alt,'A person and a Starlink with a volcano in the background')]")

        driver.find_element(By.XPATH, "//button[contains(@aria-label,'Go to next slide')]").click()
        delay()
        driver.find_element(By.XPATH, "//img[contains(@alt,'A Starlink in the snow')]")

        driver.find_element(By.XPATH, "//button[contains(@aria-label,'Go to next slide')]").click()
        delay()
        driver.find_element(By.XPATH, "//img[contains(@alt, 'Man handling a Starlink to a woman')]")

        driver.find_element(By.XPATH, "//button[contains(@aria-label,'Go to next slide')]").click()
        delay()
        driver.find_element(By.XPATH, "(//img[contains(@loading,'lazy')])[2]")

    def test_chrome_004(self):
        driver = self.driver
# 1. Go to https://www.starlink.com/
        H.StarLink(driver)
# 2. Click on the hamburger menu in the top right corner
        H.hamburger_menu(driver)
# 3. Click on the 'Customer Stories' link/button
        H.customer_stories(driver)
# 4. Scroll down
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# 5. Click on the link Careers
        original_window = driver.window_handles[0]
        driver.find_element(By.XPATH, "//a[@href='https://www.spacex.com/careers']").click()
        delay()
# 6. Navigate to the open page
        second_window = driver.window_handles[1]
        driver.switch_to.window(second_window)
        delay()
# 7. Verify that the page is correct
        try:
            assert "SpaceX" in driver.title
            print("Title is correct!")
        except WDE:
            print("Title is wrong! Title is: ", driver.title)

    def test_chrome_005(self):
        driver = self.driver
# 1. Go to https://www.starlink.com/
        H.StarLink(driver)
# 2. Click on the hamburger menu in the top right corner
        H.hamburger_menu(driver)
# 3. Click on the 'Customer Stories' link/button
        H.customer_stories(driver)
# 4. Click on the 'Submit Story' button
        driver.find_element(By.XPATH, "//button[text()='Submit a Story']").click()
        delay()
# 5. Verify that the link scrolls to the form below
        Submit_button = driver.find_element(By.XPATH, "(//button[@type='submit'])[2]")
        if Submit_button:
            print("'Submit Story' button scrolls down to the form")
        else:
            print("'Submit Story' button  doesn't work!")

    # Anything declared in tearDown will be executed for all test cases
# Closing browser. You need to use "tearDown" method only one time for every Class
    def tearDown(self):
        self.driver.quit()

class EdgeTestsPositive(unittest.TestCase):
    def setUp(self):

        options = webdriver.EdgeOptions()
        options.add_argument('--ignore-certificate-errors')
        # options.add_argument("--headless")
        # options.add_argument(
        #     "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.3")
        self.driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=options)
        self.driver.maximize_window()

        options.page_load_strategy = 'eager'
        #wait = WebDriverWait(driver, 5)

    # This is a class setUp. We will have 3 (chrome,firefox,edge)

    def test_edge_001(self):
        driver = self.driver
# 1. Go to https://www.starlink.com/
        H.StarLink(driver)
# 2. Click on the hamburger menu in the top right corner
        H.hamburger_menu(driver)
# 3. Click on the 'Customer Stories' link/button
        H.customer_stories(driver)
# 4. Verify that the page is correct by checking if the 'Submit Story' button is present on the page
        submit_story = driver.find_element(By.XPATH, "//button[text()='Submit a Story']")
        if submit_story is not None:
            print("Button 'submit_story' is visible and displayed")
        else:
            print("Button 'submit_story' is not displayed")
# 5. Verify that the page is correct by checking if the 'Progress Report' image is displayed on the page
        Progress_report_image = driver.find_element(By.XPATH, "(//img[contains(@loading,'lazy')])[110]")
        driver.execute_script("return arguments[0].scrollIntoView(true);", Progress_report_image)
        if Progress_report_image:
            print("'Progress Report' image is displayed on the page")
        else:
            print("Image is not visible!")
# 6. Verify that the page is correct by checking the title
        try:
            assert "Starlink Stories | Starlink" in driver.title
            print("Title is correct!")
        except WDE:
            print("Title is wrong! Title is: ", driver.title)

    def test_edge_002(self):
        driver = self.driver
# 1. Go to https://www.starlink.com/
        H.StarLink(driver)
# 2. Click on the hamburger menu in the top right corner
        H.hamburger_menu(driver)
# 3. Click on the 'Customer Stories' link/button
        H.customer_stories(driver)
# 4. Find story "Internet from space for global explorers", click on it
        image_GlobalExplorers = driver.find_element(By.XPATH, "//button[@aria-label='Open story preview: Internet from space for global explorers']")
        driver.execute_script("arguments[0].scrollIntoView();", image_GlobalExplorers)
        image_GlobalExplorers.click()
        delay()
# 5. Click on Read Full Story
        driver.find_element(By.XPATH, "//button[@tabindex='0'][contains(.,'Read Full Story')]").click()
        delay()
# 6. Verify link opens correct page by checking the title
        try:
            assert "Internet from space for global explorers | Starlink" in driver.title
            print('Title is correct!')
        except WDE:
            print('Title is wrong! Title is: ', driver.title)

    def test_edge_003(self):
        driver = self.driver
# 1. Go to https://www.starlink.com/
        H.StarLink(driver)
# 2. Click on the hamburger menu in the top right corner
        H.hamburger_menu(driver)
# 3. Click on the 'Customer Stories' link/button
        H.customer_stories(driver)
#4. Click on the carousel arrow 6 times while verifying each picture
    #find the first picture in the carousel
        first_slide = driver.find_element(By.XPATH, "//img[contains(@alt,'Women holding a Starlink box ')]")
        action = ActionChains(driver)
        action.move_to_element(first_slide).perform()
    #click to the next element and verify each picture
        driver.find_element(By.XPATH, "//button[contains(@aria-label,'Go to next slide')]").click()
        delay()
        driver.find_element(By.XPATH, "//img[contains(@alt, 'Man interacts with a Starlink dish')]")

        driver.find_element(By.XPATH, "//button[contains(@aria-label,'Go to next slide')]").click()
        delay()
        driver.find_element(By.XPATH,"//img[contains(@alt,'A person and a Starlink with a volcano in the background')]")

        driver.find_element(By.XPATH, "//button[contains(@aria-label,'Go to next slide')]").click()
        delay()
        driver.find_element(By.XPATH, "//img[contains(@alt,'A Starlink in the snow')]")

        driver.find_element(By.XPATH, "//button[contains(@aria-label,'Go to next slide')]").click()
        delay()
        driver.find_element(By.XPATH, "//img[contains(@alt, 'Man handling a Starlink to a woman')]")

        driver.find_element(By.XPATH, "//button[contains(@aria-label,'Go to next slide')]").click()
        delay()
        driver.find_element(By.XPATH, "(//img[contains(@loading,'lazy')])[2]")

    def test_edge_004(self):
        driver = self.driver
# 1. Go to https://www.starlink.com/
        H.StarLink(driver)
# 2. Click on the hamburger menu in the top right corner
        H.hamburger_menu(driver)
# 3. Click on the 'Customer Stories' link/button
        H.customer_stories(driver)
# 4. Scroll down
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# 5. Click on the link Careers
        original_window = driver.window_handles[0]
        driver.find_element(By.XPATH, "//a[@href='https://www.spacex.com/careers']").click()
        delay()
# 6. Navigate to the open page
        second_window = driver.window_handles[1]
        driver.switch_to.window(second_window)
        delay()
# 7. Verify that the page is correct
        try:
            assert "SpaceX" in driver.title
            print("Title is correct!")
        except WDE:
            print("Title is wrong! Title is: ", driver.title)

    def test_edge_005(self):
        driver = self.driver
# 1. Go to https://www.starlink.com/
        H.StarLink(driver)
# 2. Click on the hamburger menu in the top right corner
        H.hamburger_menu(driver)
# 3. Click on the 'Customer Stories' link/button
        H.customer_stories(driver)
# 4. Click on the 'Submit Story' button
        driver.find_element(By.XPATH, "//button[text()='Submit a Story']").click()
        delay()
# 5. Verify that the link scrolls to the form below
        Submit_button = driver.find_element(By.XPATH, "(//button[@type='submit'])[2]")
        if Submit_button:
            print("'Submit Story' button scrolls down to the form")
        else:
            print("'Submit Story' button  doesn't work!")

    # Anything declared in tearDown will be executed for all test cases
# Closing browser. You need to use "tearDown" method only one time for every Class
    def tearDown(self):
        self.driver.quit()

class ChromeTestsNegative(unittest.TestCase):
    def setUp(self):

        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        # options.add_argument("--headless")
        # options.add_argument(
        #     "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.3")
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

        self.driver.maximize_window()

        options.page_load_strategy = 'eager'
        #wait = WebDriverWait(driver, 5)

    # This is a class setUp. We will have 3 (chrome,firefox,edge)
    def test_chrome_001_1(self):
        driver = self.driver
# 1. Go to https://www.starlink.com/
        H.StarLink(driver)
# 2. Click on the hamburger menu in the top right corner
        H.hamburger_menu(driver)
# 3. Click on the 'Customer Stories' link/button
        H.customer_stories(driver)
# 4. Click on the 'Submit Story' button
        H.SubmitAStory_button(driver)
# 5. Leave the YOUR NAME field blank
        H.name(driver)
        H.username(driver)
# 6. Click on the Submit button
        H.submit_button(driver)
        driver.find_element(By.XPATH, "//span[@class='sc-b0ced1c2-2 eRetkP'][contains(.,'Your name is required.')]").is_displayed()
        print ("The message 'Your name is required' is displayed")

    def test_chrome_002_2(self):
        driver = self.driver
# 1. Go to https://www.starlink.com/
        H.StarLink(driver)
# 2. Click on the hamburger menu in the top right corner
        H.hamburger_menu(driver)
# 3. Click on the 'Customer Stories' link/button
        H.customer_stories(driver)
# 4. Click on the 'Submit Story' button
        H.SubmitAStory_button(driver)
# 5. Enter YOUR NAME
        H.nameMia(driver)
# 6. Leave the "@username (X/instagram/reddit)" field blank
        H.username(driver)
# 7. Click on the Submit button
        H.submit_button(driver)
        driver.find_element(By.XPATH,"//span[@class='sc-b0ced1c2-2 eRetkP'][contains(.,'Your username is required.')]").is_displayed()
        print("The message 'Your username is required' is displayed")

    def test_chrome_003_3(self):
        driver = self.driver
# 1. Go to https://www.starlink.com/
        H.StarLink(driver)
# 2. Click on the hamburger menu in the top right corne
        H.hamburger_menu(driver)
# 3. Click on the 'Customer Stories' link/button
        H.customer_stories(driver)
# 4. Click on the 'Submit Story' button
        H.SubmitAStory_button(driver)
# 5. Enter name and Username
        H.nameMia(driver)
        H.usernameMia(driver)
# 6. Leave the photo/video URL field blank
        driver.find_element(By.XPATH, "//input[contains(@id,'link')]").click()
        delay()
# 7. Click on the Submit button
        H.submit_button(driver)
        driver.find_element(By.XPATH, "//*[text()='Upload a valid file and/or enter a valid URL.']").is_displayed()
        print("The message 'Upload a valid file and/or enter a valid URL' is displayed")

    def test_chrome_004_4(self):
        driver = self.driver
# 1. Go to https://www.starlink.com/
        H.StarLink(driver)
# 2. Click on the hamburger menu in the top right corne
        H.hamburger_menu(driver)
# 3. Click on the 'Customer Stories' link/button
        H.customer_stories(driver)
# 4. Click on the 'Submit Story' button
        H.SubmitAStory_button(driver)
# 5. Enter name and Username
        H.nameMia(driver)
        H.usernameMia(driver)
# 6. Enter wrong URL in the "URL for your photo or video" field
        driver.find_element(By.XPATH, "//input[contains(@id,'link')]").send_keys("invalid URL")
# 7. Click on the Submit button
        H.submit_button(driver)
        driver.find_element(By.XPATH, "//*[text()='Please enter a valid URL.']").is_displayed()
        print("The message 'Please enter a valid URL' is displayed")

    def test_chrome_004_5(self):
        driver = self.driver
# 1. Go to https://www.starlink.com/
        H.StarLink(driver)
# 2. Click on the hamburger menu in the top right corne
        H.hamburger_menu(driver)
# 3. Click on the 'Customer Stories' link/button
        H.customer_stories(driver)
# 4. Scroll to the 2024 Progress Report
        label_Progress_Report = driver.find_element(By.XPATH, "//*[@aria-label='2024 Progress Report']")
        driver.execute_script("arguments[0].scrollIntoView();", label_Progress_Report)
        delay()
# 5. Leave the Email Address field blank
        driver.find_element(By.XPATH, "//input[contains(@name,'email')]").click()
# 6. Click on the Submit & Download PDF button
        driver.find_element(By.XPATH, "(//button[contains(@type,'submit')])[1]").click()
        driver.find_element(By.XPATH, "//*[text()='Email address is required to download.']").is_displayed()
        print("The message 'Email address is required to download' is displayed")

    # Anything declared in tearDown will be executed for all test cases
# Closing browser. You need to use "tearDown" method only one time for every Class
    def tearDown(self):
        self.driver.quit()

class EdgeTestsNegative(unittest.TestCase):
    def setUp(self):
        options = webdriver.EdgeOptions()
        options.add_argument('--ignore-certificate-errors')
        # options.add_argument("--headless")
        # options.add_argument(
        #     "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.3")
        self.driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=options)
        self.driver.maximize_window()

        options.page_load_strategy = 'eager'
        # wait = WebDriverWait(driver, 5)

    # This is a class setUp. We will have 3 (chrome,firefox,edge)
    def test_edge_001_1(self):
        driver = self.driver
# 1. Go to https://www.starlink.com/
        H.StarLink(driver)
# 2. Click on the hamburger menu in the top right corner
        H.hamburger_menu(driver)
# 3. Click on the 'Customer Stories' link/button
        H.customer_stories(driver)
# 4. Click on the 'Submit Story' button
        H.SubmitAStory_button(driver)
# 5. Leave the YOUR NAME field blank
        H.name(driver)
        H.username(driver)
# 6. Click on the Submit button
        H.submit_button(driver)
        driver.find_element(By.XPATH, "//span[@class='sc-b0ced1c2-2 eRetkP'][contains(.,'Your name is required.')]").is_displayed()
        print ("The message 'Your name is required' is displayed")

    def test_edge_002_2(self):
        driver = self.driver
# 1. Go to https://www.starlink.com/
        H.StarLink(driver)
# 2. Click on the hamburger menu in the top right corner
        H.hamburger_menu(driver)
# 3. Click on the 'Customer Stories' link/button
        H.customer_stories(driver)
# 4. Click on the 'Submit Story' button
        H.SubmitAStory_button(driver)
# 5. Enter YOUR NAME
        H.nameMia(driver)
# 6. Leave the "@username (X/instagram/reddit)" field blank
        H.username(driver)
# 7. Click on the Submit button
        H.submit_button(driver)
        driver.find_element(By.XPATH,"//span[@class='sc-b0ced1c2-2 eRetkP'][contains(.,'Your username is required.')]").is_displayed()
        print("The message 'Your username is required' is displayed")

    def test_edge_003_3(self):
        driver = self.driver
# 1. Go to https://www.starlink.com/
        H.StarLink(driver)
# 2. Click on the hamburger menu in the top right corne
        H.hamburger_menu(driver)
# 3. Click on the 'Customer Stories' link/button
        H.customer_stories(driver)
# 4. Click on the 'Submit Story' button
        H.SubmitAStory_button(driver)
# 5. Enter name and Username
        H.nameMia(driver)
        H.usernameMia(driver)
# 6. Leave the photo/video URL field blank
        driver.find_element(By.XPATH, "//input[contains(@id,'link')]").click()
        delay()
# 7. Click on the Submit button
        H.submit_button(driver)
        driver.find_element(By.XPATH, "//*[text()='Upload a valid file and/or enter a valid URL.']").is_displayed()
        print("The message 'Upload a valid file and/or enter a valid URL' is displayed")

    def test_edge_004_4(self):
        driver = self.driver
# 1. Go to https://www.starlink.com/
        H.StarLink(driver)
# 2. Click on the hamburger menu in the top right corne
        H.hamburger_menu(driver)
# 3. Click on the 'Customer Stories' link/button
        H.customer_stories(driver)
# 4. Click on the 'Submit Story' button
        H.SubmitAStory_button(driver)
# 5. Enter name and Username
        H.nameMia(driver)
        H.usernameMia(driver)
# 6. Enter wrong URL in the "URL for your photo or video" field
        driver.find_element(By.XPATH, "//input[contains(@id,'link')]").send_keys("invalid URL")
# 7. Click on the Submit button
        H.submit_button(driver)
        driver.find_element(By.XPATH, "//*[text()='Please enter a valid URL.']").is_displayed()
        print("The message 'Please enter a valid URL' is displayed")

    def test_edge_004_5(self):
        driver = self.driver
# 1. Go to https://www.starlink.com/
        H.StarLink(driver)
# 2. Click on the hamburger menu in the top right corne
        H.hamburger_menu(driver)
# 3. Click on the 'Customer Stories' link/button
        H.customer_stories(driver)
# 4. Scroll to the 2024 Progress Report
        label_Progress_Report = driver.find_element(By.XPATH, "//*[@aria-label='2024 Progress Report']")
        driver.execute_script("arguments[0].scrollIntoView();", label_Progress_Report)
        delay()
# 5. Leave the Email Address field blank
        driver.find_element(By.XPATH, "//input[contains(@name,'email')]").click()
# 6. Click on the Submit & Download PDF button
        driver.find_element(By.XPATH, "(//button[contains(@type,'submit')])[1]").click()
        driver.find_element(By.XPATH, "//*[text()='Email address is required to download.']").is_displayed()
        print("The message 'Email address is required to download' is displayed")

    # Anything declared in tearDown will be executed for all test cases
# Closing browser. You need to use "tearDown" method only one time for every Class
    def tearDown(self):
        self.driver.quit()

#if __name__ == '__main__':
#  unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./HtmlReports'))

#if __name__ == '__main__':
 #  suite = unittest.TestLoader().loadTestsFromTestCase(EdgeTestsNegative)
  # runner = HtmlTestRunner.HTMLTestRunner(output='./HtmlReports')
   #runner.run(suite)

#if __name__ == "__main__":
#   unittest.main(AllureReports)