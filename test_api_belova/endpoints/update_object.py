import allure
import requests

from test_api_belova.endpoints import BaseAPI


class UpdateObject(BaseAPI):
    def __init__(self, object_id):
        super().__init__()
        self.url = self.base_url + f'/object/{object_id}'

    @allure.step('Send PUT request to update object info by its ID')
    def put_response(self, data):
        self.response = requests.put(self.url, json=data)
        self.status_code = self.response.status_code
        self.json = self.response.json()


class PartiallyUpdateObject(BaseAPI):
    def __init__(self, object_id):
        super().__init__()
        self.url = self.base_url + f'/object/{object_id}'

    @allure.step('Send PATCH request to update object info by its ID')
    def patch_response(self, data):
        self.response = requests.patch(self.url, json=data)
        self.status_code = self.response.status_code
        self.json = self.response.json()
