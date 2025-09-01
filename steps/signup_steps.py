from pytest_bdd import given, when, then
import pytest
from pages.signup_page import SignupPage
from utils import generate_fake_user

@pytest.fixture
def signup_page(page):
    return SignupPage(page)

@given("I am on the signup page")
def open_signup_page(signup_page):
    pass 

@when("I complete the signup form")
def fill_signup_form(signup_page):
    user = generate_fake_user()
    signup_page.register_user(
        name=user["name"],
        company=user["company"],
        phone=user["phone"],
        email=user["email"]
    )


@then('I should see the message "User created with success"')
def verify_success_message(signup_page):
    signup_page.check_success_message("User created with success")
