from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class CheckoutStepTwoPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

        # Title of the page
        self.page_title = (By.CLASS_NAME, "subheader")  # Expected to be 'Checkout: Overview'

        # List of cart items
        self.cart_items = (By.CLASS_NAME, "cart_item")

        # Summary information box
        self.summary_info = (By.CLASS_NAME, "summary_info")

        # Payment and shipping info (labels + values)
        self.payment_info_label = (By.XPATH, "//div[@class='summary_info']/div[contains(text(),'Payment Information')]")
        self.payment_info_value = (By.XPATH, "//div[@class='summary_info']/div[contains(text(),'Payment Information')]/following-sibling::div[1]")

        self.shipping_info_label = (By.XPATH, "//div[@class='summary_info']/div[contains(text(),'Shipping Information')]")
        self.shipping_info_value = (By.XPATH, "//div[@class='summary_info']/div[contains(text(),'Shipping Information')]/following-sibling::div[1]")

        # Order totals
        self.item_total = (By.CLASS_NAME, "summary_subtotal_label")
        self.tax = (By.CLASS_NAME, "summary_tax_label")
        self.total = (By.CLASS_NAME, "summary_total_label")

        # Finish button
        self.finish_button = (By.XPATH, "//a[@class='btn_action cart_button' and text()='FINISH']")

    def get_page_title(self):
        return self.driver.find_element(*self.page_title).text

    def get_cart_items_count(self):
        return len(self.driver.find_elements(*self.cart_items))

    def get_payment_info(self):
        return self.driver.find_element(*self.payment_info_value).text

    def get_shipping_info(self):
        return self.driver.find_element(*self.shipping_info_value).text

    def get_order_totals(self):
        return {
            "item_total": self.driver.find_element(*self.item_total).text,
            "tax": self.driver.find_element(*self.tax).text,
            "total": self.driver.find_element(*self.total).text
        }

    def click_finish(self):
        self.driver.find_element(*self.finish_button).click()