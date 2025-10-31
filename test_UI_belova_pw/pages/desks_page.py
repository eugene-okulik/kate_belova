import re
import time

import allure
from playwright.sync_api import expect

from test_UI_belova_pw.pages import BasePage


class DesksPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.url = self.base_url + '/shop/category/desks-1'

        self.desks_found_counter_element = self.browser.locator(
            '.products_header .oe_search_found small',
        )
        self.components_button_element = self.browser.locator(
            'text=Components'
        )
        self.breadcrumbs_desks_link = self.browser.locator(
            '.breadcrumb-item'
        ).nth(1)

        self.dropdown_sort_by_element = self.browser.locator(
            '.dropdown_sorty_by'
        )
        self.dropdown_option_element = self.browser.locator(
            '.dropdown_sorty_by a.dropdown-item'
        )

    @property
    def desks_found(self):
        return self.products_element.all()

    @property
    def desks_found_counter(self):
        desks_found_text = self.desks_found_counter_element.text_content()
        desks_found = desks_found_text.lstrip('(').split()[0].strip()
        return int(desks_found)

    @property
    def desks_prices(self):
        desks_prices_lst = [
            float(
                desk_price.text_content()
                .replace('$', '')
                .replace(',', '')
                .strip()
            )
            for desk_price in self.products_prices_element.all()
        ]
        return desks_prices_lst

    @allure.step(
        'Assert actual count of desks found equals the one in counter'
    )
    def assert_actual_desks_count_equals_the_one_in_counter(self):
        counter_number = self.desks_found_counter
        actual_count = len(self.desks_found)
        assert counter_number == actual_count, (
            f'Desks found counter ({counter_number}) should be equal '
            f'to the actual amount of found desks ({actual_count})'
        )

    @allure.step('Assert desks count')
    def assert_found_desks_count(self, expected_count):
        actual_count = len(self.desks_found)
        self.assert_products_count(actual_count, expected_count)

    @allure.step('Assert desks are sorted by name ascending')
    def assert_sorted_by_name_asc(self):
        titles = self.products_titles
        sorted_titles = sorted(titles)
        assert titles == sorted_titles, (
            f'Titles are not sorted A-Z. '
            f'Expected: {sorted_titles}, Actual: {titles}'
        )

    @allure.step('Assert desks are sorted by price ascending')
    def assert_sorted_by_price_asc(self):
        prices = self.desks_prices
        sorted_prices = sorted(prices)
        assert prices == sorted_prices, (
            f'Prices are not sorted Low to High. '
            f'Expected: {sorted_prices}, Actual: {prices}'
        )

    @allure.step('Assert desks are sorted by price descending')
    def assert_sorted_by_price_desc(self):
        prices = self.desks_prices
        sorted_prices = sorted(prices, reverse=True)
        assert prices == sorted_prices, (
            f'Prices are not sorted High to Low. '
            f'Expected: {sorted_prices}, Actual: {prices}'
        )

    @allure.step('Click Desks in Breadcrumbs')
    def click_desks_in_breadcrumbs(self):
        self.breadcrumbs_desks_link.wait_for(state='visible', timeout=1000)
        self.breadcrumbs_desks_link.click()
        self.wait_for_url_to_change(self.url)
        expect(self.browser).to_have_url(re.compile(r'.*desks-1.*'))

    @allure.step('Click Components button')
    def click_components_button(self):
        self.components_button_element.wait_for(state='visible')
        self.components_button_element.click()
        self.wait_for_url_to_change(self.url)
        expect(self.browser).to_have_url(re.compile(r'.*desks-components.*'))

    @allure.step('Open Desks page')
    def open_desks_page(self):
        return self.open_page(self.url)

    @allure.step('Click dropdown Sort By and choose sort option')
    def select_sort_option(self, index: int) -> str:
        self.dropdown_sort_by_element.click()
        chosen_option = self.dropdown_option_element.nth(index)

        expect(chosen_option).to_be_visible()
        expect(chosen_option).to_be_enabled()
        expect(chosen_option).not_to_have_text('')

        option_text = chosen_option.text_content().strip()
        chosen_option.click()
        self.wait_for_desks_reload()

        return option_text

    def wait_for_desks_reload(self, timeout=3):
        start_time = time.time()

        initial_desks = self.desks_found
        initial_count = len(initial_desks)

        while time.time() - start_time < timeout:
            current_desks = self.desks_found
            current_count = len(current_desks)

            if current_count != initial_count:
                return True

        return False
