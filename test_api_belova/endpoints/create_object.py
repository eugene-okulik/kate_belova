import allure
import requests

from test_api_belova.endpoints import BaseAPI


class CreateObject(BaseAPI):
    def __init__(self):
        super().__init__()
        self.url = self.base_url + '/object'
        self.id = None

    @allure.step('Send POST request to create new object')
    def post_response(self, data):
        self.response = requests.post(self.url, json=data)
        self.status_code = self.response.status_code
        self.json = self.response.json()
        self.id = self.json['id']
