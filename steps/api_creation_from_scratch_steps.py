from pytest_bdd import given, when, then, scenarios
from pages.api_creation_from_scratch_page import ApiCreationFromScratchPage

@given("I am on the APIs section")
def navigate_to_apis_section(page):
    api_page = ApiCreationFromScratchPage(page)
    api_page.navigate_to_apis_section()

@when("I create a new Pokemon API from scratch")
def create_pokemon_api_from_scratch(page):
    api_page = ApiCreationFromScratchPage(page)
    api_page.create_pokemon_api_from_scratch()

@then("I should see API created successfully with full verification")
def verify_api_created_successfully(page):
    api_page = ApiCreationFromScratchPage(page)
    api_page.verify_api_created_successfullys()
