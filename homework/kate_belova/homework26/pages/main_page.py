import allure

from .base_page import BasePage


class MainPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.products_locator = ('css selector', 'td.oe_product')
        self.product_name_locator = ('css selector', 'h6 a')
        self.product_name = None
        self.product_price_locator = ('css selector', '.oe_currency_value')
        self.product_price = None
        self.expected_text_in_product_url = 'customizable-desk'
        self.product_url = None
        self.cart_locator = ('css selector', 'a[aria-label="eCommerce cart"]')
        self.hover_cart_button_locator = ('css selector', '.fa-shopping-cart')

    @allure.step('Open Main page')
    def open_main_page(self):
        self.open_page(self.url)

    @property
    def products(self):
        return self.find_elements(self.products_locator)

    @property
    def cart_button(self):
        return self.products[0].find_element(*self.hover_cart_button_locator)

    def get_product_name(self, product_element):
        name_element = product_element.find_element(*self.product_name_locator)
        return name_element.text.strip()

    def get_product_price(self, product_element):
        price_element = product_element.find_element(
            *self.product_price_locator
        )
        return price_element.text.strip()

    @allure.step('Hover over product and click "Add to" cart button')
    def click_add_to_cart_from_hover_button(self):
        first_product = self.products[0]

        self.product_name = self.get_product_name(first_product)
        self.product_price = self.get_product_price(first_product)

        self.cart_button.click()

    @allure.step('Open 1 product on Main page in new tab')
    def open_product_in_new_tab(self):
        first_product = self.products[0]

        self.product_name = self.get_product_name(first_product)
        self.product_price = self.get_product_price(first_product)

        self.open_in_new_tab(first_product)
        self.product_url = self.browser.current_url

        assert self.expected_text_in_product_url in self.product_url, (
            f'Product url should contain {self.expected_text_in_product_url}, '
            f'but actual url is {self.product_url}'
        )

    @property
    def shopping_cart(self):
        return self.find_element(self.cart_locator)

    @allure.step('Open shopping cart on Main page')
    def open_shopping_cart(self):
        self.shopping_cart.click()
        self.wait.until(self.ec.url_to_be(self.cart_url))
