import allure
import requests

from test_api_belova.endpoints import BaseAPI
from test_api_belova.models import ResponseObjectsList


class GetObjects(BaseAPI):
    def __init__(self):
        super().__init__()
        self.url = self.base_url + '/object'

    @allure.step('Send GET request to get all objects')
    def get_response(self):
        self.response = requests.get(self.url)
        self.status_code = self.response.status_code
        if self.status_code != 404:
            self.json = self.response.json()

    @allure.step('Assert there is at least one object in the list')
    def assert_has_objects(self, min_count: int = 1):
        self.object_data = ResponseObjectsList(**self.json)
        responce_data = self.object_data.model_dump()

        objects_list = responce_data['data']
        assert len(objects_list) >= min_count, (
            f'Expected at least {min_count} object(s), '
            f'but got {len(objects_list)}'
        )


class GetObject(BaseAPI):
    def __init__(self, object_id):
        super().__init__()
        self.url = self.base_url + f'/object/{object_id}'
        self.expected_text_in_error = 'Not Found'
        self.actual_text_in_error = None

    @allure.step('Send GET request to get object info by its ID')
    def get_response(self):
        self.response = requests.get(self.url)
        self.status_code = self.response.status_code
        if self.status_code != 404:
            self.json = self.response.json()
        self.actual_text_in_error = self.response.text

    @allure.step('Assert error message for unexisting object')
    def assert_error_message(self):
        assert self.expected_text_in_error in self.actual_text_in_error, (
            f'Expected message should contain "{self.expected_text_in_error}",'
            f' but text is "{self.actual_text_in_error}"'
        )
