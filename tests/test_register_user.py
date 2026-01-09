import time

from pages.account_created_page import AccountCreatedPage
from pages.account_info_page import AccountInfoPage
from pages.home_page import HomePage
from pages.signup_page import SignupPage


def test_register_user(driver):
    """
    E2E test covering user registration, account creation, login validation,
    and account deletion.
    """
    home = HomePage(driver)
    signup = SignupPage(driver)
    account_info = AccountInfoPage(driver)
    account_created = AccountCreatedPage(driver)

    # 1. Open home page
    home.open_url("https://automationexercise.com")
    assert home.is_home_page_visible()

    # 2. Navigate to Signup/Login page
    home.click_signup_login()
    assert signup.is_new_user_signup_visible()

    # 3. Signup
    email = f"testuser_{int(time.time())}@gmail.com"
    signup.enter_name("TestUser")
    signup.enter_email(email)
    signup.click_signup_button()

    # 4. Account info
    assert account_info.is_account_info_visible()
    account_info.fill_account_info()
    account_info.fill_address_info()
    account_info.select_checkboxes()
    account_info.click_create_account()

    # 5. Account created
    assert account_created.is_account_created_visible()
    account_created.click_continue()

    # 6. Delete
    home.click_delete_account()
    assert account_created.is_account_deleted_visible()
    account_created.click_continue()
    assert home.is_home_page_visible()
