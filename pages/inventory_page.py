from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.page_title = (By.CLASS_NAME, "product_label")
        self.inventory_container = (By.ID, "inventory_container")
        self.menu_button = (By.XPATH, "//div[@class='bm-burger-button']/button")
        self.menu_option_logout = (By.XPATH, "//div[@class='bm-menu']/nav/a[@id='logout_sidebar_link']")
        self.cart_link = (By.XPATH, "//div[@id='shopping_cart_container']/a/*[@data-icon='shopping-cart']")
        self.txt_cart_items_count = (By.XPATH,"//div[@id='shopping_cart_container']/a/span[contains(@class,'layers-counter')]")
        self.product_add_buttons = (By.XPATH, "//button[contains(@class,'btn_inventory')]")

    def get_page_title(self):
        return self.driver.find_element(*self.page_title).text

    def is_inventory_displayed(self):
        return self.driver.find_element(*self.inventory_container).is_displayed()
    
    def get_cart_items_count(self):
        try:
            return int(self.driver.find_element(*self.txt_cart_items_count).text)
        except ValueError:
            return 0

    def add_first_n_products(self, count):
        buttons = self.driver.find_elements(*self.product_add_buttons)
        for i in range(min(count, len(buttons))):
            buttons[i].click()

    def logout(self):
        self.driver.find_element(*self.menu_button).click()
        # Explicit wait to ensure the menu option is clickable
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.menu_option_logout)
        )
        self.driver.find_element(*self.menu_option_logout).click()

    def go_to_cart(self):
        self.driver.find_element(*self.cart_link).click()

        # Wait until the URL contains '/cart.html'
        WebDriverWait(self.driver, 10).until(
            EC.url_contains("/cart.html")
        )    
