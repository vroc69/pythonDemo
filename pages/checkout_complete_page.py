from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class CheckoutCompletePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

        # Page title (subheader)
        self.subheader = (By.CLASS_NAME, "subheader")

        # Checkout complete container
        self.complete_container = (By.CLASS_NAME, "checkout_complete_container")

        # Elements inside the container
        self.thank_you_message = (By.TAG_NAME, "h2")
        self.complete_text = (By.CLASS_NAME, "complete-text")
        self.complete_img = (By.CLASS_NAME, "pony_express")  # image with class instead of id

    def get_subheader_text(self):
        return self.driver.find_element(*self.subheader).text

    def get_thank_you_message(self):
        return self.driver.find_element(*self.thank_you_message).text

    def get_complete_text(self):
        return self.driver.find_element(*self.complete_text).text

    def is_confirmation_image_displayed(self):
        return self.driver.find_element(*self.complete_img).is_displayed()