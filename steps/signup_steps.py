from pytest_bdd import given, when, then, parsers
from pages.signup_page import SignupPage

@given("I go to the signup page")
def go_to_signup_page(page):
    signup_page = SignupPage(page)
    signup_page.navigate_to_signup()

@when(parsers.parse("I register with {data_type} data"))
def register_with_data_type(page, data_type):
    signup_page = SignupPage(page)
    
    registration_methods = {
        "valid": signup_page.register_valid_user,
        "invalid_company": signup_page.register_with_invalid_company,
        "existing_user": signup_page.register_existing_user
    }
    
    method = registration_methods.get(data_type)
    method()


@then(parsers.parse("I should see '{expected_message}'"))
def verify_message(page, expected_message):
    signup_page = SignupPage(page)
    signup_page.check_message(expected_message)