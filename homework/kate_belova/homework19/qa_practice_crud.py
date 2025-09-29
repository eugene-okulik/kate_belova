import random
from pprint import pprint

import requests
from faker import Faker

faker = Faker()

base_url = 'http://objapi.course.qa-practice.com'

sizes = ['small', 'medium', 'big', 'huge']

create_data = {
    'data': {'color': faker.safe_color_name(), 'size': random.choice(sizes)},
    'name': faker.word().capitalize() + ' object',
}
update_data = {
    'data': {'group': random.randint(1, 20), 'level': random.randint(1, 200)},
    'name': faker.word().capitalize() + ' object',
}

some_data_to_update = {'name': faker.word().capitalize() + ' object'}


def get_all_objects():
    url = base_url + '/object'
    response = requests.get(url)

    print(f'Response status code: {response.status_code}')
    data = response.json()['data']
    for obj in data:
        print(f'Object {obj["id"]}: {obj["name"]}\n' f'Data: {obj["data"]}')


def create_new_object(data):
    url = base_url + '/object'
    response = requests.post(url, json=data)
    data = response.json()
    id = data['id']

    print('Status code:', response.status_code)
    print('Response body:')
    pprint(data)

    return id


def get_one_object(id):
    url = base_url + f'/object/{id}'
    response = requests.get(url)

    data = response.json()
    assert data['id'] == id, 'id mismatch'

    print(f'Response status code: {response.status_code}')
    print('Response body:')
    pprint(data)


def update_object(id, data):
    url = base_url + f'/object/{id}'
    response = requests.put(url, json=data)

    data = response.json()
    assert data['id'] == str(id), 'id mismatch'

    print('Status code:', response.status_code)
    print('Response body:')
    pprint(data)


def partially_update_object(id, data):
    url = base_url + f'/object/{id}'
    response = requests.patch(url, json=data)

    data = response.json()
    assert data['id'] == str(id), 'id mismatch'

    print('Status code:', response.status_code)
    print('Response body:')
    pprint(data)


def delete_object(id):
    url = base_url + f'/object/{id}'
    response = requests.delete(url)

    print('Status code:', response.status_code)


print('Get all objects:\n')
get_all_objects()
print('\n', '-' * 60)

print('Create new object:\n')
obj_id = create_new_object(create_data)
print('\n', '-' * 60)

print('Get one object:\n')
get_one_object(obj_id)
print('\n', '-' * 60)

print('Update object:\n')
update_object(obj_id, update_data)
print('\n', '-' * 60)

print('Partially update object:\n')
partially_update_object(obj_id, some_data_to_update)
print('\n', '-' * 60)

print('Delete object:\n')
delete_object(obj_id)
print('\n', '-' * 60)
