# 🧪 Python Selenium Automation Framework – SauceDemo

This framework automates functional testing for the [SauceDemo V1](https://www.saucedemo.com/v1/) web application using **Python**, **Selenium WebDriver**, **Pytest**, and the **Page Object Model (POM)** pattern.

---

## 📁 Project Structure

```
pythonDemo/
│
├── pages/                  # Page Objects
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   ├── checkout_step_one_page.py
│   ├── checkout_step_two_page.py
│   └── checkout_complete_page.py
│
├── tests/                  # Test cases
│   ├── test_login.py
│   ├── test_cart.py
│   ├── test_checkout_step_one.py
│   ├── test_checkout_step_two.py
│   └── test_checkout_complete.py
│
├── utils/
│   ├── driver_factory.py   # WebDriver manager
│   └── data_loader.py      # JSON data loader
│
├── data/
│   └── users.json          # User credentials and form data
│
├── reports/                # HTML reports and screenshots
│   └── screenshots/
│
├── conftest.py             # Pytest fixtures and hooks
└── pytest.ini              # Pytest configuration
```

---

## 🔧 Requirements

- Python 3.10+
- Google Chrome (v137+)
- Updated ChromeDriver
- Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🚀 Running Tests

### Run all tests and generate an HTML report:

```bash
pytest --html=reports/full_report.html --self-contained-html
```

### Run only E2E tests:

```bash
pytest -m e2e --html=reports/e2e_report.html --self-contained-html
```

> 📝 E2E tests use the `@pytest.mark.e2e` marker

### Run a specific test file:

```bash
pytest tests/test_checkout_complete.py --html=reports/checkout.html --self-contained-html
```

---

## 📦 Data from JSON

- User credentials (`users`)
- Checkout form information (`userInfo`)
- Error and UI messages for assertions

File: `data/users.json`

---

## 🖼 Screenshots

Screenshots are saved automatically under:
```
/reports/screenshots/
```

---

## ✅ Covered Features

- Login (valid, locked, unknown users)
- Add products to cart
- Validate cart content
- Full checkout flow (steps 1, 2, confirmation)
- Logout
- Visual screenshots and HTML reports

---

## 📌 Available Pytest Markers

```ini
[pytest]
markers =
    regression: marks tests as part of the regression suite
    e2e: marks tests as part of the end-to-end flow
    smoke: marks tests as part of the smoke suite
```

---

## 🧼 To-Do / Future Enhancements

- Validate product prices and totals
- Remove items from cart
- Multi-browser support
- CI/CD integration (GitHub Actions or Jenkins)

---
