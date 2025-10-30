import allure

from test_UI_belova_pw.pages import BasePage


class MainPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.url1 = self.base_url
        self.url2 = self.base_url + 'shop/page/2'

        self.expected_text_in_product_url = None
        self.product_url = None
        self.product_title = None
        self.product_price = None
        self.hover_cart_button_selector = 'a.a-submit'
        self.product_cart_button = None

    @allure.step('Hover over product and click cart button')
    def click_add_to_cart_on_hover_button(self, product_idx):
        product = self.products_element.nth(product_idx)
        product.scroll_into_view_if_needed()

        self.product_title = self.get_product_title(product_idx)
        self.product_price = self.get_product_price(product_idx)

        product.hover()
        self.product_cart_button = self.get_product_cart_button(product_idx)
        self.product_cart_button.click()

        return self.product_title, self.product_price

    def get_product_cart_button(self, product_idx):
        product = self.products_element.nth(product_idx)
        product_cart_button = product.locator(self.hover_cart_button_selector)
        return product_cart_button

    def get_product_price(self, product_idx):
        product_price_element = self.products_prices_element.nth(product_idx)
        product_price = product_price_element.text_content()
        return product_price.strip()

    def get_product_title(self, product_idx):
        product_title_element = self.products_titles_element.nth(product_idx)
        product_title = product_title_element.text_content()
        return product_title.strip()

    @allure.step('Open Main page')
    def open_main_page(self, idx=None):
        if idx is None:
            return self.open_page(self.url1)
        elif idx == 2:
            return self.open_page(self.url2)
        return None

    @allure.step('Open product from Main page in new tab')
    def open_product_in_new_tab(self, product_idx):
        product_element = self.products_titles_element.nth(product_idx)
        self.product_title = self.get_product_title(product_idx)
        self.product_price = self.get_product_price(product_idx)

        new_tab = self.open_in_new_tab(product_element)
        return self.product_title, self.product_price, new_tab
