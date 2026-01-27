from pages.home_page import HomePage
from pages.product_page import ProductPage


def test_all_products_page(driver):

    home = HomePage(driver)
    product_page = ProductPage(driver)


    # 1. Open home page
    home.open_url("https://automationexercise.com")
    assert home.is_home_page_visible(), "Home page is not visible"

    # 2. Click 'Products' button
    product_page.click_products()

    # 3. Verify user is navigated to ALL PRODUCTS page successfully
    assert product_page.is_products_page_url(), "Not navigated to products page URL"
    assert product_page.is_products_title_visible(), "Products title is not visible"


    # 4. Verify that all products are visible
    assert product_page.are_products_visible(), "Products are not visible"

    
    # 5. Click on 'View Product' of first product
    product_page.click_view_product()

    # 6. Verify that user is navigated to product detail page
    assert product_page.is_product_details_page_url(), "Not navigated to product details page URL"


    # 7. Verify that the product detail page contains product information: name, category, price, availability, condition, brand
    assert product_page.is_product_name_visible(), "Product name is not visible"
    assert product_page.is_product_category_visible(), "Product category is not visible"
    assert product_page.is_product_price_visible(), "Product price is not visible"
    assert product_page.is_product_availability_visible(), "Product availability is not visible"
    assert product_page.is_product_condition_visible(), "Product condition is not visible"
    assert product_page.is_product_brand_visible(), "Product brand is not visible"
    

    
    


