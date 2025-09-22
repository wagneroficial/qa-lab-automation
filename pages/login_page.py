from .base_page import BasePage
from playwright.sync_api import Page, expect
from config.settings import settings
import os
import logging
import time

class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page
        self.BASE_URL = settings.BASE_URL
        self.screenshot_dir = "screenshots"
        os.makedirs(self.screenshot_dir, exist_ok=True)
        self.logger = logging.getLogger(__name__)

    def take_screenshot(self, name: str = "screenshot"):
        filename = f"{self.screenshot_dir}/{name}.png"
        self.page.screenshot(path=filename, full_page=True)
        self.logger.info(f"Screenshot saved: {filename}")
        return filename

    def navigate_to_login(self):
        self.logger.info(f"Navigating to: {self.BASE_URL}")
        self.page.goto(self.BASE_URL)
        self.take_screenshot("01_home_page")
        self.logger.info("Clicking Sign in button")
        self.page.get_by_role("button", name="Sign in").click()
        self.take_screenshot("02_login_form")

    def login(self, email: str, password: str):
        """Método base para login"""
        self.page.get_by_placeholder("mail@example.com").fill(email)
        # CORREÇÃO: Precisa encontrar o campo de senha correto
        # self.page.get_by_label("Email:").fill(password)  # ← ERRO: estava preenchendo senha no campo email
        self.page.get_by_label("Password:").fill(password)  # ← CORRETO
        self.take_screenshot("03_credentials_filled")
        self.logger.info("Clicking Sign In button")
        self.page.get_by_role("button", name="Sign In").click()

    # Métodos de login existentes
    def login_as_admin(self):
        self.logger.info("Logging in as administrator")
        self.login(settings.ADMIN_EMAIL, settings.ADMIN_PASSWORD)

    def login_as_user(self):
        self.logger.info("Logging in as regular user")
        self.login(settings.USER_EMAIL, settings.USER_PASSWORD)

    # Novos métodos para cenários de erro
    def login_with_invalid_email(self):
        self.logger.info("Logging in with invalid email")
        self.login("email_invalido@test.com", settings.ADMIN_PASSWORD)

    def login_with_invalid_password(self):
        self.logger.info("Logging in with invalid password")
        self.login(settings.ADMIN_EMAIL, "senha_incorreta123")

    def login_with_empty_fields(self):
        self.logger.info("Attempting login with empty fields")
        self.login("", "")

    # Métodos de verificação
    def verify_successful_login(self):
        self.logger.info("Verifying successful login...")
        current_url = self.page.url
        try:
            if "/admin/dashboard" in current_url or "/customer/dashboard" in current_url:
                expect(self.page.locator("body")).to_be_visible(timeout=settings.BROWSER_TIMEOUT)
                time.sleep(2)
            self.take_screenshot(f"{current_url.split('/')[-2]}_dashboard_final")
        except Exception as e:
            self.logger.error(f"Dashboard not loaded. URL: {current_url}, Error: {e}")
            self.take_screenshot("dashboard_error")
            raise

    def verify_error_message(self, expected_message):
        if expected_message == "Please fill out this field.":
            email_field = self.page.get_by_placeholder("mail@example.com")
            email_field.evaluate("el => el.checkValidity()")
            self.take_screenshot("04_js_validation")
        else:
            error_element = self.page.get_by_text(expected_message)
            expect(error_element).to_be_visible(timeout=10000)
            self.take_screenshot(f"04_error_{expected_message.replace(' ', '_').replace('.', '')}")
