from pages.home_page import HomePage
from pages.signup_page import SignupPage
from pages.account_created_page import AccountCreatedPage


def test_login_user(driver):
    """
    Verify that an existing user can log in with valid email and password
    and delete the account successfully.
    """

    home = HomePage(driver)
    signup = SignupPage(driver)
    account_created = AccountCreatedPage(driver)

    # 1. Open home page
    home.open_url("https://automationexercise.com")
    assert home.is_home_page_visible(), "Home page is not visible"

    # 2. Navigate to Signup/Login page
    home.click_signup_login()
    assert signup.is_login_title_visible(), "'Login to your account' title is not visible"
    
    # temporarily
     # 3. Login
    signup.login(
        email="testJovana@gmail.com",
        password="Test123"
    )

    # 4. Verify 'Login to your account' is visible
    assert home.is_logged_in_visible(), "'Logged in as' text is not visible"

    # 5. Delete account
    home.click_delete_account()
    assert account_created.is_account_deleted_visible(), "'ACCOUNT DELETED!' message is not visible"




   


