import time
from selenium.common.exceptions import WebDriverException as WDE
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.common.action_chains import ActionChains
import random


#common URLs
url_starlink = 'https://www.starlink.com/'
url_starlink_business_aviation = 'https://www.starlink.com/business/aviation'
url_starlink_business_aviation_http = 'http://www.starlink.com/business/aviation'
url_starlink_business_aviation_404 = 'https://www.starlink.com/business/aviation/404'
url_starlink_aviation_info = 'https://starlink.typeform.com/aviation-info'

#titles
title_starlink = 'Starlink'
title_starlink_business_aviation = 'Starlink Business | Aviation'

#header XPaths
header_logo = "//div[@class='starlink-logo-text']"
header_fixed_site = "/a[contains(text(),'Fixed Site')]"
header_land_mobility = "//a[contains(text(),'Land Mobility')]"
header_maritime = "//a[contains(text(),'Maritime')]"
header_aviation = "//a[contains(text(),'Aviation')]"
header_direct_to_cell = "//a[contains(text(),'Direct To Cell')]"
header_personal = "//a[contains(text(),'Personal')]"
header_business = "//a[contains(text(),'Business')]"
header_hamburger = "//img[@src='/assets/images/Menu_Hamburger.svg']"

#links
link_your_airframe = "//a[contains(text(),'your airframe.')]"
link_faqs_first = '//div[@class="toolbar-menu-container mat-body-1"]//a'
link_faqs_second = '//p[@class="text-description mat-body-1 ng-star-inserted"]//a'

#swiper and buttons
swiper = '//div[@class="swiper-pagination swiper-pagination-clickable swiper-pagination-bullets'
swiper_button_first = "//span[contains(@aria-label,'Go to slide 2')]"
swiper_button_second = "//span[contains(@aria-label,'Go to slide 3')]"
swiper_button_third = "//span[contains(@aria-label,'Go to slide 4')]"
swiper_button_fourth = "//span[contains(@aria-label,'Go to slide 5')]"
swiper_button_five = "//span[contains(@aria-label,'Go to slide 6')]"

#footer XPaths
footer_careers = "//a[contains(text(),'Careers')]"
footer_satellite_operators = "//a[contains(text(),'Satellite Operators')]"
footer_authorized_reseller = "//a[contains(text(),'Authorized Reseller')]"
footer_privacy_legal = "//a[contains(text(),'Privacy & Legal')]"
footer_privacy_preferences = "//a[contains(text(),'Privacy Preferences')]"
footer_x_logo = '//mat-icon[@class="mat-icon notranslate mat-icon-inline mat-icon-no-color"]'
footer_spacex_com = "//a[contains(text(),'spacex.com')]"
email_field = '//input[@type="email"]'
footer_privacy_policy = "//a[contains(text(),'Privacy Policy')]"

# messages
error_message_xpath = "//mat-error[@id='mat-error-1']"
error_message_text = "Please enter a valid email"


#headings XPaths and texts
#   Starlink for Aviation
heading_main_xpath = "//h1[contains(text(),'STARLINK FOR AVIATION')]"
heading_main_str = 'STARLINK FOR AVIATION'
heading_available_now_on_your_airframe = "//h2[contains(@class,'text-subheading mat-body-2 ng-star-inserted')]"
#   High-speed Internet in Flight
high_speed_internet = "//div[contains(text(),'High-Speed Internet In Flight')]"
high_speed_str = 'High-Speed Internet In Flight'.upper()
download_per_terminal = "//div[contains(text(),'Download per Terminal')]"
download_per_terminal_str = 'Download per Terminal'.upper()
download_per_terminal_info = "//div[contains(text(),'40-220 MBPS')]"
download_per_terminal_info_str = '40-220 MBPS'
upload_per_terminal = "//div[contains(text(),'Upload per Terminal')]"
upload_per_terminal_str = 'Upload per Terminal'.upper()
upload_per_terminal_info = "//div[contains(text(),'8-25 MBPS')]"
upload_per_terminal_info_str = '8-25 MBPS'
latency = "//div[contains(text(),'Latency')]"
latency_str = 'Latency'.upper()
latency_info = "//div[contains(text(),'Less than 99 MS')]"
latency_info_str = 'Less than 99 MS'.upper()

