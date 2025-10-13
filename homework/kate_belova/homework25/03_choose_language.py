import time

from selenium.webdriver.support.select import Select

from homework.kate_belova.homework25.browser_setup import browser

with browser:
    browser.get('https://www.qa-practice.com/elements/select/single_select')

    choose_language = browser.find_element(
        'css selector', '#id_choose_language'
    )
    select = Select(choose_language)
    select.select_by_visible_text('C#')

    submit_button = browser.find_element(
        'css selector', 'input[type="submit"]'
    )
    submit_button.click()

    result_text = browser.find_element('css selector', '#result-text').text
    print(result_text)
