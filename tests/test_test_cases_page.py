from pages.home_page import HomePage


def test_test_cases_page(driver):
    """
    Docstring for test_test_cases_page
    
    :param driver: Description
    :type driver: WebDriver
    """

    home = HomePage(driver)

    # 1. Open home page
    home.open_url("https://automationexercise.com")
    assert home.is_home_page_visible(), "Home page is not visible"

    # 2. Click 'Test Cases' button
    home.click_test_cases()

    # 3. Verify that user is navigated to test cases page successfully
    assert home.is_test_cases_page_visible(), "Test Cases page is not visible"