locators_high_speed_internet_in_flight = {
    "high_speed_internet": "//div[contains(text(),'High-Speed Internet In Flight')]",
    "high_speed_str": 'HIGH-SPEED INTERNET IN FLIGHT',

    "download_per_terminal": "//div[contains(text(),'Download per Terminal')]",
    "download_per_terminal_str": 'DOWNLOAD PER TERMINAL',

    "download_per_terminal_info": "//div[contains(text(),'40-220 MBPS')]",
    "download_per_terminal_info_str": '40-220 MBPS',

    "upload_per_terminal": "//div[contains(text(),'Upload per Terminal')]",
    "upload_per_terminal_str": 'UPLOAD PER TERMINAL',

    "upload_per_terminal_info": "//div[contains(text(),'8-25 MBPS')]",
    "upload_per_terminal_info_str": '8-25 MBPS',

    "latency": "//div[contains(text(),'Latency')]",
    "latency_str": 'LATENCY',

    "latency_info": "//div[contains(text(),'Less than 99 MS')]",
    "latency_info_str": 'LESS THAN 99 MS',
}

#buttons
button_contact_us_first = '//a[@class="mat-focus-indicator redirect-button-padding mat-flat-button mat-button-base mat-primary"]'
button_contact_us_second = "//span[contains(text(),'Contact Us')]"
button_contact_us_third = '//a[@class="mat-focus-indicator center-anchor mat-flat-button mat-button-base mat-primary ng-star-inserted"]'
button_contact_us_fourth = "//a[@class='mat-focus-indicator redirect-button mat-flat-button mat-button-base mat-primary']"
buttons_dict = {
    1: button_contact_us_first,
    2: button_contact_us_second,
    3: button_contact_us_third,
    4: button_contact_us_fourth
}

#   Arrows  and carousel
arrow_left = '//div[@aria-label="Previous slide"]'
arrow_right = '//div[@aria-label="Next slide"]'
carousel_container = '//swiper[@class="image-carousel-swiper swiper-container swiper-container-initialized swiper-container-horizontal swiper-container-pointer-events"]'
active_slide_xpath = carousel_container + "//div[contains(@class, 'active') or contains(@class, 'current')]"
carousel_items_xpath = carousel_container + "//div[contains(@class, 'item') or contains(@class, 'slide')]"

#images
img_one = '//img[@src="https://www.starlink.com/public-files/aviation_casestudy_businessaviation_m.jpg"]'
img_two = '//img[@src="https://www.starlink.com/public-files/aviation_casestudy_aircraftaanufacturers_m.jpg"]'
img_three = '//img[@src="https://www.starlink.com/public-files/aviation_casestudy_airlines_m.jpg"]'
img_four = '//img[@src="https://www.starlink.com/public-files/aviation_casestudy_charteroperators_m.jpg"]'
img_five = '//img[@src="https://www.starlink.com/public-files/aviation_casestudy_servicecenters_m.jpg"]'
img_six = '//img[@src="https://www.starlink.com/public-files/aviation_casestudy_completioncenters_m.jpg"]'
img_seven = '//img[@src="https://www.starlink.com/public-files/aviation_casestudy_government_m.jpg"]'

