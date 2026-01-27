from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductPage(BasePage):
    """
    Page Object representing the Product page and its main user interactions.
    """
    

    PRODUCTS_BUTTON = (By.CSS_SELECTOR, "a[href='/products']")
    PRODUCTS_TITLE = (By.CSS_SELECTOR, "h2.title.text-center")
    PRODUCT_ITEMS = (By.CSS_SELECTOR, "div.col-sm-4")
    VIEW_PRODUCT_BUTTON = (By.CSS_SELECTOR, "a[href='/product_details/1']")
    PRODUCT_NAME = (By.XPATH, "//div[@class='product-information']//h2")
    PRODUCT_CATEGORY = (By.XPATH, "//div[@class='product-information']//p[contains(text(),'Category')]")
    PRODUCT_PRICE = (By.XPATH, "//div[@class='product-information']//span/span")
    PRODUCT_AVAILABILITY = (By.XPATH, "//div[@class='product-information']//p/b[contains(text(),'Availability')]")
    PRODUCT_CONDITION = (By.XPATH, "//div[@class='product-information']//p/b[contains(text(),'Condition')]")
    PRODUCT_BRAND = (By.XPATH, "//div[@class='product-information']//p/b[contains(text(),'Brand')]")



    def click_products(self):
        self.driver.find_element(*self.PRODUCTS_BUTTON).click()

    def is_products_title_visible(self):
        return self.driver.find_element(*self.PRODUCTS_TITLE).is_displayed()
    

    def is_products_page_url(self):
        WebDriverWait(self.driver, 10).until(
            lambda driver: "/products" in driver.current_url
        )
        return True

    def are_products_visible(self):
        products = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(self.PRODUCT_ITEMS)
        )
        return len(products) > 0
    
    def click_view_product(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.VIEW_PRODUCT_BUTTON)
        )

        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

        try:
            element.click()
        except Exception:
            self.driver.execute_script("arguments[0].click();", element)



    def is_product_details_page_url(self):
        WebDriverWait(self.driver, 10).until(
            lambda driver: "/product_details/" in driver.current_url
        )
        return True 

    def is_product_name_visible(self):
        return self.driver.find_element(*self.PRODUCT_NAME).is_displayed()

    def is_product_category_visible(self):
        return self.driver.find_element(*self.PRODUCT_CATEGORY).is_displayed()
    
    def is_product_price_visible(self):
        return self.driver.find_element(*self.PRODUCT_PRICE).is_displayed()
    

    def is_product_availability_visible(self):
        return self.driver.find_element(*self.PRODUCT_AVAILABILITY).is_displayed()
    

    def is_product_condition_visible(self):
        return self.driver.find_element(*self.PRODUCT_CONDITION).is_displayed()
    

    def is_product_brand_visible(self):
        return self.driver.find_element(*self.PRODUCT_BRAND).is_displayed()
    


