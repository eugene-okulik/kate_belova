import allure
import requests

from test_api_belova.schemas import ResponseObjectSchema


class BaseAPI:
    def __init__(self):
        self.base_url = 'http://objapi.course.qa-practice.com'
        self.response = requests.Response
        self.status_code = None
        self.json = None
        self.object_data = None

    @allure.step('Assert response status is OK')
    def assert_response_is_200(self):
        assert (
            self.status_code == 200
        ), f'Expected status code 200, but got {self.status_code}'

    @allure.step('Assert response status is Not Found')
    def assert_response_is_404(self):
        assert (
            self.status_code == 404
        ), f'Expected status code 404, but got {self.status_code}'

    @allure.step('Assert object ID in response is the one sent in request')
    def assert_object_id(self, object_id):
        self.object_data = ResponseObjectSchema(**self.json)
        response_data = self.object_data.model_dump()

        actual_id = response_data['id']
        assert (
            actual_id == object_id
        ), f'Expected object ID {object_id}, but got {actual_id}'

    @allure.step('Assert object name in response is the one sent in request')
    def assert_object_name(self, data):
        self.object_data = ResponseObjectSchema(**self.json)
        response_data = self.object_data.model_dump()

        actual_name = response_data['name']
        expected_name = data['name']
        assert (
            actual_name == expected_name
        ), f'Expected object name {expected_name}, but got {actual_name}'

    @allure.step('Assert object data in response is the one sent in request')
    def assert_object_data(self, data):
        self.object_data = ResponseObjectSchema(**self.json)
        responce_data = self.object_data.model_dump()

        actual_data = responce_data['data']
        expected_data = data['data']
        for key, value in expected_data.items():
            assert (
                actual_data[key] == value
            ), f'Expected {key} to be {value}, but got {actual_data[key]}'
