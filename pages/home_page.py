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


    TEST_CASES_BUTTON = (By.LINK_TEXT, "Test Cases")
    TEST_CASES_TITLE = (By.XPATH, "//h2[contains(text(),'Test Cases')]")
    TEST_CASES_TITLES = (By.CSS_SELECTOR,"div.panel-group a")

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

    def click_test_cases(self):
        element = self.driver.find_element(*self.TEST_CASES_BUTTON)
        self.driver.execute_script("arguments[0].click();", element)

    def is_test_cases_page_visible(self):
        WebDriverWait(self.driver, 20).until(
        lambda d: "/test_cases" in d.current_url
    )
        return True
    
    def are_test_case_titles_visible(self, expected_titles: list[str]) -> bool:
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        element =self.driver.find_elements(*self.TEST_CASES_TITLES)
        text = [el.text.strip() for el in element]

        for title in expected_titles:
            if title not in text:
                return False
        return True
        