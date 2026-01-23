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


    # 4. Verify that all test case titles are visible
    expected_test_cases = [
    "Test Case 1: Register User",
    "Test Case 2: Login User with correct email and password",
    "Test Case 3: Login User with incorrect email and password",
    "Test Case 4: Logout User",
    "Test Case 5: Register User with existing email",
]

    assert home.are_test_case_titles_visible(expected_test_cases), \
        "Not all expected test case titles are visible"

