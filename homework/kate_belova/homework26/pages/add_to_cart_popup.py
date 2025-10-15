import allure

from .base_page import BasePage


class AddToCartPopup(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

        self.add_to_cart_popup_header_locator = (
            'xpath',
            '//h4[contains(text(), "Add to cart")]',
        )
        self.continue_shopping_button_locator = (
            'css selector',
            '.btn.btn-secondary',
        )
        self.popup_product_name_locator = ('css selector', '.product-name')
        self.popup_product_price_locator = (
            'css selector',
            '.oe_currency_value',
        )

    def get_popup_product_name(self):
        name_element = self.find_element(self.popup_product_name_locator)
        name_text = name_element.text.strip()

        if ']' in name_text and '(' in name_text:
            start_idx = name_text.find(']') + 1
            end_idx = name_text.find('(')
            return name_text[start_idx:end_idx].strip()
        elif '(' in name_text:
            return name_text[: name_text.find('(')].strip()
        else:
            return name_text

    def get_popup_product_price(self):
        price_element = self.find_element(self.popup_product_price_locator)
        price_text = price_element.text.strip()
        start_idx = price_text.find('$')
        if start_idx != -1:
            # fmt: off
            return price_text[start_idx + 1:].strip()
            # fmt: on
        return price_text

    @property
    def continue_shopping_button(self):
        return self.find_element(self.continue_shopping_button_locator)

    @allure.step('Wait for popup "Add to cart" to appear')
    def wait_for_popup(self):
        self.wait.until(
            self.ec.presence_of_element_located(
                self.add_to_cart_popup_header_locator
            )
        )

    @allure.step('Click continue shopping button')
    def click_continue_shopping(self):
        self.wait.until(
            self.ec.element_to_be_clickable(self.continue_shopping_button)
        )
        self.continue_shopping_button.click()

    @allure.step('Assert product matches the one added to popup')
    def check_product_name_and_price_in_popup(
        self, expected_name, expected_price
    ):
        actual_name = self.get_popup_product_name()
        actual_price = self.get_popup_product_price()

        self.check_name_and_price(
            actual_name, expected_name, actual_price, expected_price
        )
