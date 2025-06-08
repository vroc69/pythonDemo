from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

class DriverFactory:
    def __init__(self):
        self.driver = None

    def get_driver(self):
        if self.driver is None:
            options = Options()
            options.add_argument("--start-maximized")
            options.add_argument("--incognito")

            # Disable password manager and save credentials
            options.add_experimental_option("prefs", {
                "credentials_enable_service": False,
                "profile.password_manager_enabled": False
            })

            # Absolute path to the ChromeDriver executable
            # Update the path to match your local setup
            chrome_driver_path = r"C:\Globant\Instaladores\driversBrowsers\chromedriver-win64\chromedriver.exe"
            service = Service(executable_path=chrome_driver_path)

            self.driver = webdriver.Chrome(service=service, options=options)
        return self.driver

    def quit_driver(self):
        if self.driver:
            self.driver.quit()
            self.driver = None
