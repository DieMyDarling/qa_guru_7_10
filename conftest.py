import pytest
from selene.api import browser


@pytest.fixture(scope='function', autouse=True)
def open_browser():
    browser.config.base_url = 'https://demoqa.com'
    browser.config.window_width = 1200
    browser.config.window_height = 2400
    browser.config.reports_folder = './.reports'
    yield

    browser.quit()
