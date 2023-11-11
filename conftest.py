import pytest
from selene import Browser, Config
from selenium import webdriver


@pytest.fixture(scope='function', autouse=True)
def setup_browser(request):
    options = webdriver.ChromeOptions()
    options.browser_version = '118.0'
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-notifications')
    options.add_argument('--disable-extensions')
    options.add_argument('--disable-infobars')
    options.add_argument('--enable-automation')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-setuid-sandbox')
    options.set_capability(
        'selenoid:options',
        {
            'screenResolution': '1920x1080x24',
            'enableVNC': True,
            'enableVideo': True,
            'enableLog': True,
        },
    )

    browser = Browser(Config(
        driver_options=options,
        driver_remote_url='https://user1:1234@selenoid.autotests.cloud/wd/hub',
        driver_name='chrome',
        reports_folder='./.reports',
        save_screenshot_on_failure=True,
        save_page_source_on_failure=True,
        window_height=1920,
        window_width=1080,
        timeout=4,
        base_url='https://demoqa.com',
    ))

    yield browser

    browser.quit()
