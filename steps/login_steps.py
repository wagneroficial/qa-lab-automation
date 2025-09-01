# steps/login_steps.py
from pytest_bdd import given, when, then
from pages.login_page import LoginPage

@given("I go to the login page")
def go_to_login_page(page):
    login_page = LoginPage(page)
    login_page.navigate_to_login()


""" Successful_admin_login """
@when("I log in with valid admin credentials")
def login_with_valid_credentials(page):
    login_page = LoginPage(page)
    login_page.login_as_admin()

""" Successful_customer_login """
@when("I log in with valid customer credentials")
def login_with_valid_credentials(page):
    login_page = LoginPage(page)
    login_page.login_as_user()


@then("I should be logged in successfully")
def verify_login_success(page):
    login_page = LoginPage(page)
    login_page.wait_for_dashboard()

