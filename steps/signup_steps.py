from pytest_bdd import given, when, then
import pytest
from pages.signup_page import SignupPage

# fixture para o Page Object
@pytest.fixture
def signup_page(page):
    return SignupPage(page)

@given("I am on the signup page")
def open_signup_page(signup_page):
    pass  # só garante que o fixture é criado

@when("I complete the signup form")
def fill_signup_form(signup_page):
    signup_page.register_user(
        name="Wagner Viana Sampaio",
        company="konneqt",
        phone="+55 (93) 9393838933",
        email="wagner333@gmail.com"
    )

@then('I should see the message "User created with success"')
def verify_success_message(signup_page):
    signup_page.check_success_message("User created with success")
