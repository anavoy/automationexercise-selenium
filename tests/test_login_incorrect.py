from pages.home_page import HomePage
from pages.signup_page import SignupPage


def test_login_incorrect(driver):
    """
    Verify that an existing user cannot log in with incorrect email and password.
    """

    home = HomePage(driver)
    signup = SignupPage(driver)


    # 1. Open home page
    home.open_url("https://automationexercise.com")
    assert home.is_home_page_visible(), "Home page is not visible"


    # 2. Navigate to Signup/Login page
    home.click_signup_login()
    assert signup.is_login_title_visible(), "'Login to your account' title is not visible"


    # 3. Attempt to login with incorrect credentials
      # temporarily
    signup.login(
        email="testJovanaaaa@gmail.com",
        password="Test1234"
    )

    # 4. Verify error message is displayed
    assert signup.is_error_message_visible(), "Error message is not visible"
