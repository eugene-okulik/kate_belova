from faker import Faker

faker = Faker()

sizes = ['small', 'medium', 'big', 'huge']

create_data = [
    {
        'data': {
            'color': 'Coral',
            'size': 'Medium',
        },
        'name': 'Test object',
    },
    {
        'data': {
            'color': 'Purple',
            'size': 'Small',
        },
        'name': '',
    },
    {
        'data': {
            'color': 'Blue',
            'size': 'Big',
        },
        'name': '@#$%^&*!',
    },
]

update_data = {
    'data': {
        'color': 'White',
        'size': 'Huge',
    },
    'name': 'Updated object',
}

patch_data = {'name': 'Partially updated object'}
