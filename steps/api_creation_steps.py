from pytest_bdd import given, when, then
from pages.api_creation_page import ApiCreationPage

@given("I am on the APIs section")
def navigate_to_apis_section(page):
    api_page = ApiCreationPage(page)
    api_page.navigate_to_apis_section()

@when("I create a new API from URL")
def create_api_from_url(page):
    api_page = ApiCreationPage(page)
    api_page.create_api_from_url()

@then("I should see API created successfully")
def verify_api_created_successfully(page):
    api_page = ApiCreationPage(page)
    api_page.verify_api_created_successfully()