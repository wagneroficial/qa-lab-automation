import time
from .base_page import BasePage
from playwright.sync_api import expect
from config.settings import settings
import logging


class ApiCreationPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.screenshot_dir = "screenshots"
        self.logger = logging.getLogger(__name__)

    def take_screenshot(self, name: str = "screenshot"):
        filename = f"{self.screenshot_dir}/{name}.png"
        self.page.screenshot(path=filename, full_page=True)
        self.logger.info(f"Screenshot saved: {filename}")
        return filename

    def navigate_to_apis_section(self):
        self.logger.info("Navigating to APIs section")
        self.page.get_by_role("menuitem", name="APIs").click()
        self.take_screenshot("07_apis_section")

    def create_api_from_url(self):
        self.logger.info("Creating API from URL")
        
        # Click New button
        self.page.get_by_role("button", name="New").click()
        self.take_screenshot("08_new_api_clicked")
        
        # Select Create from URL
        self.page.get_by_text("Create from URL").click()
        self.take_screenshot("09_create_from_url_selected")
        
        # Enter API URL
        api_url = "https://api.apis.guru/v2/specs/abstractapi.com/geolocation/1.0.0/openapi.json"
        self.page.get_by_placeholder("Ex: https://api-.example.com/").fill(api_url)
        self.take_screenshot("10_api_url_entered")
        
        # Import API
        self.page.get_by_role("button", name="Import").click()
        self.take_screenshot("11_import_clicked")
        
        # Aguarda o processamento inicial do import
        self.page.wait_for_timeout(3000)
        self.take_screenshot("12_import_completed")
        
        # Create API
        self.page.get_by_role("button", name="Create").click()
        self.take_screenshot("13_create_clicked")

    def verify_api_created_successfully(self):
        self.logger.info("Verifying API created successfully")

        # Espera até 2 minutos pela mensagem de sucesso
        success_message = self.page.get_by_text("Success", exact=True)
        expect(success_message).to_be_visible(timeout=120000)
        self.take_screenshot("15_success_verified")

        # Espera até 2 minutos pela URL de detalhes
        self.page.wait_for_url("**/apis/details/**", timeout=120000)
        self.take_screenshot("14_api_details_page")

        self.logger.info("API created successfully")
        self.logger.info("Verifying API created successfully")
        time.sleep(1)

        # 🔹 Edit API
        self.page.get_by_role("button", name="edit").click()
        self.page.wait_for_url("**/apis/edit/**", timeout=120000)
        self.take_screenshot("16_edit_page")
        time.sleep(1)
        # 🔹 Aba Docs and Terms
        self.page.get_by_text("Docs and Terms").click()
        expect(self.page.get_by_text("Main Documentation:")).to_be_visible()
        self.take_screenshot("17_docs_terms_tab")

        # 🔹 Aba HTTP Methods
        self.page.get_by_text("HTTP Methods").click()
        expect(self.page.get_by_role("button", name="Add New Route")).to_be_visible()
        self.take_screenshot("18_http_methods_tab")

        # 🔹 Aba Health Check
        self.page.get_by_text("Health Check", exact=True).click()
        self.page.get_by_role("button", name="Run Health Check").click()
        expect(self.page.get_by_role("columnheader", name="Backend Endpoint")).to_be_visible()
        self.take_screenshot("19_health_check_tab")

        # 🔹 Aba OWASP Security Scan
        self.page.get_by_text("OWASP").click()
        self.page.get_by_role("button", name="Scan for Vulnerabilities with").click()
        expect(self.page.get_by_role("heading", name="Security Issues")).to_be_visible(timeout=10000)
        self.take_screenshot("20_owasp_scan")

        self.logger.info("API fully verified successfully ✅")


