from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

from pages.base_page import BasePage


class AccountInfoPage(BasePage):
    """
    Page Object representing the account details form during user registration.
    """

    ACCOUNT_INFO_TITLE = (By.CSS_SELECTOR, "h2.title.text-center")
    PASSWORD = (By.ID, "password")
    CREATE_ACCOUNT_BTN = (By.XPATH, "//button[text()='Create Account']")
    TITLE_MR = (By.ID, "id_gender1")

    DAYS = (By.ID, "days")
    MONTHS = (By.ID, "months")
    YEARS = (By.ID, "years")

    FIRST_NAME = (By.ID, "first_name")
    LAST_NAME = (By.ID, "last_name")
    ADDRESS = (By.ID, "address1")
    COUNTRY = (By.ID, "country")
    STATE = (By.ID, "state")
    CITY = (By.ID, "city")
    ZIPCODE = (By.ID, "zipcode")
    MOBILE_NUMBER = (By.ID, "mobile_number")

    NEWSLETTER_CHECKBOX = (By.ID, "newsletter")
    OFFERS_CHECKBOX = (By.ID, "optin")

    NEWSLETTER_CHECKBOX = (By.ID, "newsletter")
    OFFERS_CHECKBOX = (By.ID, "optin")

    FORM_NAME = (By.NAME, "name")
    FORM_EMAIL = (By.NAME, "email")
    FORM_SUBJECT = (By.NAME, "subject")
    FORM_MESSAGE = (By.NAME, "message")

    # CONTACT US locators
    CONTACT_US_TITLE = (By.XPATH, "//h2[text()='Get In Touch']")
    CONTACT_US_SUBMIT_BUTTON = (By.CSS_SELECTOR, "[data-qa='submit-button']")
    UPLOAD_FILE = (By.NAME, "upload_file")


    def is_account_info_visible(self):
        return self.driver.find_element(*self.ACCOUNT_INFO_TITLE).is_displayed()

    def enter_password(self, password):
        self.driver.find_element(*self.PASSWORD).send_keys(password)

    def click_create_account(self):
        button = self.wait.until(EC.element_to_be_clickable(self.CREATE_ACCOUNT_BTN))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", button)
        self.driver.execute_script("arguments[0].click();", button)

    def fill_account_info(self):
        self.driver.find_element(*self.TITLE_MR).click()
        self.driver.find_element(*self.PASSWORD).send_keys("password123")

        Select(self.driver.find_element(*self.DAYS)).select_by_value("10")
        Select(self.driver.find_element(*self.MONTHS)).select_by_value("5")
        Select(self.driver.find_element(*self.YEARS)).select_by_value("1990")

    def fill_address_info(self):
        self.driver.find_element(*self.FIRST_NAME).send_keys("John")
        self.driver.find_element(*self.LAST_NAME).send_keys("Doe")
        self.driver.find_element(*self.ADDRESS).send_keys("123 Main St")
        Select(self.driver.find_element(*self.COUNTRY)).select_by_visible_text(
            "United States"
        )
        self.driver.find_element(*self.STATE).send_keys("California")
        self.driver.find_element(*self.CITY).send_keys("Los Angeles")
        self.driver.find_element(*self.ZIPCODE).send_keys("90001")
        self.driver.find_element(*self.MOBILE_NUMBER).send_keys("1234567890")

    def select_checkboxes(self):
        self.driver.find_element(*self.NEWSLETTER_CHECKBOX).click()
        self.driver.find_element(*self.OFFERS_CHECKBOX).click()

    
    def is_contact_us_title_visible(self):
        return self.driver.find_element(*self.CONTACT_US_TITLE).is_displayed()


    def fill_contact_us_form(self):
        self.driver.find_element(*self.FORM_NAME).send_keys("John Doe")
        self.driver.find_element(*self.FORM_EMAIL).send_keys("john.doe@example.com")
        self.driver.find_element(*self.FORM_SUBJECT).send_keys("Inquiry")
        self.driver.find_element(*self.FORM_MESSAGE).send_keys("I have a question about your services.")

    def upload_file(self, file_path):
        self.driver.find_element(*self.UPLOAD_FILE).send_keys(file_path)

    def submit_contact_us_form(self):
        self.driver.find_element(*self.CONTACT_US_SUBMIT_BUTTON).click()

    def accept_alert(self):
        alert = self.wait.until(EC.alert_is_present())
        alert.accept()

  
    