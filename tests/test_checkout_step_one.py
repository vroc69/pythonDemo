import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_step_one_page import CheckoutStepOnePage
from utils.data_loader import load_json

# Load users and user info from JSON
user_data = load_json("users.json")
users = user_data["users"]
user_info = user_data["userInfo"]

@pytest.mark.regression
def test_complete_checkout_step_one(driver):
    # Step 1: Login with valid user
    login_page = LoginPage(driver)
    credentials = users["successful"]
    login_page.login(credentials["username"], credentials["password"])

    # Step 2: Add N products to cart
    inventory_page = InventoryPage(driver)
    num_products = 2
    inventory_page.add_first_n_products(num_products)

    # Step 3: Navigate to the cart page
    inventory_page.go_to_cart()
    cart_page = CartPage(driver)

    # Step 4: Start checkout
    cart_page.click_checkout()

    # Step 5: Fill in the checkout form using userInfo from JSON
    checkout_page = CheckoutStepOnePage(driver)
    checkout_page.complete_step_one(
        user_info["firstName"],
        user_info["lastName"],
        user_info["postalCode"]
    )

    # Step 6: Wait for the transition to checkout-step-two
    WebDriverWait(driver, 10).until(
        EC.url_contains("/checkout-step-two.html")
    )

    # Step 7: Final assertion - confirm we're on the next page
    assert "/checkout-step-two.html" in driver.current_url, \
        "Did not reach checkout step two page."
