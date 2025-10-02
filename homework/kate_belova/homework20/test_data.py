import random

from faker import Faker

faker = Faker()

base_url = 'http://objapi.course.qa-practice.com'

sizes = ['small', 'medium', 'big', 'huge']

data = {
    'data': {
        'color': faker.safe_color_name(),
        'size': random.choice(sizes),
    },
    'name': faker.word().capitalize() + ' object',
}

data_empty_name = {
    'data': {
        'color': faker.safe_color_name(),
        'size': random.choice(sizes),
    },
    'name': '',
}

data_special_chars = {
    'data': {
        'color': faker.safe_color_name(),
        'size': random.choice(sizes),
    },
    'name': '@#$%^&*!',
}

update_data = {
    'data': {
        'group': random.randint(1, 20),
        'level': random.randint(1, 200),
    },
    'name': faker.word().capitalize() + ' object',
}

patch_data = {'name': faker.word().capitalize() + ' object'}
