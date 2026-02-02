import time
from pages.home_page import HomePage

def test_subscription(driver):

    home = HomePage(driver)

    # 1. Open home page
    home.open_url("https://automationexercise.com")
    assert home.is_home_page_visible(), "Home page is not visible"

    # 2. Scroll to footer
    home.scroll_to_footer()
    assert home.is_subscription_section_visible(), "Subscription section is not visible"

    # 3. Verify text 'SUBSCRIPTION' is visible
    assert home.is_subscription_text_visible(), "'SUBSCRIPTION' text is not visible"


    # 4. Enter email address in input and click arrow button
    home.enter_email_subscription()
    time.sleep(1)
    home.click_subscription_button()
    time.sleep(1)

    # 5. Verify success message 'You have been successfully subscribed!' is visible
    assert home.is_subscription_success_message_visible(), "Subscription success message is not visible"
    time.sleep(2)









    