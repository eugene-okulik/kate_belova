import allure
from .base_page import BasePage


class CartPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.cart_product_name_locator = (
            'css selector',
            '#cart_products h6.fw-bold',
        )
        self.cart_product_price_locator = (
            'css selector',
            '#cart_products [name="website_sale_cart_line_price"] '
            '.oe_currency_value',
        )
        self.cart_loaded_locator = ('css selector', '#cart_products')

    def wait_for_cart_to_load(self):
        self.wait.until(
            self.ec.presence_of_element_located(self.cart_loaded_locator)
        )

    def get_cart_product_name(self):
        self.wait_for_cart_to_load()
        name_element = self.find_element(self.cart_product_name_locator)
        name_text = name_element.text.strip()
        end_idx = name_text.find('(')
        if end_idx != -1:
            return name_text[:end_idx].strip()
        return name_text

    def get_cart_product_price(self):
        self.wait_for_cart_to_load()
        price_element = self.find_element(self.cart_product_price_locator)
        return price_element.text.strip()

    @allure.step('Assert product matches the one added to cart')
    def check_product_name_and_price_in_cart(
        self, expected_name, expected_price
    ):
        actual_name = self.get_cart_product_name()
        actual_price = self.get_cart_product_price()

        self.check_name_and_price(
            actual_name, expected_name, actual_price, expected_price
        )
