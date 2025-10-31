import allure
from playwright.sync_api import expect

from test_UI_belova_pw.pages import BasePage


class CartPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.url = self.base_url + '/shop/cart'

        self.empty_cart_message_element = self.browser.locator('.alert-info')
        self.empty_cart_message_expected = 'Your cart is empty!'
        self.cart_icon_element = self.browser.locator(
            '.my_cart_quantity'
        ).first

        self.product_cart_title_element = self.browser.locator(
            '#cart_products h6'
        )
        self.product_cart_price_element = self.browser.locator(
            '#cart_products .oe_currency_value'
        )
        self.remove_cart_button_element = self.browser.locator(
            'a.js_delete_product'
        )

    @allure.step('Assert cart icon has no items')
    def assert_cart_icon_has_no_items(self):
        expect(self.cart_icon_element).to_be_hidden()
        expect(self.cart_icon_element).to_have_text('0')

    @allure.step('Assert empty cart message')
    def assert_empty_cart_message(self):
        self.assert_text(
            self.empty_cart_message_element, self.empty_cart_message_expected
        )

    @allure.step('Assert product title, quantity and price')
    def assert_product_cart_title_quantity_price(
        self, expected_title, expected_price, expected_quantity=1
    ):
        self.product_cart_title_element.wait_for(
            state='visible', timeout=10000
        )
        self.quantity_input_field_element.wait_for(
            state='visible', timeout=10000
        )
        self.product_cart_price_element.wait_for(
            state='visible', timeout=10000
        )

        expect(self.product_cart_title_element).to_have_text(expected_title)
        expect(self.quantity_input_field_element).to_have_value(
            str(expected_quantity)
        )

        def normalize_price(price_str):
            cleaned = price_str.replace(',', '')
            return f'{float(cleaned):.2f}'

        expected_price_normalized = normalize_price(expected_price)
        actual_price = self.product_cart_price_element.text_content().strip()
        actual_price_normalized = normalize_price(actual_price)

        assert expected_price_normalized == actual_price_normalized, (
            f'Expected price: {expected_price_normalized}, '
            f'Actual price: {actual_price_normalized}'
        )

    @allure.step('Click Remove button in cart so to delete product')
    def remove_product_from_cart(self):
        self.remove_cart_button_element.click()

    @allure.step('Open Cart page')
    def open_cart_page(self):
        return self.open_page(self.url)
