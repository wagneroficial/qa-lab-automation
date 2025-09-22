from pytest_bdd import given, when, then, parsers
from pages.login_page import LoginPage

@given("I go to the login page")
def go_to_login_page(page):
    login_page = LoginPage(page)
    login_page.navigate_to_login()

@when(parsers.parse("I log in with {credential_type} credentials"))
def login_with_credentials(page, credential_type):
    login_page = LoginPage(page)
    
    login_methods = {
        "valid_admin": login_page.login_as_admin,
        "valid_customer": login_page.login_as_user,
        "invalid_email": login_page.login_with_invalid_email,
        "invalid_password": login_page.login_with_invalid_password,
        "empty_fields": login_page.login_with_empty_fields
    }
    
    method = login_methods.get(credential_type)
    method()


@then(parsers.parse("I should see '{expected_message}'"))
def verify_login_result(page, expected_message):
    login_page = LoginPage(page)
    
    # Verifica se é dashboard (login bem-sucedido)
    if expected_message == "dashboard":
        login_page.verify_successful_login()
    else:
        # Para qualquer mensagem de erro específica
        login_page.verify_error_message(expected_message)