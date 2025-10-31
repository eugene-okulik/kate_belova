import re

import allure
from playwright.sync_api import Page, expect


class BasePage:
    def __init__(self, browser: Page):
        self.browser = browser
        self.base_url = 'http://testshop.qa-practice.com/'
        self.current_url = self.browser.url

        self.logo_element = self.browser.locator('a[href="/"]').first
        self.cart_icon_in_header_element = self.browser.locator(
            'a[href="/shop/cart"]'
        ).last

        self.products_element = self.browser.locator('.oe_product')
        self.products_titles_element = self.browser.locator(
            'a[itemprop="name"]'
        )
        self.products_prices_element = self.browser.locator(
            '.oe_currency_value'
        )
        self.quantity_input_field_element = self.browser.locator(
            'input.quantity'
        )
        self.search_field_element = self.browser.locator(
            '.o_wsale_products_searchbar_form input'
        ).first

    @staticmethod
    def assert_text(actual, expected):
        expect(actual).to_have_text(expected)

    @staticmethod
    def assert_products_count(actual, expected):
        actual_int = int(actual) if isinstance(actual, str) else actual
        expected_int = int(expected) if isinstance(expected, str) else expected

        assert (
            actual_int == expected_int
        ), f'Products count should be {expected_int}, but got {actual_int}'

    @staticmethod
    def get_expected_text_in_product_url_from_product_title(product_title):
        url_text = product_title.lower().strip()
        url_text = url_text.replace(' ', '-')

        return url_text

    @property
    def product_quantity(self):
        return self.quantity_input_field_element.get_attribute('value').strip()

    @property
    def products_titles(self):
        products_titles_lst = [
            desk_name.text_content().strip()
            for desk_name in self.products_titles_element.all()
        ]
        return products_titles_lst

    @allure.step('Click the website logo and go to the Main page')
    def assert_navigation_to_main_page(self):
        self.logo_element.click()
        self.wait_for_url_to_change(self.current_url)
        expect(self.browser).to_have_url(self.base_url)

    @allure.step('Assert search word in found products titles')
    def assert_search_word_in_found_products_titles(self, search_word):
        for title in self.products_titles_element.all():
            pattern = re.compile(search_word, re.IGNORECASE)
            expect(title).to_contain_text(pattern)

    def click_cart_icon_in_header(self):
        self.scroll_to_top()
        expect(self.cart_icon_in_header_element).to_be_in_viewport()
        self.cart_icon_in_header_element.click()
        self.wait_for_url_to_change(self.current_url)

    @allure.step('Enter key word into search field')
    def enter_search_word(self, search_word):
        self.search_field_element.clear()
        self.search_field_element.fill(search_word)
        self.search_field_element.press('Enter')

    def open_in_new_tab(self, element):
        with self.browser.context.expect_page() as new_page_info:
            element.click(modifiers=['Control'])

        new_tab = new_page_info.value
        new_tab.wait_for_load_state()
        new_tab.bring_to_front()

        self.browser = new_tab
        self.current_url = self.browser.url

        return new_tab

    def open_page(self, url):
        return self.browser.goto(url)

    def scroll_to_top(self):
        self.browser.keyboard.press('Home')

    def wait_for_url_to_change(self, original_url, timeout=10000):
        self.browser.wait_for_url(
            lambda url: url != original_url, timeout=timeout
        )
