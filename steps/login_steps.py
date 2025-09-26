from pytest_bdd import given, when, then
from pages.login_page import LoginPage

TEST_EMAIL = "joao@email.com"
TEST_PASSWORD = "123456"

@given('I am on the login page')
def navigate_to_login(page):
    LoginPage(page).navigate()

@when('I login with valid credentials')
def login_with_valid_credentials(page):
    LoginPage(page).login(TEST_EMAIL, TEST_PASSWORD)

@when('I click the logout button')
def logout(page):
    LoginPage(page).logout()

@given('I am logged in')
def user_logged_in(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login(TEST_EMAIL, TEST_PASSWORD)

@then('I should see welcome message')
def verify_welcome_message(page):
    login_page = LoginPage(page)
    assert login_page.has_welcome_message(), f"Mensagem de boas-vindas não encontrada."

@then('I should be on login page')
def verify_login_page(page):
    login_page = LoginPage(page)
    assert login_page.is_on_login_page(), f"Não está na página de login. URL"