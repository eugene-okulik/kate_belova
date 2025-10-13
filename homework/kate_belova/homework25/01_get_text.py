from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from homework.kate_belova.homework25.browser_setup import browser

with browser:
    browser.get('https://www.qa-practice.com/elements/input/simple')

    input_field = browser.find_element('css selector', '#id_text_string')
    input_field.send_keys('this_is_snake_case')
    input_field.send_keys(Keys.ENTER)

    result_element = WebDriverWait(browser, 2).until(
        ec.presence_of_element_located(('css selector', '#result-text'))
    )
    result_text = result_element.text
    print(result_text)
