from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class CartPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.cart_items = (By.CLASS_NAME, "cart_item")
        self.item_names = (By.CLASS_NAME, "inventory_item_name")
        self.checkout_button = (By.XPATH, "//div[@class='cart_footer']/a[contains(@class,'checkout_button')]")

    def get_cart_items_count(self):
        return len(self.driver.find_elements(*self.cart_items))

    def get_product_names(self):
        elements = self.driver.find_elements(*self.item_names)
        return [el.text for el in elements]

    def click_checkout(self):
        self.driver.find_element(*self.checkout_button).click()
