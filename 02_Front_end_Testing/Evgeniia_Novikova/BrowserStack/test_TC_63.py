import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options as ChromeOptions
import heplpers_BS as h

options = ChromeOptions()
options.set_capability('sessionName', 'BStack Sample Test')
driver = webdriver.Chrome(options=options)

driver.get(h.url_starlink_business_aviation)
driver.maximize_window()
wait = WebDriverWait(driver, 5)

# Store main window handle
main_window = driver.current_window_handle

# Verify visibility of all CONTACT US buttons
for button, xpath in h.buttons_dict.items():
    current_button = wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
    assert current_button.is_displayed(), f'{button} CONTACT US button is not visible'
    print(f'{button} CONTACT US button is visible')

# Initialize counters
counter_new_tab = 0
counter_same_tab = 0

#Verify behavior after clicks
for button, xpath in h.buttons_dict.items():
    current_button = wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))

    # Store initial window handles
    initial_handles = set(driver.window_handles)

    # Click the button
    current_button.click()
    time.sleep(2)

    # Capture new window handles
    current_handles = set(driver.window_handles)

    if len(current_handles) == len(initial_handles):  # Same tab behavior
        assert driver.current_url == h.url_starlink_aviation_info, f'URL mismatch for {button} CONTACT US button in SAME TAB'
        print(f'After clicking {button} CONTACT US button, aviation info opened on {h.url_starlink_aviation_info} in the SAME TAB')

        counter_same_tab += 1

        # Navigate back to the original page
        driver.back()

    else:  # New tab behavior
        new_tab = list(current_handles - initial_handles)[0]
        driver.switch_to.window(new_tab)

        assert driver.current_url == h.url_starlink_aviation_info, f'URL mismatch for {button} CONTACT US button in NEW TAB'
        print(f'After clicking {button} CONTACT US button, aviation info opened on {h.url_starlink_aviation_info} in a NEW TAB')

        counter_new_tab += 1

        # Close the new tab and switch back to the main window
        driver.close()
        driver.switch_to.window(main_window)

    # Wait for page to stabilize
    time.sleep(2)

print(
    f'After clicking CONTACT US buttons, {h.url_starlink_aviation_info} opened {counter_new_tab} times in a NEW TAB and {counter_same_tab} times in the SAME TAB')

driver.quit()