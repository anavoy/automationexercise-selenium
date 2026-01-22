from pages.home_page import HomePage
from pages.signup_page import SignupPage


def test_register_already_exist(driver):
    """
    Docstring for test_register_already_exist
    
    :param driver: Description
    :type driver: WebDriver
    """


    home = HomePage(driver)
    signup = SignupPage(driver)


    # 1. Open home page
    home.open_url("https://automationexercise.com")
    assert home.is_home_page_visible(), "Home page is not visible"

    # 2. Click 'Signup / Login' button
    home.click_signup_login()
    assert signup.is_new_user_signup_visible()

    # 3. Register with an existing email
    signup.enter_name("ExistingUser")
    signup.enter_email("testttt@gmail.com")
    signup.click_signup_button()

    # 4. Verify error 'Email Address already exist!' is visible
    assert signup.is_email_exist_visible(), "'Email Address already exist!' error is not visible"