elements_dict =  {
        "//div[@class='starlink-logo-text']": "Header Logo",
        "//a[contains(text(),'Fixed Site')]": "Fixed Site Link",
        "//a[contains(text(),'Land Mobility')]": "Land Mobility Link",
        "//a[contains(text(),'Maritime')]": "Maritime Link",
        "//a[contains(text(),'Aviation')]": "Aviation Link",
        "//a[contains(text(),'Direct To Cell')]": "Direct To Cell Link",
        "//a[contains(text(),'Personal')]": "Personal Link",
        "//a[contains(text(),'Business')]": "Business Link",
        "//img[@src='/assets/images/Menu_Hamburger.svg']": "Hamburger Menu",
        "//a[contains(text(),'your airframe.')]": "Your Airframe Link",
        '//div[@class="toolbar-menu-container mat-body-1"]//a': "FAQs Link (First)",
        '//p[@class="text-description mat-body-1 ng-star-inserted"]//a': "FAQs Link (Second)",
        '//a[@class="mat-focus-indicator redirect-button-padding mat-flat-button mat-button-base mat-primary"]': "Contact Us Button (First)",
        "//span[contains(text(),'Contact Us')]": "Contact Us Button (Second)",
        '//a[@class="mat-focus-indicator center-anchor mat-flat-button mat-button-base mat-primary ng-star-inserted"]': "Contact Us Button (Third)",
        "//a[@class='mat-focus-indicator redirect-button mat-flat-button mat-button-base mat-primary']": "Contact Us Button (Fourth)",
        '//div[@aria-label="Previous slide"]': "Arrow Left",
        '//div[@aria-label="Next slide"]': "Arrow Right",
        "//span[contains(@aria-label,'Go to slide 2')]": "Swiper Button 1",
        "//span[contains(@aria-label,'Go to slide 3')]": "Swiper Button 2",
        "//span[contains(@aria-label,'Go to slide 4')]": "Swiper Button 3",
        "//span[contains(@aria-label,'Go to slide 5')]": "Swiper Button 4",
        "//span[contains(@aria-label,'Go to slide 6')]": "Swiper Button 5",
        "//a[contains(text(),'Careers')]": "Careers Link",
        "//a[contains(text(),'Satellite Operators')]": "Satellite Operators Link",
        "//a[contains(text(),'Authorized Reseller')]": "Authorized Reseller Link",
        "//a[contains(text(),'Privacy & Legal')]": "Privacy & Legal Link",
        "//a[contains(text(),'Privacy Preferences')]": "Privacy Preferences Link",
        '//mat-icon[@class="mat-icon notranslate mat-icon-inline mat-icon-no-color"]': "X Logo",
        "//a[contains(text(),'spacex.com')]": "SpaceX.com Link",
        "//input[@id='email-input-footer-918']": "Email Field",
        "//a[contains(text(),'Privacy Policy')]": "Privacy Policy Link"
    }


#       HELPS FUNCTIONS/METHODS

# driver sleep from 1 to 3 seconds
def delay():
    time.sleep(random.randint(1, 3))

# Checks if the given element has a visible focus indicator
def get_active_slide(driver):
    try:
        active_slide = driver.find_element(By.XPATH, active_slide_xpath)

        # Get the class attribute and sort the class names
        class_attr = active_slide.get_attribute("class")
        if class_attr:
            class_names = class_attr.split()
            sorted_class_names = " ".join(sorted(class_names))
        else:
            sorted_class_names = ""

        # Extract attributes we care about, including the sorted class names
        slide_data = {
            'index': active_slide.get_attribute("data-swiper-slide-index"),
            'aria-label': active_slide.get_attribute("aria-label"),
            'class': sorted_class_names
        }

        return slide_data
    except:
        return {'index': 'unknown', 'aria-label': 'unknown', 'class': ''}


def get_css_properties(driver, element):
    return {
        "outline": element.value_of_css_property("outline"),
        "border": element.value_of_css_property("border"),
        "box-shadow": element.value_of_css_property("box-shadow"),
        "background": element.value_of_css_property("background")
    }

def get_css_properties_firefox(driver, element):
    script = """
        var style = window.getComputedStyle(arguments[0]);
        return {
            outline: style.outline,
            outlineWidth: style.outlineWidth,
            outlineColor: style.outlineColor,
            outlineStyle: style.outlineStyle,
            border: style.border,
            boxShadow: style.boxShadow
        };
        """
    return driver.execute_script(script, element)

def parse_outline_width(value):
    if value in ["none", "auto", ""]:
        return 0
    return float(value.replace("px", "")) if "px" in value else float(value)


def normalize_box_shadow(value):
    return value.strip().lower().replace(", ", ",")


#       MAIN FUNCTIONS/METHODS

# Function to verify an element's visibility and correct spelling.
def verify_element_visibility_and_text(driver, wait, element_xpath, expected_text):
    element = wait.until(EC.visibility_of_element_located((By.XPATH, element_xpath)))
    assert element.is_displayed(), f'{expected_text} is not visible'
    print(f'{expected_text} is visible')

    # Verify the spelling of the element
    current_spelling = element.text.strip()
    assert current_spelling == expected_text, f'Spelling is not correct. Expected: {expected_text}, Got: {current_spelling}'
    print(f"{expected_text} element has correct spelling")


# title verifying
def verify_title(driver, expected_title, timeout=2):
    try:
        # Wait until the title is not empty and matches expected title
        WebDriverWait(driver, timeout).until(lambda d: d.title and expected_title in d.title)

        # Get the current title
        current_title = driver.title

        # Assert title matches
        assert current_title == expected_title, f'Title mismatch. Expected: {expected_title}, Got: {current_title}'

        print(f"Page title verified successfully: {current_title}")

    except Exception as e:
        raise AssertionError(
            f"Failed to verify title. Expected: {expected_title}, Got: '{driver.title}'. Error: {str(WDE)}")

