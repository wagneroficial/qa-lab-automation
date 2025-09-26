from pytest_bdd import given, when, then
from pages.registration_page import RegistrationPage
from utils.test_data import TestDataGenerator

@given('I am on the home page')
def navigate_to_home_page(page):
    RegistrationPage(page).navigate_to_home()

@when('I complete registration with valid data')
def complete_registration(page):
    user_data = TestDataGenerator.generate_valid_user()
    
    reg_page = RegistrationPage(page)
    reg_page.click_register_button()
    reg_page.fill_registration_form(user_data['name'], user_data['email'], user_data['password'])
    reg_page.submit_form()

@then('I should be on dashboard')
def verify_dashboard(page):
    reg_page = RegistrationPage(page)
    assert reg_page.has_welcome_message(), f"Mensagem de boas-vindas não encontrada após registro. URL: {page.url}"