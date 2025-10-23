import json
import re

from playwright.sync_api import Route, expect


def test_iphone_title(browser):
    def modify_api_response(route: Route):
        response = route.fetch()
        content_type = response.headers.get('content-type', '')
        if 'application/json' not in content_type:
            route.fulfill(response=response)
            return

        response_data = response.json()

        def modify_product_titles(obj):
            if isinstance(obj, dict):
                for key, value in obj.items():
                    if isinstance(value, str):
                        pattern = r'iPhone\s*17\s*Pro'
                        replacement = 'яблокофон 17 про'

                        if re.search(pattern, value, re.IGNORECASE):
                            obj[key] = re.sub(
                                pattern,
                                replacement,
                                value,
                                flags=re.IGNORECASE,
                            )
                    else:
                        modify_product_titles(value)
            elif isinstance(obj, list):
                for item in obj:
                    modify_product_titles(item)

        modify_product_titles(response_data)

        route.fulfill(
            response=response,
            body=json.dumps(response_data),
            headers={**response.headers, 'content-type': 'application/json'},
        )

    browser.route(
        '**/shop/api/digital-mat?path=library/step0_iphone/digitalmat',
        modify_api_response,
    )

    browser.goto('https://www.apple.com/shop/buy-iphone')
    iphone_pro_card = browser.locator('.rf-hcard-img-wrapper').first
    iphone_pro_card.click()

    browser.wait_for_selector('[id=":r21:"]', state='visible', timeout=2000)

    popup_title = browser.locator('h2#rf-digitalmat-overlay-label-0').first
    expect(popup_title).to_contain_text('яблокофон 17 про')
    expect(browser.locator('body')).to_contain_text('яблокофон 17 про')
