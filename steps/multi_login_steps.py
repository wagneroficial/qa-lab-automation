# Versão corrigida do teste multi-login

import pytest
from playwright.sync_api import Browser, BrowserContext, Page
from pages.login_page import LoginPage
from pytest_bdd import given, when, then, scenarios

# Import dos cenários
scenarios('../features/multi_login.feature')

# Opção 1: Usar o browser padrão do pytest-playwright
@pytest.fixture
def admin_context(browser: Browser):
    """Contexto separado para admin"""
    context = browser.new_context()
    yield context
    context.close()

@pytest.fixture 
def customer_context(browser: Browser):
    """Contexto separado para customer"""
    context = browser.new_context()
    yield context
    context.close()

@pytest.fixture
def admin_page(admin_context: BrowserContext):
    """Página para admin"""
    page = admin_context.new_page()
    yield page
    page.close()

@pytest.fixture
def customer_page(customer_context: BrowserContext):
    """Página para customer"""
    page = customer_context.new_page()
    yield page
    page.close()

@pytest.fixture
def admin_login_page(admin_page: Page):
    """LoginPage para admin"""
    return LoginPage(admin_page)

@pytest.fixture
def customer_login_page(customer_page: Page):
    """LoginPage para customer"""
    return LoginPage(customer_page)

# Steps usando as fixtures corretas
@given("Admin is on the login page")
def admin_go_to_login(admin_login_page):
    admin_login_page.navigate_to_login()

@given("Customer is on the login page") 
def customer_go_to_login(customer_login_page):
    customer_login_page.navigate_to_login()

@when("Admin logs in")
def admin_login_step(admin_login_page):
    admin_login_page.login_as_admin()

@when("Customer logs in")
def customer_login_step(customer_login_page):
    customer_login_page.login_as_user()

@then("Admin dashboard is visible")
def admin_dashboard(admin_login_page):
    admin_login_page.verify_successful_login() 

@then("Customer dashboard is visible") 
def customer_dashboard(customer_login_page):
    customer_login_page.verify_successful_login()
