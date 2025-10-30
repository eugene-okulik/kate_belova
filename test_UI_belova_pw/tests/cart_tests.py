import allure
import pytest

from test_UI_belova_pw.test_data import products_indexes


@pytest.mark.cart
@pytest.mark.regression
class TestCartPage:
    @allure.feature('Cart')
    @allure.story('Empty Cart page')
    @allure.title('Empty Cart page has all the necessary details')
    def test_empty_cart(self, cart_page):
        cart_page.open_cart_page()
        cart_page.assert_empty_cart_message()
        cart_page.assert_cart_icon_has_no_items()
        cart_page.assert_navigation_to_main_page()

    @allure.feature('Cart')
    @allure.story('Adding products to cart')
    @allure.title('Successfully add product to cart by hover button')
    @pytest.mark.smoke
    @pytest.mark.parametrize('product_idx', products_indexes)
    def test_add_product_to_cart_by_hover_success(
        self, main_page, alert_page, cart_page, product_idx
    ):
        main_page.open_main_page()
        product_title, product_price = (
            main_page.click_add_to_cart_on_hover_button(product_idx)
        )
        alert_page.wait_for_alert()

        main_page.click_cart_icon_in_header()
        cart_page.assert_product_cart_title_quantity_price(
            product_title, product_price
        )

    @pytest.mark.usefixtures('cart_page')
    @allure.feature('Cart')
    @allure.story('Removing products from cart')
    @allure.title('Successfully remove product from cart')
    @pytest.mark.smoke
    def test_remove_product_from_cart_success(self, cart_with_product):
        cart_page = cart_with_product
        cart_page.remove_product_from_cart()
        cart_page.assert_empty_cart_message()
        cart_page.assert_cart_icon_has_no_items()
