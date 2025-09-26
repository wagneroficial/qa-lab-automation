from playwright.sync_api import Page


class BasePage:
    def __init__(self, page: Page):
        self.page = page
        
    def navigate_to(self, url: str):
        """Navigate to a URL"""
        self.page.goto(url)
        
    def wait_for_element(self, selector: str, timeout: int = 5000):
        """Wait for element to be present"""
        self.page.wait_for_selector(selector, timeout=timeout)
        
    def is_element_visible(self, selector: str) -> bool:
        """Check if element is visible"""
        try:
            return self.page.locator(selector).is_visible()
        except:
            return False
    
    def click(self, selector: str):
        """Click an element"""
        self.page.click(selector)
    
    def fill(self, selector: str, value: str):
        """Fill an input field"""
        self.page.fill(selector, value)
    
    def get_text(self, selector: str):
        """Get text content of element"""
        return self.page.text_content(selector) or ""
    
    def is_visible(self, selector: str):
        """Alias for is_element_visible"""
        return self.is_element_visible(selector)
    
    def wait_for_selector(self, selector: str, timeout: int = 5000):
        """Wait for selector to appear"""
        self.page.wait_for_selector(selector, timeout=timeout)