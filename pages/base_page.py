from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    """
    Base page class that provides common Selenium WebDriver actions
    shared across all page objects.
    """

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_url(self, url: str):
        self.driver.get(url)

    def get_title(self) -> str:
        return self.driver.title
