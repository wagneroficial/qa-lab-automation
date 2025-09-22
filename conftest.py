import pytest
import logging
from playwright.sync_api import Playwright, Browser, BrowserContext, Page
from config.settings import settings


def pytest_configure(config):
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    playwright_logger = logging.getLogger('playwright')
    playwright_logger.setLevel(logging.WARNING)
    
    config.addinivalue_line("markers", "regression: Full regression test suite")
    config.addinivalue_line("markers", "smoke: Essential quick tests")
    config.addinivalue_line("markers", "admin: Admin user tests")
    config.addinivalue_line("markers", "user: Regular user tests")
    config.addinivalue_line("markers", "positive: Positive test cases")
    config.addinivalue_line("markers", "negative: Negative test cases")


@pytest.fixture(scope="session")
def playwright_instance():
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        yield p


@pytest.fixture(scope="session")
def browser(playwright_instance: Playwright):
    browser = playwright_instance.chromium.launch(
        headless=settings.HEADLESS,
        slow_mo=settings.SLOW_MO
    )
    yield browser
    browser.close()


@pytest.fixture(scope="function")
def context(browser: Browser):
    context = browser.new_context(
        viewport={"width": 1280, "height": 720}
    )
    yield context
    context.close()


@pytest.fixture(scope="function") 
def page(context: BrowserContext):
    page = context.new_page()
    yield page
    page.close()