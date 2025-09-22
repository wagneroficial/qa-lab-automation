# pages/signup_page.py
import time
from .base_page import BasePage
from playwright.sync_api import Page, expect
from config.settings import settings
from utils import get_user_data
import os
import logging

class SignupPage(BasePage):
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

    def navigate_to_signup(self):
        self.logger.info(f"Navigating to: {self.BASE_URL}")
        self.page.goto(self.BASE_URL)
        self.take_screenshot("01_home_page")
        self.logger.info("Clicking Sign up button")
        self.page.get_by_role("button", name="Sign up").click()
        self.take_screenshot("02_signup_form")

    def register(self, data):
        """Método base para registro"""
        self.page.get_by_label("Full Name:").fill(data["name"])
        self.page.get_by_label("Company Name:").fill(data["company"])
        self.page.get_by_placeholder("1 (702) 123-").fill(data["phone"])
        self.page.get_by_label("Email:").fill(data["email"])
        self.page.get_by_label("I have read and agree to").check()
        self.take_screenshot("03_form_filled")
        self.logger.info("Clicking Register button")
        self.page.get_by_role("button", name="Register").click()

    def register_valid_user(self):
        self.logger.info("Registering valid user")
        data = get_user_data("valid")
        self.register(data)

    def register_with_invalid_company(self):
        self.logger.info("Registering with invalid company")
        data = get_user_data("invalid_company")
        self.register(data)

    def register_existing_user(self):
        self.logger.info("Registering existing user")
        data = get_user_data("user_exists")
        self.register(data)

    def check_message(self, message):
        self.logger.info(f"Checking for message: {message}")
        expect(self.page.get_by_text(message)).to_be_visible(timeout=10000)
        self.take_screenshot(f"04_message_{message.replace(' ', '_')}")
        time.sleep(3)