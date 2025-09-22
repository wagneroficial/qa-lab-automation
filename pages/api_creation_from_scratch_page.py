import time
from .base_page import BasePage
from playwright.sync_api import expect
from config.settings import settings
import logging


class ApiCreationFromScratchPage(BasePage):
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

    def create_api_from_scratch(self):
        self.logger.info("Creating Pokemon API from scratch")
        
        # Click New button
        self.page.get_by_role("button", name="New").click()
        self.take_screenshot("08_new_api_clicked")
        
        # Select Create from Scratch
        self.page.get_by_text("Create from Scratch").click()
        self.take_screenshot("09_create_from_scratch_selected")
        
        # Fill API Name
        api_name = "API-Pokemon-Scratch"
        self.page.get_by_label("API Name:").click()
        self.page.get_by_label("API Name:").fill(api_name)
        self.take_screenshot("10_api_name_filled")
        
        # Select API Type
        self.page.get_by_label("Type:").click()
        self.page.get_by_text("Public", exact=True).click()
        self.take_screenshot("11_api_type_selected")
        
        # Create API
        self.page.get_by_role("button", name="Create").click()
        self.take_screenshot("12_create_api_clicked")
        
        # Wait for success message
        expect(self.page.get_by_text("Success", exact=True)).to_be_visible(timeout=10000)
        self.take_screenshot("13_api_created_success")
        
        # Add New Route
        self.logger.info("Adding new route 'ditto'")
        self.page.get_by_role("button", name="Add New Route").click()
        self.take_screenshot("14_add_route_clicked")
        
        # Configure Route Name
        self.page.get_by_label("Name:", exact=True).click()
        self.page.get_by_label("Name:", exact=True).press("Control+a")
        self.page.get_by_label("Name:", exact=True).fill("ditto")
        self.take_screenshot("15_route_name_filled")
        
        # Configure Extra Settings
        self.logger.info("Configuring extra settings")
        self.page.get_by_text("Extra settings").click()
        self.take_screenshot("16_extra_settings_opened")
        
        # Select HTTP Methods
        self.page.locator(".ant-select-selection-overflow").click()
        self.page.get_by_title("HEAD", exact=True).locator("div").click()
        self.page.get_by_title("POST").locator("div").click()
        self.take_screenshot("17_http_methods_selected")
        
        # Add Expose Headers
        self.logger.info("Adding expose headers")
        self.page.get_by_role("button", name="plus Add field").nth(1).click()
        
        # First header
        self.page.locator("#expose_headers_0_value").click()
        self.page.locator("#expose_headers_0_value").fill("Content-Length")
        
        # Second header
        self.page.locator("#expose_headers_1_value").click()
        self.page.locator("#expose_headers_1_value").fill("Content-Type")
        self.take_screenshot("18_expose_headers_filled")
        
        # Configure Backend
        self.logger.info("Configuring backend")
        self.page.get_by_text("Backend", exact=True).click()
        self.take_screenshot("19_backend_tab_clicked")
        
        # Backend URI Path
        self.page.get_by_label("Backend URI Path:").click()
        self.page.get_by_label("Backend URI Path:").fill("/api/v2/pokemon/ditto")
        self.take_screenshot("20_backend_uri_filled")
        
        # Configure response type
        self.page.get_by_text("JSON").click()
        self.page.get_by_text("No-op", exact=True).click()
        self.take_screenshot("21_response_type_selected")
        
        # Backend Host
        self.page.get_by_placeholder("host").click()
        self.page.get_by_placeholder("host").fill("https://pokeapi.co")
        self.take_screenshot("22_backend_host_filled")
        
        # Create Route
        self.page.get_by_role("button", name="Create").click()
        self.take_screenshot("23_route_create_clicked")

    def verify_api_created_successfullys(self):
        self.logger.info("Verifying Pokemon API created successfully")
        
        time.sleep(2)
        self.take_screenshot("24_route_created")
        
        # Run Health Check
        self.logger.info("Running health check")
        self.page.get_by_text("Health Check", exact=True).click()
        self.take_screenshot("25_health_check_tab")
        
        self.page.get_by_role("button", name="Run Health Check").click()
        self.take_screenshot("26_health_check_running")
        

    