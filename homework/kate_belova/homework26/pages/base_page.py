from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, browser):
        self.browser = browser

        self.url = 'http://testshop.qa-practice.com/'
        self.cart_url = 'http://testshop.qa-practice.com/shop/cart'
        self.tabs = None
        self.actions = ActionChains(self.browser)
        self.wait = WebDriverWait(self.browser, 10)
        self.ec = ec

    def open_page(self, url):
        return self.browser.get(url)

    def update_tabs(self):
        self.tabs = self.browser.window_handles

    def find_element(self, args):
        return self.browser.find_element(*args)

    def find_elements(self, args):
        return self.browser.find_elements(*args)

    def open_in_new_tab(self, element):
        self.actions.key_down(Keys.CONTROL).click(element).key_up(
            Keys.CONTROL
        ).perform()

        self.update_tabs()
        new_tab = self.tabs[-1]
        self.browser.switch_to.window(new_tab)

    def close_current_tab(self):
        self.browser.close()

    def switch_to_previous_tab(self):
        self.update_tabs()
        self.browser.switch_to.window(self.tabs[-1])

    @staticmethod
    def check_name_and_price(
        actual_name, expected_name, actual_price, expected_price
    ):
        assert (
            actual_name == expected_name
        ), f'Product name should be "{expected_name}", but got "{actual_name}"'
        assert actual_price == expected_price, (
            f'Product price should be "{expected_price}", '
            f'but got "{actual_price}"'
        )
