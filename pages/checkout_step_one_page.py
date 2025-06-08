from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class CheckoutStepOnePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.input_first_name = (By.ID, "first-name")
        self.input_last_name = (By.ID, "last-name")
        self.input_postal_code = (By.ID, "postal-code")
        self.continue_button = (By.XPATH, "//div[@class='checkout_buttons']/input[@type='submit']")

    def fill_checkout_form(self, first_name, last_name, postal_code):
        self.driver.find_element(*self.input_first_name).clear()
        self.driver.find_element(*self.input_first_name).send_keys(first_name)

        self.driver.find_element(*self.input_last_name).clear()
        self.driver.find_element(*self.input_last_name).send_keys(last_name)

        self.driver.find_element(*self.input_postal_code).clear()
        self.driver.find_element(*self.input_postal_code).send_keys(postal_code)

    def click_continue(self):
        self.driver.find_element(*self.continue_button).click()

    def complete_step_one(self, first_name, last_name, postal_code):
        self.fill_checkout_form(first_name, last_name, postal_code)
        self.click_continue()
