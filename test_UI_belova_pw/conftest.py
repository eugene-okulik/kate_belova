from pathlib import Path
from typing import Any, Generator

import pytest
from playwright.sync_api import Page

from test_UI_belova_pw.browser_settings.browser_launcher import BrowserLauncher
# fmt: off
from test_UI_belova_pw.pages import (
    CartPage, MainPage, AlertPage, DesksPage, ProductPage
)
# fmt: on
from test_UI_belova_pw.test_data import product_index

CONFIG_PATH = Path(__file__).parent / 'config_browser.yaml'


def pytest_configure(config):
    project_root = Path(__file__).resolve().parent
    allure_dir = project_root / 'allure-results'
    allure_dir.mkdir(exist_ok=True)
    config.option.allure_report_dir = str(allure_dir)


@pytest.fixture()
def browser() -> Generator[Page, Any, None]:
    driver = BrowserLauncher(str(CONFIG_PATH))
    page = driver.create_page()
    page.set_viewport_size({'width': 1920, 'height': 1080})
    yield page
    driver.close()


@pytest.fixture()
def main_page(browser):
    return MainPage(browser)


@pytest.fixture()
def desks_page(browser):
    return DesksPage(browser)


@pytest.fixture()
def product_page_in_new_tab(
    main_page, request
) -> tuple[ProductPage, str, str, AlertPage]:
    if hasattr(request, 'param'):
        product_idx = request.param
    else:
        product_idx = product_index

    main_page.open_main_page(2)
    product_title, product_price, new_tab = main_page.open_product_in_new_tab(
        product_idx
    )

    product_page = ProductPage(new_tab)
    alert_page = AlertPage(new_tab)
    return product_page, product_title, product_price, alert_page


@pytest.fixture()
def alert_page(browser):
    return AlertPage(browser)


@pytest.fixture()
def cart_page(browser):
    return CartPage(browser)


@pytest.fixture()
def cart_page_from_product_tab(product_page_in_new_tab):
    product_page, product_title, product_price, alert_page = (
        product_page_in_new_tab
    )
    return CartPage(product_page.browser)


@pytest.fixture()
def cart_with_product(browser, main_page, alert_page, cart_page):
    main_page.open_main_page()
    product_title, product_price = main_page.click_add_to_cart_on_hover_button(
        10
    )
    alert_page.wait_for_alert()

    main_page.click_cart_icon_in_header()
    cart_page.assert_product_cart_title_quantity_price(
        product_title, product_price
    )

    return cart_page
