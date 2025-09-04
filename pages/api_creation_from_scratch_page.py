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

    def create_pokemon_api_from_scratch(self):
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
        

        
        """ self._verify_api_full_functionality() """

    """  def _verify_api_full_functionality(self):
        self.logger.info("Starting full API verification")
        time.sleep(1)
        
        # Edit API
        self.logger.info("Testing Edit functionality")
        self.page.get_by_role("button", name="edit").click()
        self.page.wait_for_url("**/apis/edit/**", timeout=60000)
        self.take_screenshot("28_edit_page")
        
        time.sleep(1)
        
        # Verify General tab (should be default)
        expect(self.page.get_by_label("API Name:")).to_be_visible()
        self.take_screenshot("29_general_tab")
        
        # Test Docs and Terms tab
        self.logger.info("Testing Docs and Terms tab")
        self.page.get_by_text("Docs and Terms").click()
        expect(self.page.get_by_text("Main Documentation:")).to_be_visible()
        self.take_screenshot("30_docs_terms_tab")
        
        # Test HTTP Methods tab
        self.logger.info("Testing HTTP Methods tab")
        self.page.get_by_text("HTTP Methods").click()
        expect(self.page.get_by_role("button", name="Add New Route")).to_be_visible()
        
        # Verify our created route exists
        expect(self.page.get_by_text("ditto")).to_be_visible()
        self.take_screenshot("31_http_methods_tab")
        
        # Test Health Check tab (run again from edit page)
        self.logger.info("Testing Health Check from edit page")
        self.page.get_by_text("Health Check", exact=True).click()
        
        # Check if Run Health Check button is available and clickable
        health_check_btn = self.page.get_by_role("button", name="Run Health Check")
        if health_check_btn.is_visible():
            health_check_btn.click()
            time.sleep(3)  # Wait for results
            self.take_screenshot("32_health_check_edit_page")
        
        # Test OWASP Security Scan tab
        self.logger.info("Testing OWASP Security Scan")
        self.page.get_by_text("OWASP").click()
        
        # Check if scan button exists and run scan
        scan_btn = self.page.get_by_role("button", name="Scan for Vulnerabilities with")
        if scan_btn.is_visible():
            scan_btn.click()
            
            # Wait for security scan results
            try:
                expect(self.page.get_by_role("heading", name="Security Issues")).to_be_visible(timeout=15000)
                self.take_screenshot("33_owasp_scan_completed")
            except:
                self.logger.warning("OWASP scan may have taken longer than expected")
                self.take_screenshot("33_owasp_scan_timeout")
        
        self.logger.info("Pokemon API from scratch fully verified successfully ✅")
        
        # Additional verification: Check if we can navigate back to APIs list
        self.logger.info("Verifying navigation back to APIs list")
        self.page.get_by_role("menuitem", name="APIs").click()
        time.sleep(1)
        
        # Look for our created API in the list
        expect(self.page.get_by_text("API-Pokemon-Scratch")).to_be_visible(timeout=10000)
        self.take_screenshot("34_api_in_list_verified")
        
        self.logger.info("Full verification completed successfully! 🎉")

    def create_custom_api_from_scratch(self, api_name: str, api_type: str = "Public"):
        self.logger.info(f"Creating custom API '{api_name}' from scratch")
        
        # Click New button
        self.page.get_by_role("button", name="New").click()
        self.take_screenshot(f"new_api_clicked_{api_name.lower().replace(' ', '_')}")
        
        # Select Create from Scratch
        self.page.get_by_text("Create from Scratch").click()
        
        # Fill API details
        self.page.get_by_label("API Name:").fill(api_name)
        self.page.get_by_label("Type:").click()
        self.page.get_by_text(api_type, exact=True).click()
        
        # Create API
        self.page.get_by_role("button", name="Create").click()
        
        # Wait for success
        expect(self.page.get_by_text("Success", exact=True)).to_be_visible(timeout=10000)
        self.take_screenshot(f"api_created_{api_name.lower().replace(' ', '_')}") """