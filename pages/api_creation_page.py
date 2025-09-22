import datetime
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
        
        self.page.get_by_role("button", name="New").click()
        self.take_screenshot("08_new_api_clicked")
        
        self.page.get_by_text("Create from URL").click()
        self.take_screenshot("09_create_from_url_selected")
        
        api_url = "https://api.apis.guru/v2/specs/1forge.com/0.0.1/swagger.json"
        self.page.get_by_placeholder("Ex: https://api-.example.com/").fill(api_url)
        self.take_screenshot("10_api_url_entered")
        
        self.page.get_by_role("button", name="Import").click()
        self.take_screenshot("11_import_clicked")
        
        self.page.wait_for_timeout(3000)
        self.take_screenshot("12_import_completed")
        
        self.page.get_by_role("button", name="Create").click()
        self.take_screenshot("13_create_clicked")

    def verify_api_created_successfully(self):
        self.logger.info("Verifying API created successfully")
        success_message = self.page.get_by_text("Success", exact=True)
        expect(success_message).to_be_visible(timeout=120000)
        self.take_screenshot("15_success_verified")
        self.page.wait_for_url("**/apis/details/**", timeout=120000)
        self.take_screenshot("14_api_details_page")
        self.logger.info("API created successfully")

    def navigate_to_edit_api(self):
        self.logger.info("Navigating to edit API")
        self.page.get_by_role("button", name="edit").click()
        self.page.wait_for_url("**/apis/edit/**", timeout=120000)
        self.take_screenshot("16_edit_page")
        time.sleep(2)

    def configure_api_documentation(self, is_product=False):
        """Gera documentação da API ou API Product"""
        self.logger.info("Configuring API documentation")
        self.page.get_by_text("Docs and Terms").click()
        time.sleep(1)
        self.page.get_by_role("button", name="Generate with AI").click()
        expect(self.page.get_by_text("Documentation generated successfully!")).to_be_visible(timeout=120000)
        screenshot_name = "24_api_product_docs_terms" if is_product else "17_docs_terms_tab"
        self.take_screenshot(screenshot_name)

    def verify_api_http_methods(self):
        """Verifica métodos HTTP da API"""
        self.logger.info("Verifying API HTTP methods")
        self.page.get_by_text("HTTP Methods").click()
        expect(self.page.get_by_role("button", name="Add New Route")).to_be_visible()
        self.take_screenshot("18_http_methods_tab")

    def run_api_health_check(self, is_product=False):
        """Executa health check da API ou API Product"""
        self.logger.info("Running API health check")
        self.page.get_by_text("Health Check", exact=True).click()
        time.sleep(1)
        self.page.get_by_role("button", name="Run Health Check").click()
        expect(self.page.get_by_role("columnheader", name="Backend Endpoint")).to_be_visible()
        screenshot_name = "25_api_product_health_check" if is_product else "19_health_check_tab"
        self.take_screenshot(screenshot_name)

    def run_api_security_scan(self, is_product=False):
        """Executa scan de segurança da API ou API Product"""
        self.logger.info("Running API security scan")
        self.page.get_by_text("OWASP").click()
        time.sleep(1)
        self.page.get_by_role("button", name="Scan for Vulnerabilities with").click()
        expect(self.page.get_by_role("heading", name="Security Issues")).to_be_visible(timeout=10000)
        screenshot_name = "26_api_product_owasp_scan" if is_product else "20_owasp_scan"
        self.take_screenshot(screenshot_name)

    def create_api_product(self):
        """Cria API Product e configura todas as funcionalidades"""
        self.logger.info("Creating and configuring API Product")
        
        # Criar API Product
        self.page.get_by_role("tab", name="API Products").click()
        self.page.get_by_role("button", name="Create API Product").click()
        expect(self.page.get_by_text("API Product created successfully!")).to_be_visible(timeout=10000)
        self.take_screenshot("21_api_product_created")
        self.page.wait_for_url("**/apis-products/edit/**", timeout=30000)
        time.sleep(2)
        self.take_screenshot("22_api_product_edit_page")
        
        # HTTP Methods (único diferente - mostra "2 items")
        self.page.get_by_text("HTTP Methods").click()
        time.sleep(1)
        expect(self.page.get_by_text("2 items")).to_be_visible(timeout=10000)
        self.take_screenshot("23_api_product_http_methods")
        
        # Reutilizar métodos da API (são idênticos)
        self.configure_api_documentation(is_product=True)
        self.run_api_health_check(is_product=True)
        self.run_api_security_scan(is_product=True)

    def create_billing_package(self):
        """Cria pacote de billing"""
        self.logger.info("Creating billing package")
        self.page.locator('.tab-label-container:has-text("Billing")').click()
        time.sleep(1)
        self.take_screenshot("27_api_product_billing")
        self.page.get_by_role("button", name="New").click()

        package_data = {
            "name": f"Premium Package {datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}",
            "description": "Premium API access with enhanced features and higher rate limits",
            "title": "Premium API Access Plan",
            "rate_limit_requests": "1000",
            "rate_limit_period": "60"
        }

        today = datetime.datetime.today().strftime("%Y-%m-%d")  
        future_date = (datetime.datetime.today() + datetime.timedelta(days=30)).strftime("%Y-%m-%d") 

        self.page.get_by_role("textbox", name="* Package name:").fill(package_data["name"])
        self.page.locator("input[name=\"Description\"]").fill(package_data["description"])
        self.page.get_by_role("textbox", name="* Title:").fill(package_data["title"])
        self.page.get_by_role("textbox", name="* Period:").click()
        self.page.get_by_title(today).locator("div").first.click()
        self.page.get_by_title(future_date).locator("div").first.click()
        self.page.get_by_role("spinbutton", name="* Rate Limit Requests:").fill(package_data["rate_limit_requests"])
        self.page.get_by_role("spinbutton", name="* Rate Limit Period:").fill(package_data["rate_limit_period"])
        self.take_screenshot("28_billing_form_filled")
        self.page.get_by_role("button", name="Create").click()
        time.sleep(2)
        self.take_screenshot("29_billing_package_created")
        self.logger.info("Billing package created successfully! ✅")