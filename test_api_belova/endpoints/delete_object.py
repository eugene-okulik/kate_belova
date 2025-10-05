import allure
import requests

from test_api_belova.endpoints import BaseAPI


class DeleteObject(BaseAPI):
    def __init__(self, object_id):
        super().__init__()
        self.url = self.base_url + f'/object/{object_id}'
        self.expected_message = (
            f'Object with id {object_id} successfully deleted'
        )
        self.actual_message = None

    @allure.step('Send DELETE request to delete object by its ID')
    def delete_response(self):
        self.response = requests.delete(self.url)
        self.status_code = self.response.status_code
        self.actual_message = self.response.text

    @allure.step('Assert successful deletion message')
    def assert_delete_message(self):
        assert self.actual_message == self.expected_message, (
            f'Expected message "{self.expected_message}", '
            f'but got "{self.actual_message}"'
        )
