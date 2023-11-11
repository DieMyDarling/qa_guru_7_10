import pytest
from selene.api import *
from selenium import webdriver


@pytest.fixture(scope='function', autouse=True)
def setup_browser(request):
    options = webdriver.ChromeOptions()
    options.browser_version = '100.0'
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-notifications')
    options.add_argument('--disable-extensions')
    options.add_argument('--disable-infobars')
    options.add_argument('--enable-automation')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-setuid-sandbox')

    selenoid_capability = {
        'browserName': 'chrome',
        'browserVersion': options.browser_version,
        'selenoid:options':
            {
                'screenResolution': '1920x1080x24',
                'enableVNC': True,
                'enableVideo': True,
                'enableLog': True,
            },
    }
    options.capabilities.update(selenoid_capability)

    config.driver_options = options
    config.window_width = 1920
    config.window_height = 1080
    config.reports_folder = './.reports'
    config.save_screenshot_on_failure = True
    config.save_page_source_on_failure = True
    config.timeout = 4
    config.base_url = 'https://demoqa.com'

    yield browser

    browser.quit()
