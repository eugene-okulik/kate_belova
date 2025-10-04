import allure
import requests

from .test_data import base_url


def get_all_objects():
    with allure.step('Send GET request to get all objects'):
        url = base_url + '/object'
        response = requests.get(url)
    with allure.step('Assert status code is 200'):
        response.raise_for_status()
    return response.json()


def create_new_object(data):
    with allure.step('Send POST request to create new object'):
        url = base_url + '/object'
        response = requests.post(url, json=data)
    with allure.step('Assert status code is 200'):
        response.raise_for_status()
    return response.json()


def get_one_object(id):
    with allure.step('Send GET request with id to get one object'):
        url = base_url + f'/object/{id}'
        response = requests.get(url)
    with allure.step('Assert status code is 200'):
        response.raise_for_status()
    return response.json()


def update_object(id, data):
    with allure.step('Send PUT request with id to update object'):
        url = base_url + f'/object/{id}'
        response = requests.put(url, json=data)
    with allure.step('Assert status code is 200'):
        response.raise_for_status()
    return response.json()


def partially_update_object(id, data):
    with allure.step('Send PATCH request with id to update object'):
        url = base_url + f'/object/{id}'
        response = requests.patch(url, json=data)
    with allure.step('Assert status code is 200'):
        response.raise_for_status()
    return response.json()


def delete_object(id):
    with allure.step('Send DELETE request to delete object'):
        url = base_url + f'/object/{id}'
        response = requests.delete(url)
    with allure.step('Assert status code is 200'):
        response.raise_for_status()
