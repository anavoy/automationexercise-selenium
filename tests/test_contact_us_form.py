import os
from pages.home_page import HomePage
from pages.account_info_page import AccountInfoPage



def test_contact_us_form(driver):
    """
    Docstring for test_contact_us_form
    
    :param driver: Description
    :type driver: WebDriver
    """

    home = HomePage(driver)
    account_info = AccountInfoPage(driver)


    # 1. Open home page
    home.open_url("https://automationexercise.com")
    assert home.is_home_page_visible(), "Home page is not visible"

    # 2. Click 'Contact Us' button
    home.click_contact_us()
    
    # 3. Verify 'GET IN TOUCH' title is visible and fill contact us form
    assert account_info.is_contact_us_title_visible(), "'GET IN TOUCH' title is not visible"
    account_info.fill_contact_us_form()
    file_path = os.path.abspath("files/test_file.txt")
    account_info.upload_file(file_path)
    account_info.submit_contact_us_form()


    # 4. Click "OK" button on alert
    account_info.accept_alert()


    # 5. Verify success message 'Success! Your details have been submitted successfully.' is visible
    assert home.is_success_message_visible(), "Success message is not visible"


    # 6. Click 'Home' button and verify that landed to home page successfully
    home.click_contact_us_home()
    assert home.is_home_page_visible(), "Did not land on home page successfully"


  

    
    
    
   