# Function to verify the visibility and correctness of a heading.
def verify_heading(driver, expected_heading, heading_xpath, wait_time=1):
    wait = WebDriverWait(driver, wait_time)

    # Reuse the function to verify visibility and spelling
    verify_element_visibility_and_text(driver, wait, heading_xpath, expected_heading)


# Function to verify the visibility and functionality of CONTACT US buttons
def verify_contact_us_buttons_functionality(driver, wait, buttons, expected_url):
    # Store main window handle
    main_window = driver.current_window_handle

    # Verify visibility of all CONTACT US buttons
    for button, xpath in buttons.items():
        current_button = wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
        assert current_button.is_displayed(), f'{button} CONTACT US button is not visible'
        print(f'{button} CONTACT US button is visible')

    # Initialize counters
    counter_new_tab = 0
    counter_same_tab = 0

    # Verify behavior after clicks
    for button, xpath in buttons.items():
        current_button = wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))

        # Store initial window handles
        initial_handles = set(driver.window_handles)

        # Click the button
        current_button.click()
        time.sleep(2)

        # Capture new window handles
        current_handles = set(driver.window_handles)

        if len(current_handles) == len(initial_handles):  # Same tab behavior
            assert driver.current_url == expected_url, f'URL mismatch for {button} CONTACT US button in SAME TAB'
            print(f'After clicking {button} CONTACT US button, aviation info opened on {expected_url} in the SAME TAB')

            counter_same_tab += 1

            # Navigate back to the original page
            driver.back()

        else:  # New tab behavior
            new_tab = list(current_handles - initial_handles)[0]
            driver.switch_to.window(new_tab)

            assert driver.current_url == expected_url, f'URL mismatch for {button} CONTACT US button in NEW TAB'
            print(f'After clicking {button} CONTACT US button, aviation info opened on {expected_url} in a NEW TAB')

            counter_new_tab += 1

            # Close the new tab and switch back to the main window
            driver.close()
            driver.switch_to.window(main_window)

        # Wait for page to stabilize
        time.sleep(2)

    print(f'After clicking CONTACT US buttons, {expected_url} opened {counter_new_tab} times in a NEW TAB and {counter_same_tab} times in the SAME TAB')



# Function to verify the visibility and correct spelling of elements in the High-Speed Internet section.
def verify_high_speed_internet_section(driver, wait, locators):
    # Verify each section element
    verify_element_visibility_and_text(driver, wait, locators["high_speed_internet"],locators["high_speed_str"])
    verify_element_visibility_and_text(driver, wait, locators["download_per_terminal"], locators["download_per_terminal_str"])
    verify_element_visibility_and_text(driver, wait, locators["download_per_terminal_info"], locators["download_per_terminal_info_str"])
    verify_element_visibility_and_text(driver, wait, locators["upload_per_terminal"], locators["upload_per_terminal_str"])
    verify_element_visibility_and_text(driver, wait, locators["upload_per_terminal_info"], locators["upload_per_terminal_info_str"])
    verify_element_visibility_and_text(driver, wait, locators["latency"], locators["latency_str"])
    verify_element_visibility_and_text(driver, wait, locators["latency_info"],locators["latency_info_str"])

    print("\nHigh-Speed Internet section verification completed successfully.")

# Function to verify the functionality of navigation arrows in a carousel
def verify_navigation_arrows_functionality(driver, wait, carousel_xpath, right_arrow_xpath, left_arrow_xpath, get_active_slide):
    try:
        # Locate the carousel container
        carousel = wait.until(EC.visibility_of_element_located((By.XPATH, carousel_xpath)))
        all_carousel_elements = carousel.find_elements(By.XPATH, ".//*")

        # Locate navigation arrows within the carousel
        right_arrow = carousel.find_element(By.XPATH, right_arrow_xpath)
        assert right_arrow in all_carousel_elements, 'Unsuccessfully located right arrow'

        left_arrow = carousel.find_element(By.XPATH, left_arrow_xpath)
        assert left_arrow in all_carousel_elements, 'Unsuccessfully located left arrow'

        print("Successfully located navigation arrows")
    except:
        raise AssertionError(f'Failed to locate navigation arrows: {str(WDE)}')

        # Capture initial state for comparison
    try:
        initial_slide = get_active_slide(driver)
        print("Captured initial slide state")
    except:
        raise AssertionError(f"Could not capture initial state of carousel: {str(WDE)}")

        # Click right arrow
    try:
        right_arrow.click()
        print("Clicked right navigation arrow")
        time.sleep(1)

        # Verify slide changed
        current_slide = get_active_slide(driver)
        assert initial_slide != current_slide, 'Right arrow click did not change the carousel slide'
        print("Verified carousel changed after right arrow click")
    except:
        raise AssertionError(f"Failed during right arrow click test: {str(WDE)}")

        # Click left arrow
    try:
        left_arrow.click()
        print("Clicked left navigation arrow")
        time.sleep(1)

        # Verify slide returned to initial state
        final_slide = get_active_slide(driver)
        assert initial_slide == final_slide, 'Left arrow click did not return to the initial slide'
        print("Verified carousel returned to initial slide after left arrow click")
    except:
        raise AssertionError(f"Failed during left arrow click test: {str(WDE)}")


