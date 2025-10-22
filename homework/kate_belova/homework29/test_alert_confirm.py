from playwright.sync_api import expect


def test_alert_confirm_success(browser):
    browser.goto('https://www.qa-practice.com/elements/alert/confirm')

    browser.once('dialog', lambda alert: alert.accept())
    click_button = browser.locator('.a-button')
    click_button.click()

    selected = browser.locator('#result-text')
    expect(selected).to_have_text('Ok')
