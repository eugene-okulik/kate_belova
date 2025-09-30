import requests

from .test_data import base_url


def get_all_objects():
    url = base_url + '/object'
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def create_new_object(data):
    url = base_url + '/object'
    response = requests.post(url, json=data)
    response.raise_for_status()
    return response.json()


def get_one_object(id):
    url = base_url + f'/object/{id}'
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def update_object(id, data):
    url = base_url + f'/object/{id}'
    response = requests.put(url, json=data)
    response.raise_for_status()
    return response.json()


def partially_update_object(id, data):
    url = base_url + f'/object/{id}'
    response = requests.patch(url, json=data)
    response.raise_for_status()
    return response.json()


def delete_object(id):
    url = base_url + f'/object/{id}'
    response = requests.delete(url)
    response.raise_for_status()