#Function to verify that an unsecured HTTP connection correctly redirects to HTTPS
def verify_unsecured_connection(http_url, expected_https_url):
    response = requests.get(http_url, allow_redirects=True)

    # Check that the final URL is the expected HTTPS version
    assert response.url == expected_https_url, f'Expected redirect to {expected_https_url}, Actual: {response.url}'

    # Verify that the status code is 200
    assert response.status_code == 200, f'Expected status code 200, Actual: {response.status_code}'

    print(f'Current URL is {response.url}, Status code is {response.status_code}')


#Function to verify the behavior of a non-existent (404) page.
def verify_page_behavior(url, main_page_url):
    response = requests.get(url, allow_redirects=True)

    # Print status code and final URL after redirections
    print(f"Status code received: {response.status_code}")
    print(f"Final URL after redirects: {response.url}")

    # Check if there were any redirects
    if response.history:
        print("Redirects detected:")
        for resp in response.history:
            print(f"  - {resp.status_code} -> {resp.url}")

    # Parse the HTML content of the response
    soup = BeautifulSoup(response.text, 'html.parser')
    page_text = soup.get_text().lower()

    if "/404" in response.url:
        print("Site uses a custom 404 page with a 200 status.")
    elif response.status_code == 404:
        print("Site correctly returns a 404 status code for non-existent pages.")
    elif response.status_code == 200:
        content_404 = any(term in page_text for term in ['404', 'not found', 'page not found', "doesn't exist"])
        if content_404:
            print("Site returns a 200 status but contains 404-related content - this is a custom 404 page.")
        else:
            raise AssertionError("Page returned 200 status and does not appear to be a 404 page.")

    # Check for a link back to the main page
    main_page_links = [a for a in soup.find_all('a') if a.get('href') in ['/', main_page_url]]
    assert len(main_page_links) > 0, "No link back to the main page found on the 404 page."

    print(f"Links back to the main page found: {len(main_page_links)}")
    for link in main_page_links:
        print(f"  - {link}")
        

#Function to test keyboard accessibility by verifying if elements receive focus and their outline changes.
def verify_keyboard_accessibility(driver, wait, focusable_elements, css_property_extractor, max_tabs=50):
    body = driver.find_element(By.TAG_NAME, 'body')
    body.click()  # Ensure the page is active before sending TAB
    time.sleep(1)

    # Dictionary to track elements receiving focus
    found_elements = {}

    for xpath, name in focusable_elements.items():
        try:
            element = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
            found_elements[element] = {"name": name, "focused": False, "outline_changed": False}
            print(f"FOUND: {name} on the page.")
        except:
            print(f"ERROR: {name} not found on the page.")

    # Capture initial outline property for all found elements
    for element, data in found_elements.items():
        initial_props = css_property_extractor(driver, element)
        data["initial_outline"] = initial_props.get("outline", "none 0px")

    # Reset focus to the beginning of the page
    body.click()
    time.sleep(1)

    # Press TAB repeatedly to navigate through focusable elements
    for tab_count in range(max_tabs):
        active = driver.switch_to.active_element
        active.send_keys(Keys.TAB)
        time.sleep(0.5)

        # Get the currently focused element
        focused_element = driver.switch_to.active_element

        # Check if the focused element is in our dictionary
        for element, data in found_elements.items():
            try:
                if element == focused_element:
                    data["focused"] = True

                    # Get current CSS properties
                    current_props = get_css_properties(driver, element)
                    current_outline = current_props.get("outline", "none 0px")

                    # Extract outline thickness for comparison
                    initial_thickness = data["initial_outline"].split()[-1] if " " in data["initial_outline"] else "0px"
                    current_thickness = current_outline.split()[-1] if " " in current_outline else "0px"

                    # Check if outline changed meaningfully
                    if initial_thickness == "0px" and current_thickness != "0px":
                        data["outline_changed"] = True
                        data["focused_outline"] = current_outline

                    print(f"TAB #{tab_count + 1}: Focus on {data['name']}, Outline: {current_outline}")
                    break
            except:
                # Element might have become stale
                continue

    # Print final results
    print("\n=== ACCESSIBILITY TEST RESULTS ===")
    for element, data in found_elements.items():
        name = data["name"]
        if data["focused"]:
            if data["outline_changed"]:
                print(
                    f"PASS: {name} - Received keyboard focus and outline changed from {data['initial_outline']} to {data.get('focused_outline', 'unknown')}")
            else:
                print(f"FAIL: {name} - Received keyboard focus but outline did not change significantly")
        else:
            print(f"FAIL: {name} - Never received keyboard focus during TAB navigation")


