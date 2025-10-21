import random

from homework.kate_belova.homework28.conftest import random_generator


def test_automation_practice_form(browser):
    browser.goto('https://demoqa.com/automation-practice-form')

    browser.get_by_role('textbox', name='First Name').fill(
        random_generator.first_name()
    )
    browser.get_by_role('textbox', name='Last Name').fill(
        random_generator.last_name()
    )
    browser.get_by_role('textbox', name='name@example.com').fill(
        random_generator.email()
    )

    gender_labels = ['Male', 'Female', 'Other']
    selected_gender = random.choice(gender_labels)
    browser.get_by_text(selected_gender, exact=True).click()

    mobile_number = str(
        random_generator.random_number(digits=10, fix_len=True)
    )
    browser.get_by_role('textbox', name='Mobile Number').fill(mobile_number)

    # fmt: off
    subjects = [
        'Accounting', 'Arts', 'Biology', 'Chemistry',
        'Civics', 'Commerce', 'Computer Science', 'Economics',
        'English', 'Hindi', 'History', 'Maths',
        'Physics', 'Social Studies'
    ]
    # fmt: on
    selected_subjects = random.sample(subjects, 4)
    subjects_input = browser.locator('#subjectsInput')
    for subject in selected_subjects:
        subjects_input.click()
        subjects_input.press_sequentially(subject, delay=50)
        subjects_input.press('Enter')

    random_date = random_generator.date_of_birth(minimum_age=7, maximum_age=77)
    year = random_date.year
    month = random_date.month - 1
    day = random_date.day

    browser.locator('input#dateOfBirthInput').click()
    browser.locator('.react-datepicker__year-select').select_option(
        value=str(year)
    )
    browser.locator('.react-datepicker__month-select').select_option(
        value=str(month)
    )
    browser.locator(
        f'[aria-label*="{random_date.strftime("%B")} {day}"]'
    ).click()

    hobbies = ['Music', 'Reading', 'Sports']
    selected_hobbies = random.sample(hobbies, 2)
    for hobby in selected_hobbies:
        browser.get_by_text(hobby).click()  # используем get_by_text

    current_address = browser.get_by_placeholder('Current Address')
    current_address.scroll_into_view_if_needed()
    current_address.fill(random_generator.address())

    states_cities = {
        'NCR': ['Delhi', 'Gurgaon', 'Noida'],
        'Uttar Pradesh': ['Agra', 'Lucknow', 'Merrut'],
        'Haryana': ['Karnal', 'Panipat'],
        'Rajasthan': ['Jaipur', 'Jaiselmer'],
    }

    random_state = random.choice(list(states_cities.keys()))
    random_city = random.choice(states_cities[random_state])

    state_input = browser.locator('#react-select-3-input')
    state_input.scroll_into_view_if_needed()
    state_input.fill(random_state)
    state_input.press('Enter')

    city_input = browser.locator('#react-select-4-input')
    city_input.fill(random_city)
    city_input.press('Enter')

    browser.get_by_role('button', name='Submit').click()
