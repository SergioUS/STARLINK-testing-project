from builtins import AssertionError
import Locator_Technology as lc

#import HtmlTestRunner
#import AllureReports
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException as WDE
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FF_Options
from selenium.webdriver.edge.options import Options as Edge_Options
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
import random
import unittest
import time
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService


# driver sleep from 2 to 3 seconds
def delay():
    time.sleep(random.randint(2, 5))


class AllElement:
    pass


class WebElement:
    pass


class Sign:
    pass


class ChromePositiveTechnology(unittest.TestCase):

    def setUp(self):
        # Next 3 lines of code is disabled Captcha in Google website
        options = Options()
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.page_load_strategy = 'eager'
        options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 Edg/132.0.0.")
        options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()

    # As per unittest module, individual test should start with test_
    def test_TC_016(self):
        driver = self.driver
        lc.tc16(driver)
        driver.quit()


    def test_TC_017(self):
        driver = self.driver
        lc.tc17(driver)
        driver.quit()


    def test_TC_018(self):
        driver = self.driver
        lc.tc18(driver)
        driver.quit()


    def test_TC_019(self):
        driver = self.driver
        lc.tc19(driver)
        driver.quit()


    def test_TC_020(self):
        driver = self.driver
        lc.tc20(driver)
        driver.quit()

#_________________________________________________________________________________________________
#-------------------------------------------------------------------------------------------------

# Negative tests
class ChromeNegativeTechnology(unittest.TestCase):

    def setUp(self):
        # Next 3 lines of code is disabled Captcha in Google website
        options = Options()
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.page_load_strategy = 'eager'
        options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 Edg/132.0.0.")
        options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()


    def test_TC_016_16(self):
        driver = self.driver
        lc.tc016_16(driver)
        driver.quit()


    def test_TC_017_17(self):
        driver = self.driver
        lc.tc017_17(driver)
        driver.quit()


    def test_018_18(self):
        driver = self.driver
        lc.tc018_18(driver)
        driver.quit()


    def test_019_19(self):
        driver = self.driver
        lc.tc019_19(driver)
        driver.quit()


    def test_020_20(self):
        driver = self.driver
        lc.tc020_20(driver)
        driver.quit()
#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
class FirefoxPositiveTechnology(unittest.TestCase):

    def setUp(self):

        # Next 3 lines of code is disabled Captcha in Firefox website
        options = webdriver.FirefoxOptions()
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.page_load_strategy = 'eager'
        options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 Edg/132.0.0.")
        #options.add_argument('--headless')
        self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
        self.driver.maximize_window()



    # As per unittest module, individual test should start with test_
    def test_TC_016(self):
        driver = self.driver
        lc.tc16(driver)
        driver.quit()

    def test_TC_017(self):
        driver = self.driver
        lc.tc17(driver)
        driver.quit()

    def test_TC_018(self):
        driver = self.driver
        lc.tc18(driver)
        driver.quit()

    def test_TC_019(self):
        driver = self.driver
        lc.tc19(driver)
        driver.quit()

    def test_TC_020(self):
        driver = self.driver
        lc.tc20(driver)
        driver.quit()

    # _________________________________________________________________________________________________
    # -------------------------------------------------------------------------------------------------
    # Negative tests
class FirefoxNegativeTechnology(unittest.TestCase):

    def setUp(self):
        # Next 3 lines of code is disabled Captcha in Firefox website
        options = webdriver.FirefoxOptions()
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.page_load_strategy = 'eager'
        options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 Edg/132.0.0.")
        options.add_argument('--headless')
        self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
        self.driver.maximize_window()
        time.sleep(8)

    def test_TC_016_16(self):
        driver = self.driver
        lc.tc016_16(driver)
        driver.quit()

    def test_TC_017_17(self):
        driver = self.driver
        lc.tc017_17(driver)
        driver.quit()

    def test_018_18(self):
        driver = self.driver
        lc.tc018_18(driver)
        driver.quit()

    def test_019_19(self):
        driver = self.driver
        lc.tc019_19(driver)
        driver.quit()

    def test_020_20(self):
        driver = self.driver
        lc.tc020_20(driver)
        driver.quit()
#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
class EdgePositiveTechnology(unittest.TestCase):

    def setUp(self):
        # Next 3 lines of code is disabled Captcha in Edge website
        options = webdriver.EdgeOptions()
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.page_load_strategy = 'eager'
        options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 Edg/132.0.0.")
        options.add_argument('--headless')
        self.driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=options)
        self.driver.maximize_window()

    # As per unittest module, individual test should start with test_
    def test_TC_016(self):
        driver = self.driver
        lc.tc16(driver)
        driver.quit()

    def test_TC_017(self):
        driver = self.driver
        lc.tc17(driver)
        driver.quit()

    def test_TC_018(self):
        driver = self.driver
        lc.tc18(driver)
        driver.quit()

    def test_TC_019(self):
        driver = self.driver
        lc.tc19(driver)
        driver.quit()

    def test_TC_020(self):
        driver = self.driver
        lc.tc20(driver)
        driver.quit()

    # _________________________________________________________________________________________________
    # -------------------------------------------------------------------------------------------------
    # Negative tests

class EdgeNegativeTechnology(unittest.TestCase):

    def setUp(self):
        # Next 3 lines of code is disabled Captcha in Edge website
        options = webdriver.EdgeOptions()
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.page_load_strategy = 'eager'
        options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 Edg/132.0.0.")
        options.add_argument('--headless')
        self.driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=options)
        self.driver.maximize_window()
        time.sleep(8)

    def test_TC_016_16(self):
        driver = self.driver
        lc.tc016_16(driver)
        driver.quit()

    def test_TC_017_17(self):
        driver = self.driver
        lc.tc017_17(driver)
        driver.quit()

    def test_018_18(self):
        driver = self.driver
        lc.tc018_18(driver)
        driver.quit()

    def test_019_19(self):
        driver = self.driver
        lc.tc019_19(driver)
        driver.quit()

    def test_020_20(self):
        driver = self.driver
        lc.tc020_20(driver)
        driver.quit()

    # Anything declared in tearDown will be executed for all test cases
    # Closing browser. You need to use "tearDown" method only one time for every Class
    def tearDown(self):
        self.driver.quit()

# if __name__ == '__main__':
#     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./HtmlReports'))

# if __name__ == "__main__":
#    unittest.main(AllureReports)
