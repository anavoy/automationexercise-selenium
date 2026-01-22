from pages.home_page import HomePage
from pages.signup_page import SignupPage

def test_logout_user(driver):
    """
    Docstring for test_logout_user
    """

    home = HomePage(driver)
    signup = SignupPage(driver)

    # 1. Open home page
    home.open_url("https://automationexercise.com")
    assert home.is_home_page_visible(), "Home page is not visible"


    # 2. Click 'Signup / Login' button
    home.click_signup_login()
    assert signup.is_login_title_visible(), "'Login to your account' title is not visible"

    # 3. Login
     # temporarily
    signup.login(
        email="testttt@gmail.com",
        password="123"
    )
    
    # 4. Verify 'Logged in as username' is visible
    assert home.is_logged_in_visible(), "'Logged in as' text is not visible"

    # 5. Click 'Logout' button
    home.click_logout()
    assert signup.is_login_title_visible(), "'Login to your account' title is not visible after logout"
