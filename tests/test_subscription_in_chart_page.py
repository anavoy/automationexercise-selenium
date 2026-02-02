from pages.home_page import HomePage


def test_subscription_in_chart_page(driver):

    home = HomePage(driver)

    
   
    # 1. Open home page
    home.open_url("https://automationexercise.com")
    assert home.is_home_page_visible(), "Home page is not visible"

    # 2. Click 'Cart' button
    home.click_cart_button()
    assert home.is_cart_page_visible(), "Cart page is not visible"


    # 3. Scroll to footer
    home.scroll_to_footer()
    assert home.is_subscription_section_visible(), "Subscription section is not visible"

    # 4. Verify success message 'You have been successfully subscribed!' is visible
    assert home.is_subscription_success_message_visible(), "Subscription success message is not visible"
  
