import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from utils.data_loader import load_json
import time
import os

users = load_json("users.json")["users"]

@pytest.mark.e2e
@pytest.mark.regression
def test_verify_cart_content(driver):
    login_page = LoginPage(driver)
    credentials = users["successful"]

    # Login
    login_page.login(credentials["username"], credentials["password"])
    inventory_page = InventoryPage(driver)

    # Add products
    num_products = 2
    inventory_page.add_first_n_products(num_products)

    # Go to cart
    inventory_page.go_to_cart()

    # Validate cart content
    cart_page = CartPage(driver)
    
    count = cart_page.get_cart_items_count()
    assert count == num_products, f"Expected {num_products} items, but found {count}."

    product_names = cart_page.get_product_names()
    assert len(product_names) == num_products, f"Product name count mismatch. Found: {len(product_names)}"
    time.sleep(5)

    # Take screenshot of the cart page
    screenshot_dir = os.path.join(os.getcwd(), "reports", "screenshots")
    os.makedirs(screenshot_dir, exist_ok=True)

    screenshot_path = os.path.join(screenshot_dir, "cart_page.png")
    driver.save_screenshot(screenshot_path)

    # Print the product names in the cart
    print("Products in cart:", product_names)
