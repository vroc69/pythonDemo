import pytest
import os
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_step_one_page import CheckoutStepOnePage
from pages.checkout_step_two_page import CheckoutStepTwoPage
from pages.checkout_complete_page import CheckoutCompletePage
from utils.data_loader import load_json

# Load user data
user_data = load_json("users.json")
users = user_data["users"]
user_info = user_data["userInfo"]

@pytest.mark.e2e
@pytest.mark.regression
def test_checkout_complete(driver):
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

    # Step 4: Fill out checkout form
    step_one = CheckoutStepOnePage(driver)
    step_one.complete_step_one(
        user_info["firstName"],
        user_info["lastName"],
        user_info["postalCode"]
    )

    # Step 5: Confirm arrival at step two and finish
    WebDriverWait(driver, 10).until(EC.url_contains("/checkout-step-two.html"))
    step_two = CheckoutStepTwoPage(driver)
    step_two.click_finish()

    # Step 6: Validate final confirmation page
    WebDriverWait(driver, 10).until(EC.url_contains("/checkout-complete.html"))
    complete = CheckoutCompletePage(driver)

    assert complete.get_subheader_text() == "Finish", "Subheader mismatch"
    assert complete.get_thank_you_message() == "THANK YOU FOR YOUR ORDER", "Thank you message mismatch"
    assert "Your order has been dispatched" in complete.get_complete_text(), "Missing confirmation text"
    assert complete.is_confirmation_image_displayed(), "Confirmation image not displayed"

    # Step 7: Take screenshot
    screenshot_dir = os.path.join(os.getcwd(), "reports", "screenshots")
    os.makedirs(screenshot_dir, exist_ok=True)
    driver.save_screenshot(os.path.join(screenshot_dir, "checkout_complete.png"))

    # Step 8: Wait 3 seconds for visual confirmation
    time.sleep(3)

    # Step 9: Logout
    inventory_page.logout()