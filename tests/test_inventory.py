import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.data_loader import load_json
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Load user credentials and error messages from JSON files
users = load_json("users.json")["users"]

@pytest.mark.regression
def test_user_logout(driver):
    login_page = LoginPage(driver)
    credentials = users["successful"]

    # Perform login
    login_page.login(credentials["username"], credentials["password"])

    # Verify successful login by checking inventory page
    inventory_page = InventoryPage(driver)
    assert inventory_page.is_inventory_displayed(), "Inventory container not displayed"
    assert inventory_page.get_page_title() == "Products", "Page title is incorrect"

    # Perform logout
    inventory_page.logout()

    # Verify that the user is redirected to the login page
    # Wait for the URL to change to the login page
    WebDriverWait(driver, 10).until(
        EC.url_contains("/v1/index")
    )

    assert "/v1/index" in driver.current_url, "User is not redirected to the login page after logout"

@pytest.mark.e2e
@pytest.mark.smoke
@pytest.mark.regression
def test_add_multiple_products_to_cart(driver):
    login_page = LoginPage(driver)
    credentials = users["successful"]

    # Login
    login_page.login(credentials["username"], credentials["password"])

    inventory_page = InventoryPage(driver)

    # Adding multiple products to the cart
    num_products = 3
    inventory_page.add_first_n_products(num_products)

    # Verify that the products are added to the cart
    cart_count = inventory_page.get_cart_items_count()
    assert cart_count == num_products, f"Expected cart count: {num_products}, but got: {cart_count}"
    screenshot_path = f"reports/screenshots/cart_{num_products}_items.png"
    driver.save_screenshot(screenshot_path)