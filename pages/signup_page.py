from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class SignupPage(BasePage):
    """
    Page Object representing the Signup / Login page.
    Handles new user registration actions such as entering name,
    email address, and submitting the signup form.
    """


    # NEW USER SIGNUP
    NEW_USER_FORM = (By.XPATH, "//h2[text()='New User Signup!']")
    NAME_INPUT = (By.NAME, "name")
    EMAIL_INPUT = (By.XPATH, "//input[@data-qa='signup-email']")
    SIGNUP_BUTTON = (By.XPATH, "//button[@data-qa='signup-button']")


    # LOGIN
    LOGIN_TITLE = (By.XPATH, "//h2[text()='Login to your account']")
    LOGIN_EMAIL = (By.XPATH, "//input[@data-qa='login-email']")
    LOGIN_PASSWORD = (By.XPATH, "//input[@data-qa='login-password']")
    LOGIN_BUTTON = (By.XPATH, "//button[@data-qa='login-button']")
    ERROR_MESSAGE = (By.XPATH, "//p[text()='Your email or password is incorrect!']")
    

    def is_new_user_signup_visible(self):
        return self.driver.find_element(*self.NEW_USER_FORM).is_displayed()

    def enter_name(self, name):
        self.driver.find_element(*self.NAME_INPUT).send_keys(name)

    def enter_email(self, email):
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)

    def click_signup_button(self):
        self.driver.find_element(*self.SIGNUP_BUTTON).click()

    def is_login_title_visible(self):
        return self.driver.find_element(*self.LOGIN_TITLE).is_displayed()
    
    def login(self,email,password):
        self.driver.find_element(*self.LOGIN_EMAIL).send_keys(email)
        self.driver.find_element(*self.LOGIN_PASSWORD).send_keys(password)
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    
    def is_error_message_visible(self):
        return self.driver.find_element(*self.ERROR_MESSAGE).is_displayed()