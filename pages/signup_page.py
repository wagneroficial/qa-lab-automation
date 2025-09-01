from playwright.sync_api import Page, expect

class SignupPage:
    def __init__(self, page: Page):
        self.page = page

    def register_user(self, name, company, phone, email):
        self.page.goto("https://qap-dev.konneqt.cloud/preview-apis")
        self.page.get_by_role("button", name="Sign up").click()
        self.page.get_by_label("Full Name:").fill(name)
        self.page.get_by_label("Company Name:").fill(company)
        self.page.get_by_placeholder("1 (702) 123-").fill(phone)
        self.page.get_by_label("Email:").fill(email)
        self.page.get_by_label("I have read and agree to").check()
        self.page.get_by_role("button", name="Register").click()

    def check_success_message(self, message):
        expect(self.page.get_by_text(message)).to_be_visible()
