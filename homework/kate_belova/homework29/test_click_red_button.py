import re

from playwright.sync_api import expect


def test_button_changes_color(browser):
    browser.goto('https://demoqa.com/dynamic-properties')

    potentially_red_button = browser.locator('#colorChange')
    expect(potentially_red_button).to_be_enabled()

    expect(potentially_red_button).to_have_class(
        re.compile(r'text-danger'), timeout=5000
    )
    potentially_red_button.click()
