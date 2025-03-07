from selenium.webdriver.common.by import By

class Locators:
    # Homepage
    #ACCOUNT_LOCKED_ERROR = None
    #WARNING_MESSAGE = None
    LOGIN_PAGE_TITLE = (By.XPATH, "//h1[@class='MuiTypography-root MuiTypography-h1 mui-i4qams']")
    LOGO_LOCATOR = (By.XPATH, "//div[contains(@class, 'starlink-logo-text')]")
    HAMBURGER_MENU_LOCATOR = (By.XPATH, "//img[@alt='Open Menu']")
    SIGN_IN_OPTION_LOCATOR = (By.XPATH, "//a[contains(text(), 'Sign In')]")

    # Login Page
    SIGN_IN_PAGE_LOCATOR = (By.XPATH, "//h1[contains(text(), 'Sign In')]")

    # Order Starlink
    ORDER_STARLINK_BUTTON_LOCATOR = (By.XPATH, "//span[contains(text(), 'Order Starlink')]")
    ORDER_NOW_BUTTON_LOCATOR = (By.XPATH, "(//span[contains(text(), 'Order Now')])[2]")

    # Checkout Page
    COUNTRY_LABEL_FIELD = (By.XPATH, "//div[contains(text(), 'United States')]")
    PRODUCT_DETAILS_BUTTON = (By.XPATH, "(//button[@type='button'])[7]")
    CHECKOUT_BUTTON_LOCATOR = (By.XPATH, "(//span[@class='MuiTypography-root MuiTypography-button MuiTypography-noWrap mui-11i8kmk'])[3]")
    CHECKOUT_ELEMENT = (By.XPATH, "//div[@class='MuiBox-root mui-1gzcyk']")
    SHIPPING_ADDRESS_WINDOW = (By.XPATH, "//div[@class='MuiStack-root mui-6wlff5']")
    ZIP_POSTAL_CODE_FIELD = (By.ID, ":rs:")
    SHIPPING_ADDRESS_LINE_1_FIELD = (By.NAME, "addressLine1")
    CITY_FIELD = (By.ID, ":rb:")
    STATE_PROVINCE_FIELD = (By.ID, ":rg:")
    COUNTRY_FIELD = (By.ID, ":ri:")
    UPDATE_SHIPPING_ADDRESS_BUTTON = (By.XPATH, "//span[contains(text(), 'Update Shipping Address')]")
    PLACE_ORDER_BUTTON = (By.XPATH, "//button[contains(text(), 'Place Order')]")

    # Error Message
    ERROR_MESSAGE_LOCATOR = (By.XPATH, "//span[@class='ng-star-inserted']")
    ERROR_MESSAGES_LOCATOR = (By.XPATH, "//div[contains(@class, 'error-message')]")
    EMAIL_ERROR_MESSAGE = (By.XPATH, "(//span[contains(@class, 'mui-1tmpjwc')])[1]")
    PASSWORD_ERROR_MESSAGE = (By.XPATH, "(//span[contains(@class, 'mui-1tmpjwc')])[2]")
    INVALID_EMAIL_ERROR = (By.XPATH, "//span[contains(text(), 'Invalid email address')]")


    # Modal Window
    MODAL_WINDOW_LOCATOR = (By.XPATH, "//div[contains(@class, 'modal-window')]")

    # Checkout Page Elements
    CHECKOUT_PAGE_TITLE = (By.XPATH, "//h1[contains(text(), 'Checkout')]")

    # Close Button
    CLOSE_BUTTON = (By.XPATH, "//button[text()='No thanks']")

    # Negative Test Login Page
    INVALID_CREDENTIALS_ERROR = (By.XPATH, "//div[@data-sentry-element='Alert']")
    SIGN_IN_BUTTON = (By.XPATH, "//button[@data-testid='submit-button']")
    PASSWORD_FIELD = (By.ID, ':R5qfnkql57rbkq:')
    EMAIL_FIELD = (By.ID, ':R1afnkql57rbkq:')