#  Function to test page load performance under a simulated 3G network.
def verify_page_load_under_3g(driver):
    # Open DevTools (F12)
    ActionChains(driver).send_keys(Keys.F12).perform()
    time.sleep(2)  # Allow time for DevTools to open

    # Switch to the Network tab (SHIFT + CTRL + E in DevTools)
    ActionChains(driver).key_down(Keys.CONTROL).key_down(Keys.SHIFT).send_keys("E").key_up(Keys.SHIFT).key_up(
        Keys.CONTROL).perform()
    time.sleep(2)

    # Set throttling to a slower 3G using Chrome DevTools Protocol (CDP)
    driver.execute_cdp_cmd("Network.enable", {})
    driver.execute_cdp_cmd("Network.emulateNetworkConditions", {
        "offline": False,
        "latency": 300,  # Increased latency to 300ms
        "downloadThroughput": 0.4 * 1024 * 1024 / 8,  # Reduced download speed to 400 Kbps
        "uploadThroughput": 0.2 * 1024 * 1024 / 8  # Reduced upload speed to 200 Kbps
    })
    time.sleep(2)

    # Clear browser cache and cookies
    driver.execute_cdp_cmd("Network.clearBrowserCache", {})
    driver.execute_cdp_cmd("Network.clearBrowserCookies", {})
    time.sleep(1)

    # Reload the page with cache clearing
    driver.execute_script("window.location.reload(true)")

    # Measure page load time
    start_time = time.time()
    while True:
        # Check if the page has fully loaded
        if driver.execute_script("return document.readyState") == "complete":
            break
        time.sleep(0.1)
    load_time = time.time() - start_time

    # Retrieve metrics from the Performance API
    performance = driver.execute_script("return window.performance.timing")
    dom_content_loaded = (performance["domContentLoadedEventEnd"] - performance["navigationStart"]) / 1000
    finish_time = (performance["loadEventEnd"] - performance["navigationStart"]) / 1000

    print("=== NETWORK CONDITIONS ===")
    print("Latency: 300ms")
    print("Download Speed: 400 Kbps")
    print("Upload Speed: 200 Kbps")
    print("==========================")

    return dom_content_loaded, finish_time


# Function to verify email field validation by inputting an invalid email and checking for error messages
def verify_email_field_validation(driver, wait, email_field_xpath, xpath_error_message, text_expected, faker):
    # Find the email input field
    email = wait.until(EC.element_to_be_clickable((By.XPATH, email_field_xpath)))

    # Click on the email input field to activate it
    email.click()

    delay()

    # Generate an invalid email (adding extra dot after @)
    invalid_email = faker.email().replace("@", "@.")
    email.send_keys(invalid_email)

    # Move focus away from the email field
    driver.find_element(By.TAG_NAME, 'body').click()

    # Retry locating the email field again before checking error message
    email = wait.until(EC.element_to_be_clickable((By.XPATH, email_field_xpath)))
    delay()

    # Wait for the error message to appear
    error_message = wait.until(EC.visibility_of_element_located((By.XPATH, xpath_error_message)))

    # Verify the error message contains the expected text
    assert text_expected in error_message.text, f"Expected error message containing '{text_expected}', Actual: '{error_message.text}'"

    # Log the actual result
    print(f"Invalid email used: {invalid_email}")
    print(f"Actual result: An appropriate error message appears ('{error_message.text}')")
