from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select

from homework.kate_belova.homework25.browser_setup import browser

with browser:
    browser.get('https://demoqa.com/automation-practice-form')

    first_name = browser.find_element('css selector', '#firstName')
    last_name = browser.find_element('css selector', '#lastName')
    first_name.send_keys('Brian')
    last_name.send_keys('Molko')

    email = browser.find_element('css selector', '#userEmail')
    email.send_keys('brian@placebo.com')

    other_gender = browser.find_element(
        'css selector', '[for="gender-radio-3"]'
    )
    other_gender.click()

    mobile_number = browser.find_element('css selector', '#userNumber')
    mobile_number.send_keys('7123456789')

    date_of_birth = browser.find_element(
        'css selector', 'input#dateOfBirthInput'
    )
    date_of_birth.click()
    year_select = browser.find_element(
        'css selector', '.react-datepicker__year-select'
    )
    select = Select(year_select)
    select.select_by_value('1972')
    month_select = browser.find_element(
        'css selector', '.react-datepicker__month-select'
    )
    select = Select(month_select)
    select.select_by_value('11')
    day = browser.find_element(
        'css selector', '[aria-label="Choose Sunday, December 10th, 1972"]'
    )
    day.click()

    subjects_input = browser.find_element('css selector', '#subjectsInput')
    subjects = ['Arts', 'Computer Science', 'English', 'Social Studies']
    for subject in subjects:
        subjects_input.send_keys(subject)
        subjects_input.send_keys(Keys.ENTER)

    hobby_reading = browser.find_element(
        'css selector', '[for="hobbies-checkbox-2"]'
    )
    hobby_music = browser.find_element(
        'css selector', '[for="hobbies-checkbox-3"]'
    )
    hobby_reading.click()
    hobby_music.click()

    current_address = browser.find_element('css selector', '#currentAddress')
    current_address.send_keys(
        '742 Evergreen Terrace, Springfield, IL 62704, USA'
    )

    state = browser.find_element('css selector', '#react-select-3-input')
    state.send_keys('N')
    state.send_keys(Keys.ENTER)
    city = browser.find_element('css selector', '#react-select-4-input')
    city.send_keys('D')
    city.send_keys(Keys.ENTER)

    submit_button = browser.find_element('css selector', '#submit')
    submit_button.click()

    table = browser.find_element('css selector', '.modal-body table')
    rows = table.find_elements('css selector', 'tr')

    result_data = {}
    print('\n--- Data from modal window ---')
    for row in rows:
        cells = row.find_elements('css selector', 'td')
        if len(cells) == 2:
            label = cells[0].text.strip()
            value = cells[1].text.strip()
            result_data[label] = value
            print(f'{label}: {value}')

    print('----------------------------------')

    expected_data = {
        'Student Name': 'Brian Molko',
        'Student Email': 'brian@placebo.com',
        'Gender': 'Other',
        'Mobile': '7123456789',
        'Date of Birth': '10 December,1972',
        'Subjects': 'Arts, Computer Science, English, Social Studies',
        'Hobbies': 'Reading, Music',
        'Address': '742 Evergreen Terrace, Springfield, IL 62704, USA',
        'State and City': 'NCR Delhi',
    }

    for key, expected_value in expected_data.items():
        actual_value = result_data.get(key)
        assert (
            actual_value == expected_value
        ), f'{key}: expected "{expected_value}", but got "{actual_value}"'

    print('Everything is OK')
