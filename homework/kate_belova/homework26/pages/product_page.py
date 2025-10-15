import allure

from .base_page import BasePage


class ProductPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.add_to_cart_button_locator = ('css selector', '#add_to_cart')

    @property
    def add_to_cart_button(self):
        self.wait.until(
            self.ec.presence_of_element_located(
                self.add_to_cart_button_locator
            )
        )
        return self.find_element(self.add_to_cart_button_locator)

    @allure.step('Click add to cart button')
    def click_add_to_cart(self):
        self.wait.until(
            self.ec.element_to_be_clickable(self.add_to_cart_button)
        )
        self.add_to_cart_button.click()

    @allure.step('Close product page and switch to Main page')
    def close_product_page_return_to_main(self):
        self.close_current_tab()
        self.switch_to_previous_tab()
