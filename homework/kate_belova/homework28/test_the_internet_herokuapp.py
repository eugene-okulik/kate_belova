import re


def test_form_authentication(browser):
    browser.goto('https://the-internet.herokuapp.com')
    browser.get_by_role('link', name='Form Authentication').click()

    subheader = browser.get_by_role(
        'heading', name='This is where you can log into the secure area.'
    )
    html_content = subheader.inner_html()
    matches = re.findall(r'<em>(?P<content>.*?)</em>', html_content)

    username = None
    password = None

    if len(matches) >= 2:
        username = matches[0]
        password = matches[1]

    browser.get_by_role('textbox', name='Username').fill(username)
    browser.get_by_role('textbox', name='Password').fill(password)
    browser.get_by_role('button', name='Login').click()
