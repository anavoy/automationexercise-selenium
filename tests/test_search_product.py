from pages.home_page import HomePage
from pages.product_page import ProductPage


def test_search_product(driver):

    home = HomePage(driver)
    product_page = ProductPage(driver)


    # 1. Open home page
    home.open_url("https://automationexercise.com")
    assert home.is_home_page_visible(), "Home page is not visible"

    # Click 'Products' button
    product_page.click_products()

    # 2. Verify user is navigated to ALL PRODUCTS page successfully
    assert product_page.is_products_page_url(), "Not navigated to products page URL"

    # 3. Enter product name in search input and click search button
    product_page.enter_search_product()
    product_page.click_search_button()


    # 4. Verify 'SEARCHED PRODUCTS' is visible
    assert product_page.is_searched_products_title_visible(), "'SEARCHED PRODUCTS' title is not visible"


    # 5. Verify all the products related to search are visible
    assert product_page.are_products_visible(), "No products related to search are visible"

    # 6. Verify all the products related to search have product name containing search keyword
    assert product_page.are_products_matching_search("Jeans"), "Not all products match the search keyword 'jeans'"







