from pytest_bdd import given, when, then
from pages.api_creation_page import ApiCreationPage
import pytest

@pytest.fixture
def api_page(page):
    return ApiCreationPage(page)

@given("I am on the APIs section")
def navigate_to_apis_section(api_page):
    api_page.navigate_to_apis_section()

@when("I create a new API from URL")
def create_api_from_url(api_page):
    api_page.create_api_from_url()

@when("I configure the API with all features")
def configure_api_with_all_features(api_page):
    api_page.navigate_to_edit_api()
    api_page.configure_api_documentation()
    api_page.verify_api_http_methods()
    api_page.run_api_health_check()
    api_page.run_api_security_scan()

@when("I create an API Product with billing")
def create_api_product_with_billing(api_page):
    api_page.create_api_product()
    api_page.create_billing_package()

@then("I should see API created successfully")
def verify_api_created_successfully(api_page):
    api_page.verify_api_created_successfully()

@then("I should see the complete workflow finished")
def verify_complete_workflow_finished(api_page):
    api_page.logger.info("Complete API management workflow completed successfully!")
    api_page.take_screenshot("30_workflow_completed")