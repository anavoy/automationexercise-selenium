from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class HomePage(BasePage):
    """
    Page Object representing the Home page and its main user interactions.
    """

    SIGNUP_BUTTON = (By.LINK_TEXT, "Signup / Login")
    LOGGED_IN_TEXT = (By.CSS_SELECTOR, "a > i.fa-user")
    DELETE_ACCOUNT_BUTTON = (By.XPATH, "//a[@href='/delete_account']")
    LOGOUT_BUTTON = (By.LINK_TEXT, "Logout")
    CONTACT_US_BUTTON = (By.LINK_TEXT, "Contact us")

    CONTACT_US_SUCCESS_MESSAGE = (By.XPATH, "//div[@class='status alert alert-success']")
    CONTACT_US_BUTTON_HOME = (By.LINK_TEXT, "Home")

    def is_home_page_visible(self):
        return "Automation Exercise" in self.get_title()

    def click_signup_login(self):
        self.driver.find_element(*self.SIGNUP_BUTTON).click()

    def is_logged_in_visible(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.LOGGED_IN_TEXT)
        ).is_displayed()
    
    def click_delete_account(self):
        self.wait.until(EC.element_to_be_clickable(self.DELETE_ACCOUNT_BUTTON)).click()


    def click_logout(self):
        self.wait.until(EC.element_to_be_clickable(self.LOGOUT_BUTTON)).click()

    def click_contact_us(self):
        self.driver.find_element(*self.CONTACT_US_BUTTON).click()

    def is_success_message_visible(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.CONTACT_US_SUCCESS_MESSAGE)
        ).is_displayed()

    def click_contact_us_home(self):
        self.driver.find_element(*self.CONTACT_US_BUTTON_HOME).click()
   