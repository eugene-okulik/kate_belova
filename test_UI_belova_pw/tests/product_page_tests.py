import allure
import pytest

from test_UI_belova_pw.test_data import (
    products_test_data,
    search_words,
)


@pytest.mark.product_page
@pytest.mark.regression
class TestProductPage:
    @allure.feature('Product page')
    @allure.story('Product details on Product Page')
    @allure.title('Product has all the necessary details')
    @pytest.mark.smoke
    def test_product_details(self, product_page_in_new_tab):
        product_page, product_title, product_price = product_page_in_new_tab[
            :3
        ]

        product_page.assert_product_title_and_price(
            product_title, product_price
        )
        product_page.assert_breadcrumbs_product_title()
        product_page.assert_product_quantity()

        product_page.assert_quantity_input_field_is_active()
        product_page.assert_plus_and_minus_buttons_work()

        product_page.assert_add_to_cart_button_is_active()
        product_page.assert_terms_and_conditions()

    @allure.feature('Product page')
    @allure.story('Add product to cart from Product page')
    @allure.title('Successfully add product to cart from Product page')
    @pytest.mark.smoke
    @pytest.mark.parametrize(
        'product_page_in_new_tab, quantity, price',
        products_test_data,
        indirect=['product_page_in_new_tab'],
    )
    def test_add_product_to_cart_from_product_page_success(
        # fmt: off
        self, product_page_in_new_tab, cart_page_from_product_tab,
        quantity, price
        # fmt: on
    ):
        product_page, product_title, product_price, alert_page = (
            product_page_in_new_tab
        )
        product_page.add_product_quantity(quantity)

        product_page.click_add_to_cart_button()
        alert_page.wait_for_alert()
        product_page.click_cart_icon_in_header()

        cart_page_from_product_tab.assert_product_cart_title_quantity_price(
            product_title, str(price), quantity
        )

    @allure.feature('Product page')
    @allure.story('Product page search')
    @allure.title(
        'Successfully search products by their titles on Product page'
    )
    @pytest.mark.smoke
    @pytest.mark.parametrize('search_word', search_words)
    def test_product_page_search_success(
        self, product_page_in_new_tab, search_word
    ):
        product_page = product_page_in_new_tab[0]
        product_page.enter_search_word(search_word)
        product_page.assert_search_word_in_found_products_titles(search_word)
