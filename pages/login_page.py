from pages.base_page import BasePage
from config.settings import Settings

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.base_url = Settings.BASE_URL
    
    def navigate(self):
        self.navigate_to(self.base_url)
    
    def login(self, email: str, password: str):
        self.page.get_by_test_id("login-email-input").fill(email)
        self.page.get_by_test_id("login-password-input").fill(password)
        self.page.get_by_test_id("login-submit-button").click()
    
    def logout(self):
        self.page.get_by_test_id("logout-button").click()
    
    def logout(self):
        self.page.get_by_test_id("logout-button").click()
    
    def has_welcome_message(self):
        try:
            welcome_text = self.page.locator("text=Bem-vindo")
            welcome_text.is_visible(timeout=5000)
            return True
        except:
            return False
    
    def has_error(self):
        try:
            return self.page.get_by_test_id("login-error").is_visible()
        except:
            return False
    
    def is_on_login_page(self):
        """Verifica se está na página de login"""
        return self.page.get_by_test_id("login-email-input").is_visible()