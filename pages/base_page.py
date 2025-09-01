from playwright.sync_api import Page


class BasePage:
    def __init__(self, page: Page):
        self.page = page
        
    def navigate_to(self, url: str):
        self.page.goto(url)
        
    def wait_for_element(self, selector: str, timeout: int = 5000):
        self.page.wait_for_selector(selector, timeout=timeout)
        
    def is_element_visible(self, selector: str) -> bool:
        return self.page.locator(selector).is_visible()