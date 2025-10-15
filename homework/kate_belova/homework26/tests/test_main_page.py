import time

import pytest


@pytest.mark.main_page
@pytest.mark.regression
class TestMainPage:
    def test_add_to_cart_from_product_tab(
        self, main_page, add_to_cart_popup, product_page, cart_page
    ):
        main_page.open_main_page()
        main_page.open_product_in_new_tab()

        product_page.click_add_to_cart()
        add_to_cart_popup.wait_for_popup()
        add_to_cart_popup.click_continue_shopping()
        time.sleep(1)
        product_page.close_product_page_return_to_main()

        main_page.open_shopping_cart()
        cart_page.check_product_name_and_price_in_cart(
            main_page.product_name, main_page.product_price
        )

    @pytest.mark.smoke
    def test_add_to_cart_from_main_page(self, main_page, add_to_cart_popup):
        main_page.open_main_page()
        main_page.click_add_to_cart_from_hover_button()

        add_to_cart_popup.wait_for_popup()
        add_to_cart_popup.check_product_name_and_price_in_popup(
            main_page.product_name, main_page.product_price
        )
