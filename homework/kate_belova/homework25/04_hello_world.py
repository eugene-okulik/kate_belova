from homework.kate_belova.homework25.browser_setup import browser
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

with browser:
    browser.get('https://the-internet.herokuapp.com/dynamic_loading/2')

    start_button = browser.find_element('css selector', 'button')
    start_button.click()

    wait = WebDriverWait(browser, 5)

    loader = browser.find_element('css selector', '#loading')
    wait.until(ec.visibility_of(loader))
    wait.until(ec.invisibility_of_element(loader))

    expected_text = 'Hello World!'
    actual_text = browser.find_element('css selector', '#finish').text
    assert actual_text == expected_text, (
        f'Actual text {actual_text }is not equal '
        f'to expected text {expected_text}'
    )
    print('Everything is fine')
