import allure
from playwright.sync_api import expect

from test_UI_belova_pw.pages import BasePage


class ProductPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.product_title_element = self.browser.locator('h1')
        self.breadcrumbs_product_title_element = self.browser.locator(
            '.breadcrumb-item.active span'
        )

        self.minus_button_element = self.browser.locator('.fa.fa-minus')
        self.plus_button_element = self.browser.locator('.fa.fa-plus')
        self.add_to_cart_button_element = self.browser.locator('a#add_to_cart')

        self.terms_and_conditions_element = self.browser.locator(
            '.text-muted.mb-0'
        )
        self.terms_and_conditions_title_expected = 'Terms and Conditions'
        self.terms_and_conditions_link_expected = f'{self.base_url}terms'
        self.terms_and_conditions_texts_expected = (
            '30-day money-back guarantee\nShipping: 2-3 Business Days'
        )

    @property
    def product_title(self):
        product_title = self.product_title_element.text_content().strip()
        return product_title

    @allure.step('Add product quantity on Product page')
    def add_product_quantity(self, quantity):
        current_quantity = int(self.product_quantity)
        self.plus_button_element.wait_for(state='visible', timeout=10000)
        expect(self.plus_button_element).to_be_enabled()

        for click_num in range(quantity - current_quantity):
            expected_quantity = current_quantity + 1
            self.plus_button_element.click()
            self.wait_for_quantity_to_change(current_quantity)
            self.wait_for_quantity_to_become(expected_quantity)

            current_quantity = expected_quantity

    @allure.step('Assert Add to cart button is active')
    def assert_add_to_cart_button_is_active(self):
        expect(self.add_to_cart_button_element).to_be_enabled()

    @allure.step(
        'Assert breadcrumbs product title matches original product title'
    )
    def assert_breadcrumbs_product_title(self):
        expect(self.breadcrumbs_product_title_element).to_have_text(
            self.product_title
        )

    @allure.step('Assert plus and minus buttons work')
    def assert_plus_and_minus_buttons_work(self):
        self.plus_button_element.wait_for(state='visible', timeout=10000)
        self.minus_button_element.wait_for(state='visible', timeout=10000)
        expect(self.plus_button_element).to_be_enabled()
        expect(self.minus_button_element).to_be_enabled()

        initial_quantity = int(self.product_quantity)

        self.minus_button_element.click()
        self.wait_for_quantity_load(initial_quantity, 'decrease')
        expect(self.quantity_input_field_element).to_have_value(
            str(initial_quantity)
        )

        self.plus_button_element.click()
        self.wait_for_quantity_load(initial_quantity)
        expect(self.quantity_input_field_element).to_have_value(
            str(initial_quantity + 1)
        )

        current_quantity = initial_quantity + 1
        self.minus_button_element.click()
        self.wait_for_quantity_load(current_quantity, 'decrease')
        expect(self.quantity_input_field_element).to_have_value(
            str(initial_quantity)
        )

        final_quantity = int(self.product_quantity)
        assert final_quantity == initial_quantity

    @allure.step('Assert product quantity')
    def assert_product_quantity(self, expected_quantity=1):
        expect(self.quantity_input_field_element).to_have_value(
            str(expected_quantity)
        )

    @allure.step('Assert product title and price')
    def assert_product_title_and_price(self, expected_title, expected_price):
        expect(self.product_title_element).to_have_text(expected_title)
        expect(self.products_prices_element.first).to_have_text(expected_price)

    @allure.step('Assert quantity input field is active')
    def assert_quantity_input_field_is_active(self):
        expect(self.quantity_input_field_element).to_be_enabled()

    @allure.step('Assert terms_and_conditions')
    def assert_terms_and_conditions(self):
        self.terms_and_conditions_element.wait_for(
            state='visible', timeout=10000
        )

        terms_title_element = self.terms_and_conditions_element.locator('u')
        expect(terms_title_element).to_have_text(
            self.terms_and_conditions_title_expected
        )

        terms_link_element = self.terms_and_conditions_element.locator('a')
        actual_href = terms_link_element.get_attribute('href')

        if actual_href.startswith('/'):
            actual_full_url = f'{self.base_url.rstrip('/')}{actual_href}'
        else:
            actual_full_url = actual_href

        assert actual_full_url == self.terms_and_conditions_link_expected, (
            f'Expected URL should be '
            f'{self.terms_and_conditions_link_expected}, '
            f'but got: {actual_full_url}'
        )

        expect(self.terms_and_conditions_element).to_contain_text(
            self.terms_and_conditions_texts_expected
        )

    @allure.step('Click Add to cart button')
    def click_add_to_cart_button(self):
        self.add_to_cart_button_element.click()

    def wait_for_quantity_load(
        self, initial_quantity, expected_direction='increase'
    ):
        if expected_direction == 'increase':
            expected_value = str(initial_quantity + 1)
            expect(self.quantity_input_field_element).to_have_value(
                expected_value, timeout=10000
            )
        elif expected_direction == 'decrease':
            if initial_quantity > 1:
                expected_value = str(initial_quantity - 1)
            else:
                expected_value = str(initial_quantity)

            expect(self.quantity_input_field_element).to_have_value(
                expected_value, timeout=10000
            )

    def wait_for_quantity_to_become(self, expected_quantity, timeout=5000):
        expect(self.quantity_input_field_element).to_have_value(
            str(expected_quantity), timeout=timeout
        )

    def wait_for_quantity_to_change(self, previous_quantity, timeout=5000):
        expect(self.quantity_input_field_element).not_to_have_value(
            str(previous_quantity), timeout=timeout
        )
