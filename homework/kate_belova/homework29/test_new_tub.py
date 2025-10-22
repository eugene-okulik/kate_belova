from playwright.sync_api import expect


def test_open_new_tab(browser):
    browser.goto('https://www.qa-practice.com/elements/new_tab/button')

    original_page = browser.context.pages[0]
    click_button = browser.locator('#new-page-button')

    with browser.expect_popup() as new_tab_info:
        click_button.click()

    new_tab = new_tab_info.value
    new_tab.wait_for_load_state()

    result_text = new_tab.locator('#result-text')
    expect(result_text).to_have_text('I am a new page in a new tab')
    new_tab.close()

    original_page.bring_to_front()
    expect(click_button).to_be_enabled()
