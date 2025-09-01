import pytest
from playwright.sync_api import Browser
from pages.login_page import LoginPage
from pytest_bdd import given, when, then

@pytest.fixture(scope="session")
def browser(playwright):
    return playwright.chromium.launch(headless=False)

@pytest.fixture
def admin_login(browser: Browser):
    context = browser.new_context()
    page = context.new_page()
    login_page = LoginPage(page)
    yield login_page
    context.close()

@pytest.fixture
def customer_login(browser: Browser):
    context = browser.new_context()
    page = context.new_page()
    login_page = LoginPage(page)
    yield login_page
    context.close()

@given("Admin is on the login page")
def admin_go_to_login(admin_login):
    admin_login.navigate_to_login()

@given("Customer is on the login page")
def customer_go_to_login(customer_login):
    customer_login.navigate_to_login()

@when("Admin logs in")
def admin_login_step(admin_login):
    admin_login.login_as_admin()

@when("Customer logs in")
def customer_login_step(customer_login):
    customer_login.login_as_user()

@then("Admin dashboard is visible")
def admin_dashboard(admin_login):
    admin_login.wait_for_dashboard()

@then("Customer dashboard is visible")
def customer_dashboard(customer_login):
    customer_login.wait_for_dashboard()
