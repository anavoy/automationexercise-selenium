from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class AccountCreatedPage(BasePage):
    """
    Page Object for account creation and deletion confirmation pages.
    """

    ACCOUNT_CREATED_TEXT = (By.XPATH, "//b[text()='Account Created!']")
    CONTINUE_BTN = (By.LINK_TEXT, "Continue")
    ACCOUNT_DELETED_TEXT = (By.XPATH, "//b[text()='Account Deleted!']")

    def is_account_created_visible(self):
        return self.driver.find_element(*self.ACCOUNT_CREATED_TEXT).is_displayed()

    def click_continue(self):
        self.driver.find_element(*self.CONTINUE_BTN).click()

    def is_account_deleted_visible(self):
        return WebDriverWait(self.driver, 10).until(
        EC.visibility_of_element_located(self.ACCOUNT_DELETED_TEXT)
    ).is_displayed()
