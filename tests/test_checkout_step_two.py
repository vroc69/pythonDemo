import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_step_one_page import CheckoutStepOnePage
from pages.checkout_step_two_page import CheckoutStepTwoPage
from utils.data_loader import load_json

# Load user data
user_data = load_json("users.json")
users = user_data["users"]
user_info = user_data["userInfo"]

@pytest.mark.regression
def test_checkout_step_two_and_finish(driver):
    # Step 1: Login
    login_page = LoginPage(driver)
    credentials = users["successful"]
    login_page.login(credentials["username"], credentials["password"])

    # Step 2: Add products
    inventory_page = InventoryPage(driver)
    num_products = 2
    inventory_page.add_first_n_products(num_products)

    # Step 3: Go to cart
    inventory_page.go_to_cart()
    cart_page = CartPage(driver)
    cart_page.click_checkout()

    # Step 4: Fill step-one form
    checkout_step_one = CheckoutStepOnePage(driver)
    checkout_step_one.complete_step_one(
        user_info["firstName"],
        user_info["lastName"],
        user_info["postalCode"]
    )

    # Step 5: Wait until step two page loads
    WebDriverWait(driver, 10).until(
        EC.url_contains("/checkout-step-two.html")
    )

    # Step 6: Validate and print information
    checkout_step_two = CheckoutStepTwoPage(driver)

    assert checkout_step_two.get_page_title() == "Checkout: Overview", "Incorrect page title"
    assert checkout_step_two.get_cart_items_count() == num_products, "Cart item count mismatch"

    print("Payment Info:", checkout_step_two.get_payment_info())
    print("Shipping Info:", checkout_step_two.get_shipping_info())

    totals = checkout_step_two.get_order_totals()
    print("*", totals["item_total"])
    print("*", totals["tax"])
    print("*", totals["total"])

    # Step 7: Complete the purchase
    checkout_step_two.click_finish()

    # Step 8: Confirm we reached the final confirmation page
    WebDriverWait(driver, 10).until(
        EC.url_contains("/checkout-complete.html")
    )

    assert "/checkout-complete.html" in driver.current_url, "Did not reach confirmation page"