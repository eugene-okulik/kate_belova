from pathlib import Path

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from .pages import MainPage, ProductPage, CartPage, AddToCartPopup


def pytest_configure(config):
    current_dir = Path.cwd()
    allure_dir = (
        current_dir
        / 'homework'
        / 'kate_belova'
        / 'homework26'
        / 'allure-results'
    )
    allure_dir.mkdir(parents=True, exist_ok=True)
    config.option.allure_report_dir = str(allure_dir)


@pytest.fixture()
def browser(request):
    service = Service(executable_path=ChromeDriverManager().install())

    browser_options = webdriver.ChromeOptions()
    browser_options.page_load_strategy = 'eager'
    browser_options.add_argument('--start-maximized')
    # browser_options.add_argument('--headless=new')

    browser_options.add_argument('--log-level=3')
    browser_options.add_argument('--disable-logging')
    browser_options.add_argument('--disable-dev-shm-usage')
    browser_options.add_argument('--no-sandbox')
    browser_options.add_argument('--disable-gpu-sandbox')
    browser_options.add_argument('--disable-software-rasterizer')

    browser_options.add_experimental_option(
        'excludeSwitches',
        ['enable-logging', 'enable-automation', 'ignore-certificate-errors'],
    )
    browser_options.add_experimental_option('useAutomationExtension', False)

    browser = webdriver.Chrome(service=service, options=browser_options)
    print('\nStart browser for test')

    yield browser
    print('\nQuit browser after test')
    browser.quit()


@pytest.fixture()
def main_page(browser):
    return MainPage(browser)


@pytest.fixture()
def add_to_cart_popup(browser):
    return AddToCartPopup(browser)


@pytest.fixture()
def product_page(browser):
    return ProductPage(browser)


@pytest.fixture()
def cart_page(browser):
    return CartPage(browser)
