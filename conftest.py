import pytest
import os
import base64
from pytest_html import extras
from utils.driver_factory import DriverFactory
from utils.data_loader import load_json

# Fixture to initialize and quit the WebDriver per test
@pytest.fixture(scope="function")
def driver():
    factory = DriverFactory()
    driver_instance = factory.get_driver()

    # Load base URL from config.json and open it
    config = load_json("config.json")
    base_url = config["base_url"]
    driver_instance.get(base_url)

    yield driver_instance

    # Quit browser after test
    factory.quit_driver()

# Hook to embed a screenshot in the HTML report after each test execution
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Execute the test and retrieve the result
    outcome = yield
    rep = outcome.get_result()

    # Only capture screenshot for the actual test step (not setup/teardown)
    if rep.when == "call":
        # Get the WebDriver instance from the test
        driver = item.funcargs.get("driver", None)
        if driver:
            # Ensure the screenshots folder exists
            screenshot_dir = os.path.join("reports", "screenshots")
            os.makedirs(screenshot_dir, exist_ok=True)

            # Define screenshot file path
            screenshot_path = os.path.join(screenshot_dir, f"{item.name}.png")

            # Capture screenshot
            driver.save_screenshot(screenshot_path)

            # Convert image to base64 and embed in report
            with open(screenshot_path, "rb") as f:
                encoded = base64.b64encode(f.read()).decode()
                html = f'<div><img src="data:image/png;base64,{encoded}" width="400"></div>'

                # Attach image HTML block to the test report
                extra = getattr(rep, "extra", [])
                extra.append(extras.html(html))
                rep.extra = extra