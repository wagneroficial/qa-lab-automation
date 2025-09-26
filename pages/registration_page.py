from pages.base_page import BasePage
from config.settings import Settings

class RegistrationPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.base_url = Settings.BASE_URL
    
    def navigate_to_home(self):
        self.navigate_to(self.base_url)
    
    def click_register_button(self):
        self.page.get_by_test_id("navigate-to-register-button").click()
    
    def fill_registration_form(self, name: str, email: str, password: str, confirm_password: str = None):
        self.page.get_by_test_id("register-name-input").fill(name)
        self.page.get_by_test_id("register-email-input").fill(email)
        self.page.get_by_test_id("register-password-input").fill(password)
        self.page.get_by_test_id("register-confirm-password-input").fill(confirm_password or password)
    
    def submit_form(self):
        self.page.get_by_test_id("register-submit-button").click()
    
    def has_welcome_message(self):
        try:
            welcome_text = self.page.locator("text=Bem-vindo")
            welcome_text.is_visible(timeout=2000)
            return True
        except:
            return False
    
    def has_error(self):
        try:
            return self.page.get_by_test_id("register-error").is_visible(timeout=2000)
        except:
            return False