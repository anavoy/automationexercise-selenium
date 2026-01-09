from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class SignupPage(BasePage):
    """
    Page Object representing the Signup / Login page.
    Handles new user registration actions such as entering name,
    email address, and submitting the signup form.
    """

    NEW_USER_FORM = (By.XPATH, "//h2[text()='New User Signup!']")
    NAME_INPUT = (By.NAME, "name")
    EMAIL_INPUT = (By.XPATH, "//input[@data-qa='signup-email']")
    SIGNUP_BUTTON = (By.XPATH, "//button[@data-qa='signup-button']")

    def is_new_user_signup_visible(self):
        return self.driver.find_element(*self.NEW_USER_FORM).is_displayed()

    def enter_name(self, name):
        self.driver.find_element(*self.NAME_INPUT).send_keys(name)

    def enter_email(self, email):
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)

    def click_signup_button(self):
        self.driver.find_element(*self.SIGNUP_BUTTON).click()
