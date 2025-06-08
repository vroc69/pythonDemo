import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.data_loader import load_json

# Load user credentials and error messages from JSON files
users = load_json("users.json")["users"]
messages = load_json("messages.json")["errors"]

@pytest.mark.regression
def test_locked_user_login(driver):
    login_page = LoginPage(driver)
    credentials = users["locked"]
    
    login_page.login(credentials["username"], credentials["password"])
    
    error_text = driver.find_element(*login_page.txt_error_message).text
    assert error_text == messages["locked"], f"Expected: {messages['locked']}, Got: {error_text}"

@pytest.mark.regression 
@pytest.mark.smoke
def test_unknown_user_login(driver):
    login_page = LoginPage(driver)
    credentials = users["unknown"]

    login_page.login(credentials["username"], credentials["password"])
    
    error_text = driver.find_element(*login_page.txt_error_message).text
    assert error_text == messages["invalid"], f"Expected: {messages['invalid']}, Got: {error_text}"

@pytest.mark.e2e
@pytest.mark.regression
def test_successful_login(driver):
    login_page = LoginPage(driver)
    credentials = users["successful"]

    login_page.login(credentials["username"], credentials["password"])

    inventory_page = InventoryPage(driver)

    assert inventory_page.is_inventory_displayed(), "Inventory container not displayed"
    assert inventory_page.get_page_title() == "Products", "Page title is incorrect"