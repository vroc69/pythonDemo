from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class LoginPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.username_input = (By.XPATH, "//input[@data-test='username']")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.txt_error_message = (By.XPATH, "//h3[@data-test='error']")

    def enter_username(self, username):
        self.driver.find_element(*self.username_input).clear()
        self.driver.find_element(*self.username_input).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_input).clear()
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()