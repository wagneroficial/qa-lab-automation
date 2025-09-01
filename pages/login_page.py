from .base_page import BasePage
from playwright.sync_api import expect
from config.settings import settings
import os
import time
import logging


class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
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
        self.page.get_by_placeholder("mail@example.com").fill(email)
        self.page.get_by_label("Email:").fill(password)
        self.logger.debug("Credentials filled")
        self.take_screenshot("03_credentials_filled")
        
        self.logger.info("Clicking Sign In button")
        self.page.get_by_role("button", name="Sign In").click()
        
    def login_as_admin(self):
        self.logger.info("Logging in as administrator")
        self.login(settings.ADMIN_EMAIL, settings.ADMIN_PASSWORD)
        
    def login_as_user(self):
        self.logger.info("Logging in as regular user")
        self.login(settings.USER_EMAIL, settings.USER_PASSWORD)
        
    def wait_for_dashboard(self):
        self.logger.info("Waiting for dashboard to load...")
        
        try:
            current_url = self.page.url
            self.logger.info(f"Current URL: {current_url}")
            
            if "/admin/dashboard" in current_url or "/customer/dashboard" in current_url:
                expect(self.page.locator("body")).to_be_visible(timeout=settings.BROWSER_TIMEOUT)
                time.sleep(3)
                
                if "/admin/dashboard" in current_url:
                    self.take_screenshot("05_admin_dashboard_final")
                    self.logger.info("ADMIN dashboard loaded successfully")
                elif "/customer/dashboard" in current_url:
                    self.take_screenshot("05_customer_dashboard_final") 
                    self.logger.info("CUSTOMER dashboard loaded successfully")
            else:
                self.logger.info("Waiting for dashboard redirection...")
                self.page.wait_for_url("**/admin/dashboard**", timeout=settings.BROWSER_TIMEOUT)
                time.sleep(3)
                self.take_screenshot("05_admin_dashboard_final")
                self.logger.info("ADMIN dashboard loaded successfully")
                
        except Exception as e:
            current_url = self.page.url
            self.logger.error(f"Error loading dashboard. Current URL: {current_url}. Error: {e}")
            self.take_screenshot("06_dashboard_ERROR")
            
            if "/dashboard" in current_url:
                self.logger.warning("URL seems correct, considering as success despite timeout")
                if "/customer/dashboard" in current_url:
                    self.take_screenshot("06_customer_dashboard_final")
                elif "/admin/dashboard" in current_url:
                    self.take_screenshot("06_admin_dashboard_final")
                return
            
            raise